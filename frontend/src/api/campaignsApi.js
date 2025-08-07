import axios from 'axios';

// Get the backend API URL from the environment variables.
// This makes it easy to switch between development and production URLs.
const API_BASE_URL = process.env.REACT_APP_API_URL;

/**
 * Creates a new campaign by sending campaign data to the backend.
 *
 * @param {object} campaignData - The campaign data from the setup form.
 * @returns {Promise<object>} A promise that resolves to the newly created campaign's data, including its ID.
 * @throws {Error} Throws an error if the API call fails.
 */
export const createCampaign = async (campaignData) => {
  try {
    // Make a POST request to the /campaigns endpoint.
    const response = await axios.post(`${API_BASE_URL}/campaigns`, campaignData);
    console.log('Campaign created successfully:', response.data);
    return response.data;
  } catch (error) {
    // Log the error for debugging purposes and re-throw it
    // so the calling component can handle it (e.g., show a UI notification).
    console.error("Error creating campaign:", error.response?.data || error.message);
    throw error;
  }
};

/**
 * Fetches the details of a specific campaign from the backend.
 *
 * @param {string} campaignId - The unique identifier for the campaign.
 * @returns {Promise<object>} A promise that resolves to the campaign's detailed data.
 * @throws {Error} Throws an error if the API call fails.
 */
export const getCampaign = async (campaignId) => {
  if (!campaignId) {
    throw new Error("Campaign ID is required.");
  }
  try {
    // Make a GET request to the /campaigns/{campaignId} endpoint.
    const response = await axios.get(`${API_BASE_URL}/campaigns/${campaignId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching campaign with ID ${campaignId}:`, error.response?.data || error.message);
    throw error;
  }
};