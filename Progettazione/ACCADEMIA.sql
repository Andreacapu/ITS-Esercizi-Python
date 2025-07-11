create table Persona(
	id integer primary key;
	nome varchar(100) not null,
	cognome varchar (100) not null,
	posizione strutturato not null,
	stipendio  Denaro not null		
);


create table Progetto(
	id integer not null,
	nome varchar(100) not null,
	inzio date,
	fine date,
	budget Denaro not null,
		
	primary key(id),
	unique(nome),
	check(fine > inizio)
);

create table WP(
	progetto posInteger not null,
	id posInteger not null,
	nome varchar(100) not null,
	inizio date not null,
	fine date not null,
	primary key(progetto, id),
	foreign key (progetto) references Progetto(id),
	check (inizio > fine)
);

create table AttivaProgetto(
	id posInteger not null,
	Persona posInteger not null,
	progetto posInteger not null,
	wp posInteger not null,
	giorno date,
	oreDurata NumeroOre not null,
	primary key(id)
	foreign key(persona) references Persona(id)
	foreign key(progetto, wp) references WP(progetto, id) 
);

create table AttivitaNonProgettuale(
	id posInteger not null,
	persona posInteger not null,
	progetto posInteger not null,
	giorno date,
	date NumeroOre not null,
	check(inizio > fine)
	primary key(id),
	foreign key(persona) references Persona(id)
);

create table Assenza(
	id posInteger not null,
	persona posInteger not null,
	tipo CausaAssenza not null,
	giorno date,
	primary key(id)
	foreign key(persona, id)
	foreign key(persona) references Persona(id)
);




create type strutturato as ENUM ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroPorgetto as ENUM('Ricerca e Sviluppo', 'Dimostrazione', 'Managment', 'Altro');

create type LavoroNonProgettuale as ENUM('Didattica', 'Ricerca', 'Incontro Diaprtimentale', 'Incontro Accademico', 'Altro');

create type CausaAssenza as ENUM ('Chiusura università', 'Maternità', 'Malattia');
	
create domain posInteger as integer
	check (value >= 0);
	
create domain NumeroOre as integer
	check (value 0, 8);

create domain Denaro as real
	check (value >= 0);
	

