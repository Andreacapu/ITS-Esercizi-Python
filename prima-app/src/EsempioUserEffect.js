import React, {useEffect} from 'react'

const EsempioUserEffect = () => {
    useEffect{()=>{
        console.log("Chiamo useEffect");
    });
    console.log("siamo fuori ora")
  return (
    <div>EsempioUserEffect</div>
  )
}

export default EsempioUserEffect