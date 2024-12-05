const API_URL = "https://chatbot-restaurante.onrender.com"; // Backend en Render

export const fetchData = async (endpoint, options = {}) => {
  const response = await fetch(`${API_URL}${endpoint}`, options);
  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }
  return response.json();
};
