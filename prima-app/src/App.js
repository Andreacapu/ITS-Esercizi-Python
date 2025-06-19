import logo from './logo.svg';
import './App.css';
import stampa_numeri from './Esercizi/stampanumeri';
import Clock from './Clock';
import Componente1 from './Compnente1';
function getDate(date){
  return date.toLocalDateString()+" "+date.toLocalDateString()
}

function App() {
  let nome="Andrea";
  return (
    <div className="App">
      <h1>Ciao sono {nome}!</h1>
      <stampa_numeri></stampa_numeri>
      <Componente1>Andrea</Componente1>
      <Componente1/>
      <h2>
      <Clock></Clock>
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
