import { useState } from "react"
const LoginForm =() =>{
    const [nome, setNome] = useState("");
    const [cognome, setCongome] = useState("");
    const [persona]
    const[email,setEmail]=useState("Prova@gmail.com");
    cosnt[password,setPassword]=useState("");
    
    return(<div>
        <form>
            <div>
            <label htmlFor="email">Email</label>
            <input type="email" required value={email} onChange={(e) => setEmail(e.target.value)}></input>
            </div>
            <div>
                <label htmlFor="password">Password</label>
                <input type="password" required value={password} onChange={(e) => setPassword(e.target.value)}></input>
            </div>

            <button className="btn btn-success">Login</button>
        </form>
        {email} {password}
    </div>
    );
};