import axios from 'axios';

export const fetchTeams = async () => {
  try {
    const response = await axios.get('/teams');
    return response.data;
  } catch (error) {
    console.error('Error fetching teams:', error);
    return [];
  }
};