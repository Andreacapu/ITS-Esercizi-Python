import React, { useState } from "react";

const FetchComponent = () => {
    const url = 'https://jsonplaceholder.typicode.com';
    const [users, setUsers] = useState([]);
    const getUsers= async () => {
        const response=await fetch(url)
        const result= await response.json();
        setUsers(result);
    }
    useEffect(() =>{
        getUsers()
    },[]);
    return (
        <>
        <h1>Fetch USer from jsonplaceholder</h1>
        <div>
            {
                users.map((u)=>{
                    return <p key={u.id}>{u.name}</p>
                })}
        </div>
        </>
    );
};

export default FetchComponent


