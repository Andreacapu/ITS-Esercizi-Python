ccreate database Azienda;

create domain RealGEZ as integer check(value>=0);
create domain Stringa as varchar;
create type Indirizzo as (
    via Stringa
    civico Stringa
);

begin transaction;

set constraints all deferred;

create table Impiegato(
    nome Stringa not null,
    cognome Stringa not null,
    nascita date not null,
    stipendio RealGEZ not null,
    id integer not null,
    progetto integer not null,
    dipartimento integer not null,
    primary key(id),
    foreign key(progetto) references Progetto(id) DEFERABLE,
    foreign key(dipartimento) references Dipartimento(id) DEFERABLE
);
create table Progetto(
    nome Stringa not null,
    budget RealGEZ not null,
    id integer not null,
    impiegato id not null,
    primary key(id),
    foreign key(impiegato) references(id) DEFERABLE
);

create table Affarenza(
    impiegato id not null,
    dipartimento id not null,
    data_afferenza date not null,
    primary key(data_afferenza),
    foreign key(impiegato) references Impiegato(id) DEFERABLE,
    foreign key(dipartimento) references Dipartimento(id) DEFERABLE
); 

create table NumeroTelefono(
    telefono Stringa not null,
    dipartimento id not null,
    primary key(telefono),
    foreign key(dipartimento) references Dipartimento(id) DEFERABLE
);

create table Dipartimento(
    nome Stringa not null,
    indirizzo as Indirizzo not null,
    id Stringa not null,
    impiegato id not null,
    telefono id not null,
    primary key(id),
    foreign key(impiegato) references Impiegato(id) DEFERABLE,
    foreign key(telefono) references NumeroTelefono(id) DEFERABLE
);