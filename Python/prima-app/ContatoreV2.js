import React, { useState } from "react";

function  App (){
    const [count, setCount] = useState(() => {
        console.log('run function')
        return 4
    })
    function decrementCount(){
        setCount(PrevCount => PrevCount-1)
        
    }
function incrementCount(){
    setCount(PrevCount => PrevCount+1)
}
}

return (
    <>
        <button onClick={decrementCount}>-</button>
        <span>{count}</span>
        <button>+</button>
    </>
    )