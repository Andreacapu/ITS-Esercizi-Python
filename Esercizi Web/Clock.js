import reat from "react"

const Clock = () => {
    const t=Date.now()+3600*this.props.timezone*1000;
    const date=new Date(t);
    return (
        <h3>{date.toLocaleDateString()+"sono le "+date.toLocaleDateString}</h3>
    )
}

export Clock