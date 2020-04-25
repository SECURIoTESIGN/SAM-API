USE SAM;
-- View_Module_Question: Get the set of questions for each module 
DROP VIEW IF EXISTS View_Module_Question;
CREATE VIEW View_Module_Question AS
SELECT 
	M.ID as module_ID,
    M.name as module_name,
    M.shortname as module_shortname,
    M.description as module_description,
    --
    Q.ID as question_ID, 
    q.content as question_content,
    q.description as question_description
FROM Module as M,Question as Q, Module_Question AS MQ WHERE
M.ID = MQ.moduleID AND Q.ID = MQ.questionID;

-- View_Question_Answer: Get the set of answers for each question
DROP VIEW IF EXISTS View_Question_Answer;
CREATE VIEW View_Question_Answer AS
SELECT
	Q.ID as question_ID,
    Q.content as question_content,
    Q.description as question_description,
    --
    A.ID as answer_ID,
    A.content as answer_content,
    A.description as answer_description
FROM
	Question as Q, Answer as A, Question_Answer QA
WHERE
	Q.ID = QA.questionID AND A.ID = QA.answerID;
    

-- View_Answer_Recomendation: Get the set of recomendations for each answer 
DROP VIEW IF EXISTS View_Answer_Recomendation;
CREATE VIEW View_Answer_Recomendation AS
SELECT
	A.ID as answer_ID,
    A.content as answer_content,
    A.description as answer_description,
    --
    R.ID as recomendation_ID,
    R.content as recomendation_content,
    R.description as recomendation_description,
    R.guideFilename as recomendation_guideFilename
FROM
	Answer as A, Recomendation as R, Answer_Recomendation as AR
WHERE
	A.ID = AR.answerID AND R.ID = AR.recomendationID;


-- View_Session: Gets session information for all users
DROP VIEW IF EXISTS View_Session;
CREATE VIEW View_Session AS
SELECT
    S.moduleID as module_ID,
	S.ID as session_ID,
    S.userID,
    --
    Q.ID as question_ID,
    Q.content as question,
    --
    A.ID as answer_ID, 
    A.content as answer
FROM
	Session as S, Session_User_Answer as SA, Question as Q, Answer A, Question_Answer as QA
WHERE
	S.ID = SA.sessionID AND QA.ID = SA.questionAnswerID AND Q.ID = QA.questionID AND A.ID = QA.answerID

