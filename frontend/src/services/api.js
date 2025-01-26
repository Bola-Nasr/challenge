import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // API URL

export async function login(username, password) {
  const response = await axios.post(`${API_URL}/login`, new URLSearchParams({
    username,
    password,
  }));
  return response.data.access_token;
}

export async function fetchProperties(token, page, filters) {
  const response = await axios.get(`${API_URL}/properties`, {
    headers: { Authorization: `Bearer ${token}` },
    params: {
      skip: (page - 1) * 20,
      limit: 20,
      full_address: filters.fullAddress || undefined,
      class_description: filters.classDescription || undefined,
      min_market_value: filters.minMarketValue || undefined,
      max_market_value: filters.maxMarketValue || undefined,
      building_use: filters.buildingUse || undefined,
      min_square_feet: filters.minSquareFeet || undefined,
      max_square_feet: filters.maxSquareFeet || undefined,
      sort_by: filters.sortBy || undefined,
    },
  });
  return response.data;
}