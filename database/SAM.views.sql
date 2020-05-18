USE SAM;

-- View_Module_Question: Get dependencies of a module
DROP VIEW IF EXISTS View_Module_Dependency;
CREATE VIEW View_Module_Dependency AS
SELECT
	D.moduleID as module_id,
    M.shortname as module_shortname,
    M.fullname as module_name,
    M.displayname as display,
    --
    D.dependsOn as depends_module_id
FROM 
	Module as M, Dependency as D
WHERE 
	D.moduleID = M.ID;

-- View_Module_Question: Get questions of a module.
DROP VIEW IF EXISTS View_Module_Questions_Answers;
CREATE VIEW View_Module_Questions_Answers AS
SELECT 
	M.ID as module_ID,
    M.displayname as module_displayname,
    --
    Q.ID as question_ID, 
    q.content as question,
    --
    MQ.questionOrder,
    -- 
    A.ID as answer_ID, 
    A.content as answer
FROM 
	Module as M,Question as Q, 
    Module_Question as MQ, 
    Question_Answer as QA,
    Answer as A
WHERE
	M.ID = MQ.moduleID AND Q.ID = MQ.questionID 
    AND
    A.ID = QA.answerID AND Q.ID = QA.questionID;

-- View_Module_Question: Get questions of a module.
DROP VIEW IF EXISTS View_Module_Question;
CREATE VIEW View_Module_Question AS
SELECT 
	M.ID as module_ID,
    M.displayname as module_displayname,
    --
    Q.ID as question_ID, 
    q.content as question,
    --
    MQ.questionOrder
FROM Module as M,Question as Q, Module_Question AS MQ WHERE
M.ID = MQ.moduleID AND Q.ID = MQ.questionID;

-- View_Module_Question: Get sub-questions of a question (child questions of a parent question).
DROP VIEW IF EXISTS View_Question_Childs;
CREATE VIEW View_Question_Childs AS
SELECT
	QP.parent as parent_id,
    --
    QP.child as child_id,
    Q.content as question,
    --
    QP.ontrigger,
    QP.questionOrder
FROM 
	Question_has_Child as QP,
    Question as Q
WHERE
	QP.child = Q.ID;
    
-- View_Answer_Question: Get answers of a question.
DROP VIEW IF EXISTS View_Question_Answer;
CREATE VIEW View_Question_Answer AS
SELECT
	Q.ID as question_id,
	Q.content as question,
    --
    A.ID as answer_id,
    A.content as answer
FROM 
	Question as Q, Question_Answer as QA, Answer as A
WHERE
	Q.ID = QA.questionID AND QA.answerID = A.ID;
    
    
-- View_Answer_Question: Get answers of a question.
DROP VIEW IF EXISTS View_Recomendations;
CREATE VIEW View_Recomendations AS
SELECT 
	Q.id as question_id,
    Q.content as question,
    --
    A.ID as answer_id, 
    A.content as answer,
    --
    R.content as recomendation
    
FROM 
	Question as Q, Answer as A, Question_Answer as QA, Recomendation_Question_Answer AS RQA, Recomendation as R
WHERE
	Q.ID = QA.questionID AND A.ID = QA.answerID AND
    R.ID = RQA.recomendationID AND QA.ID = RQA.questionAnswerID;


-- View_Session_Input_Answer: Get answers of a question.
DROP VIEW IF EXISTS View_Session_Input_Answer;
CREATE VIEW View_Session_Input_Answer AS
SELECT 
S.ID as session_ID, 
S.userID as session_userID,
s.moduleID as session_moduleID,
s.ended as session_ended,
s.createdon as session_createdOn,
s.updatedOn as session_updatedOn,
--
Q.ID as question_ID,
Q.content as question,
SQA.input answer_input
FROM 
	Session as S,
    Session_Question_Answer as SQA,
    Question as Q
WHERE
	S.ID = SQA.sessionID AND
	Q.ID = SQA.questionID;