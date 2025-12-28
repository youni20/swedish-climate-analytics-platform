import React, { useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { City } from '../services/api';
// Fix Leaflet default icon issue
import L from 'leaflet';

// Fix for default marker icon in React Leaflet
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
    iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

// Component to handle map centering
const MapUpdater = ({ center }: { center: [number, number] }) => {
    const map = useMap();
    useEffect(() => {
        map.setView(center, map.getZoom());
    }, [center, map]);
    return null;
};

interface MapProps {
    cities?: City[];
    selectedCity?: string;
}

const Map = ({ cities = [], selectedCity }: MapProps) => {
    // Default to Sweden center roughly
    const defaultCenter: [number, number] = [62.0, 15.0];

    // Find selected city coordinates
    const selectedCityData = cities.find(c => c.name === selectedCity);
    // Use selected city coords if available, else default. 
    // Note: Our MVP synthetic data generator didn't add lat/long to cities API yet.
    // For MVP demo, let's hardcode a few swedish cities since API returns just names mostly or we need to add lat/long there.

    // Quick MVP dictionary for coords if API doesn't provide them yet
    const cityCoords: Record<string, [number, number]> = {
        'Stockholm': [59.3293, 18.0686],
        'Gothenburg': [57.7089, 11.9746],
        'Malmö': [55.6045, 13.0038],
        'Uppsala': [59.8586, 17.6389],
        'Västerås': [59.6106, 16.5448]
    };

    const center = selectedCity && cityCoords[selectedCity] ? cityCoords[selectedCity] : defaultCenter;
    const zoom = selectedCity ? 10 : 5;

    return (
        <div className="w-full h-[400px] rounded-lg overflow-hidden border shadow-sm z-0">
            <MapContainer center={center} zoom={5} style={{ height: '100%', width: '100%' }}>
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                />
                <MapUpdater center={center} />
                {cities.map((city) => {
                    const coords = cityCoords[city.name] || [0, 0];
                    if (coords[0] === 0) return null;
                    return (
                        <Marker key={city.name} position={coords}>
                            <Popup>
                                <div className="font-semibold">{city.name}</div>
                            </Popup>
                        </Marker>
                    );
                })}
            </MapContainer>
        </div>
    );
};

export default Map;
