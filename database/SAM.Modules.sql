--
-- DB Test data for development purposes
-- 
USE SAM;

-- Insert test USER
DELETE FROM User WHERE ID >= 1;
ALTER TABLE User AUTO_INCREMENT = 1;
INSERT INTO User (email, firstName, lastName, psw) VALUES ('old@user.com', 'Old', 'User', '6e68eff9ad873e8df6d25fce9282fb9bfbd3f8f6ff32a639a42963448787d88a:7e3627579e1e4304874ce442f2e50760');

-- #####################################################################
-- # Insert Initial answers
-- #####################################################################
DELETE FROM Answer WHERE ID >= 1;
ALTER TABLE Answer AUTO_INCREMENT = 1;
DELETE FROM Question_Answer WHERE ID >= 1;
ALTER TABLE Question_Answer AUTO_INCREMENT = 1;
-- Answers For Questions of Module 1 -> Q2, Q2.1, Q2.2, Q2.3, Q2.5, Q3, Q3.1, Q4, Q5, Q6, Q7, Q8, Q9, Q10, and Q11; for Module 2 -> Q6, Q6.1, and Q7.
INSERT INTO Answer (ID, content) VALUES (10, 'Yes');
INSERT INTO Answer (ID, content) VALUES (11, 'No');

-- #####################################################################
-- # Insert Module Types
-- #####################################################################
DELETE FROM Type WHERE ID >= 1;
ALTER TABLE Type AUTO_INCREMENT = 1;
INSERT INTO Type (ID, name, description) VALUES (1, 'Security Requirements', 'Provides Security Requirements');
INSERT INTO Type (ID, name, description) VALUES (2, 'Security Pratices', 'Provides Security Guidelines');
INSERT INTO Type (ID, name, description) VALUES (3, 'Security Algorithms', 'Provides Security Cryptographic Algorithms');

-- #####################################################################
-- # Insert Modules
-- #####################################################################
DELETE FROM Module WHERE ID >= 1;
ALTER TABLE Module AUTO_INCREMENT = 1;
INSERT INTO Module (ID, typeID, shortname, fullname, displayname) VALUES (1, 1, 'SRE',  'Security Requirements Elicitation', 'Security Requirements');
INSERT INTO Module (ID, typeID, shortname, fullname, displayname) VALUES (2, 2, 'SBPG', 'Security Best Pratice Guidelines', 'Security Best Pratices');
INSERT INTO Module (ID, typeID, shortname, fullname, displayname) VALUES (3, 3, 'SCAR', 'Security Cryptographic Algorithms Recomendation', 'Security Cryptographic Algorithms'); 

-- #####################################################################
-- # Insert Questions and Associate the questions with a module
-- #####################################################################
DELETE FROM Question WHERE ID >= 1;
ALTER TABLE Question AUTO_INCREMENT = 1;
DELETE FROM Module_Question WHERE ID >= 1;
ALTER TABLE Module_Question AUTO_INCREMENT = 1;
DELETE FROM Question_has_Child WHERE ID >= 1;
ALTER TABLE Question_has_Child AUTO_INCREMENT = 1;
-- For Module 1
INSERT INTO Question (ID, content) VALUES (1, 'Q1 - State the domain type for your IoT system');
INSERT INTO Question (ID, content) VALUES (2, 'Q2 - Will the system have a user?');
	INSERT INTO Question (ID, content) VALUES (3, 'Q2.1 - Will the system have user LogIn?');
    -- Sub sub questions example
		INSERT INTO Question (ID, content) VALUES (30, 'Q2.1.2 - test 1?');
			INSERT INTO Question (ID, content) VALUES (31, 'Q2.1.2.1 - test 2?');
				INSERT INTO Question (ID, content) VALUES (32, 'Q2.1.2.1.1 - test 3?');
    INSERT INTO Question (ID, content) VALUES (4, 'Q2.2 - Will the system hold any user information?');
	INSERT INTO Question (ID, content) VALUES (5, 'Q2.3 - Will the system store any kind of information?');
	INSERT INTO Question (ID, content) VALUES (6, 'Q2.4 - What will be the level of information stored?');
	INSERT INTO Question (ID, content) VALUES (7, 'Q2.5 -  Will this information be sent to an entity?');
