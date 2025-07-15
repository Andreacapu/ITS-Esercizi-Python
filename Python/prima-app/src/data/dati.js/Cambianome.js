import { useState } from "react";
const CambiaNome =() =>{
    const[nome,setNome]=useState("Andrea")
    const cambia =()=>{
        if (nome==="Mario"){
            setNome("Andrea")
        }else{
            setNome("Mario")
        }
        };
    return(<div>
        <h3>{nome}</h3>
        <button className="btn btn-dark" onClick={cambia}>Cambia</button>
    </div>)
}

export default CambiaNome;
