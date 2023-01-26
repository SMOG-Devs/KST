import React from 'react';
import "./css/Visual.css"
import BreakingBad from "./data/sth-went-wrong.gif"
import "./VisualScript.js";

function Visual(props) {
    return (props.trigger) ? (
        <div className="visual">
            <div className='visual-inner'>
                <button className="close-btn" onClick={() => props.setTrigger(false)}>close</button>
                {props.children}
                {/* <img className="gif" src={BreakingBad} alt="loading..." /> */}
                <div>
                    <h1>KST (Kraków Smog Tracker) - simple overview how to add Folium map into the web page</h1>
                    <div class="map">
                        <iframe class="map-frame">
                        </iframe>
                    </div>
                </div>
            </div>
        </div >
    ) : "";
}

export default Visual