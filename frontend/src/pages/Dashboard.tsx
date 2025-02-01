import React, { useState } from 'react';
import Layout from '../components/Layout';
import Map from '../components/Map';
import EnvironmentalChart from '../components/EnvironmentalChart';

const Dashboard = () => {
    const [selectedCity, setSelectedCity] = useState('Stockholm');

    return (
        <Layout>
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                {/* Stats Cards */}
                <div className="p-6 bg-card rounded-xl border shadow-sm">
                    <h3 className="text-sm font-medium text-muted-foreground">Average Temp</h3>
                    <div className="text-2xl font-bold mt-2">8.4°C</div>
                </div>
                <div className="p-6 bg-card rounded-xl border shadow-sm">
                    <h3 className="text-sm font-medium text-muted-foreground">Anomaly Rate</h3>
                    <div className="text-2xl font-bold mt-2 text-yellow-600">2.1%</div>
                </div>
                <div className="p-6 bg-card rounded-xl border shadow-sm">
                    <h3 className="text-sm font-medium text-muted-foreground">Active Stations</h3>
                    <div className="text-2xl font-bold mt-2">14</div>
                </div>
            </div>

            <div className="mt-8 grid gap-6 lg:grid-cols-3">
                <div className="lg:col-span-2">
                    <Map />
                </div>
                <div>
                    <div className="bg-card p-4 rounded-lg border">
                        <h3 className="font-semibold mb-2">Select Region</h3>
                        <select
                            className="w-full p-2 border rounded bg-background"
                            value={selectedCity}
                            onChange={(e) => setSelectedCity(e.target.value)}
                        >
                            <option>Stockholm</option>
                            <option>Gothenburg</option>
                            <option>Malmö</option>
                        </select>
                    </div>
                </div>
            </div>

            <div className="mt-8">
                <EnvironmentalChart city={selectedCity} />
            </div>
        </Layout>
    );
};

export default Dashboard;
