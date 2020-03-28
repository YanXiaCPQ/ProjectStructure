-- schema.sql

--drop database if exists awesome;
--create database awesome;
--use awesome;

--grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';

--create table users (
--    `id` varchar(50) not null,
--    `passwd` varchar(50) not null,
--    `admin` bool not null,
--    key `idx_created_at` (`created_at`),
--    primary key (`id`)
--) engine=innodb default charset=utf8;

--create table blogs (
--    `id` varchar(50) not null,
--    `user_id` varchar(50) not null,
--    primary key (`id`)
--) engine=innodb default charset=utf8;

