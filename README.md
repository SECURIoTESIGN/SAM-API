# SAM-API

<p align="center"> 
<img src="https://github.com/SECURIoTESIGN/SAM-API/blob/master/static/logo.png"><br/>
SAM's Web API<br/>Be aware this project is under development.<br/>
<img src="https://github.com/SECURIoTESIGN/SAM-API/blob/master/static/sam-examples.png">
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
- The list of REST services is available at ```docs\insomnia```

# Acknowledgment
This project was performed under the <b>SECURIoTESIGN Project</b> (reference POCI-01-0145-FEDER-030657) with funding from FCT/COMPETE/FEDER. This work is also funded by operation Centro-01-0145-FEDER-000019-C4 <b>Centro de Competências em Cloud Computing (C4)</b>, co-financed by the European Regional Development Fund (ERDF) through the Programa Operacional Regional do Centro (Centro 2020), in the scope of the Sistema de Apoio à Investigação Científicas e Tecnológica Programas Integrados de ICDT.
