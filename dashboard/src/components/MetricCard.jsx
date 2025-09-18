const cardStyle = {
    padding: '20px',
    borderRadius: '8px',
    backgroundColor: '#f9f9f9',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
    textAlign: 'center',
};

const titleStyle = {
    margin: 0,
    fontSize: '16px',
    color: '#666',
};

const valueStyle = {
    margin: '10px 0 0',
    fontSize: '32px',
    fontWeight: 'bold',
    color: '#333',
};

const MetricCard = ({ title, value }) => {
    return (
        <div style={cardStyle}>
            <h3 style={titleStyle}>{title}</h3>
            <p style={valueStyle}>{value}</p>
        </div>
    );
};

export default MetricCard;
