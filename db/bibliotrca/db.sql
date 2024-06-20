
create database contatos_db;
use contatos_db;


create table contatos(
id int auto_increment not null primary key,
nome varchar (50) not null,
contato varchar (20)not null
);

INSERT INTO contatos(nome,contato) VALUES ('Maria','23427344');
INSERT INTO contatos(nome,contato) VALUES ('João','45845363');

select * from contatos; 