// src/services/api.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

export const fetchSkills = () => axios.get(`${API_URL}skills/`);
export const fetchProjects = () => axios.get(`${API_URL}projects/`);
export const fetchBlogs = () => axios.get(`${API_URL}blogs/`);
