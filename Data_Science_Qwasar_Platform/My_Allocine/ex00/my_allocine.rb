# Description of tables:
#
# actors:
# id – this is a unique ID for each actor
# act_fname – this is the first name of each actor
# act_lname – this is the last name of each actor
# act_gender – this is the gender of each actor
#
# genres:
# id – this is a unique ID for each genres
# gen_title – this is the description of the genres
#
# directors:
# id – this is a unique ID for each director
# dir_fname – this is the first name of the director
# dir_lname – this is the last name of the director
#
# movies:
# id – this is the unique ID for each movie
# mov_title – this column represents the name of the movie
# mov_year – this is the year of making the movie
# mov_time – duration of the movie i.e. how long it was running
# mov_lang – the language in which movie was casted
# mov_dt_rel – this is the release date of the movie
# mov_rel_country – this is the name of the country(s) where the movie was released
#
# movies_genres:
# mov_id – this is the ID of the movie, which is referencing the mov_id column of the table movies
# gen_id – this is the ID of each genres, which is referencing the gen_id column of the table genres
#
# directors_movies:
# dir_id – this is the ID for each director, which is referencing the dir_id column of the table directors
# mov_id – this is the ID of the movie, which is referencing the mov_id column of the table movies
#
# reviews:
# id – this is the unique ID for each reviewer
# rev_name – this is the name of the reviewer
#
# movies_ratings_reviews:
# mov_id –this is the ID of the movie, which is referencing the mov_id column of the table movies
# rev_id – this is the ID of the reviewer, which is referencing the rev_id column of the table reviews
# rev_stars – this is indicates how many stars a reviewer rated for a review of a movie
# num_o_rating – this indicates how many ratings a movie achieved
#
# movies_actors:
# act_id – this is ID of actor, which is referencing the act_id column of actors table
# mov_id – this is the ID of the movie, which is referencing the mov_id column of the table movies
# role – this is the name of a character in the movie, an actor acted for that character
#
# Objectives
# Write SQL requests. Simple, and some more complicated ;-)

requests['Display all actors'] = "SELECT * FROM actors;"
requests['Display all genres'] = "SELECT * FROM genres;"
requests['Display the name and year of the movies'] = "SELECT mov_title,mov_year FROM movies ;"
requests['Display reviewer name from the reviews table'] = "SELECT rev_name FROM reviews;"
requests["Find the year when the movie American Beauty released"] = "SELECT mov_year FROM movies WHERE mov_title='American Beauty';"
requests["Find the movie which was released in the year 1999"] = "SELECT mov_title FROM movies WHERE mov_year=1999;"
requests["Find the movie which was released before 1998"] = "SELECT mov_title FROM movies WHERE mov_year<1998;"
requests["Find the name of all reviewers who have rated 7 or more stars to their rating order by reviews rev_name (it might have duplicated names :-))"] = "SELECT rev_name FROM reviews  JOIN movies_ratings_reviews ON reviews.id=movies_ratings_reviews.rev_id WHERE rev_stars>=7 ORDER BY rev_name ASC;"
requests["Find the titles of the movies with ID 905, 907, 917"] = "SELECT mov_title FROM movies WHERE id in (905, 907, 917);"
requests["Find the list of those movies with year and ID which include the words Boogie Nights"] = "SELECT id, mov_title, mov_year FROM movies WHERE mov_title LIKE '%Boogie%Nights%' ORDER BY mov_year ASC;"
requests["Find the ID number for the actor whose first name is 'Woody' and the last name is 'Allen'"] = "SELECT id FROM actors WHERE act_fname='Woody' AND act_lname='Allen';"
requests["Find the actors with all information who played a role in the movies 'Annie Hall'"] = "SELECT * FROM actors WHERE id IN(SELECT act_id FROM movies_actors WHERE mov_id IN (SELECT id FROM movies WHERE mov_title='Annie Hall'));"
requests["Find the first and last names of all the actors who were cast in the movies 'Annie Hall', and the roles they played in that production"] = "SELECT act_fname,act_lname,role FROM actors JOIN movies_actors ON actors.id=movies_actors.act_id JOIN movies ON movies_actors.mov_id=movies.id  AND movies.mov_title='Annie Hall';"
requests["Find the name of movie and director who directed a movies that casted a role as Sean Maguire"] = "SELECT dir_fname, dir_lname, mov_title FROM  directors, directors_movies, movies, movies_actors WHERE directors.id=directors_movies.dir_id AND directors_movies.mov_id=movies.id AND movies.id=movies_actors.mov_id AND movies_actors.role='Sean Maguire';"
requests["Find all the actors who have not acted in any movie between 1990 and 2000 (select only actor first name, last name, movie title and release year)"]  = "SELECT act_fname, act_lname, mov_title, mov_year FROM actors JOIN movies_actors ON actors.id=movies_actors.act_id JOIN movies ON movies_actors.mov_id=movies.id WHERE mov_year  NOT BETWEEN 1990 AND 2000;"