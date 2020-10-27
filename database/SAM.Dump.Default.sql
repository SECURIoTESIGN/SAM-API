-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: sam
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (1,'Smart Home',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(2,'Smart Healthcare',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(3,'Smart Manufacturing',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(4,'Smart Wearables',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(5,'Smart Toys',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(6,'Smart Transportation',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(7,'Normal',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(8,'Sensitive',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(9,'Critical',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(10,'Yes',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(11,'No',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(12,'Web Application',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(13,'Web Service',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(14,'Desktop Application',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(15,'Mobile Application',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(16,'Client-Server -> Client Component',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(17,'Client-Server -> Server Component',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(18,'API Service',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(19,'Embedded System',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(20,'Others',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(21,'SQL',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(22,'NoSQL',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(23,'Local Storage',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(24,'Distributed Storage',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(25,'SQL Server',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(26,'MySQL',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(27,'PostgresSQL',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(28,'SQLite',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(29,'OracleDB',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(30,'MariaDB',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(31,'MongoDB',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(32,'CosmosDB',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(33,'DynamoDB',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:50'),(34,'Cassandra',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(35,'Personal Information (Names, Addresses...)',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(36,'Confidential Data',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(37,'Critical Data',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(38,'No Authentication',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(39,'Username and Password',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(40,'Social Networks/Google',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(41,'SmartCard',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(42,'Biometric',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(43,'Two Factor Authentication',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(44,'Multi Factor Authentication',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(45,'The users will register themselves',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(46,'An administrator will register the users',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(47,'C/C++',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(48,'Java',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(49,'Javascript',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(50,'PHP',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(51,'Python',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(52,'Ruby',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(53,'Other/Proprietary Language',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(54,'Hardware',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(55,'Field-programmable Gate Array (FPGA)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(56,'Application-specific Integrated Circuit (ASIC)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(57,'Low Power',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(58,'Ultra-low Power',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(59,'Software',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(60,'Conception, Planning, Analysis, Design',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(61,'Existing System',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(62,'ARM (32 or 64-bit RISC CPU)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(63,'AVR (8 or 32-bit RISC CPU)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(64,'MSP (16-bit RISC CPU)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(65,'PIC (8, 16 or 32-bit RISC CPU)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(66,'Other',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(67,'8-bit',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(68,'16-bit',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(69,'32-bit',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(70,'64-bit',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(71,'Smart City',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(72,'Smart Agriculture',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(73,'Smart Grid',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(74,'Smart Elderly Monitoring',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(75,'Smart Kid Monitoring',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(76,'Smart Pet Monitoring',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(77,'Smart Banking/Financial applications',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(78,'Industrial Automation',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(79,'Smart Supply Chain',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(80,'Smart Retail',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(81,'Smart Environmental Monitoring',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(82,'Smart Automotive/Transportation',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(83,'Connected Car',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(84,'Other Domain',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(85,'Small (1-128 bytes)',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(86,'Average (129-256 bytes)',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(87,'Large (> 256 bytes)',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(88,'Continuous',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(89,'Unknown',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43');
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_token_blacklist`
--

LOCK TABLES `auth_token_blacklist` WRITE;
/*!40000 ALTER TABLE `auth_token_blacklist` DISABLE KEYS */;
INSERT INTO `auth_token_blacklist` VALUES (31,2,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZW1haWwiOiJhZG1pbkBTQU0ucHQiLCJhdmF0YXIiOm51bGwsImlzX2FkbWluIjoxLCJleHAiOjE2MDM4ODE2MjR9.fWk6ky1SJw38JvZVL47Ne1zVM_swb46oJl9yfGIbFwc','2020-10-27 10:41:03','2020-10-27 10:41:03'),(33,1,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyQFNBTS5wdCIsImF2YXRhciI6bnVsbCwiaXNfYWRtaW4iOjAsImV4cCI6MTYwMzg4MTk1Mn0.cyp5MpFHFBXiwluUK1emaTYE3kuD2xUXDXkPmM2tgfs','2020-10-27 10:46:56','2020-10-27 10:46:56');
/*!40000 ALTER TABLE `auth_token_blacklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dependency`
--

LOCK TABLES `dependency` WRITE;
/*!40000 ALTER TABLE `dependency` DISABLE KEYS */;
INSERT INTO `dependency` VALUES (1,3,1,'2020-10-26 16:56:40','2020-10-26 16:56:40');
/*!40000 ALTER TABLE `dependency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
INSERT INTO `group` VALUES (1,'Standard','2020-10-23 14:58:36','2020-10-23 14:58:36');
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `module`
--

LOCK TABLES `module` WRITE;
/*!40000 ALTER TABLE `module` DISABLE KEYS */;
INSERT INTO `module` VALUES (1,1,'SRE','Security Requirements Elicitation','Security Requirements','logic_1.py',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(2,2,'SBPG','Security Best Pratice Guidelines','Security Best Pratices',NULL,NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(3,3,'LWCAR','LightWeight Criptographic Algorithm Recommendation','LightWeight Criptographic Algorithm','logic_3.py',NULL,NULL,'2020-10-26 16:56:40','2020-10-26 17:17:42');
/*!40000 ALTER TABLE `module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `module_group`
--

LOCK TABLES `module_group` WRITE;
/*!40000 ALTER TABLE `module_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `module_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `module_question`
--

LOCK TABLES `module_question` WRITE;
/*!40000 ALTER TABLE `module_question` DISABLE KEYS */;
INSERT INTO `module_question` VALUES (1,1,1,1),(2,1,2,2),(3,1,8,3),(4,1,10,4),(5,1,11,5),(6,1,12,6),(7,1,13,7),(8,1,14,8),(9,1,15,9),(10,1,16,10),(11,1,17,10),(12,2,18,1),(13,2,19,2),(14,2,23,3),(15,2,24,4),(16,2,26,5),(17,2,27,6),(18,2,29,8),(22,3,30,0),(23,3,42,0),(24,3,43,0);
/*!40000 ALTER TABLE `module_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'Q1 - State the domain type for your IoT system',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(2,'Q2 - Will the system have a user?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(3,'Q2.1 - Will the system have user LogIn?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(4,'Q2.2 - Will the system hold any user information?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(5,'Q2.3 - Will the system store any kind of information?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(6,'Q2.4 - What will be the level of information stored?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(7,'Q2.5 - Will this information be sent to an entity?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(8,'Q3 - Will the system be connected to the internet?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(9,'Q3.1 - Will it send its data to a cloud?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(10,'Q4 - Will it store data in a db?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(11,'Q5 - Will the system receive regular updates?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(12,'Q6 - Will the system work with third-party software?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(13,'Q7 - Is there a possibility of the communications being eavesdropped?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(14,'Q8 - Could the messages sent between the system components be captured and resent?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(15,'Q9 - Can someone try to impersonate a user to gain access to private information?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(16,'Q10 - Can someone with bad intentions gain physical access to the location where this software will be running and obtain private information?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(17,'Q11 - Can someone gain physical access to the machine where the system operates or some of the system components and preform some type of modification to it?',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(18,'Q1 - What is the architecture of the system?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(19,'Q2 - Does the system use a database?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(20,'Q2.1 - What is the type of data storage?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(21,'Q2.2 - Which database is used?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(22,'Q2.3 - What is the type of data stored?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(23,'Q3 - Which type of authentication will be implemented?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(24,'Q4 - Will there be user registration?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(25,'Q4.1 - Which way of user registration will be used?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(26,'Q5 - Which programming languages will be used in the implementation of the system?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(27,'Q6 - Will the system allow input forms?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(28,'Q6.1 - Will the system allow file uploads?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(29,'Q7 - Will the system have logging?',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(30,'Select Implementation Type (Hardware or Software)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(31,'Select Hardware Type (FPGA or ASIC)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(32,'Select desired energy performance',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(33,'Enter your circuit area',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(34,'Enter your throughput',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(35,'What is the development phase of the IoT system, or it is an existing system?',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(36,'Enter Hardware Type (Microcontroller or Single Board Computer)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(37,'Select your CPU Type',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(38,'Input your CPU bit amount',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(39,'Enter flash memory size (in KB)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(40,'Enter RAM size (in KB)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(41,'Enter processor speed or frequency (in MHz)',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(42,'Select your application area',NULL,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(43,'Select your Payload Size',NULL,'2020-10-26 17:17:43','2020-10-26 17:17:43');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `question_answer`
--

LOCK TABLES `question_answer` WRITE;
/*!40000 ALTER TABLE `question_answer` DISABLE KEYS */;
INSERT INTO `question_answer` VALUES (1,1,1,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(2,1,2,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(3,1,3,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(4,1,4,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(5,1,5,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(6,1,6,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(7,6,7,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(8,6,8,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(9,6,9,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(10,18,12,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(11,18,13,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(12,18,14,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(13,18,15,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(14,18,16,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(15,18,17,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(16,18,18,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(17,18,19,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(18,18,20,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(19,20,21,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(20,20,22,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(21,20,23,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(22,20,24,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(23,21,25,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(24,21,26,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(25,21,27,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(26,21,28,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(27,21,29,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(28,21,30,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(29,21,31,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(30,21,32,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(31,21,33,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(32,21,34,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(33,22,35,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(34,22,36,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(35,22,37,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(36,23,38,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(37,23,39,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(38,23,40,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(39,23,41,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(40,23,42,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(41,23,43,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(42,23,44,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(43,25,45,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(44,25,46,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(45,26,47,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(46,26,48,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(47,26,49,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(48,26,50,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(49,26,51,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(50,26,52,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(51,26,53,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(52,21,20,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(53,26,20,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(54,2,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(55,2,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(56,3,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(57,3,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(58,4,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(59,4,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(60,5,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(61,5,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(62,7,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(63,7,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(64,8,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(65,8,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(66,9,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(67,9,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(68,10,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(69,10,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(70,11,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(71,11,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(72,12,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(73,12,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(74,13,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(75,13,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(76,14,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(77,14,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(78,15,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(79,15,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(80,16,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(81,17,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(82,19,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(83,19,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(84,24,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(85,24,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(86,27,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(87,27,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(88,28,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(89,28,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(90,29,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(91,29,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(131,30,54,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(132,31,55,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(133,31,56,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(134,32,57,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(135,32,58,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(136,30,59,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(137,35,60,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(138,35,61,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(139,36,62,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(140,36,63,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(141,36,64,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(142,36,65,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(143,36,66,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(144,37,67,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(145,37,68,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(146,37,69,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(147,37,70,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(148,37,66,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(149,42,1,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(150,42,71,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(151,42,72,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(152,42,73,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(153,42,2,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(154,42,74,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(155,42,75,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(156,42,76,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(157,42,77,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(158,42,78,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(159,42,79,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(160,42,80,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(161,42,81,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(162,42,82,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(163,42,83,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(164,42,84,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(165,43,85,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(166,43,86,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(167,43,87,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(168,43,88,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(169,43,89,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(170,16,11,'2020-10-27 10:31:19','2020-10-27 10:31:19'),(171,17,10,'2020-10-27 10:31:19','2020-10-27 10:31:19');
/*!40000 ALTER TABLE `question_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `question_has_child`
--

LOCK TABLES `question_has_child` WRITE;
/*!40000 ALTER TABLE `question_has_child` DISABLE KEYS */;
INSERT INTO `question_has_child` VALUES (1,2,3,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(2,2,4,10,2,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(3,2,5,10,3,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(4,2,6,10,4,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(5,2,7,10,5,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(6,8,9,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(10,19,20,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(11,19,21,10,2,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(12,19,22,10,3,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(13,24,25,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(14,27,28,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(26,30,31,54,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(27,30,32,54,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(28,30,33,54,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(29,30,34,54,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(30,30,35,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(31,30,36,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(32,30,37,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(33,37,38,66,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(34,30,39,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(35,30,40,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(36,30,41,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42');
/*!40000 ALTER TABLE `question_has_child` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `recommendation`
--

LOCK TABLES `recommendation` WRITE;
/*!40000 ALTER TABLE `recommendation` DISABLE KEYS */;
INSERT INTO `recommendation` VALUES (4,'Authentication',NULL,'recommendation_4.md','2020-10-23 15:37:38','2020-10-23 15:37:38'),(5,'Access Control',NULL,'recommendation_5.md','2020-10-23 15:42:29','2020-10-23 15:42:29'),(6,'API',NULL,'recommendation_6.md','2020-10-23 15:42:58','2020-10-23 15:42:58'),(7,'Cross Site Scripting',NULL,'recommendation_7.md','2020-10-23 15:43:17','2020-10-23 15:43:17'),(8,'Cryptography',NULL,'recommendation_8.md','2020-10-23 15:43:30','2020-10-23 15:43:30'),(9,'File Upload',NULL,'recommendation_9.md','2020-10-23 15:43:42','2020-10-23 15:43:42'),(10,'Input Validation',NULL,'recommendation_10.md','2020-10-23 15:43:56','2020-10-23 15:43:56'),(11,'IoT Security',NULL,'recommendation_11.md','2020-10-23 15:44:11','2020-10-23 15:44:11'),(12,'Logging',NULL,'recommendation_12.md','2020-10-23 15:44:21','2020-10-23 15:44:21'),(13,'Session Management',NULL,'recommendation_13.md','2020-10-23 15:44:34','2020-10-23 15:44:34'),(14,'SQL Injection',NULL,'recommendation_14.md','2020-10-23 15:44:47','2020-10-23 15:44:47'),(15,'Web Service',NULL,'recommendation_15.md','2020-10-23 15:45:00','2020-10-23 15:45:00'),(26,'Clefia128/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(27,'Clefia128/192',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(28,'Enocoro_v2-128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(29,'Grain_v1-128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(30,'Trivium-80',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(31,'MICKEY_2.0-80',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(32,'TWINE64/80',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(33,'TWINE64/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(34,'Midori128/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(35,'SIMON64/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(36,'Piccolo64/80',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(37,'Piccolo64/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(38,'Midori64/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(39,'SIMON64/96',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(40,'Grain_v1-80',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(41,'PHOTON-80/20/16',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(42,'Keccak-f[100]',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(43,'SPONGENT-128/128/8',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(44,'PHOTON-256/32/32',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(45,'SPONGENT-88/80/8',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(46,'U-QUARK',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(47,'PHOTON-128/16/16',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(48,'SPONGENT-160/160/16',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(49,'PHOTON-160/36/36',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(50,'S-QUARK',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(51,'AES-GCM',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(52,'ACORN',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(53,'SILC-PRESENT',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(54,'SILC-AES',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(55,'Deoxys',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(56,'AES-OTR',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(57,'Ascon',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(58,'CLOC-AES',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(59,'JAMBU-AES',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(60,'ChaCha20-128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(61,'ChaCha20-256',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(62,'SPECK64/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(63,'AES_CTR128/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(64,'LED64/80',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(65,'SPECK64/96',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(66,'PRESENT64/80',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(67,'PRINCE64/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(68,'AES_CBC128/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(69,'CLOC-TWINE',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(70,'Ketje-SR',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(71,'Enocoro-80',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(72,'Clefia128/256',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(73,'PRESENT64/128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(74,'SPECK96/144',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(75,'SPECK48/72',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(76,'PHOTON-224/32/32',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(77,'SipHash-128',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(78,'No algorithm for confidentiality',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(79,'No algorithm for integrity',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(80,'No algorithm for authentication',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(81,'No algorithm for privacy',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(82,'No algorithm for non-repudiation',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(83,'No algorithm for authenticity',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(84,'No algorithm for availability',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(85,'No algorithm for accountability',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(86,'No algorithm for reliability',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(87,'No algorithm for physical security',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(88,'No algorithm for forgery resistance',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(89,'No algorithm for tamper detection',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(90,'No algorithm for data freshness',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(91,'No algorithm for confinement',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(92,'No algorithm for interoperability',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(93,'No algorithm for data origin authentication',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(94,'No algorithm for confidentiality,authenticity',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(95,'The system is not capable',NULL,NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(96,'Confidentiality','The property that ensures that information is not disclosed or made available to any unauthorized entity. In other words,personal information cannot be accessed by an unauthorized third party. This requirement is applied were the information is stored.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(97,'Integrity','Is the property of safeguarding the correctness and completeness of assets in an IoT system. In other words it involves maintaining the data consistent,  trustworthy and accurate during it life-cycle. ',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(98,'Availability','Refers to the property which ensures that an IoT device or system is accessible and usable upon demand by authorized entities. In other words the  device needs to be always available to access by authorized people. ',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(100,'Authorization','The property that determines whether the user or device has rights/privileges to access a resource, or issue commands.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(101,'Non-Repudiation','The security property that ensures that the transfer of messages or credentials between 2 IoT entities is undeniable.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(102,'Accountability','The property that ensures that every action can be traced back to a single user or device. This requirement is applied over Internet transactions.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(103,'Reliability','Refers to the property that guarantees consistent intended behavior of an a general system, in this case applied to IoT.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(104,'Privacy','In the context of IoT, privacy refers to the control of the user over the disclosure of his data. In other words only the user has control of the sharing of is personal information, is data is only made public if the user allowed it. This requirement is applied were the information is stored.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(105,'Physical Security','Refers to the security measures designed to deny unauthorized physical access to IoT devices and equipment, and to protect them from damage or in other words gaining physical access to the device won\'t give access to it\'s information.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(106,'Forgery Resistance','Is the propriety that ensures that the contents shared between entities cannot be forged by a third party trying to damage or harm the system or its users. In other words no one can try to forge content and send it in the name of another entities.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(107,'Tamper Detection','Ensures all devices are physically secured, such that any tampering attempt is detected.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(108,'Data Freshness','Status that ensures that data is the most recent, and that old messages are not mistakenly used as fresh or purposely replayed by perpetrators. In other words this requirement provides the guarantee that the data displayed is the most recent.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(109,'Confinement','Ensures that even if a party is corrupted, the spreading of the effects of the attack is as confined as possible.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(110,'Interoperability','Is the propriety that ensures that different software communicates and works well with each-other. I.e a software in health-care that works with data that comes from a third-party needs to be able to use and process the information given to it by this software.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(111,'Data Origin','Ensures that the data being received by the software comes from the source it claims to be. In other words it ensures that the data being received is authentic and from a trusted party.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53');
/*!40000 ALTER TABLE `recommendation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `recommendation_question_answer`
--

LOCK TABLES `recommendation_question_answer` WRITE;
/*!40000 ALTER TABLE `recommendation_question_answer` DISABLE KEYS */;
INSERT INTO `recommendation_question_answer` VALUES (15,4,10,'2020-10-23 15:38:15','2020-10-23 15:38:15'),(17,11,17,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(18,14,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(19,15,11,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(20,6,16,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(21,10,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(22,13,10,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(23,13,11,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(24,7,10,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(25,7,11,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(26,8,10,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(27,5,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(28,9,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(29,12,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(44,4,11,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(45,4,12,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(46,4,13,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(47,4,14,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(48,4,15,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(49,4,16,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(50,4,17,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(51,4,18,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(155,8,11,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(156,8,12,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(157,8,13,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(158,8,14,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(159,8,15,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(160,8,16,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(161,8,17,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(162,8,18,'2020-10-23 17:13:51','2020-10-23 17:13:51');
/*!40000 ALTER TABLE `recommendation_question_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `session_recommendation`
--

LOCK TABLES `session_recommendation` WRITE;
/*!40000 ALTER TABLE `session_recommendation` DISABLE KEYS */;
/*!40000 ALTER TABLE `session_recommendation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `session_user_answer`
--

LOCK TABLES `session_user_answer` WRITE;
/*!40000 ALTER TABLE `session_user_answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `session_user_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES (1,'Security Requirements','Provides Security Requirements','2020-10-23 14:58:36','2020-10-23 14:58:36'),(2,'Security Pratices','Provides Security Guidelines','2020-10-23 14:58:36','2020-10-23 14:58:36'),(3,'Security Algorithms','Provides Security Cryptographic Algorithms','2020-10-23 14:58:36','2020-10-23 14:58:36');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'user@SAM.pt','Plain','User','6e68eff9ad873e8df6d25fce9282fb9bfbd3f8f6ff32a639a42963448787d88a:7e3627579e1e4304874ce442f2e50760',NULL,0,0,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(2,'admin@SAM.pt','Admin','User','6e68eff9ad873e8df6d25fce9282fb9bfbd3f8f6ff32a639a42963448787d88a:7e3627579e1e4304874ce442f2e50760',NULL,0,1,'2020-10-23 14:58:36','2020-10-23 14:58:36');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user_group`
--

LOCK TABLES `user_group` WRITE;
/*!40000 ALTER TABLE `user_group` DISABLE KEYS */;
INSERT INTO `user_group` VALUES (3,1,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(4,2,1,'2020-10-23 14:58:36','2020-10-23 14:58:36');
/*!40000 ALTER TABLE `user_group` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-27 10:50:03
