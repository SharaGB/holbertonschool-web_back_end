-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers

-- that computes and store the average weighted score for all students.

DELIMITER //

CREATE PROCEDURE COMPUTEAVERAGEWEIGHTEDSCOREFORUSERS
() BEGIN 
	UPDATE users
	SET average_score = (
	        SELECT
	            sum(p.weight * c.score) / sum(p.weight)
	        FROM projects AS p
	            INNER JOIN corrections AS c ON p.id = c.project_id
	        WHERE c.user_id = users.id
	    );
END; 

DELIMITER; //