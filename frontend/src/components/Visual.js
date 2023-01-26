import React, {useEffect, useState} from 'react';
import "./css/Visual.css"
import BreakingBad from "./data/sth-went-wrong.gif"
import {getHeatmap} from "./VisualScript.js";

function Visual(props) {
    const [visualisation, setVisualisation] = useState(null);
    const [start_date, setStartDate] = useState(null);
    const [end_date, setEndDate] = useState(null);
    useEffect(() => {
        (async () => {
            const data = await getHeatmap(start_date, end_date);
            setVisualisation(data);
            console.log('sprawdzam')
        })();
    }, [props.trigger, start_date, end_date]);

    const handleSubmit = event => {
        event.preventDefault();
        setStartDate(event.target.start_date.value);
        setEndDate(event.target.end_date.value);
        console.log(start_date, end_date);
    }

    return (props.trigger) ? (
        <div className="visual">
            <div className='visual-inner'>
                {props.children}
                {/* <img className="gif" src={BreakingBad} alt="loading..." /> */}
                <div className="map-wrapper">
                    <h1>KST (Kraków Smog Tracker)</h1>
                    <iframe className="map-frame" srcDoc={visualisation}>
                        {/*{visualisation}*/}
                    </iframe>
                    <form onSubmit={handleSubmit}>
                        <label for="start_date">Start date:</label>
                        <input type="date" name="start_date"/>
                        <label for="end_date">End date:</label>
                        <input type="date" name="end_date"/>
                        <input type="submit" style={{"background":"#e72929"}} value="Submit"/>
                    </form>
                    <div class="map">
                    </div>
                </div>
            </div>
        </div>
    ) : "";
}

export default Visual