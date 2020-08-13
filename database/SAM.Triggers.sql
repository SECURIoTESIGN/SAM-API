USE SAM;

-- Trigger_Recommendation_Delete: After deleting a recommendation that cascades to table session_recommendation delete also linked sessions.
DROP TRIGGER IF EXISTS Trigger_Recommendation_Delete;
CREATE TRIGGER Trigger_Recommendation_Delete BEFORE DELETE on Recommendation
FOR EACH ROW
	-- Only delete a session, if the session linked to the deleted recommendation has no more recommendations linked to it.
    DELETE FROM Session WHERE Session.id = (SELECT SessionID FROM Session_Recommendation WHERE Session_Recommendation.recommendationID = OLD.id)
	AND EXISTS (SELECT sessionID FROM session_recommendation WHERE sessionID = Session.id GROUP BY sessionID HAVING count(sessionID) = 1);

-- Trigger_Question_Delete: After deleting a question that cascades to other tables, also delete linked sessions. These sessions become invalid.
DROP TRIGGER IF EXISTS Trigger_Question_Delete;
CREATE TRIGGER Trigger_Question_Delete BEFORE DELETE on Question
FOR EACH ROW
	-- Delete sessions linked to this question
    DELETE FROM Session WHERE 
    Session.id = (SELECT SessionID FROM Session_User_Answer WHERE questionID = OLD.id OR questionAnswerID IN (SELECT ID FROM Question_Answer WHERE questionID = OLD.ID));

-- Trigger_Answer_Delete: After deleting an answer that cascades to other tables, also delete linked sessions. These sessions become invalid.
DROP TRIGGER IF EXISTS Trigger_Answer_Delete;
CREATE TRIGGER Trigger_Answer_Delete BEFORE DELETE on Answer
FOR EACH ROW
	-- Delete sessions linked to this question
    DELETE FROM Session WHERE 
    Session.id = (SELECT SessionID FROM Session_User_Answer WHERE questionAnswerID IN (SELECT ID FROM Question_Answer WHERE answerID = OLD.ID));

-- Before updating an entry, set NOW() into the 'updatedon' date, apply this to the following tables:
DROP TRIGGER IF EXISTS Trigger_Question_Update;
CREATE TRIGGER Trigger_Question_Update BEFORE UPDATE on Question
FOR EACH ROW
	SET NEW.updatedon = NOW();

DROP TRIGGER IF EXISTS Trigger_Module_Update;
CREATE TRIGGER Trigger_Module_Update BEFORE UPDATE on Module
FOR EACH ROW
	SET NEW.updatedon = NOW();

DROP TRIGGER IF EXISTS Trigger_Answer_Update;
CREATE TRIGGER Trigger_Answer_Update BEFORE UPDATE on Answer
FOR EACH ROW
	SET NEW.updatedon = NOW();

DROP TRIGGER IF EXISTS Trigger_Type_Update;
CREATE TRIGGER Trigger_Type_Update BEFORE UPDATE on Type
FOR EACH ROW
	SET NEW.updatedon = NOW();

DROP TRIGGER IF EXISTS Trigger_Session_Update;
CREATE TRIGGER Trigger_Session_Update BEFORE UPDATE on Session
FOR EACH ROW
	SET NEW.updatedon = NOW();

DROP TRIGGER IF EXISTS Trigger_User_Update;
CREATE TRIGGER Trigger_User_Update BEFORE UPDATE on User
FOR EACH ROW
	SET NEW.updatedon = NOW();

DROP TRIGGER IF EXISTS Trigger_Group_Update;
CREATE TRIGGER Trigger_Group_Update BEFORE UPDATE on SAM.Group
FOR EACH ROW
	SET NEW.updatedon = NOW();