INSERT INTO Question (ID, content) VALUES (8, 'Q3 - Will the system be connected to the internet?');
	INSERT INTO Question (ID, content) VALUES (9, 'Q3.1 - Will it send its data to a cloud?');
INSERT INTO Question (ID, content) VALUES (10, 'Q4 - Will it store data in a db?');
INSERT INTO Question (ID, content) VALUES (11, 'Q5 - Will the system receive regular updates?');
INSERT INTO Question (ID, content) VALUES (12, 'Q6 - Will the system work with third-party software?');
INSERT INTO Question (ID, content) VALUES (13, 'Q7 - Is there a possibility of the communications being eavesdropped?');
INSERT INTO Question (ID, content) VALUES (14, 'Q8 - Could the messages sent between the system components be captured and resent?');
INSERT INTO Question (ID, content) VALUES (15, 'Q9 - Can someone try to impersonate a user to gain access to private information?');
INSERT INTO Question (ID, content) VALUES (16, 'Q10 - Can someone with bad intentions gain physical access to the location where this software will be running and obtain private information?');
INSERT INTO Question (ID, content) VALUES (17, 'Q11 - Can someone gain physical access to the machine where the system operatesor some of the system components and preform some type of modification to');

-- Some of the previous questions have sub questions (childs), we need to store this mapping information.
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (2, 3, 1, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (2, 4, 2, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (2, 5, 3, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (2, 6, 4, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (2, 7, 5, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (8, 9, 1, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (3, 30, 1, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (30, 31, 1, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (31, 32, 1, 10);

-- Associate Questions to Module 1 (only the parent questions, the childs can be easily found).
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 1, 1);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 2, 2);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 8, 3);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 10, 4);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 11, 5);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 12, 6);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 13, 7);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 14, 8);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 15, 9);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 16, 10);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (1, 17, 10);

-- For Module 2
INSERT INTO Question (ID, content) VALUES (18, 'Q1 - What is the architecture of the system ?');
INSERT INTO Question (ID, content) VALUES (19, 'Q2 - Does the system use a database?');
	INSERT INTO Question (ID, content) VALUES (20, 'Q2.1 - What is the type of data storage?');
	INSERT INTO Question (ID, content) VALUES (21, 'Q2.2 - Which database is used?');
	INSERT INTO Question (ID, content) VALUES (22, 'Q2.3 - What is the type of data stored?');
INSERT INTO Question (ID, content) VALUES (23, 'Q3 - Which type of authentication will be implemented?');
INSERT INTO Question (ID, content) VALUES (24, 'Q4 - Will there be user registration?');
	INSERT INTO Question (ID, content) VALUES (25, 'Q4.1 - Which way of user registration will be used?');
INSERT INTO Question (ID, content) VALUES (26, 'Q5 - Which programming languages will be used in the implementation of the system?');
INSERT INTO Question (ID, content) VALUES (27, 'Q6 - Will the system allow input forms?');
	INSERT INTO Question (ID, content) VALUES (28, 'Q6.1 - Will the system allow file uploads?');
INSERT INTO Question (ID, content) VALUES (29, 'Q7 - Will th system have logging?');

