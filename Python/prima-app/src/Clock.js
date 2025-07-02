import React from "react";
const Clock = (props) => {
    const t=Date.now()+3600*props.timezone*1000
    const date=new Date()
    return(
        <h3> in {props.country} del giorno {date.toLocaleDateString()} solo le {date.toLocaleDateString()}</h3>
    )
}
export default Clock