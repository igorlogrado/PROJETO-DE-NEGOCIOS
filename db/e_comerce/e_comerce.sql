create database e_comerce;
use e_comerce;

create table produto (
id int auto_increment not null primary key,
nome varchar(50)not null,
descricao varchar(50)not null,
preco varchar(50)not null,
estoque varchar(50) not null
);
insert into produto(nome, descricao, preco, estoque)values('perfume', '16485186', '100',' tem alguns');

create table cliente(
id int auto_increment not null primary key,
nome varchar(50)not null,
email varchar(50)not null,
idade varchar(50)not null

);
insert into cliente(nome, email,idade) values ('Juan','jeanluis@hotmail.com','25');

select * from cliente;


