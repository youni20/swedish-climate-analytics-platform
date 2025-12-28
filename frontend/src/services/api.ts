import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000',
});

export interface City {
    city_id: string;
    city_name: string;
    county: string;
    population: number;
}

export const fetchCities = async (): Promise<City[]> => {
    try {
        const response = await api.get('/cities');
        return response.data;
    } catch (error) {
        console.error("Failed to fetch cities", error);
        return [];
    }
};

export const fetchForecast = async (city: string) => {
    try {
        const response = await api.get(`/predictions/${city}/forecast`);
        return response.data;
    } catch (error) {
        console.error("Failed to fetch forecast", error);
        return null;
    }
};
