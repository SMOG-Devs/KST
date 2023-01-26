import React from 'react';
import "./css/Visual.css"
import Engine from "./data/engine.png"


function Chart(props) {


    return (props.trigger) ? (
        <div className="visual">
            <div className='visual-inner'>
                <div className="chart">
                    <button className="close-btn" onClick={() => props.setTrigger(false)}>close</button>
                    {props.children}
                    <img className="gif" src={Engine} alt="loading..."/>
                </div>
            </div>
        </div>
    ) : "";
}

export default Chart