# SAM-API
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=javascript&logoColor=white)
![](https://img.shields.io/badge/MariaDB-fe814c?style=for-the-badge&logo=mariadb&logoColor=white)
![](https://img.shields.io/badge/Sphinx-97ca00?style=for-the-badge&logo=readthedocs&logoColor=white)

<p align="center"> 
<img src="https://github.com/SECURIoTESIGN/SAM/blob/master/public/logo_c.png"><br/>
</p>

# Project Overview

Security Advising Modules (SAM) is a framework that aggregates and connects the various modules developed under the scope of the [SECURIoTESIGN](https://lx.it.pt/securIoTesign/) project while providing a graphical interface to interact with them. SAM is modular, allowing for both quick integrations of newly developed modules and updates to existing modules. SAM works as a personal security assistant, more relatable, and capable of communicating with the end-user through a series of easily understandable questions, which the user can answer directly or through a set of predefined answers.

SAM's Web API or backend is availabe on this repository, while the frontend is available [here](https://github.com/SECURIoTESIGN/SAM/).

# Documentation

You can find the API documentation at the following [link](https://securiotesign.github.io/SAM-API/). Additionally, the documentationcan can be recompiled as follows:
``` 
 cd docs
 make html
```

# Installation

The installation, for development proposes only, can be accomplished through a group of Docker containers.

1) Clone the public repository.
2) Create the API and database docker imagens and subsequent containers:
```
cd sam-api
make
```
The database and API container will be deployed with API port set to ``8080`` and database port set to ``3306``. The database user will be ``root`` and the password ``secure``.

3) Deploy the database into the database container:
```
sudo docker exec -it sam-db python3 install_db.py
```
You can access the database using DBeaver or similar (use ``sudo docker inspect sam-db`` to get the IP assigneted to the ``sam-db`` container).

4) Develop away! :) You can start both containers as follows:
```
sudo docker stop sam-api && sudo docker start sam-api
```
SAM's REST services can be tested and accessed through insomnia – The Insomnia JSON file of this project can be found [here](https://github.com/SECURIoTESIGN/SAM-API/blob/master/docs/insomnia/Insomnia-SAM-API-Services.json).

⚠️ The contents of folder ``sam-api`` are mapped to the ``sam-api`` container, any local changes will be reflected.

# Acknowledgment

This work was performed under the scope of Project SECURIoTESIGN with funding from FCT/COMPETE/FEDER with reference number POCI-01-0145-FEDER-030657. This work is funded by Portuguese FCT/MCTES through national funds and, when applicable, co-funded by EU funds under the project UIDB/50008/2020, research grants BIL/Nº11/2019-B00701, BIL/Nº12/2019-B00702, and FCT research and doctoral grant SFRH/BD/133838/2017 and BIM/n°32/2018-B00582, respectively, and also supported by project CENTRO-01-0145-FEDER-000019 - C4 - Competence Center in Cloud Computing, Research Line 1: Cloud Systems, Work package WP 1.2 - Systems design and development processes and software for Cloud and Internet of Things ecosystems, cofinanced by the European Regional Development Fund (ERDF) through the Programa Operacional Regional do Centro (Centro 2020), in the scope of the Sistema de Apoio à Investigação Científica e Tecnológica - Programas Integrados de IC&DT.
