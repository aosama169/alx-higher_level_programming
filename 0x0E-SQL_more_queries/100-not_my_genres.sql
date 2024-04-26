-- Lists all genres of database hbtn_0d_tvshows
SELECT DISTINCT `name`
FROM `tv_genres` AS genres
INNER JOIN `tv_show_genres` AS ser
ON genreser.`id` = ser.`genre_id`

INNER JOIN `tv_shows` AS t
ON ser.`show_id` = t.`id`
WHERE genres.`name` NOT IN
	 (SELECT `name`
		FROM `tv_genres` AS g
		 INNER JOIN `tv_show_genres` AS s
	 ON genres.`id` = ser.`genre_id`

	 INNER JOIN `tv_shows` AS t
	 ON ser.`show_id` = t.`id`
	 WHERE t.`title` = "Dexter")
ORDER BY genres.`name`;
