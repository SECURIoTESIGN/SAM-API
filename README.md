# SAM-API

<p align="center"> 
<img src="https://github.com/SECURIoTESIGN/SAM-API/blob/master/static/logo.png"><br/>
SAM's Web API<br/>Be aware this project is under initial development.
</p>


# Installation (for developers only):
1) Create a virtual environment called ```venv``` in the project directory and install the main Python packages into the environment: 
```
$ python3 -m venv venv
$ source venv/bin/activate
$ (venv) pip install flask python-dotenv
```
2) Install all the necessary libraries in the virtual environment:
```
$ (venv) pip install -r requirements.txt
```
3) Define the environment variables by placing a ```.flaskenv``` file on the root of the application with the following content:<br/>
```
FLASK_APP=api.py
FLASK_ENV=development
```
4) Create a folder called ```instance``` in the project directory with a copy of the ```.config.cfg``` file. Configure the contents of the file accordingly to your environment.

# Run SAM's Web API (for developers only):
```
$ source venv/bin/activate
$ (venv) flask run 
```
- If necessary, install any missing or additional modules using the newly created virtual environment. 
- The swagger documentation is available at ```http://localhost:5000/apidocs/```
