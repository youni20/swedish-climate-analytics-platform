import React from 'react';
import Layout from '../components/Layout';
import EnvironmentalChart from '../components/EnvironmentalChart';

const Analytics = () => {
    return (
        <Layout>
            <h1 className="text-3xl font-bold mb-6">Deep Analytics</h1>
            <p className="text-muted-foreground mb-8">
                Detailed analysis of environmental trends and similarities between Swedish cities.
            </p>

            <div className="grid gap-6 md:grid-cols-2">
                <div className="bg-card p-6 rounded-lg border shadow-sm">
                    <h2 className="text-xl font-semibold mb-4">City Clustering</h2>
                    <div className="aspect-square bg-muted/20 rounded flex items-center justify-center">
                        <span className="text-muted-foreground">Cluster Visualization Placeholder (Scatter Plot)</span>
                    </div>
                    <p className="mt-4 text-sm text-muted-foreground">
                        K-Means clustering grouping cities by similar temperature and humidity patterns.
                    </p>
                </div>

                <div className="bg-card p-6 rounded-lg border shadow-sm">
                    <h2 className="text-xl font-semibold mb-4">Correlation Matrix</h2>
                    <div className="aspect-square bg-muted/20 rounded flex items-center justify-center">
                        <span className="text-muted-foreground">Heatmap Placeholder</span>
                    </div>
                </div>
            </div>

            <div className="mt-8">
                <h2 className="text-xl font-semibold mb-4">Seasonal Decomposition</h2>
                <EnvironmentalChart city="Aggregate" />
            </div>
        </Layout>
    );
};

export default Analytics;
