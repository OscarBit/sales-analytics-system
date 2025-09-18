// dashboard/src/components/DashboardFilters.jsx

const filterContainerStyle = {
    display: 'flex',
    gap: '20px',
    alignItems: 'center',
    padding: '20px',
    backgroundColor: '#f0f2f5',
    borderRadius: '8px',
    marginBottom: '30px',
};

const filterGroupStyle = {
    display: 'flex',
    flexDirection: 'column',
};

const labelStyle = {
    marginBottom: '5px',
    fontSize: '14px',
    fontWeight: 'bold',
};

const DashboardFilters = ({ filters, onFilterChange }) => {
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        onFilterChange(name, value);
    };

    return (
        <div style={filterContainerStyle}>
            <div style={filterGroupStyle}>
                <label htmlFor="start_date" style={labelStyle}>Start Date:</label>
                <input type="date" id="start_date" name="start_date" value={filters.start_date} onChange={handleInputChange} />
            </div>
            <div style={filterGroupStyle}>
                <label htmlFor="end_date" style={labelStyle}>End Date:</label>
                <input type="date" id="end_date" name="end_date" value={filters.end_date} onChange={handleInputChange} />
            </div>
            <div style={filterGroupStyle}>
                <label htmlFor="region" style={labelStyle}>Region:</label>
                <select name="region" id="region" value={filters.region} onChange={handleInputChange}>
                    <option value="">All Regions</option>
                    <option value="North">North</option>
                    <option value="South">South</option>
                    <option value="East">East</option>
                    <option value="West">West</option>
                </select>
            </div>
        </div>
    );
};

export default DashboardFilters;
