select wp.nome, wp.inizio, wp.fine

from progetto p, wp
where wp.progetto = p.id
    and p.nome = 'Pegasus'
limit 50;

select pers.nome, pers.cognome, pers.posizione
from persona pers, progetto prog, attivaprogetto ap
where ap.persona = pers.id
    and ap.progetto = prog.id
    and prog.nome = 'Pegasus'
order by pers.cognome desc;

--3. Idnetificazione del nome, cognome e posizione degli sturtturali all'interno del progett oPegasus

select * 
from persona pers, progetto prog, attivitaprogetto ap2
where
    and ap1.persona = pers.id
    and ap2.persona = pers.id
    and ap1.progetto = prog.id
    and ap2.progetto = prog id
    and ap1.id <> ap2.id;

select *
from persona p,attivitaprogettuale AttivitaNonProgettuale
where ap.giorno = anp.giorno
    and ap.persona = p.id
    and anp.persona = p.id;


