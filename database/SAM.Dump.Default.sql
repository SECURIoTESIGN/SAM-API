-- MySQL dump 10.13  Distrib 8.0.18, for macos10.14 (x86_64)
--
-- Host: localhost    Database: SAM
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `Answer`
--

LOCK TABLES `Answer` WRITE;
/*!40000 ALTER TABLE `Answer` DISABLE KEYS */;
INSERT INTO `Answer` VALUES (1,'Smart Home',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(2,'Smart Healthcare',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(3,'Smart Manufacturing',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(4,'Smart Wearables',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(5,'Smart Toys',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(6,'Smart Transportation',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(7,'Yes',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(8,'No',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(9,'Normal',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(10,'Sensitive',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(11,'Critical',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(12,'Web Application',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(13,'Web Service',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(14,'Desktop Application',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(15,'Client-Server (Client Component)',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(16,'Client-Server (Server Component)',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(17,'API Service',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(18,'Embedded System',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(19,'Others',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(20,'SQL',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(21,'NoSQL',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(22,'Local Storage',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(23,'Distributed Storage',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(24,'SQL Server',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(25,'MySQL',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(26,'PostgresSQL',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(27,'SQLite',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(28,'OracleDB',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(29,'MongoDB',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(30,'CosmosDB',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(31,'DynamoDB',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(32,'Cassandra',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(33,'Other',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(34,'Personal information',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(35,'Confidential Data',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(36,'Critical Data',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(37,'No authentication',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(38,'Username and password',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(39,'Social network',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(40,'Smartcard',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(41,'Biometric',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(42,'Two factor authentication',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(43,'Multi factor authentication',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(44,'The users will register themselves',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(45,'An administrator will register the users',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(46,'Input your answer',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(47,'C#',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(48,'C/C++',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(49,'Java',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(50,'Javascript',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(51,'PHP',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(52,'Python',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(53,'Ruby',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12');
/*!40000 ALTER TABLE `Answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Auth_Token_Blacklist`
--

LOCK TABLES `Auth_Token_Blacklist` WRITE;
/*!40000 ALTER TABLE `Auth_Token_Blacklist` DISABLE KEYS */;
INSERT INTO `Auth_Token_Blacklist` VALUES (37,1,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyQFNBTS5wdCIsImF2YXRhciI6bnVsbCwiaXNfYWRtaW4iOm51bGwsImV4cCI6MTYwMTU0ODYzMn0.LO7sbfs57Yoq94rIXVLgfecuARBhe__AtWQqpHkXxrk','2020-09-30 11:57:20','2020-09-30 11:57:20'),(38,2,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZW1haWwiOiJhZG1pbkBTQU0ucHQiLCJhdmF0YXIiOm51bGwsImlzX2FkbWluIjoxLCJleHAiOjE2MDE1NDk4NDd9.zBK3AhhshF0ANTXKaCe2D9hWZAE8CjBcwMDbcXRSwF8','2020-09-30 11:57:35','2020-09-30 11:57:35');
/*!40000 ALTER TABLE `Auth_Token_Blacklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Dependency`
--

LOCK TABLES `Dependency` WRITE;
/*!40000 ALTER TABLE `Dependency` DISABLE KEYS */;
/*!40000 ALTER TABLE `Dependency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Group`
--

LOCK TABLES `Group` WRITE;
/*!40000 ALTER TABLE `Group` DISABLE KEYS */;
INSERT INTO `Group` VALUES (1,'Test Users',NULL,NULL);
/*!40000 ALTER TABLE `Group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Module`
--

LOCK TABLES `Module` WRITE;
/*!40000 ALTER TABLE `Module` DISABLE KEYS */;
INSERT INTO `Module` VALUES (1,NULL,'SRE','Security Requirements Elicitation','Security Requirements',NULL,NULL,NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(2,NULL,'SBPG','Security Best Pratice Guidelines','Security Best Pratices',NULL,NULL,NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(3,NULL,'CA','CPU Adviser','CPU Adviser','logic_3.py',NULL,NULL,'2020-08-12 15:36:24','2020-08-12 15:36:24');
/*!40000 ALTER TABLE `Module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Module_Group`
--

LOCK TABLES `Module_Group` WRITE;
/*!40000 ALTER TABLE `Module_Group` DISABLE KEYS */;
/*!40000 ALTER TABLE `Module_Group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Module_Question`
--

LOCK TABLES `Module_Question` WRITE;
/*!40000 ALTER TABLE `Module_Question` DISABLE KEYS */;
INSERT INTO `Module_Question` VALUES (1,1,1,0),(2,1,2,0),(3,1,8,0),(4,1,10,0),(5,1,11,0),(6,1,12,0),(7,1,13,0),(8,1,14,0),(9,1,15,0),(10,1,16,0),(11,1,17,0),(12,2,18,0),(13,2,19,0),(14,2,23,0),(15,2,24,0),(16,2,26,0),(17,2,27,0),(18,2,29,0),(19,3,30,0);
/*!40000 ALTER TABLE `Module_Question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Question`
--

LOCK TABLES `Question` WRITE;
/*!40000 ALTER TABLE `Question` DISABLE KEYS */;
INSERT INTO `Question` VALUES (1,'State the domain type for your IoT system',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(2,'Will the system have a user?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(3,'Will the system have user LogIn?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(4,'Will the system hold any user information?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(5,'Will the system store any kind of information?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(6,'What will be the level of information stored?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(7,'Will this information be sent to an entity?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(8,'Will the system be connected to the internet?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(9,'Will it send its data to a cloud?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(10,' Will it store data in a db?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(11,'Will the system receive regular updates?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(12,'Will the system work with third-party software?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(13,' Is there a possibility of the communications being eavesdropped?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(14,'Could the messages sent between the system components be captured and resent?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(15,'Can someone try to impersonate a user to gain access to private information?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(16,'Can someone with bad intentions gain physical access to the location where  this software will be running and obtain private information?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(17,' Can someone gain physical access to the machine where the system operates or some of the system components and preform some type of modification to ?',NULL,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(18,'What is the architecture of the system ?',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(19,'Does the system use a database ?',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(20,'What is the type of the data storage ?',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(21,'Which database is used ?',NULL,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(22,'What is the type of data stored ?',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(23,'Which type of authentication will be implemented ?',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(24,'Will there be user registration ?',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(25,'Which way of user registration will be used ?',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(26,'Which programming languages will be used in the implementation of the system ?',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(27,'Will the system allow input forms ?',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(28,'Will the system allow file upload ?',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(29,'Will the system have logging ?',NULL,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(30,'Please, specify if you have a 16 or 32 bit CPU.',NULL,'2020-08-12 15:36:24','2020-08-12 15:36:24');
/*!40000 ALTER TABLE `Question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Question_Answer`
--

LOCK TABLES `Question_Answer` WRITE;
/*!40000 ALTER TABLE `Question_Answer` DISABLE KEYS */;
INSERT INTO `Question_Answer` VALUES (1,1,1,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(2,1,2,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(3,1,3,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(4,1,4,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(5,1,5,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(6,1,6,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(7,2,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(8,3,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(9,3,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(10,4,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(11,4,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(12,5,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(13,5,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(14,6,9,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(15,6,10,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(16,6,11,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(17,7,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(18,7,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(19,2,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(20,8,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(21,9,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(22,9,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(23,8,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(24,10,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(25,10,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(26,11,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(27,11,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(28,12,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(29,12,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(30,13,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(31,13,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(32,14,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(33,14,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(34,15,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(35,15,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(36,16,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(37,16,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(38,17,7,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(39,17,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(40,18,12,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(41,18,13,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(42,18,14,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(43,18,15,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(44,18,16,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(45,18,17,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(46,18,18,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(47,18,19,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(48,19,7,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(49,20,20,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(50,20,21,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(51,20,22,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(52,20,23,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(53,21,24,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(54,21,25,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(55,21,26,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(56,21,27,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(57,21,28,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(58,21,29,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(59,21,30,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(60,21,31,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(61,21,32,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(62,21,33,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(63,22,34,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(64,22,35,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(65,22,36,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(66,22,33,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(67,19,8,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(68,23,37,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(69,23,38,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(70,23,39,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(71,23,40,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(72,23,41,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(73,23,42,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(74,23,43,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(75,24,7,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(76,25,44,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(77,25,45,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(78,24,46,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(79,26,47,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(80,26,48,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(81,26,49,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(82,26,50,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(83,26,51,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(84,26,52,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(85,26,53,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(86,26,33,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(87,27,7,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(88,28,7,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(89,28,8,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(90,27,8,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(91,29,7,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(92,29,8,'2020-08-12 15:11:12','2020-08-12 15:11:12');
/*!40000 ALTER TABLE `Question_Answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Question_has_Child`
--

LOCK TABLES `Question_has_Child` WRITE;
/*!40000 ALTER TABLE `Question_has_Child` DISABLE KEYS */;
INSERT INTO `Question_has_Child` VALUES (1,2,3,7,0,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(2,2,4,7,0,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(3,2,5,7,0,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(4,2,6,7,0,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(5,2,7,7,0,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(6,8,9,7,0,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(7,19,20,7,0,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(8,19,21,7,0,'2020-08-12 15:11:11','2020-08-12 15:11:11'),(9,19,22,7,0,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(10,24,25,7,0,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(11,27,28,7,0,'2020-08-12 15:11:12','2020-08-12 15:11:12');
/*!40000 ALTER TABLE `Question_has_Child` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Recommendation`
--

LOCK TABLES `Recommendation` WRITE;
/*!40000 ALTER TABLE `Recommendation` DISABLE KEYS */;
INSERT INTO `Recommendation` VALUES (1,'Confidentiality','The property that ensures that information is not disclosed or made available to any unauthorized entity. In other words,personal information cannot be accessed by an unauthorized third party. This requirement is applied were the information is stored.','recommendation_1.md','2020-08-11 16:15:59','2020-08-11 16:15:59'),(2,'Integrity','Is the property of safeguarding the correctness and completeness of assets in an IoT system. In other words it involves maintaining the data consistent,  trustworthy and accurate during it life-cycle. ','recommendation_2.md','2020-08-11 16:16:16','2020-08-11 16:16:16'),(3,'Availability','Refers to the property which ensures that an IoT device or system is accessible and usable upon demand by authorized entities. In other words the  device needs to be always available to access by authorized people. ','recommendation_3.md','2020-08-11 16:16:33','2020-08-11 16:16:33'),(4,'Authentication','Is the assurance that information transaction is from the source it claims to be from. The device authenticates itself prior to receiving or transmitting any information. It assures that the information received is authentic.  ','recommendation_4.md','2020-08-11 16:16:47','2020-08-11 16:16:47'),(5,'Authorization','The property that determines whether the user or device has rights/privileges to access a resource, or issue commands.','recommendation_5.md','2020-08-11 16:17:00','2020-08-11 16:17:00'),(6,'Non-Repudiation','The security property that ensures that the transfer of messages or credentials between 2 IoT entities is undeniable.',NULL,'2020-08-11 16:17:09','2020-08-11 16:17:09'),(7,'Accountability','The property that ensures that every action can be traced back to a single user or device. This requirement is applied over Internet transactions.',NULL,'2020-08-11 16:17:27','2020-08-11 16:17:27'),(8,'Reliability','Refers to the property that guarantees consistent intended behavior of an a general system, in this case applied to IoT.',NULL,'2020-08-11 16:17:35','2020-08-11 16:17:35'),(9,'Privacy','In the context of IoT, privacy refers to the control of the user over the disclosure of his data. In other words only the user has control of the sharing of is personal information, is data is only made public if the user allowed it. This requirement is applied were the information is stored.',NULL,'2020-08-11 16:17:48','2020-08-11 16:17:48'),(10,'Physical Security','Refers to the security measures designed to deny unauthorized physical access to IoT devices and equipment, and to protect them from damage or in other words gaining physical access to the device won\'t give access to it\'s information.',NULL,'2020-08-11 16:17:58','2020-08-11 16:17:58'),(11,'Forgery Resistance','Is the propriety that ensures that the contents shared between entities cannot be forged by a third party trying to damage or harm the system or its users. In other words no one can try to forge content and send it in the name of another entities.',NULL,'2020-08-11 16:18:05','2020-08-11 16:18:05'),(12,'Tamper Detection','Ensures all devices are physically secured, such that any tampering attempt is detected.',NULL,'2020-08-11 16:18:12','2020-08-11 16:18:12'),(13,'Data Freshness','Status that ensures that data is the most recent, and that old messages are not mistakenly used as fresh or purposely replayed by perpetrators. In other words this requirement provides the guarantee that the data displayed is the most recent.',NULL,'2020-08-11 16:18:21','2020-08-11 16:18:21'),(14,'Confinement','Ensures that even if a party is corrupted, the spreading of the effects of the attack is as confined as possible.',NULL,'2020-08-11 16:18:30','2020-08-11 16:18:30'),(15,'Interoperability','Is the propriety that ensures that different software communicates and works well with each-other. I.e a software in health-care that works with data that comes from a third-party needs to be able to use and process the information given to it by this software.',NULL,'2020-08-11 16:18:37','2020-08-11 16:18:37'),(16,'Data Origin','Ensures that the data being received by the software comes from the source it claims to be. In other words it ensures that the data being received is authentic and from a trusted party.',NULL,'2020-08-11 16:18:44','2020-08-11 16:18:44'),(17,'IoT Security Guidelines',NULL,'recommendation_17.md','2020-08-12 14:56:53','2020-08-12 14:56:53'),(18,'SQL Injection Prevention',NULL,'recommendation_18.md','2020-08-12 14:57:32','2020-08-12 14:57:32'),(19,'Upgrade CPU to 32bit','In computer architecture, 32-bit integers, memory addresses, or other data units are those that are 32 bits (4 octets) wide.',NULL,'2020-08-12 15:21:36','2020-08-12 15:21:36'),(20,'Upgrade CPU to 64bit','In computer architecture, 64-bit integers, memory addresses, or other data units are those that are 64 bits (8 octets) wide.',NULL,'2020-08-12 15:21:58','2020-08-12 15:21:58');
/*!40000 ALTER TABLE `Recommendation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Recommendation_Question_Answer`
--

LOCK TABLES `Recommendation_Question_Answer` WRITE;
/*!40000 ALTER TABLE `Recommendation_Question_Answer` DISABLE KEYS */;
INSERT INTO `Recommendation_Question_Answer` VALUES (1,1,1,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(2,1,2,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(3,1,4,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(4,1,6,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(5,2,1,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(6,2,2,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(7,2,3,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(8,2,4,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(9,2,5,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(10,2,6,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(11,2,20,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(12,2,24,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(13,3,1,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(14,3,2,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(15,3,4,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(16,3,5,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(17,3,6,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(18,3,21,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(19,3,24,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(20,3,26,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(21,4,1,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(22,4,2,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(23,4,3,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(24,4,6,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(25,4,8,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(26,4,24,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(27,4,34,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(28,5,1,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(29,5,2,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(30,5,3,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(31,5,4,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(32,5,6,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(33,5,15,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(34,5,16,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(35,5,30,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(36,6,2,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(37,6,3,'2020-08-11 16:49:25','2020-08-11 16:49:25'),(38,6,6,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(39,6,8,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(40,6,16,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(41,6,17,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(42,6,20,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(43,6,21,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(44,6,24,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(45,7,1,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(46,7,2,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(47,7,3,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(48,7,6,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(49,7,20,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(50,8,1,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(51,8,2,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(52,8,3,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(53,8,4,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(54,8,6,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(55,9,1,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(56,9,2,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(57,9,4,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(58,9,5,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(59,9,6,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(60,9,10,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(61,9,12,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(62,9,14,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(63,9,15,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(64,9,16,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(65,10,1,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(66,10,2,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(67,10,3,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(68,10,4,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(69,10,6,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(70,10,14,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(71,10,15,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(72,10,16,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(73,10,36,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(74,11,15,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(75,11,16,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(76,11,24,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(77,12,5,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(78,12,36,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(79,13,21,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(80,13,34,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(81,1,17,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(82,1,28,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(83,15,28,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(84,16,32,'2020-08-11 16:49:26','2020-08-11 16:49:26'),(85,17,40,'2020-08-12 15:11:12','2020-08-12 15:11:12'),(86,18,75,'2020-08-12 15:11:12','2020-08-12 15:11:12');
/*!40000 ALTER TABLE `Recommendation_Question_Answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Session`
--

LOCK TABLES `Session` WRITE;
/*!40000 ALTER TABLE `Session` DISABLE KEYS */;
INSERT INTO `Session` VALUES (29,1,1,1,'2020-09-30 11:27:56','2020-09-30 11:28:11'),(30,1,1,1,'2020-09-30 11:35:56','2020-09-30 11:36:07'),(31,1,3,0,'2020-09-30 11:37:21','2020-09-30 11:37:21');
/*!40000 ALTER TABLE `Session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Session_Recommendation`
--

LOCK TABLES `Session_Recommendation` WRITE;
/*!40000 ALTER TABLE `Session_Recommendation` DISABLE KEYS */;
INSERT INTO `Session_Recommendation` VALUES (46,30,1,'2020-09-30 11:36:07','2020-09-30 11:36:07'),(47,30,2,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(48,30,3,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(49,30,4,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(50,30,5,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(51,30,7,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(52,30,8,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(53,30,9,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(54,30,10,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(55,30,6,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(56,30,13,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(57,30,11,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(58,30,15,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(59,30,16,'2020-09-30 11:36:08','2020-09-30 11:36:08'),(60,30,12,'2020-09-30 11:36:08','2020-09-30 11:36:08');
/*!40000 ALTER TABLE `Session_Recommendation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Session_User_Answer`
--

LOCK TABLES `Session_User_Answer` WRITE;
/*!40000 ALTER TABLE `Session_User_Answer` DISABLE KEYS */;
INSERT INTO `Session_User_Answer` VALUES (101,29,1,NULL,NULL,'2020-09-30 11:27:57','2020-09-30 11:27:57'),(102,29,7,NULL,NULL,'2020-09-30 11:27:58','2020-09-30 11:27:58'),(103,29,8,NULL,NULL,'2020-09-30 11:27:58','2020-09-30 11:27:58'),(104,29,10,NULL,NULL,'2020-09-30 11:27:59','2020-09-30 11:27:59'),(105,29,12,NULL,NULL,'2020-09-30 11:27:59','2020-09-30 11:27:59'),(106,29,14,NULL,NULL,'2020-09-30 11:28:00','2020-09-30 11:28:00'),(107,29,17,NULL,NULL,'2020-09-30 11:28:00','2020-09-30 11:28:00'),(108,29,20,NULL,NULL,'2020-09-30 11:28:01','2020-09-30 11:28:01'),(109,29,21,NULL,NULL,'2020-09-30 11:28:01','2020-09-30 11:28:01'),(110,29,24,NULL,NULL,'2020-09-30 11:28:02','2020-09-30 11:28:02'),(111,29,26,NULL,NULL,'2020-09-30 11:28:02','2020-09-30 11:28:02'),(112,29,28,NULL,NULL,'2020-09-30 11:28:03','2020-09-30 11:28:03'),(113,29,30,NULL,NULL,'2020-09-30 11:28:04','2020-09-30 11:28:04'),(114,29,32,NULL,NULL,'2020-09-30 11:28:04','2020-09-30 11:28:04'),(115,29,34,NULL,NULL,'2020-09-30 11:28:05','2020-09-30 11:28:05'),(116,29,36,NULL,NULL,'2020-09-30 11:28:05','2020-09-30 11:28:05'),(117,29,38,NULL,NULL,'2020-09-30 11:28:06','2020-09-30 11:28:06'),(119,30,1,NULL,NULL,'2020-09-30 11:35:58','2020-09-30 11:35:58'),(120,30,7,NULL,NULL,'2020-09-30 11:35:58','2020-09-30 11:35:58'),(121,30,8,NULL,NULL,'2020-09-30 11:35:59','2020-09-30 11:35:59'),(122,30,10,NULL,NULL,'2020-09-30 11:36:00','2020-09-30 11:36:00'),(123,30,12,NULL,NULL,'2020-09-30 11:36:00','2020-09-30 11:36:00'),(124,30,14,NULL,NULL,'2020-09-30 11:36:02','2020-09-30 11:36:02'),(125,30,17,NULL,NULL,'2020-09-30 11:36:02','2020-09-30 11:36:02'),(126,30,20,NULL,NULL,'2020-09-30 11:36:03','2020-09-30 11:36:03'),(127,30,21,NULL,NULL,'2020-09-30 11:36:03','2020-09-30 11:36:03'),(128,30,24,NULL,NULL,'2020-09-30 11:36:04','2020-09-30 11:36:04'),(129,30,26,NULL,NULL,'2020-09-30 11:36:05','2020-09-30 11:36:05'),(130,30,28,NULL,NULL,'2020-09-30 11:36:05','2020-09-30 11:36:05'),(131,30,30,NULL,NULL,'2020-09-30 11:36:06','2020-09-30 11:36:06'),(132,30,32,NULL,NULL,'2020-09-30 11:36:06','2020-09-30 11:36:06'),(133,30,34,NULL,NULL,'2020-09-30 11:36:06','2020-09-30 11:36:06'),(134,30,36,NULL,NULL,'2020-09-30 11:36:07','2020-09-30 11:36:07'),(135,30,38,NULL,NULL,'2020-09-30 11:36:07','2020-09-30 11:36:07');
/*!40000 ALTER TABLE `Session_User_Answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Type`
--

LOCK TABLES `Type` WRITE;
/*!40000 ALTER TABLE `Type` DISABLE KEYS */;
/*!40000 ALTER TABLE `Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'user@SAM.pt','Forrest','Gump','6e68eff9ad873e8df6d25fce9282fb9bfbd3f8f6ff32a639a42963448787d88a:7e3627579e1e4304874ce442f2e50760',NULL,1,NULL,NULL,NULL),(2,'admin@SAM.pt','Ellen','Ripley','6e68eff9ad873e8df6d25fce9282fb9bfbd3f8f6ff32a639a42963448787d88a:7e3627579e1e4304874ce442f2e50760',NULL,1,1,NULL,NULL);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `User_Group`
--

LOCK TABLES `User_Group` WRITE;
/*!40000 ALTER TABLE `User_Group` DISABLE KEYS */;
INSERT INTO `User_Group` VALUES (1,1,1,NULL,NULL),(2,2,1,NULL,NULL);
/*!40000 ALTER TABLE `User_Group` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-30 12:11:43
