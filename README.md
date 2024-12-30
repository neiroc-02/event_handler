# BorgConnect Interface with CYMANII - MITH Cluster
## Context
This repository contains the code for the BorgConnect interface with CYMANII and MITH. This has a simple API to handle GET and POST requests using `Django`.
## Usage 
This API can be used to place GET and POST requests for the BorgConnect interface. It writes to JSON files in the following format...
```json
{
    {
        "event type": "Non TLS Connection",            
        "mitre_threat_no": "CWE_9999", 
        "description": "originated from 192.168.1.65",
        "timestamp": "yyyy-MM-DD HH:MM:ss"
    }
}
```

The API has the following endpoints:
- `/security/event/`
    - POST: Post a new security event to the database
    - GET: Get all security events
- `/security/event/<start_time>/<end_time>/`
    - GET: Get all security events between the start and end time
        - Place them in the following format: `yyyy-MM-DDTHH:MM:ss/yyyy-MM-DDTHH:MM:ss`

Currently, there is functionality for all end points!

It also properly thows Error Code 400 errors if the endpoint is not found or the JSON posted is in the incorrect format.
## Installation
To begin setup for the project, first __clone__ the repository:
```bash 
git clone https://github.com/neiroc-02/event_handler.git
```
Then, navigate to the project directory:
```bash
cd event_handler
```
Create a virtual environment for all the python packages:
```bash
python3 -m venv venv        # Create a virtual environment
source venv/bin/activate    # Activate the virtual environment
```
Then install the required packages to run the Django REST API:
```bash
pip install -r requirements.txt
```
## Running the Server
After all the setup is complete, you can run the server.

First, ensure that your virtual environment is activated:
```bash
source venv/bin/activate    # Activate the virtual environment
```

Then, you can run the server using the following command:
```bash
python manage.py makemigration event_handler    # This command may be needed in development
python manage.py migrate    # It may recommend you to run the following command to migrate the database
python manage.py runserver  # Start the server
```
## Cleaning Up
After you are done with the server, you can deactivate the virtual environment:
```bash
deactivate                  # Deactivate the virtual environment
```
