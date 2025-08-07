import axios from 'axios';

// The base URL for your backend API, configured for different environments.
const API_BASE_URL = process.env.REACT_APP_API_URL;

/**
 * Triggers the backend process to discover and analyze influencers for a given campaign.
 * This function sends a request to the backend, which then performs the heavy lifting
 * of finding and scoring influencers based on the campaign's brand profile.
 *
 * @param {string} campaignId - The unique identifier of the campaign to run discovery for.
 * @returns {Promise<object>} A promise that resolves to the API response, typically a confirmation message.
 * @throws {Error} Throws an error if the API call fails, allowing the UI to handle the error state.
 */
export const runDiscovery = async (campaignId) => {
  if (!campaignId) {
    throw new Error("A Campaign ID is required to run discovery.");
  }
  try {
    // Make a POST request to the discovery endpoint. The backend uses the campaignId
    // to find the relevant brand profile and criteria for its search.
    const response = await axios.post(`${API_BASE_URL}/campaigns/${campaignId}/discover`);
    console.log('Discovery process initiated successfully:', response.data);
    return response.data;
  } catch (error) {
    // Provide a detailed error message for easier debugging.
    console.error(`Error initiating discovery for campaign ${campaignId}:`, error.response?.data || error.message);
    throw error;
  }
};