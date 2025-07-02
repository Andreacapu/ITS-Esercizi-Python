import React from 'react'

const contatore = () => {
    const increment = () => {
        //  setTimeout(()=>{
        setCount((oldCount) => {
          if (oldCount < 4) {
            return oldCount + 1;
          } else {
            return oldCount;
          }
        });
        //},2000)
      };
      return (
        <>
          <div>{count}</div>
          <div>
            <button onClick={() => setCount(count - 1)}>Descremente</button>&nbsp;
            <button onClick={increment}>Incrementa</button>
          </div>
        </>
      );

    }


export default contatore
