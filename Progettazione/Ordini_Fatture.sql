create database Ordini_Fatture

create domain Stringa as varchar;
create domain RealGEZ as Real
        check (value >= 0)
create domain IntGZ as Integer
        check (value >= 0)

create domain telefono as char (10)

create domain cf as char(16)
check (value ~[A-Z] {6} {0-9} {2}{1} {0-9}{3}{A-Z}{10})

create domain email as char
        check (value ~ like %@%%)

create domain partita_iva as char
        check (value ~ [0-9] {11})

create domain cap as char (5)
        check (value~[0-9]{5})

create type indirizzo as
        ( via varchar
        cap CAP
        civico varchar
        )
create table Nazione (
	nome stringa primary key
);

create table Regione (
	nome stringa not null,
	nazione stringa not null,
	primary key (nome, nazione),
	foreign key (nazione) references nazione(nome)
);

create table Citta (
	id integer primary key, 
	nome stringa not null,
	regione stringa not null,
	nazione stringa not null,
	unique (nome, regione, nazione),
	foreign key (regione, nazione)
		references regione(nome, nazione)
);

create table dipartimento (
	nome stringa primary key,
	indirizzo indirizzo not null
	citta integer not null,
    direttore cf not null,
    primary key(id)
	foreign key (citta) references Citta(id)
    foreign key (direttore) references Direttore(cf)
);

create table Ordine (
	codice integer primary key,
	data_stipula date not null,
	imponibile RealGEZ not null,
	aliquota Real_0_1 not null,
	descrizione stringa not null,
	dipartimento stringa not null,
    primary key (id)
	foreign key (dipartimento)
		references dipartimento(nome)
);

create table StatoOrdine(
    nome stringa primary key,
    ordine integer not null,    
    foreign key (ordine) references Ordine(codice)
)

create table Direttore(
    nome stringa not null,
    cognome varchar not null,
    cf char primary key,
    anni_servizio IntGZ not null,
    data_nascita data not null.
);

create table Fornitore(
    ragione_sociale stringa not null,
    partita_iva char primary key,
    indirizzo indirizzo not null,
    telefono telefono not null,
    email email not null,
    citta stringa not null
    foreign key(citta) references Citta(id)

);