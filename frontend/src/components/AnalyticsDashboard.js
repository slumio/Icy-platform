import React from 'react';
import './AnalyticsDashboard.css'; // We'll create this CSS file

// Mock data to visualize the dashboard structure
const mockStats = {
  messagesSent: 50,
  openRate: 32,
  positiveResponses: 12,
  collaborations: 5,
};

function AnalyticsDashboard({ campaignName }) {
  // Calculate a simple conversion rate for visualization
  const conversionRate = ((mockStats.collaborations / mockStats.positiveResponses) * 100).toFixed(1);

  return (
    <div className="dashboard-container">
      <div className="dashboard-header">
        <h3>Campaign Analytics: "{campaignName}"</h3>
      </div>
      <div className="stats-grid">
        <div className="stat-card">
          <h4>Messages Sent</h4>
          <p className="stat-value">{mockStats.messagesSent}</p>
        </div>
        <div className="stat-card">
          <h4>Open Rate</h4>
          <p className="stat-value">{mockStats.openRate}%</p>
        </div>
        <div className="stat-card">
          <h4>Positive Replies</h4>
          <p className="stat-value">{mockStats.positiveResponses}</p>
        </div>
        <div className="stat-card">
          <h4>Collaborations</h4>
          <p className="stat-value">{mockStats.collaborations}</p>
          <small>({conversionRate}% conversion)</small>
        </div>
      </div>
      <div className="chart-placeholder">
        <p>Performance charts and influencer breakdown will be displayed here.</p>
        {/* In a real app, a charting library like Chart.js or Recharts would be used here */}
      </div>
    </div>
  );
}

export default AnalyticsDashboard;