-- Some of the previous questions have sub questions (childs), we need to store this mapping information.
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (19, 20, 1, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (19, 21, 2, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (19, 22, 3, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (24, 25, 1, 10);
INSERT INTO Question_has_Child (parent, child, questionOrder, ontrigger) VALUES (27, 28, 1, 10);

-- Associate Questions to Module 2 (only the parent questions, the childs can be easily found).
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (2, 18, 1);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (2, 19, 2);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (2, 23, 3);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (2, 24, 4);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (2, 26, 5);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (2, 27, 6);
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (2, 29, 8);

-- #####################################################################
-- # Insert more Answers and Associate the answers with one or more questions
-- #####################################################################


-- Answers For Question Q1 of Module 1
INSERT INTO Answer (ID, content) VALUES (1, 'Smart Home');
INSERT INTO Answer (ID, content) VALUES (2, 'Smart Healthcare');
INSERT INTO Answer (ID, content) VALUES (3, 'Smart Manufacturing');
INSERT INTO Answer (ID, content) VALUES (4, 'Smart Wearables');
INSERT INTO Answer (ID, content) VALUES (5, 'Smart Toys');
INSERT INTO Answer (ID, content) VALUES (6, 'Smart Transportation');

-- Answers For Question Q2.4 of Module 1
INSERT INTO Answer (ID, content) VALUES (7, 'Normal');
INSERT INTO Answer (ID, content) VALUES (8, 'Sensitive');
INSERT INTO Answer (ID, content) VALUES (9, 'Critical');



-- Answers For Question Q1 of Module 2
INSERT INTO Answer (ID, Content) VALUES (12, 'Web Application');
INSERT INTO Answer (ID, Content) VALUES (13, 'Web Service');
INSERT INTO Answer (ID, Content) VALUES (14, 'Desktop Application');
INSERT INTO Answer (ID, Content) VALUES (15, 'Mobile Application');
INSERT INTO Answer (ID, Content) VALUES (16, 'Client-Server -> Client Component');
INSERT INTO Answer (ID, Content) VALUES (17, 'Client-Server -> Server Component');
INSERT INTO Answer (ID, Content) VALUES (18, 'API Service');
INSERT INTO Answer (ID, Content) VALUES (19, 'Embedded System');
INSERT INTO Answer (ID, Content) VALUES (20, 'Others');

-- Answers For Question Q2.1 of Module 2
INSERT INTO Answer (ID, Content) VALUES (21, 'SQL');
INSERT INTO Answer (ID, Content) VALUES (22, 'NoSQL');
INSERT INTO Answer (ID, Content) VALUES (23, 'Local Storage');
INSERT INTO Answer (ID, Content) VALUES (24, 'Distributed Storage');

-- Answers For Question Q2.2 of Module 2
INSERT INTO Answer (ID, Content) VALUES (25, 'SQL Server');
INSERT INTO Answer (ID, Content) VALUES (26, 'MySQL');
INSERT INTO Answer (ID, Content) VALUES (27, 'PostgresSQL');
INSERT INTO Answer (ID, Content) VALUES (28, 'SQLite');
INSERT INTO Answer (ID, Content) VALUES (29, 'OracleDB');
INSERT INTO Answer (ID, Content) VALUES (30, 'MariaDB');
INSERT INTO Answer (ID, Content) VALUES (31, 'MongoDB');
INSERT INTO Answer (ID, Content) VALUES (32, 'CosmosDB');
INSERT INTO Answer (ID, Content) VALUES (33, 'DynamoDB');
INSERT INTO Answer (ID, Content) VALUES (34, 'Cassandra');

-- Answers For Question Q2.3 of Module 2
INSERT INTO Answer (ID, Content) VALUES (35, 'Personal Information (Names, Addresses...)');
INSERT INTO Answer (ID, Content) VALUES (36, 'Confidential Data');
INSERT INTO Answer (ID, Content) VALUES (37, 'Critical Data');

-- Answers For Question Q3 of Module 2
INSERT INTO Answer (ID, Content) VALUES (38, 'No Authentication');
INSERT INTO Answer (ID, Content) VALUES (39, 'Username and Password');
INSERT INTO Answer (ID, Content) VALUES (40, 'Social Networks/Google');
INSERT INTO Answer (ID, Content) VALUES (41, 'SmartCard');
INSERT INTO Answer (ID, Content) VALUES (42, 'Biometric');
INSERT INTO Answer (ID, Content) VALUES (43, 'Two Factor Authentication');
INSERT INTO Answer (ID, Content) VALUES (44, 'Multi Factor Authentication');

-- Answers For Question Q4.1 of Module 2
INSERT INTO Answer (ID, Content) VALUES (45, 'The users will register themselves');
INSERT INTO Answer (ID, Content) VALUES (46, 'An administrator will register the users');

-- Answers For Question Q5 of Module 2
INSERT INTO Answer (ID, Content) VALUES (47, 'C/C++');
INSERT INTO Answer (ID, Content) VALUES (48, 'Java');
INSERT INTO Answer (ID, Content) VALUES (49, 'Javascript');
INSERT INTO Answer (ID, Content) VALUES (50, 'PHP');
INSERT INTO Answer (ID, Content) VALUES (51, 'Python');
INSERT INTO Answer (ID, Content) VALUES (52, 'Ruby');
INSERT INTO Answer (ID, Content) VALUES (53, 'Other/Proprietary Language');

-- Associate Answers and Questions 
INSERT INTO Question_Answer(questionID, answerID) VALUES (1, 1);
INSERT INTO Question_Answer(questionID, answerID) VALUES (1, 2);
INSERT INTO Question_Answer(questionID, answerID) VALUES (1, 3);
INSERT INTO Question_Answer(questionID, answerID) VALUES (1, 4);
INSERT INTO Question_Answer(questionID, answerID) VALUES (1, 5);
INSERT INTO Question_Answer(questionID, answerID) VALUES (1, 6);
--
INSERT INTO Question_Answer(questionID, answerID) VALUES (6, 7);
INSERT INTO Question_Answer(questionID, answerID) VALUES (6, 8);
INSERT INTO Question_Answer(questionID, answerID) VALUES (6, 9);
--
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 12);
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 13);
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 14);
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 15);
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 16);
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 17);
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 18);
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 19);
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 20);
--
INSERT INTO Question_Answer(questionID, answerID) VALUES (20, 21);
INSERT INTO Question_Answer(questionID, answerID) VALUES (20, 22);
INSERT INTO Question_Answer(questionID, answerID) VALUES (20, 23);
INSERT INTO Question_Answer(questionID, answerID) VALUES (20, 24);
--
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 25);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 26);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 27);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 28);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 29);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 30);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 31);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 32);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 33);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 34);
--
INSERT INTO Question_Answer(questionID, answerID) VALUES (22, 35);
INSERT INTO Question_Answer(questionID, answerID) VALUES (22, 36);
INSERT INTO Question_Answer(questionID, answerID) VALUES (22, 37);
--
INSERT INTO Question_Answer(questionID, answerID) VALUES (23, 38);
INSERT INTO Question_Answer(questionID, answerID) VALUES (23, 39);
INSERT INTO Question_Answer(questionID, answerID) VALUES (23, 40);
INSERT INTO Question_Answer(questionID, answerID) VALUES (23, 41);
INSERT INTO Question_Answer(questionID, answerID) VALUES (23, 42);
INSERT INTO Question_Answer(questionID, answerID) VALUES (23, 43);
INSERT INTO Question_Answer(questionID, answerID) VALUES (23, 44);
--
INSERT INTO Question_Answer(questionID, answerID) VALUES (25, 45);
INSERT INTO Question_Answer(questionID, answerID) VALUES (25, 46);
--
INSERT INTO Question_Answer(questionID, answerID) VALUES (26, 47);
INSERT INTO Question_Answer(questionID, answerID) VALUES (26, 48);
INSERT INTO Question_Answer(questionID, answerID) VALUES (26, 49);
INSERT INTO Question_Answer(questionID, answerID) VALUES (26, 50);
INSERT INTO Question_Answer(questionID, answerID) VALUES (26, 51);
INSERT INTO Question_Answer(questionID, answerID) VALUES (26, 52);
INSERT INTO Question_Answer(questionID, answerID) VALUES (26, 53);
--
INSERT INTO Question_Answer(questionID, answerID) VALUES (18, 20);
INSERT INTO Question_Answer(questionID, answerID) VALUES (21, 20);
INSERT INTO Question_Answer(questionID, answerID) VALUES (26, 20);

