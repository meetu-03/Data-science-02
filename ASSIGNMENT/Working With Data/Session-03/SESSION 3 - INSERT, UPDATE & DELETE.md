# 1. Create a table called Playlist with columns: id (INT, primary key), song_name (VARCHAR), artist (VARCHAR), and duration (INT, seconds). Insert a single row for your current favorite song.

ANSWER...

**syntax is here**

create table music_streaming_app.Playlist
(id int auto_increment primary key,
song_name varchar(255),
artist varchar(255),
duration int
)

insert data (my favorite song)

**syntax**

insert into music_streaming_app.playlist value(null,'halka halka','nusarat fateh ali khan',18.23);

# 2. Insert three more songs into the Playlist table using a single INSERT statement

ANSWER...

**syntax**

all data insert in one statment

insert into music_streaming_app.playlist value(null,'at peace','karan aujla',2.50),(null,'GOAT','sidhu moosewala',3.00),(null,'ye tune kya kiya','Javed Bashir',3),(null,'aisa ban na sawarna',' Nizami Kanpuri',4)

# 3.Update the duration of your favorite song to a new value using the UPDATE statement.

ANSWER...

-Before the update, the duration of the song with **id = 1** was **18 seconds**.
-After executing the `UPDATE` statement, the duration was successfully changed to **20 seconds**.

**syntax is here**

UPDATE music_streaming_app.playlist
SET duration = 20
WHERE id = 1;

# 4.Delete the song you inserted last using the DELETE statement.

ANSWER...



-The record with **id = 2** was present in the `Playlist` table before executing the `DELETE` statement.
-After executing the `DELETE` query, the record with **id = 2** was successfully removed from the `Playlist` table.
-The remaining records can be verified using the `SELECT * FROM Playlist;` statement.

**syntax is here**

delete  FROM music_streaming_app.playlist
Where id = 2


# 5. Write an SQL statement that would update the song_name for all songs by 'nusarat fateh ali khan' in your Playlist to add 'suroor he' at the end of the name, but only if the duration is more than 180 seconds.

ANSWER...

-Due to MySQL Workbench Safe Update Mode, the record was updated using **id** instead of **artist**.
-The `song_name` for the record with **id = 1** was successfully updated.

**syntax is here**
UPDATE music_streaming_app.playlist
SET song_name = 'Halka Halka Suroor Hai'
WHERE id = 1
 

 and duration more then 180 second so syntax is here

 UPDATE music_streaming_app.playlist
SET duration = 200
WHERE id = 1;