# Abner_wrapper
ABNER is a widely used named entity recognition (NER) tool. AOPbot provides seamless integration with ABNER through a dedicated Python wrapper. For detailed installation instructions, please refer to the ABNER python wrapper repository.

## Requirements
1. Install Java JDK 8 or 11
2. All other requirements mentioned in requirements.txt  
3. Unzip **ABNER** related Folder/files in scope of app.py file.

## Installation
Easy implementation through docker container
```shell
git clone https://github.com/Crispae/Abner_wrapper.git
cd Abner_wrapper
docker build --no-cache -t abner-image .
docker run -p 9000:9000 abner-image
```
