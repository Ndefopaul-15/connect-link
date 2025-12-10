// ============================================================================
// API SERVICE - FRONTEND TO BACKEND COMMUNICATION
// ============================================================================
// This file contains ALL functions that communicate with the Flask backend
// Location: frontend/src/services/api.ts
// Backend URL: http://127.0.0.1:5000/api
// ============================================================================

import axios from 'axios';

// Backend server URL - Automatically uses production URL when built
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:5000/api';

// Create Axios instance with default configuration
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',  // All requests send JSON data
  },
});

// ============================================================================
// AUTOMATIC JWT TOKEN INJECTION
// ============================================================================
// This interceptor automatically adds the JWT token to every request
// Token is stored in browser's localStorage after login
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');  // Get token from localStorage
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;  // Add to Authorization header
  }
  return config;
});

// ============================================================================
// AUTHENTICATION API
// ============================================================================
// All authentication-related API calls (login, register, password reset)
// Backend file: app/routes/auth.py
export const authAPI = {
  // Register new user
  // Sends: { email, password }
  // Returns: { access_token, user }
  // Backend route: POST /auth/register
  register: (email: string, password: string) =>
    api.post('/auth/register', { email, password }),
  
  // Login existing user
  // Sends: { email, password }
  // Returns: { access_token, user }
  // Backend route: POST /auth/login
  login: (email: string, password: string) =>
    api.post('/auth/login', { email, password }),
  
  // Get current user profile (requires JWT token)
  // Returns: { user }
  // Backend route: GET /auth/me
  getProfile: () =>
    api.get('/auth/me'),
  
  // Change password for logged-in user (requires JWT token)
  // Sends: { current_password, new_password }
  // Returns: { message }
  // Backend route: PUT /auth/change-password
  changePassword: (currentPassword: string, newPassword: string) =>
    api.put('/auth/change-password', {
      current_password: currentPassword,
      new_password: newPassword,
    }),
  
  // Request password reset (forgot password)
  // Sends: { email }
  // Returns: { message }
  // Backend route: POST /auth/forgot-password
  forgotPassword: (email: string) =>
    api.post('/auth/forgot-password', { email }),
  
  // Reset password using token from email
  // Sends: { token, new_password }
  // Returns: { message }
  // Backend route: POST /auth/reset-password
  resetPassword: (token: string, newPassword: string) =>
    api.post('/auth/reset-password', {
      token,
      new_password: newPassword,
    }),
};

// ============================================================================
// LINKS API
// ============================================================================
// All link management API calls (create, read, update, delete)
// Backend file: app/routes/links.py
export const linksAPI = {
  // Create new short link (requires JWT token)
  // Sends: { long_url, custom_slug?, expiration_days? }
  // Returns: { link_id, short_url, short_url_slug, ... }
  // Backend route: POST /links
  create: (longUrl: string, customSlug?: string, expirationDays?: number) =>
    api.post('/links', {
      long_url: longUrl,
      custom_slug: customSlug,
      expiration_days: expirationDays,
    }),
  
  // Get all links for current user (requires JWT token)
  // Query params: page, per_page, search
  // Returns: { links: [...], total, pages }
  // Backend route: GET /links
  getAll: (page = 1, perPage = 10, search?: string) =>
    api.get('/links', {
      params: { page, per_page: perPage, search },
    }),
  
  // Get single link details (requires JWT token)
  // Returns: { link_id, long_url, short_url, click_count, ... }
  // Backend route: GET /links/{slug}
  getOne: (slug: string) =>
    api.get(`/links/${slug}`),
  
  // Update link (requires JWT token)
  // Sends: { long_url?, is_active?, ... }
  // Returns: { message, link }
  // Backend route: PUT /links/{slug}
  update: (slug: string, data: any) =>
    api.put(`/links/${slug}`, data),
  
  // Delete link (requires JWT token)
  // Returns: { message }
  // Backend route: DELETE /links/{slug}
  delete: (slug: string) =>
    api.delete(`/links/${slug}`),
  
  // Get link statistics summary (requires JWT token)
  // Returns: { total_clicks, unique_visitors, ... }
  // Backend route: GET /links/{slug}/stats/summary
  getStats: (slug: string) =>
    api.get(`/links/${slug}/stats/summary`),
  
  // Get daily click statistics (requires JWT token)
  // Query params: start_date, end_date
  // Returns: { daily_stats: [...] }
  // Backend route: GET /links/{slug}/stats/daily
  getDailyStats: (slug: string, startDate?: string, endDate?: string) =>
    api.get(`/links/${slug}/stats/daily`, {
      params: { start_date: startDate, end_date: endDate },
    }),
  
  // Get click history (requires JWT token)
  // Query params: page, per_page
  // Returns: { clicks: [...], total }
  // Backend route: GET /links/{slug}/clicks
  getClicks: (slug: string, page = 1, perPage = 20) =>
    api.get(`/links/${slug}/clicks`, {
      params: { page, per_page: perPage },
    }),
};

// Domains API
export const domainsAPI = {
  create: (domainName: string) =>
    api.post('/domains', { domain_name: domainName }),
  
  getAll: () =>
    api.get('/domains'),
  
  getOne: (id: number) =>
    api.get(`/domains/${id}`),
  
  update: (id: number, status: string) =>
    api.put(`/domains/${id}`, { status }),
  
  delete: (id: number) =>
    api.delete(`/domains/${id}`),
  
  verify: (id: number) =>
    api.post('/domains/verify', { domain_id: id }),
};

// QR Codes API
export const qrCodesAPI = {
  get: (slug: string) =>
    api.get(`/links/${slug}/qr-code`),
  
  create: (slug: string, codeType: string, designParameters?: string) =>
    api.post(`/links/${slug}/qr-code`, {
      code_type: codeType,
      design_parameters: designParameters,
    }),
  
  update: (slug: string, codeType: string, designParameters?: string) =>
    api.put(`/links/${slug}/qr-code`, {
      code_type: codeType,
      design_parameters: designParameters,
    }),
};

// Rewards API
export const rewardsAPI = {
  getAll: () =>
    api.get('/rewards'),
  
  redeem: (rewardId: number) =>
    api.post('/rewards/redeem', { reward_id: rewardId }),
};

export default api;
