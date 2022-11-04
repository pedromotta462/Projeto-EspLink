#CREATE DATABASE bd_projeto;
USE bd_projeto;

create table cadastro1(
	id int unsigned not null auto_increment,
	nome varchar(60) not null,
    senha varchar(60) not null,
    telefone varchar(15) not null,
    cidade varchar(60) not null,
    primary key (id)
); 
create table cadastro2(
	id int unsigned not null auto_increment,
	idade int not null,
    esporte varchar(20) not null,
    posicao varchar(20) not null,
    descricao varchar(250) not null,
    primary key (id)
);
SELECT * FROM cadastro1, cadastro2;
