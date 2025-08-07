import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createCampaign } from '../api/campaignsApi';
import './CampaignSetupForm.css'; // We'll create this CSS file next

function CampaignSetupForm() {
  const [campaignName, setCampaignName] = useState('');
  const [productDetails, setProductDetails] = useState('');
  const [niche, setNiche] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!campaignName || !productDetails || !niche) {
      alert("Please fill out all fields.");
      return;
    }
    setLoading(true);

    const campaignData = {
      user_id: "user123", // This would come from auth context in a real app
      campaign_name: campaignName,
      brand_profile: {
        product_details: productDetails,
        target_audience: { "age": [25, 35], "gender": "Female", "interests": ["sustainability"] }, // Mock data for now
        brand_tone: "friendly",
        budget: "micro",
        niche: niche.split(',').map(n => n.trim().toLowerCase()),
      },
    };

    try {
      const result = await createCampaign(campaignData);
      // Navigate to the discovery page with the new campaign ID
      navigate(`/discover/${result.campaign_id}`);
    } catch (error) {
      alert("Failed to create campaign. Please check the console for details.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <div className="form-header">
        <h2>Launch Your Next Campaign</h2>
        <p>Tell us about your brand. Our AI will find the perfect influencers for you.</p>
      </div>
      <form onSubmit={handleSubmit} className="campaign-form">
        <div className="form-group">
          <label htmlFor="campaignName">Campaign Name</label>
          <input
            id="campaignName"
            type="text"
            placeholder="e.g., Summer Skincare Launch"
            value={campaignName}
            onChange={(e) => setCampaignName(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="productDetails">Product Details</label>
          <textarea
            id="productDetails"
            placeholder="e.g., Organic, vegan skincare products for sensitive skin..."
            value={productDetails}
            onChange={(e) => setProductDetails(e.target.value)}
            required
            rows="4"
          />
        </div>
        <div className="form-group">
          <label htmlFor="niche">Primary Niches</label>
          <input
            id="niche"
            type="text"
            placeholder="e.g., beauty, sustainability, fitness"
            value={niche}
            onChange={(e) => setNiche(e.target.value)}
            required
          />
          <small>Separate niches with a comma.</small>
        </div>
        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? 'Analyzing...' : 'Find My Influencers'}
        </button>
      </form>
    </div>
  );
}

export default CampaignSetupForm;