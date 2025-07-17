create database Azienda;

create domain RealGEZ as integer check(value>=0);
create domain Stringa as varchar;
create type Indirizzo as (
    via Stringa
    civico Stringa
);

create table Impiegato(
    nome Stringa not null,
    cognome Stringa not null,
    nascita date not null,
    stipendio RealGEZ not null,
    id integer not null,
    primary key(Impiegato, Dipartimento, Progetto),
    foreign key(Impiegato) references Impiegato(id),
    foreign key(Progetto) references(id),
    foreign key(Dipartimento) references(id)
);

create table Progetto(
    nome Stringa not null,
    budget RealGEZ not null,
    id integer not null,
    primary key(Progetto, Impiegato),
    foreign key(Progetto) references(id),
    foreign key(Impiegato) references(id)
);

create table Affarenza(
    data_afferenza date not null,
    foreign key(Impiegato) references(id),
    foreign key(Dipartimento) references(id)
);
create table NumeroTelefono(
    telefono Stringa not null,
    primary key(NumeroTelefono, Dipartimento),
    foreign key(Dipartimento) references(id)
    foreign key(NumeroTelefono) references(id)
);

create table Dipartimento(
    nome Stringa not null,
    indirizzo as Indirizzo not null,
    id Stringa not null,
    primary key(Dipartimento, Impiegato, NumeroTelefono)
    foreign key(Dipartimento) references(id)
    foreign key(Impiegato) references(id)
    foreign key(NumeroTelefono) references(id)
);