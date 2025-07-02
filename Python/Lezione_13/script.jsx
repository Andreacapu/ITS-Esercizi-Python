const rootElement=document.querySelector("#root");
const root = ReactDOM.createRoot(rootElement);
const App= ()=>{
    return(
        <main>
        <h1>Primo Componente</h1>
        </main>
    )
}

root.render(
    <App></App>
)

const List=()=>{
    return
    <ul>
        <li>Php</li>
        <li>Js</li>
        <li>Python</li>
    </ul>
}

root.render(
    <>
    <App>
        <h2>Lista competenze</h2>
        <List></List>
    </App>
    </>
);