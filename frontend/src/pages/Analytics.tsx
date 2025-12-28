import React, { useEffect, useState } from 'react';
import Layout from '../components/Layout';
import EnvironmentalChart from '../components/EnvironmentalChart';
import { fetchClusters, fetchCorrelations } from '../services/api';
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

const Analytics = () => {
    const [clusters, setClusters] = useState<any[]>([]);
    const [correlations, setCorrelations] = useState<any[]>([]);

    useEffect(() => {
        const loadData = async () => {
            const clusterData = await fetchClusters();
            if (Array.isArray(clusterData)) {
                setClusters(clusterData);
            }

            const corrData = await fetchCorrelations();
            if (Array.isArray(corrData)) {
                setCorrelations(corrData);
            }
        };
        loadData();
    }, []);

    return (
        <Layout>
            <h1 className="text-3xl font-bold mb-6">Deep Analytics</h1>
            <p className="text-muted-foreground mb-8">
                Detailed analysis of environmental trends and similarities between Swedish cities.
            </p>

            <div className="grid gap-6 md:grid-cols-2">
                <div className="bg-card p-6 rounded-lg border shadow-sm">
                    <h2 className="text-xl font-semibold mb-4">City Clustering</h2>
                    <div className="h-[300px] w-full">
                        {clusters.length > 0 ? (
                            <ResponsiveContainer width="100%" height="100%">
                                <ScatterChart margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
                                    <CartesianGrid />
                                    <XAxis type="number" dataKey="temperature" name="Temperature" unit="°C" />
                                    <YAxis type="number" dataKey="humidity" name="Humidity" unit="%" />
                                    <Tooltip cursor={{ strokeDasharray: '3 3' }}
                                        content={({ active, payload }) => {
                                            if (active && payload && payload.length) {
                                                return (
                                                    <div className="bg-popover p-2 border rounded shadow-sm text-sm">
                                                        <p className="font-semibold">{payload[0].payload.city}</p>
                                                        <p>Temp: {payload[0].value}°C</p>
                                                        <p>Humidity: {payload[1].value}%</p>
                                                    </div>
                                                );
                                            }
                                            return null;
                                        }}
                                    />
                                    <Scatter name="Cities" data={clusters} fill="#8884d8">
                                        {clusters.map((entry, index) => (
                                            <Cell key={`cell-${index}`} fill={COLORS[entry.cluster % COLORS.length]} />
                                        ))}
                                    </Scatter>
                                </ScatterChart>
                            </ResponsiveContainer>
                        ) : (
                            <div className="flex items-center justify-center h-full text-muted-foreground">
                                Loading clustering data...
                            </div>
                        )}
                    </div>
                    <p className="mt-4 text-sm text-muted-foreground">
                        K-Means clustering grouping cities by similar temperature and humidity patterns.
                    </p>
                </div>

                <div className="bg-card p-6 rounded-lg border shadow-sm">
                    <h2 className="text-xl font-semibold mb-4">Correlation Matrix</h2>
                    <div className="w-full flex items-center justify-center bg-card rounded overflow-hidden">
                        {correlations.length > 0 ? (
                            <div className="grid grid-cols-5 gap-1 text-xs w-full">
                                {/* Header Row */}
                                <div className="p-2"></div>
                                {['Temp', 'Humid', 'Press', 'Wind'].map(h => (
                                    <div key={h} className="font-bold flex items-center justify-center p-2 bg-muted">{h}</div>
                                ))}

                                {/* Data Rows */}
                                {['temperature', 'humidity', 'pressure', 'wind_speed'].map((rowKey) => (
                                    <React.Fragment key={rowKey}>
                                        <div className="font-bold flex items-center p-2 bg-muted capitalize">
                                            {rowKey.replace('temperature', 'Temp').replace('humidity', 'Humid').replace('pressure', 'Press').replace('wind_speed', 'Wind')}
                                        </div>
                                        {['temperature', 'humidity', 'pressure', 'wind_speed'].map((colKey) => {
                                            const item = correlations.find(c => c.x === rowKey && c.y === colKey);
                                            const val = item ? item.value : 0;
                                            // Color scale: Red (pos), Blue (neg)
                                            const bg = val > 0
                                                ? `rgba(220, 38, 38, ${Math.abs(val)})`
                                                : `rgba(37, 99, 235, ${Math.abs(val)})`;
                                            const color = Math.abs(val) > 0.5 ? 'white' : 'black';

                                            return (
                                                <div key={`${rowKey}-${colKey}`}
                                                    className="flex items-center justify-center p-4 font-mono rounded"
                                                    style={{ backgroundColor: bg, color }}
                                                >
                                                    {val.toFixed(2)}
                                                </div>
                                            );
                                        })}
                                    </React.Fragment>
                                ))}
                            </div>
                        ) : (
                            <div className="text-muted-foreground p-8">Loading correlations...</div>
                        )}
                    </div>
                </div>
            </div>

            <div className="mt-8">
                <h2 className="text-xl font-semibold mb-4">Seasonal Decomposition</h2>
                <EnvironmentalChart city="Stockholm" />
            </div>
        </Layout>
    );
};

export default Analytics;