-- Yes or No answers
INSERT INTO Question_Answer(questionID, answerID) VALUES (2, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (2, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (3, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (3, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (4, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (4, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (5, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (5, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (7, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (7, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (8, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (8, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (9, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (9, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (10, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (10, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (11, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (11, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (12, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (12, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (13, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (13, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (14, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (14, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (15, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (15, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (16, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (17, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (19, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (19, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (24, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (24, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (27, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (27, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (28, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (28, 11);
INSERT INTO Question_Answer(questionID, answerID) VALUES (29, 10);
INSERT INTO Question_Answer(questionID, answerID) VALUES (29, 11);

-- #####################################################################
-- # Insert Dependencies
-- #####################################################################
DELETE FROM Dependency WHERE ID >= 1;
ALTER TABLE Dependency AUTO_INCREMENT = 1;
-- Module 3 (SCAR) depends on Module 1 (SRE)
INSERT INTO Dependency (moduleID, dependsOn) VALUES (3, 1);


-- #####################################################################
-- # Insert Recomendations / outputs of each module according to the set of answers given to a set of questions.
-- # Incomplete!
-- #####################################################################

-- For Module 1
INSERT INTO Recomendation (ID, content) VALUES (1, 'Confidentiality');
INSERT INTO Recomendation (ID, content) VALUES (2, 'Integrity');
-- INSERT INTO Recomendation (ID, content) VALUES (3, 'Availability');
-- INSERT INTO Recomendation (ID, content) VALUES (4, 'Authentication');
-- INSERT INTO Recomendation (ID, content) VALUES (5, 'Non-Repudiation');
-- INSERT INTO Recomendation (ID, content) VALUES (6, 'Accountability');
-- INSERT INTO Recomendation (ID, content) VALUES (7, 'Reliability');
-- INSERT INTO Recomendation (ID, content) VALUES (8, 'Privacy');
-- INSERT INTO Recomendation (ID, content) VALUES (9, 'Physical Security');
-- INSERT INTO Recomendation (ID, content) VALUES (10, 'Forgery Resistance');
-- INSERT INTO Recomendation (ID, content) VALUES (11, 'Tamper Detection');
-- INSERT INTO Recomendation (ID, content) VALUES (12, 'Data Freshness');
-- INSERT INTO Recomendation (ID, content) VALUES (13, 'Confinement');
-- INSERT INTO Recomendation (ID, content) VALUES (14, 'Interoperability');
-- INSERT INTO Recomendation (ID, content) VALUES (15, 'Data Origin');

-- Associate recomendations with answers
-- Answers that needs to be answer in order to suggest 'Confidentiality' as an output .
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (1, 1);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (1, 2);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (1, 3);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (1, 4);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (1, 5);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (1, 6);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (1, 9);

-- Answers that needs to be answer in order to suggest 'Integrity' as an output.
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (2, 1);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (2, 2);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (2, 3);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (2, 4);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (2, 5);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (2, 6);
INSERT INTO Recomendation_Question_Answer (recomendationID, questionAnswerID) VALUES (2, 67);

-- #####################################################################
-- # Test Modules for user input with some logic
-- #####################################################################
INSERT INTO Module (ID, typeID, shortname, fullname, displayname) VALUES (4, 1, 'AL',  'Algorithms', 'Algorithms');
INSERT INTO Question (ID, content) VALUES (33, 'Q1 - Enter the bit number of your first CPU');
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (4, 33, 1);
INSERT INTO Question (ID, content) VALUES (34, 'Q2 - Enter the bit number of your second CPU');
INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (4, 34, 2);

-- Simulate also a session that needs a module with user input and some logic attached
INSERT INTO SESSION (ID, userID, moduleID, ended) VALUES (1, 1, 4, 1);
INSERT INTO Session_Question_Answer (sessionID, questionID, input) VALUES (1, 33, '16');
INSERT INTO Session_Question_Answer (sessionID, questionID, input) VALUES (1, 34, '32');
-- Add a recomendation based on some logic used by an external module
INSERT INTO Recomendation (ID, content) VALUES (3, 'Algorithm XYZ');




-- #####################################################################
-- # Insert Dependency examples, for example, IoT-HarPSecA needs the answers given to other modules.
-- #####################################################################