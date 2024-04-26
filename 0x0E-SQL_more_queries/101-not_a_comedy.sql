-- Lists all shows without comedy genre in database hbtn_0d_tvshows
SELECT DISTINCT `title`
FROM `tv_shows` AS shows
LEFT JOIN `tv_show_genres` AS ser
ON ser.`show_id` = shows.`id`
LEFT JOIN `tv_genres` AS g
ON g.`id` = ser.`genre_id`
WHERE shows.`title` NOT IN
	 (SELECT `title`
		FROM `tv_shows` AS t
		 INNER JOIN `tv_show_genres` AS s
	 ON ser.`show_id` = shows.`id`
	 INNER JOIN `tv_genres` AS g
	 ON g.`id` = ser.`genre_id`
	 WHERE g.`name` = "Comedy")
ORDER BY `title`;
