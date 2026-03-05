-- Create Database
CREATE DATABASE IF NOT EXISTS hms;
USE hms;

--Create Doctor table
CREATE TABLE hms_add_doctor (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255),
    roles VARCHAR(100),
    user_name VARCHAR(100),
    email VARCHAR(255),
    password VARCHAR(255),
    date DATE,
    gender VARCHAR(10),
    address VARCHAR(255),
    country VARCHAR(100),
    city VARCHAR(100),
    State VARCHAR(100),
    postal VARCHAR(20),
    phone_number VARCHAR(20),
    image VARCHAR(255),
    bio TEXT,
    status VARCHAR(50)
);

-- Table for patient
CREATE TABLE hms_add_patient (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullName VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    password VARCHAR(255)
);

-- Table for user
CREATE TABLE hms_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(255)
);
