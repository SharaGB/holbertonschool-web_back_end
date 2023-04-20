-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the overall score for a student.

DELIMITER //

DROP PROCEDURE if EXISTS ComputeAverageScoreForUser;

CREATE PROCEDURE COMPUTEAVERAGESCOREFORUSER(IN USER_ID 
INT) BEGIN 
	UPDATE users
	SET average_score = (
	        SELECT AVG(score)
	        FROM corrections AS c
	        WHERE c.user_id = user_id
	    )
	WHERE id = user_id;
	END // 


DELIMITER ;