import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { runDiscovery } from '../api/discoveryApi';
import { getCampaign } from '../api/campaignsApi';
import InfluencerCard from '../components/InfluencerCard';
import AnalyticsDashboard from '../components/AnalyticsDashboard';
import './DiscoveryPage.css'; // We'll create this CSS file

function DiscoveryPage() {
  const { campaignId } = useParams(); // Get campaignId from the URL
  const [campaign, setCampaign] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    // This function runs once when the component mounts
    const initializeDiscovery = async () => {
      try {
        setLoading(true);
        setError('');
        // 1. Tell the backend to start the discovery process
        await runDiscovery(campaignId);
        // 2. Once done, fetch the updated campaign data with the influencer list
        const campaignData = await getCampaign(campaignId);
        setCampaign(campaignData);
      } catch (err) {
        setError("Oops! Something went wrong while finding influencers. Please try creating a new campaign.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    initializeDiscovery();
  }, [campaignId]); // The effect re-runs if the campaignId changes

  // Conditional Rendering based on the state
  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <h2>Analyzing & Scoring Influencers...</h2>
        <p>Our AI is finding the perfect match for your brand.</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container">
        <h2>{error}</h2>
        <Link to="/" className="home-link">Go back to Dashboard</Link>
      </div>
    );
  }

  return (
    <div className="page-container">
      <header className="discovery-header">
        <h1>Discovery Results for "{campaign?.campaign_name}"</h1>
        <p>
          We've analyzed and scored these influencers based on your brand's unique profile.
        </p>
      </header>

      <div className="influencer-grid">
        {campaign?.discovered_influencers.map(influencer => (
          <InfluencerCard key={influencer.handle} influencer={influencer} />
        ))}
      </div>
      
      <hr className="divider" />
      
      {/* Include the analytics dashboard with mock data */}
      <AnalyticsDashboard campaignName={campaign?.campaign_name} />
    </div>
  );
}

export default DiscoveryPage;