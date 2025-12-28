import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { fetchForecast } from '../services/api';

const EnvironmentalChart = ({ city }: { city: string }) => {
    const [data, setData] = useState<any[]>([]);

    useEffect(() => {
        const loadForecast = async () => {
            // Basic fetch, in real app handle loading/error
            const forecast = await fetchForecast(city);
            // Assuming forecast structure has dates/values or we adapt it
            // Real API response: { forecast: [{ ds: "date", yhat: value }, ...] } presumably from Prophet
            if (forecast && forecast.forecast) {
                setData(forecast.forecast.map((item: any) => ({
                    date: new Date(item.ds).toLocaleDateString(),
                    temp: item.yhat
                })).slice(0, 30)); // Show 30 points
            }
        };
        loadForecast();
    }, [city]);

    return (
        <div className="w-full h-[400px] bg-card rounded-lg border p-4 shadow-sm">
            <h3 className="font-semibold mb-4">Temperature Forecast (30 Days): {city}</h3>
            <div className="w-full h-[300px] min-h-[300px]">
                {data.length > 0 ? (
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                            <CartesianGrid strokeDasharray="3 3" opacity={0.2} vertical={false} />
                            <XAxis
                                dataKey="date"
                                tick={{ fontSize: 12, fill: 'var(--muted-foreground)' }}
                                minTickGap={30}
                            />
                            <YAxis
                                unit="°C"
                                width={40}
                                tick={{ fontSize: 12, fill: 'var(--muted-foreground)' }}
                            />
                            <Tooltip
                                contentStyle={{
                                    backgroundColor: 'hsl(var(--card))',
                                    borderColor: 'hsl(var(--border))',
                                    borderRadius: '0.5rem'
                                }}
                                itemStyle={{ color: 'hsl(var(--foreground))' }}
                                labelStyle={{ color: 'hsl(var(--muted-foreground))' }}
                            />
                            <Line
                                type="monotone"
                                dataKey="temp"
                                name="Temperature"
                                stroke="hsl(var(--primary))"
                                strokeWidth={2}
                                dot={{ fill: 'hsl(var(--primary))', r: 2 }}
                                activeDot={{ r: 6 }}
                            />
                        </LineChart>
                    </ResponsiveContainer>
                ) : (
                    <div className="flex flex-col items-center justify-center h-full text-muted-foreground animate-pulse">
                        <p>Loading Forecast...</p>
                        <span className="text-xs mt-2 opacity-70">Model is calculating projections (Prophet)</span>
                    </div>
                )}
            </div>
        </div>
    );
};

export default EnvironmentalChart;
