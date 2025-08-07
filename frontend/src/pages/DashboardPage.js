import React from 'react';
import CampaignSetupForm from '../components/CampaignSetupForm';
import './DashboardPage.css'; // We'll create this CSS file

function DashboardPage() {
  return (
    <div className="page-container">
      <header className="page-header">
        <h1>ICY Influencer Platform</h1>
        <p className="subtitle">Your AI-Powered Co-Pilot for Influencer Marketing</p>
      </header>
      <main>
        <CampaignSetupForm />
      </main>
    </div>
  );
}

export default DashboardPage;