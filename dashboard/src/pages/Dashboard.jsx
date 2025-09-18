import { useState, useEffect } from 'react';
import DashboardFilters from '../components/DashboardFilters';
import LineChart from '../components/LineChart';
import BarChart from '../components/BarChart';
import PieChart from '../components/PieChart';
import MetricCard from '../components/MetricCard';
import {
    getMonthlyRevenue,
    getCategoryRevenue,
    getTopSellers,
    getRegionSales,
} from '../services/AnalyticsApi';

const Dashboard = () => {
    const [loading, setLoading] = useState(true);
    const [metrics, setMetrics] = useState({ totalRevenue: 0, totalSales: 0 });
    const [monthlyRevenueData, setMonthlyRevenueData] = useState(null);
    const [categoryRevenueData, setCategoryRevenueData] = useState(null);
    const [topSellersData, setTopSellersData] = useState(null);
    const [regionSalesData, setRegionSalesData] = useState(null);
    const [filters, setFilters] = useState({
        start_date: '',
        end_date: '',
        region: '',
    });
    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            // Fetch all data in parallel for efficiency
            const [monthly, category, sellers, region] = await Promise.all([
                getMonthlyRevenue(filters),
                getCategoryRevenue(filters),
                getTopSellers(),
                getRegionSales(),
            ]);

            // --- Process Monthly Revenue (Line Chart) ---
            setMonthlyRevenueData({
                labels: monthly.map((item) => new Date(item.month).toLocaleString('default', { month: 'short', year: '2-digit' })),
                datasets: [{
                    label: 'Monthly Revenue',
                    data: monthly.map((item) => item.total_revenue),
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1,
                }],
            });

            // --- Process Category Revenue (Bar Chart) ---
            setCategoryRevenueData({
                labels: category.map(item => item.category),
                datasets: [{
                    label: 'Revenue by Category',
                    data: category.map(item => item.total_revenue),
                    backgroundColor: 'rgba(54, 162, 235, 0.6)',
                }]
            });

            // --- Process Top Sellers (Horizontal Bar Chart) ---
            setTopSellersData({
                labels: sellers.map(item => item.name),
                datasets: [{
                    label: 'Top 10 Sellers Revenue',
                    data: sellers.map(item => item.total_revenue),
                    backgroundColor: 'rgba(255, 159, 64, 0.6)',
                    borderColor: 'rgba(255, 159, 64, 1)',
                    borderWidth: 1,
                }]
            });

            // --- Process Region Sales (Pie Chart) ---
            setRegionSalesData({
                labels: region.map(item => item.region),
                datasets: [{
                    label: 'Sales by Region',
                    data: region.map(item => item.total_revenue),
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(255, 206, 86, 0.6)',
                        'rgba(153, 102, 255, 0.6)',
                    ],
                }]
            });

            // --- Calculate Overall Metrics ---
            const totalRevenue = monthly.reduce((sum, item) => sum + parseFloat(item.total_revenue), 0);
            setMetrics({ totalRevenue: totalRevenue.toLocaleString('en-US', { style: 'currency', currency: 'USD' }) });

            setLoading(false);
        };
        fetchData();
    }, [filters]);

    const handleFilterChange = (filterName, value) => {
        setFilters(prevFilters => ({
            ...prevFilters,
            [filterName]: value,
        }));
    };
    if (loading) {
        return <div>Loading Dashboard...</div>;
    }

    return (
        <div className="dashboard-container">
            <DashboardFilters filters={filters} onFilterChange={handleFilterChange} />
            <div className="metrics-grid">
                <MetricCard title="Total Revenue" value={metrics.totalRevenue} />
                {/* You can add more metric cards here */}
            </div>
            <div className="charts-grid">
                <div className="chart-card">
                    <LineChart chartData={monthlyRevenueData} options={{ responsive: true, plugins: { title: { display: true, text: 'Monthly Sales Revenue' } } }} />
                </div>
                <div className="chart-card">
                    <BarChart chartData={categoryRevenueData} options={{ responsive: true, plugins: { title: { display: true, text: 'Revenue by Product Category' } } }} />
                </div>
                <div className="chart-card">
                    <BarChart chartData={topSellersData} options={{ indexAxis: 'y', responsive: true, plugins: { title: { display: true, text: 'Top 10 Sellers by Revenue' } } }} />
                </div>
                <div className="chart-card">
                    <PieChart chartData={regionSalesData} options={{ responsive: true, plugins: { title: { display: true, text: 'Sales Distribution by Region' } } }} />
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
