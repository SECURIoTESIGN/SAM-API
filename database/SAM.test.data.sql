-- #############################
-- CREATE MODULE M1
-- #############################
USE SAM;

-- SQL Test data Table "MODULES"
INSERT INTO Module (ID, name, shortname, description, typeID) VALUES (1, 'M1', 'M1', 'M1 Description', NULL);

-- SQL Test Data Table "QUESTION"
INSERT INTO Question (ID, content, description) VALUES (1, 'M1 Question 1', 'Q1 Description');
INSERT INTO Question (ID, content, description) VALUES (2, 'M2 Question 2', 'Q2 Description');

-- SQL Test Data Table "ANSWER"
INSERT INTO Answer (ID, content, description) VALUES (1, 'Answer 1 to Question 1 of M1', 'A1 Description');
INSERT INTO Answer (ID, content, description) VALUES (2, 'Answer 2 to Question 1 of M1', 'A2 Description');

-- SQL Test Data Table "RECOMENDATION"
INSERT INTO Recomendation (ID, content, description, guideFilename) VALUES (1, 'Recomendation to A1 of M1', 'R1 Description', 'R1.txt');
INSERT INTO Recomendation (ID, content, description, guideFilename) VALUES (2, 'Recomendation to A2 of M1', 'R2 Description', 'R1.txt');

-- SQL Test Data Junction-Tables "MODULES_QUESTION"
INSERT INTO Module_Question (ID, moduleID, questionID) VALUES (1, 1, 1);
INSERT INTO Module_Question (ID, moduleID, questionID) VALUES (2, 1, 2);

-- SQL Test Data Junction-Tables "QUESTION_ANSWER"
INSERT INTO Question_Answer (ID, questionID, answerID) VALUES (1, 1, 1);
INSERT INTO Question_Answer (ID, questionID, answerID) VALUES (2, 1, 2);

-- SQL Test Data Junction-Tables "ANSWER_RECOMENDATION"
-- One Recomendation mapped to multiple answers
INSERT INTO Answer_Recomendation (ID, answerID, recomendationID) VALUES (1, 1, 1);
INSERT INTO Answer_Recomendation (ID, answerID, recomendationID) VALUES (3, 1, 2);
INSERT INTO Answer_Recomendation (ID, answerID, recomendationID) VALUES (2, 2, 2);


-- #############################
-- CREATE MULTIPLE SESSIONS FOR MODULE M1
-- #############################
-- SQL Test data Table "User"
INSERT INTO User (ID, email) VALUES (1, "test@test.com");
INSERT INTO User (ID, email) VALUES (2, "test2@test.com");


-- SQL Test data Table "Session"
INSERT INTO Session (ID, moduleID, userID) VALUES (1, 1, 1); -- SESSION 1 for USER 1
INSERT INTO Session (ID, moduleID, userID) VALUES (2, 1, 2); -- SESSION 2 for USER 2

-- SQL Test Data Junction-Tables "ANSWER_RECOMENDATION"
INSERT INTO Session_User_Answer (ID, sessionID, questionAnswerID) VALUES (1, 1, 1); -- USER ANSWERS FOR SESSION 1
INSERT INTO Session_User_Answer (ID, sessionID, questionAnswerID) VALUES (2, 1, 2); -- USER ANSWERS FOR SESSION 1
INSERT INTO Session_User_Answer (ID, sessionID, questionAnswerID) VALUES (3, 2, 1); -- USER ANSWERS FOR SESSION 2



