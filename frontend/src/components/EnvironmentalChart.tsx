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
            <div className="w-full h-[300px]">
                {data.length > 0 ? (
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data}>
                            <CartesianGrid strokeDasharray="3 3" opacity={0.2} />
                            <XAxis dataKey="date" hide />
                            <YAxis />
                            <Tooltip
                                contentStyle={{ backgroundColor: 'var(--card)', borderColor: 'var(--border)' }}
                                itemStyle={{ color: 'var(--foreground)' }}
                            />
                            <Line
                                type="monotone"
                                dataKey="temp"
                                stroke="hsl(var(--primary))"
                                strokeWidth={2}
                                dot={false}
                            />
                        </LineChart>
                    </ResponsiveContainer>
                ) : (
                    <div className="flex items-center justify-center h-full text-muted-foreground">
                        Loading forecast data...
                    </div>
                )}
            </div>
        </div>
    );
};

export default EnvironmentalChart;
