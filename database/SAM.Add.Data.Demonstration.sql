-- MySQL dump 10.19  Distrib 10.3.28-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: sam
-- ------------------------------------------------------
-- Server version	10.3.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (1,'Smart Home',NULL,'2020-10-23 14:58:36','2020-11-06 12:40:43'),(2,'Smart Healthcare',NULL,'2020-10-23 14:58:36','2020-11-06 12:40:43'),(3,'Smart Manufacturing',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(4,'Smart Wearables',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(5,'Smart Toys',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(6,'Smart Transportation',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(7,'Normal',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(8,'Sensitive',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(9,'Critical',NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(10,'Yes',NULL,'2020-10-23 14:58:36','2021-06-08 14:28:02'),(11,'No',NULL,'2020-10-23 14:58:36','2021-06-08 14:28:02'),(12,'Web Application',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(13,'Web Service',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(14,'Desktop Application',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(15,'Mobile Application',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(16,'Client-Server -> Client Component',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(17,'Client-Server -> Server Component',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(18,'API Service',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(19,'Embedded System',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(20,'Others',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(21,'SQL',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(22,'NoSQL',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(23,'Local Storage',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(24,'Distributed Storage',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(25,'SQL Server',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(26,'MySQL',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(27,'PostgresSQL',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(28,'SQLite',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(29,'OracleDB',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(30,'MariaDB',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(31,'MongoDB',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(32,'CosmosDB',NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(33,'DynamoDB',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:50'),(34,'Cassandra',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(35,'Personal Information (Names, Addresses...)',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(36,'Confidential Data',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(37,'Critical Data',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(38,'No Authentication',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(39,'Username and Password',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(40,'Social Networks/Google',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(41,'SmartCard',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(42,'Biometric',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(43,'Two Factor Authentication',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(44,'Multi Factor Authentication',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(45,'The users will register themselves',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(46,'An administrator will register the users',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(47,'C/C++',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(48,'Java',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(49,'Javascript',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(50,'PHP',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(51,'Python',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(52,'Ruby',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(53,'Other/Proprietary Language',NULL,'2020-10-23 14:58:37','2020-10-23 17:13:51'),(54,'Hardware',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(55,'Field-programmable Gate Array (FPGA)',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(56,'Application-specific Integrated Circuit (ASIC)',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(57,'Low Power',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(58,'Ultra-low Power',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(59,'Software',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(60,'Conception, Planning, Analysis, Design',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(61,'Existing System',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(62,'ARM (32 or 64-bit RISC CPU)',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(63,'AVR (8 or 32-bit RISC CPU)',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(64,'MSP (16-bit RISC CPU)',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(65,'PIC (8, 16 or 32-bit RISC CPU)',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(66,'Other',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(67,'8-bit',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(68,'16-bit',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(69,'32-bit',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(70,'64-bit',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(71,'Smart City',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(72,'Smart Agriculture',NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(73,'Smart Grid',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:43'),(74,'Smart Elderly Monitoring',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:43'),(75,'Smart Kid Monitoring',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:43'),(76,'Smart Pet Monitoring',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:43'),(77,'Smart Banking/Financial applications',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:43'),(78,'Industrial Automation',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:43'),(79,'Smart Supply Chain',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:43'),(80,'Smart Retail',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:43'),(81,'Smart Environmental Monitoring',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:43'),(82,'Smart Automotive/Transportation',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:44'),(83,'Connected Car',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:44'),(84,'Other Domain',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:44'),(85,'Small (1-128 bytes)',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:44'),(86,'Average (129-256 bytes)',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:44'),(87,'Large (> 256 bytes)',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:44'),(88,'Continuous',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:44'),(89,'Unknown',NULL,'2020-10-26 17:17:43','2020-11-06 12:40:44'),(90,'Android Application',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(91,'iOS Application',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(92,'Hybrid Application',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(93,'Sailfish OS Application',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(94,'Tizen Application',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(95,'Ubuntu Touch Application',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(96,'Game',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(97,'m-Commerce',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(98,'m-Health',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(99,'m-Learning',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(100,'m-Payment',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(101,'m-Social Networking',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(102,'m-Tourism',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(103,'Multi-user Collaboration',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(104,'Entertainment',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(105,'Smart Air Quality',NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(106,'Smart Manufacturing ',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(107,'Smart Wearables ',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(108,'Biometrics',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(109,'Mult Factor Authentication',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(110,'Local Database',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(111,'Remote Database',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(112,'Both',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(113,'Personal Information (Names, Address,...)',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(114,'Personal Information & Confidential Data',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(115,'Personal Information & Critical Data',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(116,'All',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(117,'Will be an administrator that will register the users',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(118,'C#',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(119,'HTML5 + CSS + JavaScript',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(120,'Java (Android)',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(121,'Objective C',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(122,'Perl',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(123,'Swift',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(124,'Kotlin',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(125,'None',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(126,'HTML',NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(127,'Community Cloud (Remote connection)',NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(128,'Public Cloud (Remote connection)',NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(129,'Private Cloud (Local connection)',NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(130,'Hybrid Cloud (Mix Connection)',NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(131,'Virtual Private Cloud',NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(132,'Hongmeng OS',NULL,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(133,'Mobile Game',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(134,'Mult User Collaboration',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(135,'Smart Waste Monitoring',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(136,'Social Networks / Google',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(137,'PostgreSQL',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(138,'JADE',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(139,'HBase',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(140,'Neo4j',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(141,'Redis',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(142,'Will be a administrator that will register the users',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(143,'C/C++/Objective C',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(144,'HTML5',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(145,'Other/Property Language',NULL,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(146,'Symmetric Key',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(147,'Basic Authentication (user/pass)',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(148,'Certificates (X.509)',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(149,'TPM (Trusted Platform Module)',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(150,'4G / LTE',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(151,'3G',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(152,'GSM (2G)',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(153,'Radio Frequency',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(154,'Bluetooth',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(155,'Wi-Fi',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(156,'GPS',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(157,'RFID',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(158,'NFC',NULL,'2020-11-26 18:55:27','2020-11-26 18:55:27');
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_Answer_Update BEFORE UPDATE on Answer
FOR EACH ROW
	SET NEW.updatedon = NOW() */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_Answer_Delete BEFORE DELETE on Answer
FOR EACH ROW
	-- Delete sessions linked to this question
    DELETE FROM Session WHERE 
    Session.id IN (SELECT SessionID FROM Session_User_Answer WHERE questionAnswerID IN (SELECT ID FROM Question_Answer WHERE answerID = OLD.ID)) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `auth_token_blacklist`
--

DROP TABLE IF EXISTS `auth_token_blacklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_token_blacklist` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `token` varchar(255) NOT NULL COMMENT 'Avoid doubles',
  `createdOn` datetime NOT NULL DEFAULT current_timestamp(),
  `updatedOn` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `token_UNIQUE` (`token`),
  KEY `fk_Auth_Token_Blacklist_User1_idx` (`userID`),
  CONSTRAINT `fk_Auth_Token_Blacklist_User1` FOREIGN KEY (`userID`) REFERENCES `user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=335 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_token_blacklist`
--

LOCK TABLES `auth_token_blacklist` WRITE;
/*!40000 ALTER TABLE `auth_token_blacklist` DISABLE KEYS */;
INSERT INTO `auth_token_blacklist` VALUES (328,1,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZW1haWwiOiJ1c2VyQFNBTS5wdCIsImF2YXRhciI6bnVsbCwiaXNfYWRtaW4iOm51bGwsImV4cCI6MTYyMzI2MzM5OX0.WV-l3oYiSyyoKwge3dlOMgrGLSwTjzuYebVjS8AmNes','2021-06-08 19:31:12','2021-06-08 19:31:12'),(331,2,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZW1haWwiOiJhZG1pbkBTQU0ucHQiLCJhdmF0YXIiOm51bGwsImlzX2FkbWluIjoxLCJleHAiOjE2MjMyNjQ3MDZ9.gdtMCFBt_q_h2MiXZrcLmaqowF3kceRjkq1CNgbX7o4','2021-06-08 19:52:48','2021-06-08 19:52:48'),(332,4,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwiZW1haWwiOiJjYXJvbGluYUBTQU0ucHQiLCJhdmF0YXIiOiJkZWZhdWx0IiwiaXNfYWRtaW4iOjAsImV4cCI6MTYyMzI2NDc3M30.tU7cGCuag-3Gg7kQuVvBBj0M7o-Uo7l5DNbzmVinou4','2021-06-08 20:06:40','2021-06-08 20:06:40'),(334,3,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZW1haWwiOiJqb2FuYUBTQU0ucHQiLCJhdmF0YXIiOiJkZWZhdWx0IiwiaXNfYWRtaW4iOjAsImV4cCI6MTYyMzMxNzE0Mn0.iphLGjdxdgWmXnsbrk92-dF2uyHxd9N3ipvFCqWTBLs','2021-06-09 14:57:05','2021-06-09 14:57:05');
/*!40000 ALTER TABLE `auth_token_blacklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dependency`
--

DROP TABLE IF EXISTS `dependency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dependency` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `moduleID` int(11) NOT NULL,
  `dependsOn` int(11) NOT NULL,
  `createdOn` datetime NOT NULL DEFAULT current_timestamp(),
  `updatedOn` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `moduleID_dependsOn_UNIQUE` (`moduleID`,`dependsOn`),
  KEY `fk_Dependency_Module1_idx` (`moduleID`),
  KEY `fk_Dependency_Module2_idx` (`dependsOn`),
  CONSTRAINT `fk_Dependency_Module1` FOREIGN KEY (`moduleID`) REFERENCES `module` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Dependency_Module2` FOREIGN KEY (`dependsOn`) REFERENCES `module` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dependency`
--

LOCK TABLES `dependency` WRITE;
/*!40000 ALTER TABLE `dependency` DISABLE KEYS */;
INSERT INTO `dependency` VALUES (1,3,1,'2020-10-26 16:56:40','2020-10-26 16:56:40'),(2,6,1,'2021-04-05 15:17:47','2021-04-05 15:17:47'),(3,6,2,'2021-04-05 15:17:47','2021-04-05 15:17:47'),(8,8,3,'2021-06-08 19:28:20','2021-06-08 19:28:20'),(9,8,6,'2021-06-08 19:28:20','2021-06-08 19:28:20');
/*!40000 ALTER TABLE `dependency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group`
--

DROP TABLE IF EXISTS `group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `designation` varchar(45) NOT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
INSERT INTO `group` VALUES (1,'Test Users',NULL,NULL);
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_Group_Update BEFORE UPDATE on SAM.Group
FOR EACH ROW
	SET NEW.updatedon = NOW() */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `module`
--

DROP TABLE IF EXISTS `module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `module` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `typeID` int(11) DEFAULT NULL,
  `shortname` varchar(45) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `displayName` varchar(45) NOT NULL,
  `logicFileName` varchar(45) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `avatar` varchar(45) DEFAULT NULL,
  `createdOn` datetime NOT NULL DEFAULT current_timestamp(),
  `updatedOn` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  KEY `fk_Module_Type1_idx` (`typeID`),
  CONSTRAINT `fk_Module_Type1` FOREIGN KEY (`typeID`) REFERENCES `type` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module`
--

LOCK TABLES `module` WRITE;
/*!40000 ALTER TABLE `module` DISABLE KEYS */;
INSERT INTO `module` VALUES (1,1,'SRE','Security Requirements Elicitation','Security Requirements','logic_1.py',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(2,2,'SBPG','Security Best Pratice Guidelines','Security Best Pratices',NULL,NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(3,3,'LWCAR','LightWeight Criptographic Algorithm Recommendation','LightWeight Criptographic Algorithm','logic_3.py',NULL,NULL,'2020-10-26 16:56:40','2020-11-06 12:40:43'),(4,1,'CSRE','Cloud Security Requirements Elicitation','Cloud Security Requirements','logic_4.py',NULL,NULL,'2020-10-27 11:10:50','2020-10-27 11:10:52'),(5,2,'CSBPG','Cloud Security Best Pratice Guidelines ','Cloud Security Best Pratice Guidelines ','logic_5.py',NULL,NULL,'2020-11-26 18:55:25','2020-11-26 18:55:27'),(6,NULL,'TMS','Threat Modeling Solution','Threat Modeling','logic_6.py',NULL,NULL,'2021-04-05 15:17:47','2021-06-08 14:28:01'),(8,NULL,'ACISM','Assessment of the Correct Integration of Security Mechanisms','Assessment of the Integration of Security','logic_8.py',NULL,NULL,'2021-06-08 19:28:20','2021-06-08 19:29:16');
/*!40000 ALTER TABLE `module` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_Module_Update BEFORE UPDATE on Module
FOR EACH ROW
	SET NEW.updatedon = NOW() */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `module_group`
--

DROP TABLE IF EXISTS `module_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `module_group` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `moduleID` int(11) NOT NULL,
  `groupID` int(11) NOT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `moduleID_groupID_unique` (`moduleID`,`groupID`),
  KEY `fk_Module_has_Group_Group1_idx` (`groupID`),
  KEY `fk_Module_has_Group_Module1_idx` (`moduleID`),
  CONSTRAINT `fk_Module_has_Group_Group1` FOREIGN KEY (`groupID`) REFERENCES `group` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Module_has_Group_Module1` FOREIGN KEY (`moduleID`) REFERENCES `module` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module_group`
--

LOCK TABLES `module_group` WRITE;
/*!40000 ALTER TABLE `module_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `module_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `module_question`
--

DROP TABLE IF EXISTS `module_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `module_question` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `moduleID` int(11) NOT NULL,
  `questionID` int(11) NOT NULL,
  `questionOrder` int(11) NOT NULL COMMENT 'If the current question should be show in first, second, … place. ',
  PRIMARY KEY (`ID`),
  KEY `fk_Module_has_Question_Question1_idx` (`questionID`),
  KEY `fk_Module_has_Question_Module_idx` (`moduleID`),
  CONSTRAINT `fk_Module_has_Question_Module` FOREIGN KEY (`moduleID`) REFERENCES `module` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Module_has_Question_Question1` FOREIGN KEY (`questionID`) REFERENCES `question` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module_question`
--

LOCK TABLES `module_question` WRITE;
/*!40000 ALTER TABLE `module_question` DISABLE KEYS */;
INSERT INTO `module_question` VALUES (1,1,1,1),(2,1,2,2),(3,1,8,3),(4,1,10,4),(5,1,11,5),(6,1,12,6),(7,1,13,7),(8,1,14,8),(9,1,15,9),(10,1,16,10),(11,1,17,10),(12,2,18,1),(13,2,19,2),(14,2,23,3),(15,2,24,4),(16,2,26,5),(17,2,27,6),(18,2,29,8),(22,3,30,0),(23,3,42,0),(24,3,43,0),(25,4,44,0),(26,4,45,0),(27,4,46,0),(28,4,47,0),(29,4,51,0),(30,4,53,0),(31,4,54,0),(32,4,55,0),(33,4,56,0),(34,4,57,0),(35,4,58,0),(36,4,59,0),(37,4,60,0),(38,4,61,0),(39,4,62,0),(40,5,63,0),(41,5,64,0),(42,5,65,0),(43,5,66,0),(44,5,71,0),(45,5,73,0),(46,5,74,0),(47,5,75,0),(48,5,76,0),(49,5,77,0),(50,5,78,0),(51,5,79,0),(52,5,80,0),(53,6,96,0),(54,6,97,0),(55,6,98,0),(59,6,104,0),(60,6,105,0),(61,6,106,0),(62,6,107,0),(63,6,108,0),(64,6,109,0),(65,6,116,0);
/*!40000 ALTER TABLE `module_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `multipleAnswers` tinyint(4) DEFAULT 0,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'Q1 - State the domain type for your IoT system',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(2,'Q2 - Will the system have a user?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(3,'Q2.1 - Will the system have user LogIn?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(4,'Q2.2 - Will the system hold any user information?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(5,'Q2.3 - Will the system store any kind of information?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(6,'Q2.4 - What will be the level of information stored?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(7,'Q2.5 - Will this information be sent to an entity?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:33'),(8,'Q3 - Will the system be connected to the internet?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(9,'Q3.1 - Will it send its data to a cloud?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(10,'Q4 - Will it store data in a db?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(11,'Q5 - Will the system receive regular updates?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(12,'Q6 - Will the system work with third-party software?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(13,'Q7 - Is there a possibility of the communications being eavesdropped?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(14,'Q8 - Could the messages sent between the system components be captured and resent?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(15,'Q9 - Can someone try to impersonate a user to gain access to private information?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(16,'Q10 - Can someone with bad intentions gain physical access to the location where this software will be running and obtain private information?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(17,'Q11 - Can someone gain physical access to the machine where the system operates or some of the system components and preform some type of modification to it?',NULL,NULL,'2020-10-23 14:58:36','2020-10-27 10:31:34'),(18,'Q1 - What is the architecture of the system?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(19,'Q2 - Does the system use a database?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(20,'Q2.1 - What is the type of data storage?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(21,'Q2.2 - Which database is used?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:50'),(22,'Q2.3 - What is the type of data stored?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(23,'Q3 - Which type of authentication will be implemented?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(24,'Q4 - Will there be user registration?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(25,'Q4.1 - Which way of user registration will be used?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(26,'Q5 - Which programming languages will be used in the implementation of the system?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(27,'Q6 - Will the system allow input forms?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(28,'Q6.1 - Will the system allow file uploads?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(29,'Q7 - Will the system have logging?',NULL,NULL,'2020-10-23 14:58:36','2020-10-23 17:13:51'),(30,'Select Implementation Type (Hardware or Software)',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(31,'Select Hardware Type (FPGA or ASIC)',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(32,'Select desired energy performance',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(33,'Enter your circuit area (between 135 and 9000)',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(34,'Enter your throughput (between 0.3 and 6400)',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(35,'What is the development phase of the IoT system, or it is an existing system?',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(36,'Enter Hardware Type (Microcontroller or Single Board Computer)',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(37,'Select your CPU Type',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(38,'Input your CPU bit amount',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(39,'Enter flash memory size (in KB, between 10 and 524288000)',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(40,'Enter RAM size (in KB, between 4 and 16777216)',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(41,'Enter processor speed or frequency (in MHz, greater than 4)',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(42,'Select your application area',NULL,NULL,'2020-10-26 17:17:42','2020-11-06 12:40:43'),(43,'Select your Payload Size',NULL,NULL,'2020-10-26 17:17:43','2020-11-06 12:40:44'),(44,'Which will be the archicteture of the system?',NULL,NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(45,'State the domain type for your Cloud and Mobile system:',NULL,NULL,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(46,'Which type of authentication will be implemented? ',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(47,' Will the system use a database?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(48,'Where the system will store the data?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(49,'What is the type of database?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(50,'Which type of data will be stored?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(51,'There will be a user registration?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(52,'Which way of user registration will be used?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(53,'What programming language will be used in the implementation of the system?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(54,'What programming language will be used in the implementation of the server-side system?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(55,'The system will allow user input forms? ',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(56,'The system will allow upload files?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(57,'The system will have a regist of logs?',NULL,NULL,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(58,'Will the system receive regular updates?',NULL,NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(59,'Will the system work with third-party software?',NULL,NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(60,'In what environment will the system be used?',NULL,NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(61,'Can someone with bad intentions gain physical access to the location where this software will be running and obtain private information? ',NULL,NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(62,'Can someone gain physical access to the machine where the system operates or some of the system components and preform some type of modification to it\'s hardware? ',NULL,NULL,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(63,'What is the architecture of the system ?',NULL,1,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(64,'What is the domain of the system',NULL,1,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(65,'What is the type of authentication implemented in the system ?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(66,'The system use a Database ?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(67,'What is type of data storage ?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(68,'What is the Database used ?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(69,'What is the Database used ?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(70,'What is the type of data stored ?',NULL,1,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(71,'There is a user registration ?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(72,'Which way of user registration it\'s used ?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(73,'What is the programming languages used in the implementation of the system ?',NULL,1,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(74,'The system has user input forms ?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(75,'The system allow upload files ?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(76,'The system has a logging regist?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(77,'The system has a regular updates?',NULL,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(78,'The system uses third-party apps?',NULL,0,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(79,'What is the environment in which the system is used?',NULL,0,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(80,'Do you want to further specify hardware details concerning the system ?',NULL,0,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(81,'What is the type of authentication implemented in hardware?',NULL,0,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(82,'What are the wireless tecnologies presents in hardware?',NULL,1,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(83,'Input your first question',NULL,0,'2021-02-05 18:50:24','2021-02-05 19:46:59'),(84,'Input your question',NULL,0,'2021-02-05 18:50:24','2021-02-05 19:46:59'),(85,'Input your question',NULL,0,'2021-02-05 18:50:24','2021-02-05 19:46:59'),(86,'Input your question',NULL,0,'2021-02-05 18:50:24','2021-02-05 19:46:59'),(87,'Input your question',NULL,0,'2021-02-05 18:50:24','2021-02-05 19:46:59'),(88,'Input your question',NULL,0,'2021-02-05 18:50:25','2021-02-05 19:46:59'),(89,'Input your question',NULL,0,'2021-02-05 19:11:04','2021-02-05 19:46:59'),(90,'Input your first question',NULL,0,'2021-02-05 19:52:13','2021-02-05 19:52:13'),(91,'Input your question',NULL,0,'2021-02-05 19:52:13','2021-02-05 19:52:13'),(92,'Input your question',NULL,0,'2021-02-05 19:52:13','2021-02-05 19:52:13'),(93,'Input your first question',NULL,0,'2021-02-05 19:55:10','2021-02-05 19:55:10'),(94,'Input your question',NULL,0,'2021-02-05 19:55:10','2021-02-05 19:55:10'),(95,'Input your question',NULL,0,'2021-02-05 19:55:10','2021-02-05 19:55:10'),(96,'Will there be any type of cryptographic algorithms?',NULL,0,'2021-04-05 15:17:47','2021-06-08 14:28:01'),(97,'Are there functionalities that need privilege escalation?',NULL,0,'2021-04-05 15:17:47','2021-06-08 14:28:01'),(98,'The system uses XML to store or transport data?',NULL,0,'2021-04-05 15:17:47','2021-06-08 14:28:01'),(104,'Will the system be implemented using a Hardware Description Language?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:01'),(105,'Will the system be outsourced to Outsorced Semiconductor Assembly and Test (OAST) entities?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:01'),(106,'All functionalities are correctly documented?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:01'),(107,'Does the system depend on additional hardware units?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:01'),(108,'Is the system properly isolated/prepared to handle external events?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:01'),(109,'Do you wish to get vulnerabilities regarding the implementation phase of the product?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:01'),(110,'Will the system be tested to evaluate the program behavior?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:01'),(111,'Will the code be actively reviewed and refactored?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:01'),(112,'Is assumed-immutable data stored in write-only memory?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:02'),(113,'The code follows the specifications provided by the third-party software to be used?',NULL,0,'2021-05-03 17:52:51','2021-06-08 14:28:02'),(114,'Is there any protection mechanism assigned to sensitive code (e.g., boot code)?',NULL,0,'2021-05-03 17:52:52','2021-06-08 14:28:02'),(115,'Will unnecessary Debug functionalities be removed from production devices?',NULL,0,'2021-05-03 17:52:52','2021-06-08 14:28:02'),(116,'Will the platform have a standardized error handling mechanism?',NULL,0,'2021-05-03 21:28:03','2021-06-08 14:28:02');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_Question_Update BEFORE UPDATE on Question
FOR EACH ROW
	SET NEW.updatedon = NOW() */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_Question_Delete BEFORE DELETE on Question
FOR EACH ROW
	-- Delete sessions linked to this question
    DELETE FROM Session WHERE 
    Session.id IN (SELECT SessionID FROM Session_User_Answer WHERE questionID = OLD.id OR questionAnswerID IN (SELECT ID FROM Question_Answer WHERE questionID = OLD.ID)) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `question_answer`
--

DROP TABLE IF EXISTS `question_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_answer` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `questionID` int(11) NOT NULL,
  `answerID` int(11) NOT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `questionID_answerID_Unique` (`answerID`,`questionID`),
  KEY `fk_Answer_has_Question_Question1_idx` (`questionID`),
  KEY `fk_Answer_has_Question_Answer1_idx` (`answerID`),
  CONSTRAINT `fk_Answer_has_Question_Answer1` FOREIGN KEY (`answerID`) REFERENCES `answer` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Answer_has_Question_Question1` FOREIGN KEY (`questionID`) REFERENCES `question` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=397 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_answer`
--

LOCK TABLES `question_answer` WRITE;
/*!40000 ALTER TABLE `question_answer` DISABLE KEYS */;
INSERT INTO `question_answer` VALUES (1,1,1,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(2,1,2,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(3,1,3,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(4,1,4,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(5,1,5,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(6,1,6,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(7,6,7,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(8,6,8,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(9,6,9,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(10,18,12,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(11,18,13,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(12,18,14,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(13,18,15,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(14,18,16,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(15,18,17,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(16,18,18,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(17,18,19,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(18,18,20,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(19,20,21,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(20,20,22,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(21,20,23,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(22,20,24,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(23,21,25,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(24,21,26,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(25,21,27,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(26,21,28,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(27,21,29,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(28,21,30,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(29,21,31,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(30,21,32,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(31,21,33,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(32,21,34,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(33,22,35,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(34,22,36,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(35,22,37,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(36,23,38,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(37,23,39,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(38,23,40,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(39,23,41,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(40,23,42,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(41,23,43,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(42,23,44,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(43,25,45,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(44,25,46,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(45,26,47,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(46,26,48,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(47,26,49,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(48,26,50,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(49,26,51,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(50,26,52,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(51,26,53,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(52,21,20,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(53,26,20,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(54,2,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(55,2,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(56,3,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(57,3,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(58,4,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(59,4,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(60,5,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(61,5,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(62,7,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(63,7,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(64,8,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(65,8,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(66,9,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(67,9,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(68,10,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(69,10,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(70,11,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(71,11,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(72,12,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(73,12,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(74,13,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(75,13,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(76,14,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(77,14,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(78,15,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(79,15,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(80,16,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(81,17,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(82,19,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(83,19,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(84,24,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(85,24,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(86,27,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(87,27,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(88,28,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(89,28,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(90,29,10,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(91,29,11,'2020-10-23 14:58:37','2020-10-23 14:58:37'),(131,30,54,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(132,31,55,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(133,31,56,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(134,32,57,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(135,32,58,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(136,30,59,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(137,35,60,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(138,35,61,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(139,36,62,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(140,36,63,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(141,36,64,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(142,36,65,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(143,36,66,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(144,37,67,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(145,37,68,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(146,37,69,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(147,37,70,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(148,37,66,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(149,42,1,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(150,42,71,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(151,42,72,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(152,42,73,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(153,42,2,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(154,42,74,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(155,42,75,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(156,42,76,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(157,42,77,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(158,42,78,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(159,42,79,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(160,42,80,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(161,42,81,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(162,42,82,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(163,42,83,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(164,42,84,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(165,43,85,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(166,43,86,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(167,43,87,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(168,43,88,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(169,43,89,'2020-10-26 17:17:43','2020-10-26 17:17:43'),(170,16,11,'2020-10-27 10:31:19','2020-10-27 10:31:19'),(171,17,10,'2020-10-27 10:31:19','2020-10-27 10:31:19'),(172,44,90,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(173,44,91,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(174,44,92,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(175,44,93,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(176,44,94,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(177,44,95,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(178,44,12,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(179,45,96,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(180,45,97,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(181,45,98,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(182,45,99,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(183,45,100,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(184,45,101,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(185,45,102,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(186,45,103,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(187,45,104,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(188,45,72,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(189,45,105,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(190,45,2,'2020-10-27 11:10:50','2020-10-27 11:10:50'),(191,45,1,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(192,45,106,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(193,45,6,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(194,45,107,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(195,46,38,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(196,46,39,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(197,46,40,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(198,46,108,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(199,46,43,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(200,46,109,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(201,47,10,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(202,48,110,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(203,48,111,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(204,48,112,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(205,49,21,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(206,49,22,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(207,50,113,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(208,50,36,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(209,50,37,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(210,50,114,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(211,50,115,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(212,50,116,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(213,47,11,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(214,51,10,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(215,52,45,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(216,52,117,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(217,51,11,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(218,53,118,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(219,53,47,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(220,53,119,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(221,53,120,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(222,53,121,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(223,53,122,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(224,53,52,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(225,53,123,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(226,53,124,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(227,53,51,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(228,53,125,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(229,54,118,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(230,54,50,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(231,54,51,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(232,54,126,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(233,54,125,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(234,55,10,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(235,55,11,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(236,56,10,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(237,56,11,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(238,57,10,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(239,57,11,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(240,58,10,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(241,58,11,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(242,59,10,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(243,59,11,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(244,60,127,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(245,60,128,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(246,60,129,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(247,60,130,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(248,60,131,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(249,61,10,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(250,61,11,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(251,62,10,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(252,62,11,'2020-10-27 11:10:52','2020-10-27 11:10:52'),(253,63,90,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(254,63,91,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(255,63,132,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(256,63,92,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(257,63,94,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(258,63,95,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(259,63,12,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(260,63,19,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(261,63,20,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(262,64,104,'2020-11-26 18:55:25','2020-11-26 18:55:25'),(263,64,133,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(264,64,97,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(265,64,98,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(266,64,99,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(267,64,100,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(268,64,101,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(269,64,134,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(270,64,102,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(271,64,72,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(272,64,105,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(273,64,2,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(274,64,1,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(275,64,3,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(276,64,6,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(277,64,135,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(278,64,4,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(279,65,38,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(280,65,39,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(281,65,136,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(282,65,41,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(283,65,108,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(284,65,43,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(285,65,44,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(286,66,10,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(287,67,21,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(288,68,25,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(289,68,26,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(290,68,137,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(291,68,28,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(292,68,29,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(293,68,30,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(294,67,22,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(295,69,34,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(296,69,32,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(297,69,33,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(298,69,138,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(299,69,139,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(300,69,140,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(301,69,141,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(302,69,66,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(303,67,23,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(304,67,24,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(305,70,113,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(306,70,36,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(307,70,37,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(308,70,66,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(309,66,11,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(310,71,10,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(311,72,45,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(312,72,142,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(313,71,11,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(314,73,118,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(315,73,143,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(316,73,144,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(317,73,48,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(318,73,49,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(319,73,50,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(320,73,51,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(321,73,124,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(322,73,52,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(323,73,145,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(324,74,10,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(325,74,11,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(326,75,10,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(327,75,11,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(328,76,10,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(329,76,11,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(330,77,10,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(331,77,11,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(332,78,10,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(333,78,11,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(334,79,127,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(335,79,130,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(336,79,129,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(337,79,128,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(338,79,131,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(339,80,10,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(340,81,38,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(341,81,146,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(342,81,147,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(343,81,148,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(344,81,149,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(345,82,150,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(346,82,151,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(347,82,152,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(348,82,153,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(349,82,154,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(350,82,155,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(351,82,156,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(352,82,157,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(353,82,158,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(354,80,11,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(360,96,10,'2021-04-05 15:17:47','2021-04-05 15:17:47'),(361,96,11,'2021-04-05 15:17:47','2021-04-05 15:17:47'),(362,97,10,'2021-04-05 15:17:47','2021-04-05 15:17:47'),(363,97,11,'2021-04-05 15:17:47','2021-04-05 15:17:47'),(364,98,10,'2021-04-05 15:17:47','2021-04-05 15:17:47'),(365,98,11,'2021-04-05 15:17:47','2021-04-05 15:17:47'),(371,104,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(372,104,11,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(373,105,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(374,105,11,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(375,106,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(376,106,11,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(377,107,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(378,107,11,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(379,108,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(380,108,11,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(381,109,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(382,110,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(383,110,11,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(384,111,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(385,111,11,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(386,112,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(387,112,11,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(388,113,10,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(389,113,11,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(390,114,10,'2021-05-03 17:52:52','2021-05-03 17:52:52'),(391,114,11,'2021-05-03 17:52:52','2021-05-03 17:52:52'),(392,115,10,'2021-05-03 17:52:52','2021-05-03 17:52:52'),(393,115,11,'2021-05-03 17:52:52','2021-05-03 17:52:52'),(394,109,11,'2021-05-03 17:52:52','2021-05-03 17:52:52'),(395,116,10,'2021-05-03 21:28:03','2021-05-03 21:28:03'),(396,116,11,'2021-05-03 21:28:03','2021-05-03 21:28:03');
/*!40000 ALTER TABLE `question_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_has_child`
--

DROP TABLE IF EXISTS `question_has_child`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_has_child` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `parent` int(11) NOT NULL,
  `child` int(11) NOT NULL,
  `ontrigger` int(11) NOT NULL COMMENT 'The answer (ID) that triggers this sub-question (child) to be ask.',
  `questionOrder` int(11) NOT NULL,
  `createdOn` datetime NOT NULL DEFAULT current_timestamp(),
  `updatedOn` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  KEY `fk_Question_has_Question_Question2_idx` (`child`),
  KEY `fk_Question_has_Question_Question1_idx` (`parent`),
  KEY `fk_Question_has_Parent_Answer1_idx` (`ontrigger`),
  CONSTRAINT `fk_Question_has_Parent_Answer1` FOREIGN KEY (`ontrigger`) REFERENCES `answer` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Question_has_Question_Question1` FOREIGN KEY (`parent`) REFERENCES `question` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Question_has_Question_Question2` FOREIGN KEY (`child`) REFERENCES `question` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_has_child`
--

LOCK TABLES `question_has_child` WRITE;
/*!40000 ALTER TABLE `question_has_child` DISABLE KEYS */;
INSERT INTO `question_has_child` VALUES (1,2,3,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(2,2,4,10,2,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(3,2,5,10,3,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(4,2,6,10,4,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(5,2,7,10,5,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(6,8,9,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(10,19,20,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(11,19,21,10,2,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(12,19,22,10,3,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(13,24,25,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(14,27,28,10,1,'2020-10-23 14:58:36','2020-10-23 14:58:36'),(26,30,31,54,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(27,30,32,54,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(28,30,33,54,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(29,30,34,54,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(30,30,35,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(31,30,36,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(32,30,37,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(33,37,38,66,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(34,30,39,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(35,30,40,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(36,30,41,59,0,'2020-10-26 17:17:42','2020-10-26 17:17:42'),(37,47,48,10,0,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(38,47,49,10,0,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(39,47,50,10,0,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(40,51,52,10,0,'2020-10-27 11:10:51','2020-10-27 11:10:51'),(41,66,67,10,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(42,67,68,21,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(43,67,69,22,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(44,66,70,10,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(45,71,72,10,0,'2020-11-26 18:55:26','2020-11-26 18:55:26'),(46,80,81,10,0,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(47,80,82,10,0,'2020-11-26 18:55:27','2020-11-26 18:55:27'),(53,109,110,10,0,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(54,109,111,10,0,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(55,111,112,11,0,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(56,109,113,10,0,'2021-05-03 17:52:51','2021-05-03 17:52:51'),(57,109,114,10,0,'2021-05-03 17:52:52','2021-05-03 17:52:52'),(58,109,115,10,0,'2021-05-03 17:52:52','2021-05-03 17:52:52');
/*!40000 ALTER TABLE `question_has_child` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recommendation`
--

DROP TABLE IF EXISTS `recommendation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recommendation` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `guideFileName` varchar(45) DEFAULT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=455 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recommendation`
--

LOCK TABLES `recommendation` WRITE;
/*!40000 ALTER TABLE `recommendation` DISABLE KEYS */;
INSERT INTO `recommendation` VALUES (4,'Authentication','Is the assurance that information transaction is from the source it claims to be from. The device authenticates itself prior to receiving or transmitting any information. It assures that the information received is authentic.','recommendation_4.md','2020-10-23 15:37:38','2020-10-23 15:37:38'),(5,'Access Control',NULL,'recommendation_5.md','2020-10-23 15:42:29','2020-10-23 15:42:29'),(6,'API',NULL,'recommendation_6.md','2020-10-23 15:42:58','2020-10-23 15:42:58'),(7,'Cross Site Scripting',NULL,'recommendation_7.md','2020-10-23 15:43:17','2020-10-23 15:43:17'),(8,'Cryptography',NULL,'recommendation_8.md','2020-10-23 15:43:30','2020-10-23 15:43:30'),(9,'File Upload',NULL,'recommendation_9.md','2020-10-23 15:43:42','2020-10-23 15:43:42'),(10,'Input Validation',NULL,'recommendation_10.md','2020-10-23 15:43:56','2020-10-23 15:43:56'),(11,'IoT Security',NULL,'recommendation_11.md','2020-10-23 15:44:11','2020-10-23 15:44:11'),(12,'Logging',NULL,'recommendation_12.md','2020-10-23 15:44:21','2020-10-23 15:44:21'),(13,'Session Management',NULL,'recommendation_13.md','2020-10-23 15:44:34','2020-10-23 15:44:34'),(14,'SQL Injection',NULL,'recommendation_14.md','2020-10-23 15:44:47','2020-10-23 15:44:47'),(15,'Web Service',NULL,'recommendation_15.md','2020-10-23 15:45:00','2020-10-23 15:45:00'),(26,'Clefia128/128','Stream cipher designed by Hitachi Ltd. It is included in the ISO/IEC 29192, an international standard for lightweight cryptography. It takes two inputs, a 128-bit secret Key and a 64-bit public initialization vector (IV) and produces an 8-bit output on every round. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(27,'Clefia128/192','Conventional block cipher designed by Sony. It has been created to achieve good results both in hardware and software. It ciphers block of length 128 bits under keys of length 192 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(28,'Enocoro_v2-128','Stream cipher designed by Hitachi Ltd. It is included in the ISO/IEC 29192, an international standard for lightweight cryptography. It takes two inputs, a 128-bit secret Key and a 64-bit public initialization vector (IV) and produces an 8-bit output on every round. This recommendation fulfills the Confidentiality and Privacy requirements. A GitHub implementation may be found at https://github.com/entropic-security/enocoro128v2',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(29,'Grain_v1-128','Stream cipher designed by Martin Hell, Thomas Johansson, Alexander Maximov and Willi Meier. The Grain-128 supports a 128-bit secret key and a 96-bit initialization vector. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(30,'Trivium-80','Stream cipher designed by Christophe De Cannière and Bart Preneel. Trivium is a hardware oriented synchronous stream cipher. Generates up to 2^64 bits of key stream from an 80-bit secret key and an 80-bit initial value (IV). This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(31,'MICKEY_2.0-80','Stream cipher designed by Steve Babbage and Matthew Dodd. MICKEY 2.0 is aimed at resource-constrained hardware platforms. It takes two inputs, a 80-bit secret Key and a 80-bit public initialization vector (IV). This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(32,'TWINE64/80','Lightweight block cipher designed by Tomoyasu Suzaki, Kazuhiko Minematsu, Sumio Morioka and Eita Kobayashi. It ciphers block of length 64 bits under keys of length 80 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(33,'TWINE64/128','Lightweight block cipher designed by Tomoyasu Suzaki, Kazuhiko Minematsu, Sumio Morioka and Eita Kobayashi. It ciphers block of length 64 bits under keys of length 128 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(34,'Midori128/128','Lightweight block cipher designed by Banik S. et al. It ciphers block of length 128 bits under keys of length 128 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(35,'SIMON64/128','Lightweight block cipher designed by National Security Agency (NSA). It ciphers block of length 64 bits under keys of length 128 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(36,'Piccolo64/80','Ultra-lightweight block cipher designed by Sony. It ciphers block of length 64 bits under keys of length 80 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(37,'Piccolo64/128','Ultra-lightweight block cipher designed by Sony. It ciphers block of length 64 bits under keys of length 128 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(38,'Midori64/128','Lightweight block cipher designed by Banik S. et al. It ciphers block of length 64 bits under keys of length 128 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(39,'SIMON64/96','Lightweight block cipher designed by National Security Agency (NSA). It ciphers block of length 64 bits under keys of length 96 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(40,'Grain_v1-80','Stream cipher designed by Martin Hell, Thomas Johansson, Alexander Maximov and Willi Meier. The Grain supports a 80-bit secret key and a 96-bit initialization vector. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(41,'PHOTON-80/20/16','Lightweight hash-function designed by Jian Guo, Thomas Peyrin and Axel Poschmann. Its hash output size 80, its input and its output bitrate 20 and 16, respectively. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(42,'Keccak-f[100]','Hash function designed by Guido Bertoni, Joan Daemen, Michaël Peeters and Gilles Van Assche. Its hash output size ranges from 224 to 512 bits. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(43,'SPONGENT-128/128/8','Lightweight cryptographic hashing function designed by Andrey Bogdanov, Miroslav Knežević, Gregor Leander, Deniz Toz, Kerem Varιcι, and Ingrid Verbauwhede. Its hash output size 128. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(44,'PHOTON-256/32/32','Lightweight hash-function designed by Jian Guo, Thomas Peyrin and Axel Poschmann. Its hash output size 256, its input and its output bitrate 32 and 32, respectively. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(45,'SPONGENT-88/80/8','Lightweight cryptographic hashing function designed by Andrey Bogdanov, Miroslav Knežević, Gregor Leander, Deniz Toz, Kerem Varιcι, and Ingrid Verbauwhede. Its hash output size 88. This recommendation fulfills the Integrity and Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(46,'U-QUARK','Lightweight hash function designed by Jean-Philippe Aumasson, Luca Henzen, Willi Meier and María Naya-Plasencia. Its hash output size 136, its input. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(47,'PHOTON-128/16/16','Lightweight hash-function designed by Jian Guo, Thomas Peyrin and Axel Poschmann. Its hash output size 128, its input and its output bitrate 16 and 16, respectively. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(48,'SPONGENT-160/160/16','Lightweight cryptographic hashing function designed by Andrey Bogdanov, Miroslav Knežević, Gregor Leander, Deniz Toz, Kerem Varιcι, and Ingrid Verbauwhede. Its hash output size 160. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(49,'PHOTON-160/36/36','Lightweight hash-function designed by Jian Guo, Thomas Peyrin and Axel Poschmann. Its hash output size 160, its input and its output bitrate 36 and 36, respectively. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(50,'S-QUARK','Lightweight hash function designed by Jean-Philippe Aumasson, Luca Henzen, Willi Meier and María Naya-Plasencia. Its hash output size 256, its input. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(51,'AES-GCM','Authenticated encryption scheme designed by Joan Daemen and Vincent Rijmen. It processes 128-bit blocks, and is programmable for 128-, 192-, and 256-bit key lengths. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(52,'ACORN','Lightweight authenticated cipher designed by Hongjun Wu. It uses 128-bit key and a 128-bit initialization vector and the authentication tag length is less than or equal to 128 bits. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(53,'SILC-PRESENT','Lightweight authenticated cipher designed by A. Bogdanov, L.R. Knudsen, G. Leander, C. Paar, A. Poschmann, M.J.B. Robshaw, Y. Seurin and C. Vikkelsoe. It uses 80-bit key and a 64-bit block length and the authentication tag length equal to 32 bits. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(54,'SILC-AES','Lightweight authenticated cipher designed by Morris J. Dworkin, Elaine B. Barker, James R. Nechvatal, James Foti, Lawrence E. Bassham, E. Roback, James F. Dray Jr. It uses 128-bit key and a 128-bit block length and the authentication tag length equal to 64 bits. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(55,'Deoxys','Authenticated encryption designed by Jérémy Jean, Ivica Nikolić, Thomas Peyrin, Yannick Seurin. It uses 128- or 256-bit key and a 128-bit block length and the authentication tag length equal to 128 bits. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(56,'AES-OTR','Authenticated encryption designed by Kazuhiko Minematsu. It uses 128-, 192- or 256-bit key and the authentication tag length equal to 128 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(57,'Ascon','Authenticated encryption designed by Christoph Dobraunig, Maria Eichlseder, Florian Mendel and Martin Schläffer. It uses 128-bit key and a 64-bit block length and the authentication tag length equal to 128 bits. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(58,'CLOC-AES','Authenticated encryption designed by Tetsu Iwata, Kazuhiko Minematsu, Jian Guo and Sumio Morioka. It uses 128-bit key and a 128-bit block length and the authentication tag length equal to 64 bits. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(59,'JAMBU-AES','Authenticated encryption designed by Hongjun Wu, Tao Huang. It uses 128-bit key and a 64-bit block length and the authentication tag length equal to 64 bits. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(60,'ChaCha20-128','Stream cipher designed by Daniel J. Bernstein. It takes two inputs, a 128-bit secret Key and a 64-bit nonce. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(61,'ChaCha20-256','Stream cipher designed by Daniel J. Bernstein. It takes two inputs, a 256-bit secret Key and a 64-bit nonce. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(62,'SPECK64/128','Lightweight block cipher designed by Ray Beaulieu, Douglas Shors, Jason Smith, Stefan Treatman-Clark, Bryan Weeks and Louis Wingers. It ciphers block of length 64 bits under keys of length 128 bits. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(63,'AES_CTR128/128','Block cipher designed by Vincent Rijmen and Joan Daemen. It supports a 256-bit secret key and a 256-bit initialization vector. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(64,'LED64/80','Block cipher designed by Jian Guo, Thomas Peyrin, Axel Poschmann and Matt Robshaw. It ciphers block of length 64 bits under keys of length 64 and 128 bits. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(65,'SPECK64/96','Lightweight block cipher designed by Ray Beaulieu, Douglas Shors, Jason Smith, Stefan Treatman-Clark, Bryan Weeks and Louis Wingers. It ciphers block of length 64 bits under keys of length 96 bits. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(66,'PRESENT64/80','Block cipher designed by A. Bogdanov, L.R. Knudsen, G. Leander, C. Paar, A. Poschmann, M.J.B. Robshaw, Y. Seurin and C. Vikkelsoe. The block length is 64 bits and one key length of 80 bits is supported. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(67,'PRINCE64/128','Block cipher designed by Julia Borghof et al. The block length is 64 bits and one key length of 128 bits is supported. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(68,'AES_CBC128/128','Block cipher designed by Vincent Rijmen and Joan Daemen. The block length is 128 bits and one key length of 128 bits is supported. This recommendation fulfills the Confidentiality and Authentication requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(69,'CLOC-TWINE','Authenticated encryption designed by Tetsu Iwata, Kazuhiko Minematsu, Jian Guo and Sumio Morioka. It uses 80-bit key and a 64-bit block length and the authentication tag length equal to 32 bits. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(70,'Ketje-SR','Lightweight authenticated encryption designed by Guido Bertoni, Joan Daemen, Michaël Peeters, Gilles Van Assche and Ronny Van Keer. It supports a key of length up to 382-bit and 128-bit authentication tag. This recommendation fulfills the Confidentiality and Authenticity requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(71,'Enocoro-80','Hardware oriented stream cipher designed by Hitachi Ltd. The key length of Enocoro-80 is 80 bits and the IV length is 64 bits. This recommendation fulfills the Confidentiality and Privacy requirements.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(72,'Clefia128/256','Conventional block cipher designed by Sony. It has been created to achieve good results both in hardware and software. It ciphers block of length 128 bits under keys of length 256 bits. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(73,'PRESENT64/128','Block cipher designed by A. Bogdanov, L.R. Knudsen, G. Leander, C. Paar, A. Poschmann, M.J.B. Robshaw, Y. Seurin and C. Vikkelsoe. The block length is 64 bits and one key length of 128 bits is supported. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(74,'SPECK96/144','Lightweight block cipher designed by Ray Beaulieu, Douglas Shors, Jason Smith, Stefan Treatman-Clark, Bryan Weeks and Louis Wingers. It ciphers block of length 96 bits under keys of length 144 bits. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(75,'SPECK48/72','Lightweight block cipher designed by Ray Beaulieu, Douglas Shors, Jason Smith, Stefan Treatman-Clark, Bryan Weeks and Louis Wingers. It ciphers block of length 48 bits under keys of length 72 bits. This recommendation fulfills the Confidentiality requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(76,'PHOTON-224/32/32','Lightweight hash-function designed by Jian Guo, Thomas Peyrin and Axel Poschmann. Its hash output size 224, its input and its output bitrate 32 and 32, respectively. This recommendation fulfills the Integrity requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(77,'SipHash-128','Keyed hash function designed by Jean-Philippe Aumasson and Daniel J. Bernstein. SipHash computes a 128-bit message authentication code from a variable-length message and 128-bit secret key. This recommendation fulfills the Authentication requirement.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(95,'The system is not capable','For an existing system that does not meet the minimum requirements necessary to implement cryptographic algorithms.',NULL,'2020-10-26 16:53:23','2020-10-26 16:53:23'),(96,'Confidentiality','The property that ensures that information is not disclosed or made available to any unauthorized entity. In other words,personal information cannot be accessed by an unauthorized third party. This requirement is applied were the information is stored.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(97,'Integrity','Is the property of safeguarding the correctness and completeness of assets in an IoT system. In other words it involves maintaining the data consistent,  trustworthy and accurate during it life-cycle. ',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(98,'Availability','Refers to the property which ensures that an IoT device or system is accessible and usable upon demand by authorized entities. In other words the  device needs to be always available to access by authorized people. ',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(100,'Authorization','The property that determines whether the user or device has rights/privileges to access a resource, or issue commands.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(101,'Non-Repudiation','The security property that ensures that the transfer of messages or credentials between 2 IoT entities is undeniable.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(102,'Accountability','The property that ensures that every action can be traced back to a single user or device. This requirement is applied over Internet transactions.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(103,'Reliability','Refers to the property that guarantees consistent intended behavior of an a general system, in this case applied to IoT.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(104,'Privacy','In the context of IoT, privacy refers to the control of the user over the disclosure of his data. In other words only the user has control of the sharing of is personal information, is data is only made public if the user allowed it. This requirement is applied were the information is stored.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(105,'Physical Security','Refers to the security measures designed to deny unauthorized physical access to IoT devices and equipment, and to protect them from damage or in other words gaining physical access to the device won\'t give access to it\'s information.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(106,'Forgery Resistance','Is the propriety that ensures that the contents shared between entities cannot be forged by a third party trying to damage or harm the system or its users. In other words no one can try to forge content and send it in the name of another entities.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(107,'Tamper Detection','Ensures all devices are physically secured, such that any tampering attempt is detected.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(108,'Data Freshness','Status that ensures that data is the most recent, and that old messages are not mistakenly used as fresh or purposely replayed by perpetrators. In other words this requirement provides the guarantee that the data displayed is the most recent.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(109,'Confinement','Ensures that even if a party is corrupted, the spreading of the effects of the attack is as confined as possible.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(110,'Interoperability','Is the propriety that ensures that different software communicates and works well with each-other. I.e a software in health-care that works with data that comes from a third-party needs to be able to use and process the information given to it by this software.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(111,'Data Origin','Ensures that the data being received by the software comes from the source it claims to be. In other words it ensures that the data being received is authentic and from a trusted party.',NULL,'2020-10-26 17:57:53','2020-10-26 17:57:53'),(112,'Android App',NULL,'recommendation_112.md','2020-11-26 19:01:57','2020-11-26 19:01:57'),(113,'Third-Party Applications','Many social networks also offer the possibility to create additional applications that extend the functionality of the network. The two major platforms for such applications are the Facebook Platform and Open Social. While applications designed for the Facebook Platform can only be executed in Facebook, Open Social is a combined effort to allow developers to run their applications on any social network that supports the Open Social platform (e.g., MySpace and Orkut).','recommendation_113.md','2020-11-26 19:04:28','2020-11-26 19:04:28'),(114,'Application Regular Updates',NULL,'recommendation_114.md','2020-11-26 19:05:08','2020-11-26 19:05:08'),(115,'Buffer Overflows','Buffer overflows is anomaly where a program, while writing data to a buffer, overruns the buffer\'s boundary and  overwrites adjacent memory. It can be triggered by non-validated inputs that are designed to execute code.','recommendation_115.md','2020-11-26 19:06:31','2020-11-26 19:06:31'),(116,'HTML Secure Fashion',NULL,'recommendation_116.md','2020-11-26 19:09:03','2020-11-26 19:09:03'),(118,'Secure Java and C # Deployment',NULL,'recommendation_118.md','2020-11-26 19:12:42','2020-11-26 19:12:42'),(119,'Security Risk Analysis 1',NULL,'recommendation_119.md','2020-11-26 19:13:36','2020-11-26 19:13:36'),(120,'Security Risk Analysis 2',NULL,'recommendation_120.md','2020-11-26 19:13:48','2020-11-26 19:13:48'),(121,'Security Risk Analysis 3',NULL,'recommendation_121.md','2020-11-26 19:13:59','2020-11-26 19:13:59'),(122,'Security Risk Analysis 4',NULL,'recommendation_122.md','2020-11-26 19:14:12','2020-11-26 19:14:12'),(123,'SSL/TLS','This cheat sheet provides a simple model to follow when implementing transport layer protection for an application. Although the concept of SSL is known to many, the actual details and security specific decisions of implementation are often poorly understood and frequently result in insecure deployments. This article establishes clear rules which provide guidance on securely designing and configuring transport layer security for an application. This article is focused on the use of SSL/TLS between a web application and a web browser, but we also encourage the use of SSL/TLS or other network encryption technologies, such as VPN, on back end and other non-browser based connections.','recommendation_123.md','2020-11-26 19:15:22','2020-11-26 19:15:22'),(231,'Improper Input Validation','CWE-20 -  https://cwe.mitre.org/data/definitions/20.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(232,'Improper Limitation of a Pathname to a Restricted Directory (\'Path Traversal\')','CWE-22 -  https://cwe.mitre.org/data/definitions/22.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(233,'Improper Neutralization of Special Elements in Output Used by a Downstream Component (\'Injection\')','CWE-74 -  https://cwe.mitre.org/data/definitions/74.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(234,'Improper Neutralization of Special Elements used in an OS Command (\'OS Command Injection\')','CWE-78 -  https://cwe.mitre.org/data/definitions/78.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(235,'Improper Neutralization of Input During Web Page Generation (\'Cross-site Scripting\')','CWE-79 -  https://cwe.mitre.org/data/definitions/79.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(236,'Improper Neutralization of Special Elements used in an SQL Command (\'SQL Injection\')','CWE-89 -  https://cwe.mitre.org/data/definitions/89.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(237,'Improper Control of Generation of Code (\'Code Injection\')','CWE-94 -  https://cwe.mitre.org/data/definitions/94.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(238,'Improper Control of Filename for Include/Require Statement in PHP Program','CWE-98 -  https://cwe.mitre.org/data/definitions/98.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(239,'Improper Restriction of Operations within the Bounds of a Memory Buffer','CWE-119 -  https://cwe.mitre.org/data/definitions/119.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(240,'Out-of-bounds Read','CWE-125 -  https://cwe.mitre.org/data/definitions/125.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(241,'Improper Null Termination','CWE-170 -  https://cwe.mitre.org/data/definitions/170.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(242,'Exposure of Sensitive Information to an Unauthorized Actor','CWE-200 -  https://cwe.mitre.org/data/definitions/200.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(243,'Uncaught Exception','CWE-248 -  https://cwe.mitre.org/data/definitions/248.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(244,'Unchecked Return Value','CWE-252 -  https://cwe.mitre.org/data/definitions/252.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(245,'Improper Privilege Management','CWE-269 -  https://cwe.mitre.org/data/definitions/269.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(246,'Improper Authentication','CWE-287 -  https://cwe.mitre.org/data/definitions/287.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(247,'Missing Authentication for Critical Function','CWE-306 -  https://cwe.mitre.org/data/definitions/306.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(248,'Use of a Broken or Risky Cryptographic Algorithm','CWE-327 -  https://cwe.mitre.org/data/definitions/327.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(249,'Use of Insufficiently Random Values','CWE-330 -  https://cwe.mitre.org/data/definitions/330.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(250,'Cross-Site Request Forgery (CSRF)','CWE-352 -  https://cwe.mitre.org/data/definitions/352.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(251,'Uncontrolled Resource Consumption','CWE-400 -  https://cwe.mitre.org/data/definitions/400.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(252,'Improper Resource Shutdown or Release','CWE-404 -  https://cwe.mitre.org/data/definitions/404.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(253,'Use After Free','CWE-416 -  https://cwe.mitre.org/data/definitions/416.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(254,'Unrestricted Upload of File with Dangerous Type','CWE-434 -  https://cwe.mitre.org/data/definitions/434.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(255,'Unintended Proxy or Intermediary (\'Confused Deputy\')','CWE-441 -  https://cwe.mitre.org/data/definitions/441.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(256,'Use of Pointer Subtraction to Determine Size','CWE-469 -  https://cwe.mitre.org/data/definitions/469.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(257,'NULL Pointer Dereference','CWE-476 -  https://cwe.mitre.org/data/definitions/476.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(258,'Use of Obsolete Function','CWE-477 -  https://cwe.mitre.org/data/definitions/477.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(259,'Signal Handler Use of a Non-reentrant Function','CWE-479 -  https://cwe.mitre.org/data/definitions/479.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(260,'Deserialization of Untrusted Data','CWE-502 -  https://cwe.mitre.org/data/definitions/502.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(261,'Covert Storage Channel','CWE-515 -  https://cwe.mitre.org/data/definitions/515.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(262,'Insufficiently Protected Credentials','CWE-522 -  https://cwe.mitre.org/data/definitions/522.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(263,'Missing Standardized Error Handling Mechanism','CWE-544 -  https://cwe.mitre.org/data/definitions/544.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(264,'Improper Following of Specification by Caller','CWE-573 -  https://cwe.mitre.org/data/definitions/573.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(265,'Improper Restriction of XML External Entity Reference','CWE-611 -  https://cwe.mitre.org/data/definitions/611.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(266,'Permissive Regular Expression','CWE-625 -  https://cwe.mitre.org/data/definitions/625.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(267,'Exposure of Resource to Wrong Sphere','CWE-668 -  https://cwe.mitre.org/data/definitions/668.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(268,'Incorrect Control Flow Scoping','CWE-705 -  https://cwe.mitre.org/data/definitions/705.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(269,'Incorrect Permission Assignment for Critical Resource','CWE-732 - https://cwe.mitre.org/data/definitions/732.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(270,'Insufficient Logging','CWE-778 -  https://cwe.mitre.org/data/definitions/778.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(271,'Out-of-bounds Write','CWE-787 -  https://cwe.mitre.org/data/definitions/787.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(272,'Use of Hard-coded Credentials','CWE-798 -  https://cwe.mitre.org/data/definitions/798.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(273,'Business Logic Errors','CWE-840 -  https://cwe.mitre.org/data/definitions/840.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(274,'Missing Authorization','CWE-862 -  https://cwe.mitre.org/data/definitions/862.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(275,'Improper Control of Dynamically-Managed Code Resources','CWE-913 -  https://cwe.mitre.org/data/definitions/913.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(276,'Empty Exception Block','CWE-1069 -  https://cwe.mitre.org/data/definitions/1069.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(277,'Use of Same Variable for Multiple Purposes','CWE-1109 -  https://cwe.mitre.org/data/definitions/1109.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(278,'Failure to Disable Reserved Bits','CWE-1209 -  https://cwe.mitre.org/data/definitions/1209.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(279,'Insufficient Granularity of Access Control','CWE-1220 -  https://cwe.mitre.org/data/definitions/1220.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(280,'Incorrect Register Defaults or Module Parameters','CWE-1221 -  https://cwe.mitre.org/data/definitions/1221.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(281,'Improper Restriction of Write-Once Bit Fields','CWE-1224 -  https://cwe.mitre.org/data/definitions/1224.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(282,'Inclusion of Undocumented Features or Chicken Bits','CWE-1242 -  https://cwe.mitre.org/data/definitions/1242.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(283,'Improper Access to Sensitive Information Using Debug and Test Interfaces','CWE-1244 -  https://cwe.mitre.org/data/definitions/1244.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(284,'Improper Finite State Machines (FSMs) in Hardware Logic','CWE-1245 -  https://cwe.mitre.org/data/definitions/1245.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(285,'Missing or Improperly Implemented Protection Against Voltage and Clock Glitches','CWE-1247 -  https://cwe.mitre.org/data/definitions/1247.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(286,'Mirrored Regions with Different Values','CWE-1251 -  https://cwe.mitre.org/data/definitions/1251.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(287,'Incorrect Selection of Fuse Values','CWE-1253 -  https://cwe.mitre.org/data/definitions/1253.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(288,'Comparison Logic is Vulnerable to Power Side-Channel Attacks','CWE-1255 -  https://cwe.mitre.org/data/definitions/1255.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(289,'Improper Handling of Single Event Upsets','CWE-1261 -  https://cwe.mitre.org/data/definitions/1261.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(290,'Register Interface Allows Software Access to Sensitive Data or Security Settings','CWE-1262 -  https://cwe.mitre.org/data/definitions/1262.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(291,'Improper Physical Access Control','CWE-1263 -  https://cwe.mitre.org/data/definitions/1263.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(292,'Policy Uses Obsolete Encoding','CWE-1267 -  https://cwe.mitre.org/data/definitions/1267.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(293,'Policy Privileges are not Assigned Consistently Between Control and Data Agents','CWE-1268 -  https://cwe.mitre.org/data/definitions/1268.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(294,'Uninitialized Value on Reset for Registers Holding Security Settings','CWE-1271 -  https://cwe.mitre.org/data/definitions/1271.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(295,'Device Unlock Credential Sharing','CWE-1273 -  https://cwe.mitre.org/data/definitions/1273.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(296,'Insufficient Protections on the Volatile Memory Containing Boot Code','CWE-1274 -  https://cwe.mitre.org/data/definitions/1274.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(297,'Hardware Child Block Incorrectly Connected to Parent System','CWE-1276 -  https://cwe.mitre.org/data/definitions/1276.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(298,'Firmware Not Updateable','CWE-1277 -  https://cwe.mitre.org/data/definitions/1277.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(299,'Cryptographic Operations are run Before Supporting Units are Ready','CWE-1279 -  https://cwe.mitre.org/data/definitions/1279.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(300,'Access Control Check Implemented After Asset is Accessed','CWE-1280 -  https://cwe.mitre.org/data/definitions/1280.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(301,'Sequence of Processor Instructions Leads to Unexpected Behavior (Halt and Catch Fire)','CWE-1281 -  https://cwe.mitre.org/data/definitions/1281.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(302,'Assumed-Immutable Data is Stored in Writable Memory','CWE-1282 -  https://cwe.mitre.org/data/definitions/1282.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(303,'Public Key Re-Use for Signing both Debug and Production Code','CWE-1291 -  https://cwe.mitre.org/data/definitions/1291.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(304,'Insecure Security Identifier Mechanism','CWE-1294 -  https://cwe.mitre.org/data/definitions/1294.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(305,'Debug Messages Revealing Unnecessary Information','CWE-1295 -  https://cwe.mitre.org/data/definitions/1295.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(306,'Incorrect Chaining or Granularity of Debug Components','CWE-1296 -  https://cwe.mitre.org/data/definitions/1296.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(307,'Unprotected Confidential Information on Device is Accessible by OSAT Vendors','CWE-1297 -  https://cwe.mitre.org/data/definitions/1297.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(308,'Hardware Logic Contains Race Conditions','CWE-1298 -  https://cwe.mitre.org/data/definitions/1298.html',NULL,'2021-05-03 21:12:49','2021-05-03 21:12:49'),(309,'Missing Protection Mechanism for Alternate Hardware Interface','CWE-1299 -  https://cwe.mitre.org/data/definitions/1299.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(310,'Improperly Preserved Integrity of Hardware Configuration State During a Power Save/Restore Operation','CWE-1304 -  https://cwe.mitre.org/data/definitions/1304.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(311,'Missing Ability to Patch ROM Code','CWE-1310 -  https://cwe.mitre.org/data/definitions/1310.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(312,'Improper Translation of Security Attributes by Fabric Bridge','CWE-1311 -  https://cwe.mitre.org/data/definitions/1311.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(313,'Hardware Allows Activation of Test or Debug Logic at Runtime','CWE-1313 -  https://cwe.mitre.org/data/definitions/1313.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(314,'Improper Protection against Electromagnetic Fault Injection (EM-FI)','CWE-1319 -  https://cwe.mitre.org/data/definitions/1319.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(315,'Missing Immutable Root of Trust in Hardware','CWE-1326 -  https://cwe.mitre.org/data/definitions/1326.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(316,'Improper Isolation of Shared Resources in Network On Chip','CWE-1331 -  https://cwe.mitre.org/data/definitions/1331.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(317,'Unauthorized Error Injection Can Degrade Hardware Redundancy','CWE-1334 -  https://cwe.mitre.org/data/definitions/1334.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(318,'Improper Protections Against Hardware Overheating','CWE-1338 -  https://cwe.mitre.org/data/definitions/1338.html',NULL,'2021-05-03 21:12:50','2021-05-03 21:12:50'),(319,'Reliance on Undefined, Unspecified, or Implementation-Defined Behavior','CWE-758 - https://cwe.mitre.org/data/definitions/758.html',NULL,'2021-05-03 21:13:32','2021-05-03 21:13:32'),(320,'Missing Protection Against Hardware Reverse Engineering Using Integrated Circuit Imaging Techniques','CWE-1278 - https://cwe.mitre.org/data/definitions/1278.html',NULL,'2021-05-03 21:38:55','2021-05-03 21:38:55'),(413,'No NIST Approved Algorithms','There are no lightweight algorithms approved by the National Institute of Standards and Technology for the provided specifications.',NULL,'2021-06-08 18:04:40','2021-06-08 18:04:40'),(414,'Testing Access Control','Recommended Tools: OWASP ZAP','recommendation_414.md','2021-06-08 18:37:39','2021-06-08 18:37:39'),(415,'Testing Brute Force','Recommended Tools: Cain & Abel, THC Hydra , John the Ripper','recommendation_415.md','2021-06-08 18:41:08','2021-06-08 18:41:08'),(416,'Testing if Assumed-Immutable Data is Stored in Writable Memory','Recommended Tools: Manually','recommendation_416.md','2021-06-08 18:44:54','2021-06-08 18:44:54'),(417,'Testing Buffer Overflow','Recommended Tools: OllyDbg','recommendation_417.md','2021-06-08 18:45:35','2021-06-08 18:45:35'),(418,'Testing Code Injection','Recommended Tools: Burp Suite','recommendation_418.md','2021-06-08 18:46:35','2021-06-08 18:46:35'),(419,'Testing Code Signing','Recommended Tools: Manually','recommendation_419.md','2021-06-08 18:47:45','2021-06-08 18:47:45'),(421,'Testing Command Injection','Recommended Tools: Burp Suite, Manually','recommendation_421.md','2021-06-08 18:49:33','2021-06-08 18:49:33'),(422,'Testing Assessment of Cryptographic protocols','Recommended Tools: ProVerif','recommendation_422.md','2021-06-08 18:50:35','2021-06-08 18:50:35'),(423,'Testing CSRF','Recommended Tools: OWASP ZAP, Burp Suite','recommendation_423.md','2021-06-08 18:51:26','2021-06-08 18:51:26'),(424,'Testing CSV Injection','Recommended Tools: Manually','recommendation_424.md','2021-06-08 18:52:15','2021-06-08 18:52:15'),(425,'Testing DoS','Recommended Tools: hping3, HULK, GoldenEye, Wireshark','recommendation_425.md','2021-06-08 18:53:10','2021-06-08 18:53:10'),(426,'Testing DNS Poisoning','Recommended Tools: Ettercap, Arpspoof & DNSspoof, Cain & Abel, Wireshark','recommendation_426.md','2021-06-08 18:59:58','2021-06-08 18:59:58'),(427,'Testing Error Handling','Recommended Tools: Manually','recommendation_427.md','2021-06-08 19:00:34','2021-06-08 19:00:34'),(428,'Testing Expired Domain','Recommended Tools: Manually','recommendation_428.md','2021-06-08 19:01:11','2021-06-08 19:01:11'),(429,'Testing Firmware Cracking','Recommended Tools: IoT Inspector, Binwalk, QEMU, FIRMADYNE, Firmware Analysis Toolkit (FAT)','recommendation_429.md','2021-06-08 19:02:34','2021-06-08 19:02:34'),(430,'Testing Forced Browsing','Recommended Tools: Manually','recommendation_430.md','2021-06-08 19:03:14','2021-06-08 19:03:14'),(431,'Testing Format String','Recommended Tools: Wfuzz, Manually','recommendation_431.md','2021-06-08 19:04:23','2021-06-08 19:04:23'),(432,'Testing for Hardware Fault Injections','Recommended Tools: Manually','recommendation_432.md','2021-06-08 19:05:38','2021-06-08 19:05:38'),(433,'Testing Heartbleed Bug','Recommended Tools: Openssl','recommendation_433.md','2021-06-08 19:06:12','2021-06-08 19:06:12'),(434,'Testing Log Injection','Recommended Tools: Manually','recommendation_434.md','2021-06-08 19:07:06','2021-06-08 19:07:06'),(435,'Testing for Malicious Apps','Recommended Tools: Wafw00f','recommendation_435.md','2021-06-08 19:08:01','2021-06-08 19:08:01'),(436,'Testing Man in The Middle','Recommended Tools: Ettercap, Bettercap','recommendation_436.md','2021-06-08 19:08:53','2021-06-08 19:08:53'),(437,'Testing Overheating','Recommended Tools: Manually','recommendation_437.md','2021-06-08 19:09:41','2021-06-08 19:09:41'),(438,'Testing Path Traversal','Recommended Tools: OWASP ZAP, Burp Suite','recommendation_438.md','2021-06-08 19:11:33','2021-06-08 19:11:33'),(439,'ProVerif Testing Symmetrical Cyphers','Code for testing Symmetrical Cyphers in ProVerif','recommendation_439.md','2021-06-08 19:13:24','2021-06-08 19:13:24'),(440,'ProVerif Testing Hash Functions','Code for testing Hash Functions in ProVerif','recommendation_440.md','2021-06-08 19:14:03','2021-06-08 19:14:03'),(441,'ProVerif Testing MAC Functions','Code for testing MAC Functions in ProVerif','recommendation_441.md','2021-06-08 19:14:48','2021-06-08 19:14:48'),(442,'ProVerif Testing HMAC Functions','Code for testing HMAC Functions in ProVerif','recommendation_442.md','2021-06-08 19:15:44','2021-06-08 19:15:44'),(443,'Testing for Race Conditions','Recommended Tools: CHESS by Microsoft Research','recommendation_443.md','2021-06-08 19:16:30','2021-06-08 19:16:30'),(444,'Testing Random and Pseudorandom Number Generators for Cryptographic Applications','Recommended Tools: Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications (NIST)','recommendation_444.md','2021-06-08 19:17:15','2021-06-08 19:17:15'),(445,'Testing Reflected XSS','Recommended Tools: OWASP ZAP, Burp Suite','recommendation_445.md','2021-06-08 19:18:01','2021-06-08 19:18:01'),(446,'Testing Remote File Inclusion','Recommended Tools: Manually','recommendation_446.md','2021-06-08 19:18:42','2021-06-08 19:18:42'),(447,'Testing Replay Attack','Recommended Tools:Tcpreplay, Wireshark','recommendation_447.md','2021-06-08 19:19:31','2021-06-08 19:19:31'),(448,'Avoid Incorrect Selection of Fuse Values','Recommended Tools:Manually (a guide is provided)','recommendation_448.md','2021-06-08 19:20:28','2021-06-08 19:20:28'),(449,'Testing for Shared Resource Manipulation','Recommended Tools: OWASP ZAP','recommendation_449.md','2021-06-08 19:21:09','2021-06-08 19:21:09'),(450,'Testing SQL Injection','Recommended Tools: sqlmap, SQLi Dumper, Netsparker','recommendation_450.md','2021-06-08 19:22:05','2021-06-08 19:22:05'),(451,'Testing SSL','Recommended Tools: Testssl, OWASP O-Saft','recommendation_451.md','2021-06-08 19:22:49','2021-06-08 19:22:49'),(452,'Testing Stored XSS','Recommended Tools: OWASP ZAP, Burp Suite','recommendation_452.md','2021-06-08 19:23:35','2021-06-08 19:23:35'),(453,'Testing for Insecure Direct Object References','Recommended Tools: Manually','recommendation_453.md','2021-06-08 19:24:16','2021-06-08 19:24:16'),(454,'Testing for XXE Injection','Recommended Tools: OWASP ZAP, Burp Suite','recommendation_454.md','2021-06-08 19:25:00','2021-06-08 19:25:00');
/*!40000 ALTER TABLE `recommendation` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_Recommendation_Delete BEFORE DELETE on Recommendation
FOR EACH ROW
	-- Only delete a session, if the session linked to the deleted recommendation has no more recommendations linked to it.
    DELETE FROM Session WHERE Session.id = (SELECT SessionID FROM Session_Recommendation WHERE Session_Recommendation.recommendationID = OLD.id)
	AND EXISTS (SELECT sessionID FROM session_recommendation WHERE sessionID = Session.id GROUP BY sessionID HAVING count(sessionID) = 1) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `recommendation_question_answer`
--

DROP TABLE IF EXISTS `recommendation_question_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recommendation_question_answer` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `recommendationID` int(11) NOT NULL,
  `questionAnswerID` int(11) NOT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `recommendationID_questionAnswerID_UNIQUE` (`recommendationID`,`questionAnswerID`),
  KEY `fk_Question_Answer_has_Recomendation_Recomendation1_idx` (`recommendationID`),
  KEY `fk_Question_Answer_has_Recomendation_Question_Answer1_idx` (`questionAnswerID`),
  CONSTRAINT `fk_Question_Answer_has_Recomendation_Question_Answer1` FOREIGN KEY (`questionAnswerID`) REFERENCES `question_answer` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Question_Answer_has_Recomendation_Recomendation1` FOREIGN KEY (`recommendationID`) REFERENCES `recommendation` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recommendation_question_answer`
--

LOCK TABLES `recommendation_question_answer` WRITE;
/*!40000 ALTER TABLE `recommendation_question_answer` DISABLE KEYS */;
INSERT INTO `recommendation_question_answer` VALUES (15,4,10,'2020-10-23 15:38:15','2020-10-23 15:38:15'),(17,11,17,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(18,14,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(19,15,11,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(20,6,16,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(21,10,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(22,13,10,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(23,13,11,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(24,7,10,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(25,7,11,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(26,8,10,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(27,5,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(28,9,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(29,12,82,'2020-10-23 15:50:36','2020-10-23 15:50:36'),(44,4,11,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(45,4,12,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(46,4,13,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(47,4,14,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(48,4,15,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(49,4,16,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(50,4,17,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(51,4,18,'2020-10-23 16:13:35','2020-10-23 16:13:35'),(155,8,11,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(156,8,12,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(157,8,13,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(158,8,14,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(159,8,15,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(160,8,16,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(161,8,17,'2020-10-23 17:13:51','2020-10-23 17:13:51'),(162,8,18,'2020-10-23 17:13:51','2020-10-23 17:13:51');
/*!40000 ALTER TABLE `recommendation_question_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `moduleID` int(11) NOT NULL,
  `ended` tinyint(4) DEFAULT 0,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  KEY `fk_Session_Module1_idx` (`moduleID`),
  KEY `fk_Session_User1_idx` (`userID`),
  CONSTRAINT `fk_Session_Module1` FOREIGN KEY (`moduleID`) REFERENCES `module` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Session_User1` FOREIGN KEY (`userID`) REFERENCES `user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1287 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_Session_Update BEFORE UPDATE on Session
FOR EACH ROW
	SET NEW.updatedon = NOW() */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `session_recommendation`
--

DROP TABLE IF EXISTS `session_recommendation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session_recommendation` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `sessionID` int(11) NOT NULL,
  `recommendationID` int(11) NOT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `u_sessionID_recommendationID` (`sessionID`,`recommendationID`),
  KEY `fk_Session_has_Recomendation_Recomendation1_idx` (`recommendationID`),
  KEY `fk_Session_has_Recomendation_Session1_idx` (`sessionID`),
  CONSTRAINT `fk_Session_has_Recomendation_Recomendation1` FOREIGN KEY (`recommendationID`) REFERENCES `recommendation` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Session_has_Recomendation_Session1` FOREIGN KEY (`sessionID`) REFERENCES `session` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2990 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_recommendation`
--

LOCK TABLES `session_recommendation` WRITE;
/*!40000 ALTER TABLE `session_recommendation` DISABLE KEYS */;
/*!40000 ALTER TABLE `session_recommendation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session_user_answer`
--

DROP TABLE IF EXISTS `session_user_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session_user_answer` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `sessionID` int(11) NOT NULL,
  `questionAnswerID` int(11) DEFAULT NULL COMMENT 'This FK is only set if the answer is static (i.e. not provided by the user).',
  `questionID` int(11) DEFAULT NULL COMMENT 'This FK is only set if the answer is dynamic (i.e. provided by the user in field input).',
  `input` varchar(45) DEFAULT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `sessionID_questionAnswerID` (`sessionID`,`questionAnswerID`),
  KEY `fk_Answer_has_Session_Session1_idx` (`sessionID`),
  KEY `fk_Session_User_Answer_Question_Answer1_idx` (`questionAnswerID`),
  KEY `fk_Session_User_Answer_Question1_idx` (`questionID`),
  CONSTRAINT `fk_Answer_has_Session_Session1` FOREIGN KEY (`sessionID`) REFERENCES `session` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Session_User_Answer_Question1` FOREIGN KEY (`questionID`) REFERENCES `question` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Session_User_Answer_Question_Answer1` FOREIGN KEY (`questionAnswerID`) REFERENCES `question_answer` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8480 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_user_answer`
--

LOCK TABLES `session_user_answer` WRITE;
/*!40000 ALTER TABLE `session_user_answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `session_user_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `type` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` text DEFAULT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES (1,'Security Requirements','Provides Security Requirements','2020-10-23 14:58:36','2020-10-23 14:58:36'),(2,'Security Pratices','Provides Security Guidelines','2020-10-23 14:58:36','2020-10-23 14:58:36'),(3,'Security Algorithms','Provides Security Cryptographic Algorithms','2020-10-23 14:58:36','2020-10-23 14:58:36');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_Type_Update BEFORE UPDATE on Type
FOR EACH ROW
	SET NEW.updatedon = NOW() */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `firstName` varchar(30) NOT NULL,
  `lastName` varchar(30) NOT NULL,
  `psw` varchar(255) NOT NULL,
  `avatar` varchar(45) DEFAULT NULL,
  `userStatus` tinyint(4) NOT NULL DEFAULT 0 COMMENT 'Flag to define if the user is active or not.',
  `administrator` tinyint(4) DEFAULT 0,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'user@SAM.pt','Forrest','Gump','6e68eff9ad873e8df6d25fce9282fb9bfbd3f8f6ff32a639a42963448787d88a:7e3627579e1e4304874ce442f2e50760',NULL,1,NULL,NULL,NULL),(2,'admin@SAM.pt','Ellen','Ripley','6e68eff9ad873e8df6d25fce9282fb9bfbd3f8f6ff32a639a42963448787d88a:7e3627579e1e4304874ce442f2e50760',NULL,1,1,NULL,NULL),(3,'joana@SAM.pt','Joana','Costa','c4843f59e8ef86face9917bdad2fbfaacbfceb56953d94f638a7530467f5a114:9ac8ea4e81a0baa64e04ce38a7d5283a','default',0,0,'2021-04-22 14:34:36','2021-06-08 18:00:39'),(4,'carolina@SAM.pt','Carolina','Lopes','e3b73c7116d9c390a1ddc5c47ff3ce805bbccf093d9d78ddda16b1c2ba5cb589:90c80a9f4cfbec5423649bd1c1050a0e','default',0,0,'2021-06-08 11:21:11','2021-06-08 11:21:11'),(5,'prmi@ubi.pt','Pedro','Inácio','e9815c3382220f01b20b422c41424dfa4495f0511ef8dd003a06977f40a5e485:eaf9eaa090203f4d0ed6d34f8607becf','default',0,0,'2021-06-08 11:28:53','2021-06-08 11:28:53');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`SAM`@`%`*/ /*!50003 TRIGGER Trigger_User_Update BEFORE UPDATE on User
FOR EACH ROW
	SET NEW.updatedon = NOW() */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `user_group`
--

DROP TABLE IF EXISTS `user_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_group` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `groupID` int(11) NOT NULL,
  `createdOn` datetime DEFAULT current_timestamp(),
  `updatedOn` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`ID`),
  UNIQUE KEY `userID_GroupID_Unique` (`userID`,`groupID`),
  KEY `fk_User_has_Group_Group1_idx` (`groupID`),
  KEY `fk_User_has_Group_User1_idx` (`userID`),
  CONSTRAINT `fk_User_has_Group_Group1` FOREIGN KEY (`groupID`) REFERENCES `group` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_User_has_Group_User1` FOREIGN KEY (`userID`) REFERENCES `user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_group`
--

LOCK TABLES `user_group` WRITE;
/*!40000 ALTER TABLE `user_group` DISABLE KEYS */;
INSERT INTO `user_group` VALUES (1,1,1,NULL,NULL),(2,2,1,NULL,NULL);
/*!40000 ALTER TABLE `user_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `view_module_answers`
--

DROP TABLE IF EXISTS `view_module_answers`;
/*!50001 DROP VIEW IF EXISTS `view_module_answers`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_module_answers` (
  `module_ID` tinyint NOT NULL,
  `answer_ID` tinyint NOT NULL,
  `answer` tinyint NOT NULL,
  `createdon` tinyint NOT NULL,
  `updatedon` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_module_dependency`
--

DROP TABLE IF EXISTS `view_module_dependency`;
/*!50001 DROP VIEW IF EXISTS `view_module_dependency`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_module_dependency` (
  `dependency_ID` tinyint NOT NULL,
  `module_id` tinyint NOT NULL,
  `module_shortname` tinyint NOT NULL,
  `module_name` tinyint NOT NULL,
  `display` tinyint NOT NULL,
  `depends_module_id` tinyint NOT NULL,
  `createdon` tinyint NOT NULL,
  `updatedon` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_module_question`
--

DROP TABLE IF EXISTS `view_module_question`;
/*!50001 DROP VIEW IF EXISTS `view_module_question`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_module_question` (
  `module_ID` tinyint NOT NULL,
  `module_displayname` tinyint NOT NULL,
  `question_ID` tinyint NOT NULL,
  `multipleAnswers` tinyint NOT NULL,
  `question` tinyint NOT NULL,
  `question_description` tinyint NOT NULL,
  `questionOrder` tinyint NOT NULL,
  `createdon` tinyint NOT NULL,
  `updatedon` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_module_questions_answers`
--

DROP TABLE IF EXISTS `view_module_questions_answers`;
/*!50001 DROP VIEW IF EXISTS `view_module_questions_answers`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_module_questions_answers` (
  `module_ID` tinyint NOT NULL,
  `module_displayname` tinyint NOT NULL,
  `question_ID` tinyint NOT NULL,
  `question` tinyint NOT NULL,
  `questionOrder` tinyint NOT NULL,
  `answer_ID` tinyint NOT NULL,
  `answer` tinyint NOT NULL,
  `question_createdon` tinyint NOT NULL,
  `question_updatedon` tinyint NOT NULL,
  `answer_createdon` tinyint NOT NULL,
  `answer_updatedon` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_module_recommendations`
--

DROP TABLE IF EXISTS `view_module_recommendations`;
/*!50001 DROP VIEW IF EXISTS `view_module_recommendations`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_module_recommendations` (
  `recommendation_ID` tinyint NOT NULL,
  `module_ID` tinyint NOT NULL,
  `recommendation_content` tinyint NOT NULL,
  `recommendation_description` tinyint NOT NULL,
  `recommendation_guide` tinyint NOT NULL,
  `createdon` tinyint NOT NULL,
  `updatedon` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_module_recommendations_questions_answers`
--

DROP TABLE IF EXISTS `view_module_recommendations_questions_answers`;
/*!50001 DROP VIEW IF EXISTS `view_module_recommendations_questions_answers`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_module_recommendations_questions_answers` (
  `module_ID` tinyint NOT NULL,
  `recommendation_ID` tinyint NOT NULL,
  `recommendation_content` tinyint NOT NULL,
  `recommendation_question_answer_ID` tinyint NOT NULL,
  `question_id` tinyint NOT NULL,
  `answer_id` tinyint NOT NULL,
  `createdon` tinyint NOT NULL,
  `updatedon` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_question_answer`
--

DROP TABLE IF EXISTS `view_question_answer`;
/*!50001 DROP VIEW IF EXISTS `view_question_answer`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_question_answer` (
  `question_answer_id` tinyint NOT NULL,
  `question_id` tinyint NOT NULL,
  `question` tinyint NOT NULL,
  `answer_id` tinyint NOT NULL,
  `answer` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_question_answer_recommendation`
--

DROP TABLE IF EXISTS `view_question_answer_recommendation`;
/*!50001 DROP VIEW IF EXISTS `view_question_answer_recommendation`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_question_answer_recommendation` (
  `question_ID` tinyint NOT NULL,
  `answer_ID` tinyint NOT NULL,
  `recommendation_ID` tinyint NOT NULL,
  `content` tinyint NOT NULL,
  `description` tinyint NOT NULL,
  `guide` tinyint NOT NULL,
  `createdOn` tinyint NOT NULL,
  `updatedOn` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_question_childs`
--

DROP TABLE IF EXISTS `view_question_childs`;
/*!50001 DROP VIEW IF EXISTS `view_question_childs`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_question_childs` (
  `parent_id` tinyint NOT NULL,
  `child_id` tinyint NOT NULL,
  `question` tinyint NOT NULL,
  `multipleAnswers` tinyint NOT NULL,
  `ontrigger` tinyint NOT NULL,
  `questionOrder` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_recommendation`
--

DROP TABLE IF EXISTS `view_recommendation`;
/*!50001 DROP VIEW IF EXISTS `view_recommendation`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_recommendation` (
  `session_ID` tinyint NOT NULL,
  `recommendation_ID` tinyint NOT NULL,
  `recommendation` tinyint NOT NULL,
  `recommendation_description` tinyint NOT NULL,
  `guideFileName` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_recommendation_logic`
--

DROP TABLE IF EXISTS `view_recommendation_logic`;
/*!50001 DROP VIEW IF EXISTS `view_recommendation_logic`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_recommendation_logic` (
  `session_ID` tinyint NOT NULL,
  `recommendation_ID` tinyint NOT NULL,
  `recommendation` tinyint NOT NULL,
  `recommendation_description` tinyint NOT NULL,
  `guideFileName` tinyint NOT NULL,
  `session_recommendation_ID` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_recommendations`
--

DROP TABLE IF EXISTS `view_recommendations`;
/*!50001 DROP VIEW IF EXISTS `view_recommendations`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_recommendations` (
  `question_id` tinyint NOT NULL,
  `question` tinyint NOT NULL,
  `answer_id` tinyint NOT NULL,
  `answer` tinyint NOT NULL,
  `recommendation` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_session_answers`
--

DROP TABLE IF EXISTS `view_session_answers`;
/*!50001 DROP VIEW IF EXISTS `view_session_answers`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_session_answers` (
  `session_ID` tinyint NOT NULL,
  `session_userID` tinyint NOT NULL,
  `session_moduleID` tinyint NOT NULL,
  `session_ended` tinyint NOT NULL,
  `session_createdon` tinyint NOT NULL,
  `session_updatedon` tinyint NOT NULL,
  `module_logic` tinyint NOT NULL,
  `question_ID` tinyint NOT NULL,
  `question` tinyint NOT NULL,
  `answer_input` tinyint NOT NULL,
  `answer_id` tinyint NOT NULL,
  `answer` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_session_recommendation`
--

DROP TABLE IF EXISTS `view_session_recommendation`;
/*!50001 DROP VIEW IF EXISTS `view_session_recommendation`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_session_recommendation` (
  `session_ID` tinyint NOT NULL,
  `session_userID` tinyint NOT NULL,
  `session_moduleID` tinyint NOT NULL,
  `session_ended` tinyint NOT NULL,
  `session_createdOn` tinyint NOT NULL,
  `session_updatedOn` tinyint NOT NULL,
  `recommendation_ID` tinyint NOT NULL,
  `recommendation` tinyint NOT NULL,
  `recommendation_description` tinyint NOT NULL,
  `recommendation_guide` tinyint NOT NULL,
  `recommendation_createdOn` tinyint NOT NULL,
  `recommendation_updatedOn` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_user_group`
--

DROP TABLE IF EXISTS `view_user_group`;
/*!50001 DROP VIEW IF EXISTS `view_user_group`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_user_group` (
  `user_id` tinyint NOT NULL,
  `user_email` tinyint NOT NULL,
  `group_id` tinyint NOT NULL,
  `user_group` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `view_user_sessions`
--

DROP TABLE IF EXISTS `view_user_sessions`;
/*!50001 DROP VIEW IF EXISTS `view_user_sessions`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `view_user_sessions` (
  `session_id` tinyint NOT NULL,
  `user_id` tinyint NOT NULL,
  `user_email` tinyint NOT NULL,
  `moduleID` tinyint NOT NULL,
  `ended` tinyint NOT NULL,
  `createdon` tinyint NOT NULL,
  `updatedon` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `view_module_answers`
--

/*!50001 DROP TABLE IF EXISTS `view_module_answers`*/;
/*!50001 DROP VIEW IF EXISTS `view_module_answers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_module_answers` AS select distinct `m`.`ID` AS `module_ID`,`a`.`ID` AS `answer_ID`,`a`.`content` AS `answer`,`a`.`createdOn` AS `createdon`,`a`.`updatedOn` AS `updatedon` from ((((`module` `m` join `question` `q`) join `module_question` `mq`) join `answer` `a`) join `question_answer` `qa`) where `m`.`ID` = `mq`.`moduleID` and `q`.`ID` = `mq`.`questionID` and `a`.`ID` = `qa`.`answerID` and `q`.`ID` = `qa`.`questionID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_module_dependency`
--

/*!50001 DROP TABLE IF EXISTS `view_module_dependency`*/;
/*!50001 DROP VIEW IF EXISTS `view_module_dependency`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_module_dependency` AS select `d`.`ID` AS `dependency_ID`,`d`.`moduleID` AS `module_id`,`m`.`shortname` AS `module_shortname`,`m`.`fullname` AS `module_name`,`m`.`displayName` AS `display`,`d`.`dependsOn` AS `depends_module_id`,`d`.`createdOn` AS `createdon`,`d`.`updatedOn` AS `updatedon` from (`module` `m` join `dependency` `d`) where `d`.`moduleID` = `m`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_module_question`
--

/*!50001 DROP TABLE IF EXISTS `view_module_question`*/;
/*!50001 DROP VIEW IF EXISTS `view_module_question`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_module_question` AS select `m`.`ID` AS `module_ID`,`m`.`displayName` AS `module_displayname`,`q`.`ID` AS `question_ID`,`q`.`multipleAnswers` AS `multipleAnswers`,`q`.`content` AS `question`,`q`.`description` AS `question_description`,`mq`.`questionOrder` AS `questionOrder`,`q`.`createdOn` AS `createdon`,`q`.`updatedOn` AS `updatedon` from ((`module` `m` join `question` `q`) join `module_question` `mq`) where `m`.`ID` = `mq`.`moduleID` and `q`.`ID` = `mq`.`questionID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_module_questions_answers`
--

/*!50001 DROP TABLE IF EXISTS `view_module_questions_answers`*/;
/*!50001 DROP VIEW IF EXISTS `view_module_questions_answers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_module_questions_answers` AS select `m`.`ID` AS `module_ID`,`m`.`displayName` AS `module_displayname`,`q`.`ID` AS `question_ID`,`q`.`content` AS `question`,`mq`.`questionOrder` AS `questionOrder`,`a`.`ID` AS `answer_ID`,`a`.`content` AS `answer`,`q`.`createdOn` AS `question_createdon`,`q`.`updatedOn` AS `question_updatedon`,`a`.`createdOn` AS `answer_createdon`,`a`.`updatedOn` AS `answer_updatedon` from ((((`module` `m` join `question` `q`) join `module_question` `mq`) join `question_answer` `qa`) join `answer` `a`) where `m`.`ID` = `mq`.`moduleID` and `q`.`ID` = `mq`.`questionID` and `a`.`ID` = `qa`.`answerID` and `q`.`ID` = `qa`.`questionID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_module_recommendations`
--

/*!50001 DROP TABLE IF EXISTS `view_module_recommendations`*/;
/*!50001 DROP VIEW IF EXISTS `view_module_recommendations`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_module_recommendations` AS select distinct `r`.`ID` AS `recommendation_ID`,`m`.`ID` AS `module_ID`,`r`.`content` AS `recommendation_content`,`r`.`description` AS `recommendation_description`,`r`.`guideFileName` AS `recommendation_guide`,`r`.`createdOn` AS `createdon`,`r`.`updatedOn` AS `updatedon` from (((((`module` `m` join `module_question` `mq`) join `question` `q`) join `question_answer` `qa`) join `recommendation_question_answer` `rqa`) join `recommendation` `r`) where `m`.`ID` = `mq`.`moduleID` and `mq`.`questionID` = `q`.`ID` and `q`.`ID` = `qa`.`questionID` and `rqa`.`questionAnswerID` = `qa`.`ID` and `rqa`.`recommendationID` = `r`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_module_recommendations_questions_answers`
--

/*!50001 DROP TABLE IF EXISTS `view_module_recommendations_questions_answers`*/;
/*!50001 DROP VIEW IF EXISTS `view_module_recommendations_questions_answers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_module_recommendations_questions_answers` AS select distinct `m`.`ID` AS `module_ID`,`r`.`ID` AS `recommendation_ID`,`r`.`content` AS `recommendation_content`,`rqa`.`ID` AS `recommendation_question_answer_ID`,`qa`.`questionID` AS `question_id`,`qa`.`answerID` AS `answer_id`,`rqa`.`createdOn` AS `createdon`,`rqa`.`updatedOn` AS `updatedon` from (((((`module` `m` join `module_question` `mq`) join `question` `q`) join `question_answer` `qa`) join `recommendation_question_answer` `rqa`) join `recommendation` `r`) where `m`.`ID` = `mq`.`moduleID` and `mq`.`questionID` = `q`.`ID` and `q`.`ID` = `qa`.`questionID` and `rqa`.`questionAnswerID` = `qa`.`ID` and `rqa`.`recommendationID` = `r`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_question_answer`
--

/*!50001 DROP TABLE IF EXISTS `view_question_answer`*/;
/*!50001 DROP VIEW IF EXISTS `view_question_answer`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_question_answer` AS select `qa`.`ID` AS `question_answer_id`,`q`.`ID` AS `question_id`,`q`.`content` AS `question`,`a`.`ID` AS `answer_id`,`a`.`content` AS `answer` from ((`question` `q` join `question_answer` `qa`) join `answer` `a`) where `q`.`ID` = `qa`.`questionID` and `qa`.`answerID` = `a`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_question_answer_recommendation`
--

/*!50001 DROP TABLE IF EXISTS `view_question_answer_recommendation`*/;
/*!50001 DROP VIEW IF EXISTS `view_question_answer_recommendation`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_question_answer_recommendation` AS select `qa`.`questionID` AS `question_ID`,`qa`.`answerID` AS `answer_ID`,`r`.`ID` AS `recommendation_ID`,`r`.`content` AS `content`,`r`.`description` AS `description`,`r`.`guideFileName` AS `guide`,`r`.`createdOn` AS `createdOn`,`r`.`updatedOn` AS `updatedOn` from ((`question_answer` `qa` join `recommendation_question_answer` `rqa`) join `recommendation` `r`) where `qa`.`ID` = `rqa`.`questionAnswerID` and `r`.`ID` = `rqa`.`recommendationID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_question_childs`
--

/*!50001 DROP TABLE IF EXISTS `view_question_childs`*/;
/*!50001 DROP VIEW IF EXISTS `view_question_childs`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_question_childs` AS select `qp`.`parent` AS `parent_id`,`qp`.`child` AS `child_id`,`q`.`content` AS `question`,`q`.`multipleAnswers` AS `multipleAnswers`,`qp`.`ontrigger` AS `ontrigger`,`qp`.`questionOrder` AS `questionOrder` from (`question_has_child` `qp` join `question` `q`) where `qp`.`child` = `q`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_recommendation`
--

/*!50001 DROP TABLE IF EXISTS `view_recommendation`*/;
/*!50001 DROP VIEW IF EXISTS `view_recommendation`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_recommendation` AS select distinct `s`.`ID` AS `session_ID`,`r`.`ID` AS `recommendation_ID`,`r`.`content` AS `recommendation`,`r`.`description` AS `recommendation_description`,`r`.`guideFileName` AS `guideFileName` from ((((`session` `s` join `session_user_answer` `sua`) join `question_answer` `qa`) join `recommendation_question_answer` `rqa`) join `recommendation` `r`) where `s`.`ID` = `sua`.`sessionID` and `sua`.`questionAnswerID` = `qa`.`ID` and `qa`.`ID` = `rqa`.`questionAnswerID` and `rqa`.`recommendationID` = `r`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_recommendation_logic`
--

/*!50001 DROP TABLE IF EXISTS `view_recommendation_logic`*/;
/*!50001 DROP VIEW IF EXISTS `view_recommendation_logic`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_recommendation_logic` AS select distinct `s`.`ID` AS `session_ID`,`r`.`ID` AS `recommendation_ID`,`r`.`content` AS `recommendation`,`r`.`description` AS `recommendation_description`,`r`.`guideFileName` AS `guideFileName`,`sr`.`ID` AS `session_recommendation_ID` from ((`session` `s` join `session_recommendation` `sr`) join `recommendation` `r`) where `s`.`ID` = `sr`.`sessionID` and `r`.`ID` = `sr`.`recommendationID` order by `sr`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_recommendations`
--

/*!50001 DROP TABLE IF EXISTS `view_recommendations`*/;
/*!50001 DROP VIEW IF EXISTS `view_recommendations`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_recommendations` AS select `q`.`ID` AS `question_id`,`q`.`content` AS `question`,`a`.`ID` AS `answer_id`,`a`.`content` AS `answer`,`r`.`content` AS `recommendation` from ((((`question` `q` join `answer` `a`) join `question_answer` `qa`) join `recommendation_question_answer` `rqa`) join `recommendation` `r`) where `q`.`ID` = `qa`.`questionID` and `a`.`ID` = `qa`.`answerID` and `r`.`ID` = `rqa`.`recommendationID` and `qa`.`ID` = `rqa`.`questionAnswerID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_session_answers`
--

/*!50001 DROP TABLE IF EXISTS `view_session_answers`*/;
/*!50001 DROP VIEW IF EXISTS `view_session_answers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_session_answers` AS select distinct `s`.`ID` AS `session_ID`,`s`.`userID` AS `session_userID`,`s`.`moduleID` AS `session_moduleID`,`s`.`ended` AS `session_ended`,`s`.`createdOn` AS `session_createdon`,`s`.`updatedOn` AS `session_updatedon`,NULL AS `module_logic`,`q`.`ID` AS `question_ID`,`q`.`content` AS `question`,`sua`.`input` AS `answer_input`,`a`.`ID` AS `answer_id`,`a`.`content` AS `answer` from (((((`session` `s` join `session_user_answer` `sua`) join `question` `q`) join `question_answer` `qa`) join `answer` `a`) join `module` `m`) where `s`.`ID` = `sua`.`sessionID` and `sua`.`questionAnswerID` = `qa`.`ID` and `qa`.`questionID` = `q`.`ID` and `qa`.`answerID` = `a`.`ID` union select distinct `s`.`ID` AS `session_ID`,`s`.`userID` AS `session_userID`,`s`.`moduleID` AS `session_moduleID`,`s`.`ended` AS `session_ended`,`s`.`createdOn` AS `session_createdon`,`s`.`updatedOn` AS `session_updatedon`,`m`.`logicFileName` AS `module_logic`,`q`.`ID` AS `question_ID`,`q`.`content` AS `question`,`sua`.`input` AS `answer_input`,NULL AS `answer_ID`,NULL AS `answer` from ((((`session` `s` join `session_user_answer` `sua`) join `question` `q`) join `question_answer` `qa`) join `module` `m`) where `s`.`ID` = `sua`.`sessionID` and `sua`.`questionID` = `q`.`ID` and `s`.`moduleID` = `m`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_session_recommendation`
--

/*!50001 DROP TABLE IF EXISTS `view_session_recommendation`*/;
/*!50001 DROP VIEW IF EXISTS `view_session_recommendation`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_session_recommendation` AS select `s`.`ID` AS `session_ID`,`s`.`userID` AS `session_userID`,`s`.`moduleID` AS `session_moduleID`,`s`.`ended` AS `session_ended`,`s`.`createdOn` AS `session_createdOn`,`s`.`updatedOn` AS `session_updatedOn`,`r`.`ID` AS `recommendation_ID`,`r`.`content` AS `recommendation`,`r`.`description` AS `recommendation_description`,`r`.`guideFileName` AS `recommendation_guide`,`r`.`createdOn` AS `recommendation_createdOn`,`r`.`updatedOn` AS `recommendation_updatedOn` from ((`session` `s` join `session_recommendation` `sr`) join `recommendation` `r`) where `s`.`ID` = `sr`.`sessionID` and `sr`.`recommendationID` = `r`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_user_group`
--

/*!50001 DROP TABLE IF EXISTS `view_user_group`*/;
/*!50001 DROP VIEW IF EXISTS `view_user_group`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_user_group` AS select `u`.`ID` AS `user_id`,`u`.`email` AS `user_email`,`g`.`ID` AS `group_id`,`g`.`designation` AS `user_group` from ((`group` `g` join `user_group` `ug`) join `user` `u`) where `g`.`ID` = `ug`.`groupID` and `u`.`ID` = `ug`.`userID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_user_sessions`
--

/*!50001 DROP TABLE IF EXISTS `view_user_sessions`*/;
/*!50001 DROP VIEW IF EXISTS `view_user_sessions`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`SAM`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `view_user_sessions` AS select `s`.`ID` AS `session_id`,`u`.`ID` AS `user_id`,`u`.`email` AS `user_email`,`s`.`moduleID` AS `moduleID`,`s`.`ended` AS `ended`,`s`.`createdOn` AS `createdon`,`s`.`updatedOn` AS `updatedon` from (`session` `s` join `user` `u`) where `u`.`ID` = `s`.`userID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-11 11:55:59
