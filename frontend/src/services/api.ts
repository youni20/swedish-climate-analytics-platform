import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/api',
});

// Matches backend/api/schemas/schemas.py class City
export interface City {
    name: string;
    latitude?: number;
    longitude?: number;
}

// Matches backend/api/schemas/schemas.py class ForecastPoint
export interface ForecastPoint {
    date: string;
    predicted_value: number;
    lower_bound?: number;
    upper_bound?: number;
}

export interface ForecastResponse {
    city: string;
    model: string;
    forecast: ForecastPoint[];
}

export const fetchCities = async (): Promise<City[]> => {
    try {
        const response = await api.get<City[]>('/cities');
        return response.data;
    } catch (error) {
        console.error("Failed to fetch cities", error);
        return [];
    }
};

export const fetchForecast = async (city: string): Promise<ForecastResponse | null> => {
    try {
        const response = await api.get<ForecastResponse>(`/predictions/${city}/forecast`);
        return response.data;
    } catch (error) {
        console.error("Failed to fetch forecast", error);
        return null;
    }
};

export const fetchClusters = async () => {
    try {
        const response = await api.get('/analytics/clusters');
        return response.data;
    } catch (error) {
        console.error("Failed to fetch clusters", error);
        return [];
    }
};

export const fetchCorrelations = async () => {
    try {
        const response = await api.get('/analytics/correlations');
        return response.data;
    } catch (error) {
        console.error("Failed to fetch correlations", error);
        return [];
    }
};
