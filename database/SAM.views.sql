USE SAM;

-- View_Module_Recommendations: Get the recommendations mapped to a module.
DROP VIEW IF EXISTS View_Module_Recommendations;
CREATE VIEW View_Module_Recommendations AS
SELECT DISTINCT
	R.ID as recommendation_ID,
    M.ID as module_ID,
    R.content as recommendation_content,
    R.description as recommendation_description,
    R.guidefilename as recommendation_guide,
	R.createdon,
    R.updatedon
FROM 
	Module as M,
    Module_Question as MQ,
    Question as Q,
    Question_Answer as QA,
    Recommendation_Question_Answer as RQA,
    Recommendation as R
WHERE
	M.ID = MQ.moduleID AND MQ.questionID = Q.ID AND 
    Q.ID = QA.questionID AND
    RQA.questionAnswerID = QA.ID AND RQA.recommendationID = R.ID;
    

-- View_Module_Recommendations: Get the recommendations, questions and answers mapped to a module.
DROP VIEW IF EXISTS View_Module_Recommendations_Questions_Answers;
CREATE VIEW View_Module_Recommendations_Questions_Answers AS
SELECT DISTINCT
	M.ID as module_ID,
    R.ID as recommendation_ID,
    R.content as recommendation_content,
    RQA.id as recommendation_question_answer_ID,
    QA.questionID as question_id,
    QA.answerID as answer_id,
    RQA.createdon,
    RQA.updatedon
FROM 
	Module as M,
    Module_Question as MQ,
    Question as Q,
    Question_Answer as QA,
    Recommendation_Question_Answer as RQA,
    Recommendation as R
WHERE
	M.ID = MQ.moduleID AND MQ.questionID = Q.ID AND 
    Q.ID = QA.questionID AND
    RQA.questionAnswerID = QA.ID AND RQA.recommendationID = R.ID;


-- View_User_Group: Get groups of user
DROP VIEW IF EXISTS View_User_Group;
CREATE VIEW View_User_Group AS
SELECT
	U.ID as user_id,
    U.email as user_email,
    G.designation as user_group
FROM
SAm.Group as G,
User_Group as UG,
User as U
WHERE
G.ID = UG.groupID AND
U.ID = UG.userID;



-- View_Module_Question: Get dependencies of a module
DROP VIEW IF EXISTS View_Module_Dependency;
CREATE VIEW View_Module_Dependency AS
SELECT
	D.ID as dependency_ID,
	D.moduleID as module_id,
    M.shortname as module_shortname,
    M.fullname as module_name,
    M.displayname as display,
    --
    D.dependsOn as depends_module_id,
    D.createdon,
    D.updatedon
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
    A.content as answer,
    --
    Q.createdon as question_createdon,
    Q.updatedon as question_updatedon,
    A.createdon as answer_createdon,
    A.updatedon as answer_updatedon
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
    MQ.questionOrder,
    --
    Q.createdon,
    Q.updatedon
FROM Module as M,Question as Q, Module_Question AS MQ WHERE
M.ID = MQ.moduleID AND Q.ID = MQ.questionID;

-- View_Module_Question: Get answers of a module.
DROP VIEW IF EXISTS View_Module_Answers;
CREATE VIEW View_Module_Answers AS
SELECT 
	DISTINCT
	M.ID as module_ID,
    --
    A.ID as answer_ID, 
    A.content as answer,
    --
    A.createdon,
    A.updatedon
FROM 
	Module as M,
    Question as Q, 
    Module_Question AS MQ,
    Answer as A, 
    Question_Answer as QA
    WHERE
	M.ID = MQ.moduleID AND 
    Q.ID = MQ.questionID AND
    A.ID = QA.answerID AND
    Q.ID = QA.questionID;

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
	QA.ID as question_answer_id,
	--
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
DROP VIEW IF EXISTS View_recommendations;
CREATE VIEW View_recommendations AS
SELECT 
	Q.id as question_id,
    Q.content as question,
    --
    A.ID as answer_id, 
    A.content as answer,
    --
    R.content as recommendation
    
FROM 
	Question as Q, Answer as A, Question_Answer as QA, recommendation_Question_Answer AS RQA, recommendation as R
WHERE
	Q.ID = QA.questionID AND A.ID = QA.answerID AND
    R.ID = RQA.recommendationID AND QA.ID = RQA.questionAnswerID;


