create database escolar;
use escolar;

create table matricula (
id int auto_increment not null primary key,
nome varchar(50)not null,
idade varchar(50)not null,
ano varchar(50)not null
);
insert into matricula (nome,idade,ano)values('Lucas','17','3 ano');
insert into matricula (nome,idade,ano)values('Maria','16','2 ano');

create table aluno(
id int auto_increment not null primary key,
nome varchar(50)not null,
email varchar(50)not null,
identificacao varchar(50)not null

);
insert into aluno (nome, email,identificacao) values ('Lucas','Lucasalencar@hotmail.com','25861521');
insert into aluno (nome, email,identificacao) values ('Maria','Marialuiza@hotmail.com','28565165');

select * from matricula,aluno;