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
create table publicacao(
	id int unsigned not null auto_increment,
    id_cadastro1 int unsigned not null,
	publi varchar(500) not null,
    primary key (id)
);
create table escolhas(
	id int unsigned not null auto_increment,
    id_cadastro1 int unsigned not null,
	basquete varchar(20) not null,
    futebol varchar(20) not null,
    treinador varchar(20) not null,
    patrocinio varchar(20) not null,
    paratletas varchar(20) not null,
    natacao varchar(20) not null,
    primary key (id)
);
SELECT * FROM publicacao;
SELECT * FROM cadastro1, cadastro2;
