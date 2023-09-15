from flask import Flask, request, jsonify
from jnius import autoclass
import re

app = Flask(__name__)

# Initialize the Tagger as a global variable
Tagger = autoclass("abner.Tagger")
t = Tagger()

## To extract entites with position and types
def extract_entities_from_text(text):
    
    # Get the entities using abner
    annotated_text = dict(zip(*t.getEntities(text.strip()))) ## This store both the word,type

    if annotated_text:
        ## creating a pattern
        escaped_keys = [re.escape(key) for key in annotated_text.keys()]
        pattern = r"|".join(escaped_keys)
        matches = re.finditer(pattern, text)
        
        entities_list =[]
        for idx,match in enumerate(matches):
            start_index = match.start()
            end_index = match.end() 
            match_text = match.group()
            entity_type = annotated_text.get(match_text)

            if entity_type:
                entites_dict ={"start":start_index,
                                "end":end_index,
                                "word":match_text,
                                "entity_type":entity_type.lower()}
                entities_list.append(entites_dict)
        return entities_list
    else:
        return None

@app.route('/extract_entities', methods=['POST'])
def extract_entities():
    text = request.json.get('text')
    try:
        entities = extract_entities_from_text(text)
        return jsonify({"Result":entities})
    except:
        print("Error occured while processing the text, the tokens may cross the size limitation")
        return jsonify({"Result":"Error"})

    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)