-- View_Session_Input_Answer: Get sessions of users.
DROP VIEW IF EXISTS View_User_Sessions;
CREATE VIEW View_User_Sessions AS
SELECT
	S.id as session_id,
    U.id as user_id,
    U.email as user_email,    
	S.moduleID,
    S.ended,
    S.createdon,
    S.updatedon
FROM
	Session as S,
    User as U
WHERE
	U.ID = S.userID;


-- View_Session_Input_Answer: Get answers of a question.
DROP VIEW IF EXISTS View_Session_Answers;
CREATE VIEW View_Session_Answers AS
-- ## Shows user selected answers
SELECT 
S.ID as session_ID, 
S.userID as session_userID,
S.moduleID as session_moduleID,
S.ended as session_ended,
S.createdon as session_createdon,
S.updatedon as session_updatedon,
--
NULL as module_logic,
--
Q.ID as question_ID,
Q.content as question,
--
SUA.input answer_input,
--
A.ID as answer_id,
A.content as answer
FROM 
	Session as S,
    Session_User_Answer as SUA,
    Question as Q,
    Question_Answer as QA,
    Answer as A
WHERE
	S.ID = SUA.sessionID AND
    SUA.questionAnswerID = QA.ID AND
    QA.questionID = Q.ID AND
    QA.answerID = A.ID

UNION
-- ## Shows user inputted answers
SELECT DISTINCT
S.ID as session_ID, 
S.userID as session_userID,
S.moduleID as session_moduleID,
S.ended as session_ended,
S.createdon as session_createdon,
S.updatedon as session_updatedon,
--
M.logicFileName as module_logic,
--
Q.ID as question_ID,
Q.content as question,
--
SUA.input answer_input,
--
Null as answer_ID,
Null as answer
FROM 
	Session as S,
    Session_User_Answer as SUA,
    Question as Q,
    Question_Answer as QA,
    Module as M
WHERE
	S.ID = SUA.sessionID AND
    SUA.questionID = Q.ID AND
    S.moduleID = M.ID;

-- View_Session_Recommendation: Get recommendations stored in a session.
DROP VIEW IF EXISTS View_Session_Recommendation;
CREATE VIEW View_Session_Recommendation AS
SELECT 
S.ID as session_ID, 
S.userID as session_userID,
s.moduleID as session_moduleID,
s.ended as session_ended,
s.createdon as session_createdOn,
s.updatedOn as session_updatedOn,
--
R.ID as recommendation_ID,
R.content as recommendation,
R.description as recommendation_description,
R.guideFilename as recommendation_guide,
R.createdOn as recommendation_createdOn,
R.updatedOn as recommendation_updatedOn
FROM 
	Session as S,
    Session_Recommendation as SR,
    Recommendation as R
WHERE
	S.ID = SR.sessionID AND
    SR.recommendationID = R.ID;

-- View_Session_recommendation: Get recommendations to be stored in a session. 
DROP VIEW IF EXISTS View_Recommendation;
CREATE VIEW View_Recommendation AS
Select DISTINCT
S.ID as session_ID,
R.ID as recommendation_ID,
R.content as recommendation,
R.description as recommendation_description,
R.guideFileName
FROM
	Session as S,
	session_user_Answer as SUA,
    question_answer as QA,
    Recommendation_question_answer as RQA,
    recommendation as R
WHERE
	S.ID = SUA.sessionID AND
    SUA.questionAnswerID = QA.ID AND
    --
    QA.ID = RQA.questionAnswerID AND
    RQA.recommendationID = R.ID;
    
-- View_Session_recommendation: Get recommendations to be stored in a session that were computed using some logic.
DROP VIEW IF EXISTS View_Recommendation_Logic;
CREATE VIEW View_Recommendation_Logic AS
Select DISTINCT
S.ID as session_ID,
R.ID as recommendation_ID,
R.content as recommendation,
R.description as recommendation_description,
R.guideFileName
FROM
	Session as S,
    Session_Recommendation as SR,
    Recommendation as R
WHERE
	S.ID = SR.sessionID AND
    R.ID = SR.recommendationID;
    
DROP VIEW IF EXISTS View_Question_Answer_Recommendation;
CREATE VIEW View_Question_Answer_Recommendation AS
SELECT
QA.questionID as question_ID,
QA.answerID as answer_ID,
R.ID as recommendation_ID,
R.content as content,
R.description as description,
R.guideFileName as guide,
R.createdOn as createdOn,
R.updatedOn as updatedOn
FROM
Question_Answer AS QA, 
Recommendation_Question_Answer as RQA,
Recommendation as R
WHERE
QA.ID = RQA.questionAnswerID AND
R.ID = RQA.recommendationID;

