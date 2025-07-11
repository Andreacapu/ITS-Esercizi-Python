create database cielo;

create domain PostInteger as integer check(value >= 0);
create domain StringaM as varchar(100);
create domain CodIATA as char(3);


create table Volo(
    codice PostInteger not null,
    comp StringaM not null,
    durataMinuti PostInteger not null,
    check(value >= 0),
    primary key(codice),
    foreign key(comp) references Compagnia(nome),
    foreign key(codice, comp) references ArrPart(codice, comp)
);


create table ArrPart(
    codice PostInteger not null,
    comp StringaM not null,
    durataMinuti PostInteger not null,
    check(value > 0)
    primary key(codice),
    foreign key(comp) references Compagnia()
);

create table Aeroporto(
    codice CodIATA not null,
    nome StringaM not null,
    primary key(codice)
   pippo foreign key(codice) references Aeroporto(codice)
);

create table Compagnia(
    nome StringaM not null,
    annoFondaz PostInteger,
    nazione StringaM not null,
    primary key(nome)
);

create table LuogoAeroporto(
    aeroporto CodIATA not null,
    citta StringaM not null,
    nazione StringaM not null,
    primary key(aeroporto),
    foreign key(aeroporto) references Aeroporto(codice)
);