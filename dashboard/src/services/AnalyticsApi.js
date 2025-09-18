import axios from 'axios';

// Create an Axios instance configured for our analytics API
const apiClient = axios.create({
    baseURL: '/api/analytics',
});

/**
 * Fetches the monthly sales revenue data.
 * @returns {Promise<Array>} A promise that resolves to the data.
 */
export const getMonthlyRevenue = async () => {
    try {
        const response = await apiClient.get('/monthly_revenue/', { params });
        return response.data;
    } catch (error) {
        console.error("Error fetching monthly revenue:", error);
        return []; // Return empty array on error
    }
};

/**
 * Fetches the total revenue per product category.
 * @returns {Promise<Array>} A promise that resolves to the data.
 */
export const getCategoryRevenue = async () => {
    try {
        const response = await apiClient.get('/category_revenue/', { params });
        return response.data;
    } catch (error) {
        console.error("Error fetching category revenue:", error);
        return [];
    }
};

/**
 * Fetches the top 10 sellers by revenue.
 * @returns {Promise<Array>} A promise that resolves to the data.
 */
export const getTopSellers = async () => {
    try {
        const response = await apiClient.get('/top_sellers/');
        return response.data;
    } catch (error) {
        console.error("Error fetching top sellers:", error);
        return [];
    }
};

/**
 * Fetches the sales distribution by customer region.
 * @returns {Promise<Array>} A promise that resolves to the data.
 */
export const getRegionSales = async () => {
    try {
        const response = await apiClient.get('/region_sales/');
        return response.data;
    } catch (error) {
        console.error("Error fetching region sales:", error);
        return [];
    }
};
