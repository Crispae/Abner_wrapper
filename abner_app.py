from flask import Flask, request, jsonify
from jnius import autoclass
import re

app = Flask(__name__)

# Initialize the Tagger as a global variable
Tagger = autoclass("abner.Tagger")
t = Tagger()

def extract_entities_from_text(text):
    # Get the entities using abner
    annotated_text = t.getEntities(text.strip())
    entities = annotated_text[0]

    # Create a regex pattern to find the entities in the text
    pattern = r"|".join(entities)
    matches = re.finditer(pattern, text)

    entities_list = []
    for idx, match in enumerate(matches):
        start_index = match.start()
        end_index = match.end()
        match_text = match.group()
        entity_type = annotated_text[1][idx]

        entities_dict = {
            "start": start_index,
            "end": end_index,
            "word": match_text,
            "entity_type": entity_type.lower()
        }
        entities_list.append(entities_dict)

    return entities_list

@app.route('/extract_entities', methods=['POST'])
def extract_entities():
    text = request.json.get('text')

    entities = extract_entities_from_text(text)

    return jsonify(entities)

if __name__ == '__main__':
    app.run(port=8743,debug=True)
