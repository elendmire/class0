CREATE TABLE flights(
    /*serial demek otomatik olarak sayılan integerlardır.*/
    id SERIAL PRIMARY KEY,
    /*varchar text demek.*/
    origin  VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    /*sayı integer demek ve boş olamaz demek de not null demek.*/
    duration INTEGER NOT NULL
);  