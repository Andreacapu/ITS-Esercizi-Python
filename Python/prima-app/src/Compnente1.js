import React from "react";

const Componente1 = (props) => {
    const anni = 26;
    return(
        <div style={{color: "white", fontWeight:"600",margin:"15px", border:"1px #000 solid", padding:"15 px", backgroundColor:"grey"}}>
            <Anagrafica></Anagrafica>
            <Messaggio></Messaggio>
        </div>
    )
}

const Anagrafica = () => {
    return(
        <div>
            Anagrafica
        </div>
    )
}

const Messaggio = () => {
    return(
        <div>
            Messaggio
        </div>
    )
}

export default Componente1