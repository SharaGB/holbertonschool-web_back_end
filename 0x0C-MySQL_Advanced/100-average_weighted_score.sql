-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE COMPUTEAVERAGEWEIGHTEDSCOREFORUSER
(IN USER_ID INT) BEGIN 
	UPDATE users
	SET average_score = (
	        SELECT
	            sum(p.weight * c.score) / sum(p.weight)
	        FROM projects AS p
	            INNER JOIN corrections AS c ON p.id = c.project_id AND c.user_id = user_id
	    )
	WHERE users.id = user_id;
END; 

DELIMITER; //