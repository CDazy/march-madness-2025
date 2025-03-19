import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'https://march-madness-2025.onrender.com';

export const fetchTeams = async () => {
  try {
    const response = await axios.get(`${API_URL}/teams`);
    return response.data;
  } catch (error) {
    console.error('Error fetching teams:', error);
    return [];
  }
};