# SAM-API
SAM's Web API

# Installation (for developers only):
1) Create a virtual environment called ```venv``` in the project directory: 
```
python3 -m venv venv
```
2) Install all the necessary libraries in the virtual environment:
```
(venv) $ pip install -r requirements.txt
```
3) Define the environment variables by placing a ```.flaskenv``` file on the root of the application with the following content:<br/>
```
FLASK_APP=api.py
FLASK_ENV=development
```

# Run SAM's Web API (for developers only):
```
source venv/bin/activate
flask run 
```
- If necessary, install any missing or additional modules using the newly created virtual environment. 
- The swagger documentation is available at ```http://localhost:5000/apidocs/```
