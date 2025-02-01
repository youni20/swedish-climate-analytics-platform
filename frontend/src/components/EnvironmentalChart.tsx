import React from 'react';

// Would involve Recharts here
const EnvironmentalChart = ({ city }: { city: string }) => {
    return (
        <div className="w-full h-[300px] bg-card rounded-lg border p-4 shadow-sm">
            <h3 className="font-semibold mb-4">Temperature Trend: {city}</h3>
            <div className="w-full h-[200px] bg-muted/10 flex items-end justify-between px-2 gap-1">
                {/* Fake Bars */}
                {[...Array(10)].map((_, i) => (
                    <div key={i} className="bg-primary/80 w-full" style={{ height: `${Math.random() * 80 + 20}%` }}></div>
                ))}
            </div>
        </div>
    );
};

export default EnvironmentalChart;
