USE SAM;
DELIMITER $$

-- Trigger_Recommendation_Delete: After deleting a recommendation that cascades to table session_recommendation delete also linked sessions.
DROP TRIGGER IF EXISTS Trigger_Recommendation_Delete;
CREATE TRIGGER Trigger_Recommendation_Delete BEFORE DELETE on Recommendation
FOR EACH ROW
BEGIN
	-- Only delete a session, if the session linked to the deleted recommendation has no more recommendations linked to it.
    DELETE FROM Session WHERE 
		Session.id = (SELECT SessionID FROM Session_Recommendation WHERE Session_Recommendation.recommendationID = OLD.id)
        AND
        EXISTS (SELECT sessionID FROM session_recommendation WHERE sessionID = Session.id GROUP BY sessionID HAVING count(sessionID) = 1);
END$$

DELIMITER ; 