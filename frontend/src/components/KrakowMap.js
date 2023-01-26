import React from 'react'
import {
  MapContainer,
  TileLayer,
  Polygon
} from 'react-leaflet';
import { statesData } from './data/KrakowData.js';
import 'leaflet/dist/leaflet.css'
import './css/App.css';

const center = [50.0618776320393, 19.940024729251924]

const KrakowMap = () => {
    return (
        <MapContainer
      center={center}
      zoom={14}
      style={{width: '95.8vw', height: '100vh', left: '4.2vw', position: 'absolute'}}
    >
      <TileLayer
        url="https://api.maptiler.com/maps/basic-v2/256/{z}/{x}/{y}.png?key=SFmapqVTKGKRIDlMS2tT"
        attribution='<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
      ></TileLayer>
      {
        statesData.features.map((state) => {
          const coordinates = state.geometry.coordinates[0].map((item) => [item[1], item[0]]);

          return (<Polygon
            pathOptions={{
              fillColor: '#FD8D3C',
              fillOpacity: 0.7,
              weight: 2,
              opacity: 1,
              dashArray: 3,
              color: 'white'
            }}
            positions={coordinates}
            eventHandlers={{
              mouseover: (e) => {
                const layer = e.target;
                layer.setStyle({
                  fillOpacity: 0.7,
                  weight: 5,
                  dashArray: "",
                  color: '#666',
                  fillColor: '#FACDCC'
                })
              },
              mouseout: (e) => {
                const layer = e.target;
                layer.setStyle({
                  fillOpacity: 0.7,
                  weight: 2,
                  dashArray: "3",
                  color: '#white',
                  fillColor: '#FD8D3C'
                })
              },
              click: (e) => {
                
              }
            }}
            />)
        })
        }
      </MapContainer>
    )
}

export default KrakowMap