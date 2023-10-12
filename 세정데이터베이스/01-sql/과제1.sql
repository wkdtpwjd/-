CREATE TABLE users(
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    phoneNumber NOT NULL,
    gender INTEGER
);

ALTER TABLE users
 ADD COLUMN address NOT NULL DEFAULT 'no address';

 
ALTER TABLE users
 RENAME COLUMN phoneNumber TO numbers;