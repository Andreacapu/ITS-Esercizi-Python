    import './App.css';
import Componente1 from './Componente1';
import Clock from './Clock';

    function getDate(date){
        function App() {
            let nome = "Andrea";
            return (
                <div className="Andrea">
                    <h1>Primo Elemento {nome}</h1>
                    <Componente1></Componente1>
                    <Componente1/>
                    <h2>
                        {
                            new Date().toLocaleDateString()+" "+new Date().toLocaleDateString

                        }
                    </h2>
                    <h2>{getDate(new Date())}</h2>
                </div>
            )
        }
    }