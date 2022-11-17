import React from 'react';
import 'leaflet/dist/leaflet.css'
import './App.css';
import ToolBar from './ToolBar.js';
import Sidebar from './Sidebar.js';
import KrakowMap from './KrakowMap.js';

export default function App() {
  return (
    <div style={{ position: 'relative' }}>
      <div style={{ left: 'auto', position: 'absolute' }}>
        <ToolBar />
        <Sidebar />
      </div>
      <KrakowMap />
    </div>
  );
}
