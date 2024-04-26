-- List all show from hbtn_0d_tvshows_rate by their rating
SELECT `title`, SUM(`rate`) AS `rating`
FROM `tv_shows` AS tv
   INNER JOIN `tv_show_ratings` AS r
   ON tv.`id` = r.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;
