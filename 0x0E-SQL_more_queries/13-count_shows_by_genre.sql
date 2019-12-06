-- database dump from hbtn_0d_tvshows to your MySQL server

SELECT name AS genre, COUNT(*) AS number_shows
FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre_id ORDER BY COUNT(*) DESC;
