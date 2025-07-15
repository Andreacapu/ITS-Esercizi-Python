create database Accademia

create type Strutturato as ENUM ("Ricercatore", "Professore Associato", "Professore Ordinario")

create type LavoroProgetto as ENUM ("Ricerca e Sviluppo", "Dimostrazione", "Managment", "Altro")

create type LavoroNonProgettuale as ENUM ("Didattica", "Ricerca", "Missione", "Incontro Dipartimentale", "Incontro Accademico", "Altro")

create type CausaAssenza as ENUM ("Chiusura Universitaria", "Maternità", "Malattia")

create domain posInteger as integer
check(value >= 0)

create domain StringaM as varchar(100)

create domain NumeroOre as integer
check(value 0, 8)

create domain Denaro as integer
check(value >= 0)

create table Persona(
    id posInteger not null,
    nome StringaM not null,
    cognome StringaM not null,
    posizione Strutturato not null,
    stipendio Denaro not null,
    primary key(id)
);

create table
