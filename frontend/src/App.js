import React from 'react';
import 'leaflet/dist/leaflet.css'
import './components/css/App.css';
import Sidebar from './components/Sidebar.js';
import KrakowMap from './components/KrakowMap.js';

export default function App() {
  return (
    <div style={{ position: 'relative' }}>
      <div style={{ left: 'auto', position: 'absolute', 'background-color': '#fff' }}>
        <Sidebar />
      </div>
      <KrakowMap />
    </div>
  );
}
