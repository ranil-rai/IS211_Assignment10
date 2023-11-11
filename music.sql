
-- SQL script for Music Database Schema

-- Creating the Artists Table
CREATE TABLE Artists (
    artist_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Creating the Albums Table
CREATE TABLE Albums (
    album_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES Artists (artist_id)
);

-- Creating the Songs Table
CREATE TABLE Songs (
    song_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    album_id INTEGER,
    track_number INTEGER,
    duration INTEGER,
    FOREIGN KEY (album_id) REFERENCES Albums (album_id)
);
