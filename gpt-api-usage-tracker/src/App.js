import React, { useEffect, useState } from 'react';
import { Line, LineChart, CartesianGrid, Legend, Tooltip, XAxis, YAxis } from 'recharts';

const API_URL = 'http://localhost:5000/api/usage'; // Replace with your Flask backend URL

const App = () => {
  const [usageData, setUsageData] = useState([]);

  useEffect(() => {
    const fetchUsageData = async () => {
      try {
        const response = await fetch(API_URL);
        const data = await response.json();
        console.log(data)
        const transformedData = data.map((item) => ({
          name: `Cost as of ${item.date}`,
          cost: item.cost,
          // date: item.date
        }));
        console.log(transformedData)
        setUsageData(transformedData);
      } catch (error) {
        console.error('Error fetching usage data:', error);
      }
    };

    fetchUsageData();
  }, [usageData]);

  return (
    <div className="container">
      <h1>API Usage Graph</h1>
      <div className="chart-container">
        <LineChart width={730} height={250} data={usageData}
          margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="cost" stroke="#8884d8" />
        </LineChart>
      </div>
    </div>
  );
};

export default App;

// Make sure you have the `recharts` package installed in your project.
