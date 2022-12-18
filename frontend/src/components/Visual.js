import React from 'react';
import "./css/Visual.css"
import BreakingBad from "./data/sth-went-wrong.gif"


function Visual(props) {

    

    return (props.trigger) ? (
        <div className="visual">
            <div className='visual-inner'>
                <button className="close-btn" onClick={() => props.setTrigger(false)}>close</button>
                {props.children}
                <img className="gif" src={BreakingBad} alt="loading..." />
            </div>
        </div >
    ) : "";
}

export default Visual