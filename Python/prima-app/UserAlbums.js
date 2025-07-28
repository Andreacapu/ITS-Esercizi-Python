import { useState } from "react";

const UserAlbums = () => {
    const url = 'https://jsonplaceholder.typicode.com';
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch(url)
            .then((response) => response.json())
            .then(

                (ris) => setUsers(ris))
    }
    )
    return (
        <>
            <h1>Fetch user form jsnopalceholder</h1>
            <div>
                {
                    users.map((u)=> {
                        return <p key={u.id}>{u.name}</p>
                    })}
            </div>
        </>
    );
}

export default UserAlbums