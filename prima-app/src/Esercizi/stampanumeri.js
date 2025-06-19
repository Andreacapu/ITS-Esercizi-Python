import React from "react";

const stampa_numeri = () => {
    let numeri = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10]

return (
    <div>
        {
            numeri.map((i) => {
                return <p> (i)</p>
            
        })
        }
    </div>
)
}

export default stampa_numeri