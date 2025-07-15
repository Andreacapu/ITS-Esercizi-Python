import logo from './logo.svg';
import './App.css';
import stampa_numeri from './Esercizi/stampanumeri';
import Clock from './Clock';
import Componente1 from './Compnente1';
import {anagrafica} from "./data/dati";
import { useState } from 'react';
function getDate(date){
  return date.toLocalDateString()+" "+date.toLocalDateString()
}

function App() {
  let nome="Andrea";
  const [nome1, setNome1] = useState(nome);
  const [persona, selfPersone] = useState(anagrafica)

  const cambiaNome = () => {
    console.log(nome);
    nome = "Andrea";
    setNome1(nome);
    console.log(nome);
  };
  const cliccami = (nome, cognome) =>
     {
    //istruzioni
    alert ("Ciao" + nome +" " + cognome);
  };
  const [persone, setPersone] = useState(anagrafica);
const elimina = (id) => {
  const newAnag = persone.filter((p) => p.id !== id);
}

  return (
    <div className="App">
      <h1>Ciao 2 {nome}!</h1>
      <cleanUp></cleanUp>
      <stampa_numeri></stampa_numeri>
      <Componente1>Andrea</Componente1>
      <Componente1/>
      <h2>
      <Clock timezone="1" country="Italy"></Clock>
      <Clock timezone="-6" country="USA"></Clock>
      <Clock timezone="8" country="Japan"></Clock>
      <Contatore></Contatore>
      <CambiaNome></CambiaNome>
      <LoginForm></LoginForm>
      </h2>

      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
export default App;
