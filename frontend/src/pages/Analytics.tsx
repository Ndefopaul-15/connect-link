import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { linksAPI } from '../services/api';
import { ArrowLeft, ExternalLink, Calendar, MousePointerClick, Users } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import NetworkBackground from '../components/NetworkBackground';

interface LinkStats {
  link_id: number;
  short_url_slug: string;
  total_clicks: number;
  unique_clicks: number;
}

interface DailyStat {
  date: string;
  total_clicks: number;
  unique_clicks: number;
}

const Analytics: React.FC = () => {
  const { slug } = useParams<{ slug: string }>();
  const navigate = useNavigate();
  const [stats, setStats] = useState<LinkStats | null>(null);
  const [dailyStats, setDailyStats] = useState<DailyStat[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (slug) {
      loadAnalytics();
    }
  }, [slug]);

  const loadAnalytics = async () => {
    try {
      const [statsResponse, dailyResponse] = await Promise.all([
        linksAPI.getStats(slug!),
        linksAPI.getDailyStats(slug!),
      ]);
      
      setStats(statsResponse.data);
      setDailyStats(dailyResponse.data.stats);
    } catch (err) {
      console.error('Failed to load analytics:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-gray-500">Loading analytics...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen" style={{ 
      background: 'linear-gradient(135deg, #020508 0%, #030a0f 50%, #050f16 100%)', 
      position: 'relative' 
    }}>
      <NetworkBackground />
      <div style={{ position: 'relative', zIndex: 10 }}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <button
            onClick={() => navigate('/dashboard')}
            className="flex items-center space-x-2 text-gray-300 hover:text-white mb-4"
          >
            <ArrowLeft className="h-5 w-5" />
            <span>Back to Dashboard</span>
          </button>
          
          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center justify-between">
              <div>
                <h1 className="text-2xl font-bold text-gray-900 mb-2">Link Analytics</h1>
                <div className="flex items-center space-x-2">
                  <code className="text-lg font-mono text-blue-600">/{slug}</code>
                  <ExternalLink className="h-5 w-5 text-gray-400" />
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500 mb-1">Total Clicks</p>
                <p className="text-3xl font-bold text-gray-900">{stats?.total_clicks || 0}</p>
              </div>
              <div className="bg-blue-100 p-3 rounded-full">
                <MousePointerClick className="h-8 w-8 text-blue-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500 mb-1">Unique Visitors</p>
                <p className="text-3xl font-bold text-gray-900">{stats?.unique_clicks || 0}</p>
              </div>
              <div className="bg-green-100 p-3 rounded-full">
                <Users className="h-8 w-8 text-green-600" />
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500 mb-1">Days Active</p>
                <p className="text-3xl font-bold text-gray-900">{dailyStats.length}</p>
              </div>
              <div className="bg-purple-100 p-3 rounded-full">
                <Calendar className="h-8 w-8 text-purple-600" />
              </div>
            </div>
          </div>
        </div>

        {/* Chart */}
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-6">Click History</h2>
          
          {dailyStats.length > 0 ? (
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={dailyStats}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis 
                  dataKey="date" 
                  tickFormatter={(value) => new Date(value).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                />
                <YAxis />
                <Tooltip 
                  labelFormatter={(value) => new Date(value).toLocaleDateString()}
                />
                <Line 
                  type="monotone" 
                  dataKey="total_clicks" 
                  stroke="#3b82f6" 
                  strokeWidth={2}
                  name="Total Clicks"
                />
                <Line 
                  type="monotone" 
                  dataKey="unique_clicks" 
                  stroke="#10b981" 
                  strokeWidth={2}
                  name="Unique Visitors"
                />
              </LineChart>
            </ResponsiveContainer>
          ) : (
            <div className="text-center py-12 text-gray-500">
              No click data available yet
            </div>
          )}
        </div>
      </div>
      </div>
    </div>
  );
};

export default Analytics;
