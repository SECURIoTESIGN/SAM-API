# SQL Injection

With a successful SQL Attack it is possible for the attacker to execute sql instructions. This attack can lead to the gathering of all the database information by a malicious entity.

If, by using any of the tools mentioned above, the tester can access the any information from the SUT database the system is not protected against SQL Injection attacks.

## sqlmap

sqlmap  is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine.

This tool is compatible with the following database management systems: MySQL, Oracle, PostgreSQL, Microsoft SQL Server, Microsoft Access, IBM DB2, SQLite, Firebird, Sybase, SAP MaxDB, Informix, MariaDB, MemSQL, TiDB, CockroachDB, HSQLDB, H2, MonetDB, Apache Derby, Amazon Redshift, Vertica, Mckoi, Presto, Altibase, MimerSQL, CrateDB, Greenplum, Drizzle, Apache Ignite, Cubrid, InterSystems Cache, IRIS, eXtremeDB, FrontBase, Raima Database Manager, YugabyteDB and Virtuoso.

To install this tool the user needs to run:

```bash
    sudo apt-get install -y sqlmap
```

A simple way to test if the database has vulnerabilities, with this tool, is simply running the following command in the terminal to use the detection engine embedded in this tool:

``` bash
    python sqlmap.py -u "[URL]"
```

This command will perform a scan of the URL and it will return the found vulnerabilities within it.

## SQLi Dumper

SQLi Dumper tool is a windows tool that automates the process of detection and exploitation of SQL Injection vulnerabilities. This tool is capable of performing from detection or identification of vulnerabilities to exploitation of said vulnerabilities, automatically. 

To check if a system is vulnerable to SQLInjection the tester should use de URL Analyzer function fo this tool and do the following:

1- Open the "URL Analyzer" tab;

2- Paste the URL;

3- Select the GET method;

4- Select the intended methods of SQLi vulnerability like Error based, Union Integer based, Union Keyword based, etc.;

5- Click "GO".

If a vulnerability is found then the tool will use said vulnerability to dump the data from the database.

## Netsparker 

Netsparker is an automated, fully configurable, web application security scanner that enables you to scan websites, web applications and web services, and identify security flaws. It can scan all types of web applications, regardless of the platform or the language with which they are built.
Netsparker provides a SQL Injection Vulnerability Scanner, with this scanner trough penetration testing the tool will scan for vulnerabilities, exploit the vulnerability and extract data related to the database. 