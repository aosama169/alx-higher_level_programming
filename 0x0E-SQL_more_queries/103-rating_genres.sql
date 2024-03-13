-- List all genres in database hbtn_0d_tvshows_rate by their rating
SELECT `name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS genres
   INNER JOIN `tv_show_genres` AS ser
   ON shows.`genre_id` = genres.`id`
   INNER JOIN `tv_show_ratings` AS r
   ON r.`show_id` = shows.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;
