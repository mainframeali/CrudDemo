CREATE DATABASE rubik;

CREATE TABLE rubik.listings (
    listing_id INT auto_increment NOT NULL,
    address varchar(1000) NULL,
    price DECIMAL NULL,
    CONSTRAINT listings_pk PRIMARY KEY (listing_id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(1, 'test address 1', 1200000);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(2, 'test address 2', 359999);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(3, 'test address 3', 2458999);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(4, 'test address 4', 123000);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(5, 'test address 5', 1324554);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(6, 'test address 6', 2344555);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(7, 'test address 7', 1230000);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(8, 'test address 8', 456000);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(9, 'test address 9', 560000);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(10, 'test address 10', 430000);
INSERT INTO rubik.listings
(listing_id, address, price)
VALUES(11, 'test address 11', 345000);
