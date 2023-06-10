# Use the base Ubuntu image
FROM ubuntu:latest

# Update package list and install dependencies
RUN apt-get update \
    && apt-get install -y default-jdk wget curl git nano unzip python3-pip

# Set the working directory
WORKDIR /home

# Clone the Abner_wrapper repository
RUN git clone https://github.com/Crispae/Abner_wrapper.git

# Change directory to Abner_wrapper
WORKDIR /home/Abner_wrapper

# Unzip the files and remove the zip archives
RUN unzip "*.zip" \
    && rm -rf "*.zip"

# Install Flask and Pyjnius
RUN pip3 install flask pyjnius

# Set the entry point to run the Flask application
CMD ["python3", "abner_app.py"]
