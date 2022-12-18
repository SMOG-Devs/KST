import React, { useState } from 'react';
import SideNav, { Toggle, Nav, NavItem, NavIcon, NavText } from '@trendmicro/react-sidenav';
import Visual from './Visual';
import Chart from './Chart';
// Be sure to include styles at some point, probably during your bootstraping
import '@trendmicro/react-sidenav/dist/react-sidenav.css';



const Sidebar = () => {

    const [buttonVisual, setButtonVisual] = useState(false);
    const [buttonChart, setButtonChart] = useState(false);

    return (
        // chyba trzeba będzie to ulepszyć za pomocą Sidebar bo wydaje się bardziej spoko
        <SideNav
                onSelect={selected => {
                    console.log(selected)
                }}
            >
            <SideNav.Toggle style={{'background-color': '#16b3df'}}/>
            <SideNav.Nav deafultSelected="home" style={{'background-color': '#16b3df'}}>
                <NavItem eventKey="home">
                    <NavIcon>
                        <i className='fa fa-fw fa-home' style={{ fontSize: '2em', color: "#fff", 'padding-top': '10px' }}></i>
                    </NavIcon>
                    <NavText>O aplikacji</NavText>
                    <NavItem>
                        <NavText>
                            <p>
                            Aplikacja do przewidywania ruchu zanieczyszczeń na terenie Krakowa.
                            Na podstawie sztucznej inteligencji i pomiarów z czujników zanieczyszczeń
                            z AirlyAPI i meteoAGH
                            </p>
                        </NavText>
                    </NavItem>
                </NavItem>
                <NavItem eventKey="visualization" onClick={() => setButtonVisual(true)}>
                    <NavIcon>
                        <i className='fa-solid fa-film' style={{ fontSize: '2em', color: "#fff", 'padding-top': '10px' }}></i>
                    </NavIcon>
                    <NavText>Wizualizacja</NavText>
                </NavItem>
                <NavItem eventKey="chart" onClick={() => setButtonChart(true)}>
                    <NavIcon>
                        <i className='fa fa-fw fa-chart-simple' style={{ fontSize: '2em', color: "#fff", 'padding-top': '10px' }}></i>
                    </NavIcon>
                    <NavText>Wykres</NavText>
                </NavItem>
                <NavItem eventKey="about">
                    <NavIcon>
                        <i className='fa-solid fa-circle-info' style={{ fontSize: '2em', color: "#fff", 'padding-top': '10px' }}></i>
                    </NavIcon>
                    <NavText>O nas</NavText>
                    <NavItem eventKey="new user">
                        <NavText>
                            <p>
                            Autorzy:<br />
                            Jakub Ziomek<br />
                            Jakub Szpunar<br />
                            Bartłomiej Wajdzik<br />
                            Bartosz Sambór
                            </p>
                        </NavText>
                    </NavItem>
                </NavItem>
            </SideNav.Nav>
            <Visual trigger={buttonVisual} setTrigger={setButtonVisual}/>
            <Chart trigger={buttonChart} setTrigger={setButtonChart} />

        </SideNav>
        
    )
}

export default Sidebar