import React, { useState, useEffect } from 'react';
import toast from 'react-hot-toast';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import { linksAPI } from '../services/api';
import { Link as LinkIcon, Plus, Copy, Trash2, BarChart3, LogOut, ExternalLink, QrCode, Moon, Sun } from 'lucide-react';
import { Link } from 'react-router-dom';
import Logo from '../components/Logo';
import NetworkBackground from '../components/NetworkBackground';
import QRCodeDesigner from '../components/QRCodeDesigner';

interface LinkData {
  link_id: number;
  long_url: string;
  short_url: string;
  short_url_slug: string;
  creation_date: string;
  click_count: number;
  is_active: boolean;
}

const Dashboard: React.FC = () => {
  const { user, logout } = useAuth();
  const { isDarkMode, toggleTheme } = useTheme();
  const [links, setLinks] = useState<LinkData[]>([]);
  const [loading, setLoading] = useState(true);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [longUrl, setLongUrl] = useState('');
  const [customSlug, setCustomSlug] = useState('');
  const [useCustomSlug, setUseCustomSlug] = useState(false);
  const [expirationDays, setExpirationDays] = useState<number | ''>('');
  const [useExpiration, setUseExpiration] = useState(false);
  const [creating, setCreating] = useState(false);
  const [error, setError] = useState('');
  const [copiedSlug, setCopiedSlug] = useState<string | null>(null);
  const [showQRModal, setShowQRModal] = useState(false);
  const [selectedLinkForQR, setSelectedLinkForQR] = useState<string | null>(null);

  useEffect(() => {
    loadLinks();
  }, []);

  const isValidSlug = (slug: string): boolean => {
    // Check if slug contains protocol or slashes (invalid)
    return !slug.includes('://') && !slug.includes('/');
  };

  const loadLinks = async () => {
    try {
      const response = await linksAPI.getAll(1, 50);
      // Filter out links with malformed slugs
      const validLinks = response.data.links.filter((link: LinkData) => isValidSlug(link.short_url_slug));
      setLinks(validLinks);
      
      // Warn if any links were filtered out
      const filteredCount = response.data.links.length - validLinks.length;
      if (filteredCount > 0) {
        toast.error(`${filteredCount} malformed link(s) hidden. Please delete them from the database.`, {
          duration: 5000,
        });
      }
    } catch (err) {
      console.error('Failed to load links:', err);
    } finally {
      setLoading(false);
    }
  };

  const sanitizeSlug = (input: string): string => {
    // Remove protocol and domain if a URL is pasted
    let slug = input;
    
    // If it contains ://, extract just the path
    if (slug.includes('://')) {
      try {
        const url = new URL(slug);
        slug = url.pathname.substring(1); // Remove leading /
      } catch {
        // If URL parsing fails, just remove the protocol part
        slug = slug.split('://')[1] || slug;
      }
    }
    
    // Remove any remaining slashes and special characters
    slug = slug.replace(/[^a-zA-Z0-9-_]/g, '-');
    
    // Remove leading/trailing hyphens
    slug = slug.replace(/^-+|-+$/g, '');
    
    return slug;
  };

  const handleCustomSlugChange = (value: string) => {
    const sanitized = sanitizeSlug(value);
    setCustomSlug(sanitized);
    
    // Show warning if input was modified
    if (value !== sanitized && value.length > 0) {
      toast('Slug sanitized: only letters, numbers, hyphens, and underscores allowed', {
        duration: 2000,
        icon: 'ℹ️',
      });
    }
  };

  const handleCreateLink = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setCreating(true);

    // Validate custom slug if provided
    if (useCustomSlug && customSlug) {
      if (customSlug.length < 3) {
        setError('Custom slug must be at least 3 characters');
        setCreating(false);
        return;
      }
      if (!/^[a-zA-Z0-9-_]+$/.test(customSlug)) {
        setError('Custom slug can only contain letters, numbers, hyphens, and underscores');
        setCreating(false);
        return;
      }
    }

    try {
      await linksAPI.create(
        longUrl, 
        customSlug || undefined,
        useExpiration && expirationDays ? Number(expirationDays) : undefined
      );
      setLongUrl('');
      setCustomSlug('');
      setUseCustomSlug(false);
      setExpirationDays('');
      setUseExpiration(false);
      setShowCreateModal(false);
      toast.success('✨ Link created successfully!');
      loadLinks();
    } catch (err: any) {
      const errorMsg = err.response?.data?.error || 'Failed to create link';
      setError(errorMsg);
      toast.error(errorMsg);
    } finally {
      setCreating(false);
    }
  };

  const handleDeleteLink = async (slug: string) => {
    if (!confirm('Are you sure you want to delete this link?')) return;

    try {
      await linksAPI.delete(slug);
      toast.success('🗑️ Link deleted successfully');
      loadLinks();
    } catch (err) {
      console.error('Failed to delete link:', err);
      toast.error('Failed to delete link');
    }
  };

  const copyToClipboard = (text: string, slug: string) => {
    navigator.clipboard.writeText(text);
    setCopiedSlug(slug);
    toast.success('Link copied to clipboard!');
    setTimeout(() => setCopiedSlug(null), 2000);
  };

  const handleLogout = () => {
    toast.success('👋 Goodbye! See you soon!', {
      duration: 3000,
      style: {
        background: '#3b82f6',
        color: '#fff',
      },
    });
    setTimeout(() => {
      logout();
    }, 500);
  };

  const handleGenerateQR = (slug: string) => {
    setSelectedLinkForQR(slug);
    setShowQRModal(true);
  };

  return (
    <div className="min-h-screen" style={{ 
      background: 'linear-gradient(135deg, #020508 0%, #030a0f 50%, #050f16 100%)', 
      position: 'relative' 
    }}>
      <NetworkBackground />
      <div style={{ position: 'relative', zIndex: 10 }}>
      {/* Header */}
      <header className="glass backdrop-blur-md border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex justify-between items-center">
            <div className="flex items-center space-x-3">
              <Logo className="h-14 w-14 drop-shadow-lg" />
              <div>
                <p className="text-sm text-gray-300 font-medium">{user?.email}</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <div className="text-right glass-dark px-4 py-2 rounded-xl">
                <p className="text-xs text-gray-400 uppercase tracking-wide">Points</p>
                <p className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">{user?.point_balance}</p>
              </div>
              <button
                onClick={toggleTheme}
                className="p-2 text-gray-300 hover:text-white hover:bg-white/10 rounded-lg transition-colors scale-hover"
                title={isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
              >
                {isDarkMode ? <Sun className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
              </button>
              <button
                onClick={handleLogout}
                className="flex items-center space-x-2 px-4 py-2 text-gray-300 hover:text-white hover:bg-white/10 rounded-lg transition-colors"
              >
                <LogOut className="h-5 w-5" />
                <span>Logout</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="glass-dark rounded-2xl p-8 card-animate scale-hover cursor-pointer border border-white/10 relative overflow-hidden group">
            <div className="absolute inset-0 bg-gradient-to-br from-blue-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            <div className="relative flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400 uppercase tracking-wide mb-2">Total Links</p>
                <p className="text-4xl font-bold text-white bounce-in">{links.length}</p>
              </div>
              <div className="p-4 bg-blue-500/20 rounded-2xl">
                <LinkIcon className="h-10 w-10 text-blue-400 pulse-slow" />
              </div>
            </div>
          </div>
          <div className="glass-dark rounded-2xl p-8 card-animate scale-hover cursor-pointer border border-white/10 relative overflow-hidden group" style={{ animationDelay: '0.1s' }}>
            <div className="absolute inset-0 bg-gradient-to-br from-green-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            <div className="relative flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400 uppercase tracking-wide mb-2">Total Clicks</p>
                <p className="text-4xl font-bold text-white bounce-in">
                  {links.reduce((sum, link) => sum + link.click_count, 0)}
                </p>
              </div>
              <div className="p-4 bg-green-500/20 rounded-2xl">
                <BarChart3 className="h-10 w-10 text-green-400 pulse-slow" />
              </div>
            </div>
          </div>
          <div className="glass-dark rounded-2xl p-8 card-animate scale-hover cursor-pointer border border-white/10 relative overflow-hidden group" style={{ animationDelay: '0.2s' }}>
            <div className="absolute inset-0 bg-gradient-to-br from-purple-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            <div className="relative flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400 uppercase tracking-wide mb-2">Active Links</p>
                <p className="text-4xl font-bold text-white bounce-in">
                  {links.filter(l => l.is_active).length}
                </p>
              </div>
              <div className="p-4 bg-purple-500/20 rounded-2xl">
                <ExternalLink className="h-10 w-10 text-purple-400 pulse-slow" />
              </div>
            </div>
          </div>
        </div>

        {/* Create Link Button */}
        <div className="mb-8">
          <button
            onClick={() => setShowCreateModal(true)}
            className="flex items-center space-x-3 px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl hover:from-blue-700 hover:to-purple-700 transition-all shadow-2xl btn-hover neon-glow font-semibold text-lg"
          >
            <Plus className="h-6 w-6" />
            <span>Create New Link</span>
          </button>
        </div>

        {/* Links Table */}
        <div className="glass-dark rounded-2xl shadow-2xl overflow-hidden border border-white/10">
          <div className="px-8 py-6 border-b border-white/10 bg-gradient-to-r from-blue-600/20 to-purple-600/20">
            <h2 className="text-2xl font-bold text-white">Your Links</h2>
          </div>
          
          {loading ? (
            <div className="p-8 text-center text-gray-500">Loading...</div>
          ) : links.length === 0 ? (
            <div className="p-8 text-center text-gray-500">
              No links yet. Create your first link!
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Short URL
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Original URL
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Clicks
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Created
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Actions
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {links.map((link) => (
                    <tr key={link.link_id} className="hover:bg-gray-50">
                      <td className="px-6 py-4 whitespace-nowrap">
                        <div className="flex items-center space-x-2">
                          <code className="text-sm font-mono text-blue-600">
                            {link.short_url_slug}
                          </code>
                          <button
                            onClick={() => copyToClipboard(`http://127.0.0.1:5000/${link.short_url_slug}`, link.short_url_slug)}
                            className="text-gray-400 hover:text-gray-600"
                          >
                            {copiedSlug === link.short_url_slug ? (
                              <span className="text-green-600 text-xs">Copied!</span>
                            ) : (
                              <Copy className="h-4 w-4" />
                            )}
                          </button>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <div className="text-sm text-gray-900 truncate max-w-md">
                          {link.long_url}
                        </div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className="text-sm text-gray-900">{link.click_count}</span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {new Date(link.creation_date).toLocaleDateString()}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                        <div className="flex items-center space-x-3">
                          <Link
                            to={`/analytics/${link.short_url_slug}`}
                            className="text-blue-600 hover:text-blue-900 scale-hover transition-all"
                            title="View Analytics"
                          >
                            <BarChart3 className="h-5 w-5" />
                          </Link>
                          <button
                            onClick={() => handleGenerateQR(link.short_url_slug)}
                            className="text-green-600 hover:text-green-900 scale-hover transition-all"
                            title="Generate QR Code"
                          >
                            <QrCode className="h-5 w-5" />
                          </button>
                          <button
                            onClick={() => handleDeleteLink(link.short_url_slug)}
                            className="text-red-600 hover:text-red-900 scale-hover transition-all"
                            title="Delete Link"
                          >
                            <Trash2 className="h-5 w-5" />
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </main>

      {/* Create Link Modal */}
      {showCreateModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50 slide-in-right">
          <div className="bg-white rounded-lg max-w-md w-full p-6 bounce-in">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Create New Link</h3>
            
            <form onSubmit={handleCreateLink} className="space-y-4">
              {error && (
                <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
                  {error}
                </div>
              )}

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Original URL *
                </label>
                <input
                  type="url"
                  required
                  value={longUrl}
                  onChange={(e) => setLongUrl(e.target.value)}
                  placeholder="https://example.com"
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500"
                />
              </div>

              <div>
                <div className="flex items-center justify-between mb-2">
                  <label className="block text-sm font-medium text-gray-700">
                    Short Link
                  </label>
                  <label className="flex items-center cursor-pointer">
                    <input
                      type="checkbox"
                      checked={useCustomSlug}
                      onChange={(e) => {
                        setUseCustomSlug(e.target.checked);
                        if (!e.target.checked) {
                          setCustomSlug('');
                        }
                      }}
                      className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                    />
                    <span className="text-sm text-gray-600">Use custom slug</span>
                  </label>
                </div>
                
                {useCustomSlug ? (
                  <div className="space-y-1">
                    <input
                      type="text"
                      value={customSlug}
                      onChange={(e) => handleCustomSlugChange(e.target.value)}
                      placeholder="my-custom-link"
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500"
                    />
                    <p className="text-xs text-gray-500">
                      Only letters, numbers, hyphens (-), and underscores (_) allowed
                    </p>
                  </div>
                ) : (
                  <div className="w-full px-3 py-2 border border-gray-200 rounded-lg bg-gray-50 text-gray-500 text-sm flex items-center">
                    <svg className="w-4 h-4 mr-2 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    Auto-generated slug will be created
                  </div>
                )}
              </div>

              <div>
                <div className="flex items-center justify-between mb-2">
                  <label className="block text-sm font-medium text-gray-700">
                    Expiration
                  </label>
                  <label className="flex items-center cursor-pointer">
                    <input
                      type="checkbox"
                      checked={useExpiration}
                      onChange={(e) => {
                        setUseExpiration(e.target.checked);
                        if (!e.target.checked) {
                          setExpirationDays('');
                        }
                      }}
                      className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                    />
                    <span className="text-sm text-gray-600">Set expiration date</span>
                  </label>
                </div>
                
                {useExpiration ? (
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <input
                        type="number"
                        min="1"
                        value={expirationDays}
                        onChange={(e) => setExpirationDays(e.target.value ? Number(e.target.value) : '')}
                        placeholder="7"
                        className="w-24 px-3 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500"
                      />
                      <span className="text-sm text-gray-600">days from now</span>
                    </div>
                    {expirationDays && (
                      <p className="text-xs text-gray-500">
                        Link will expire on {new Date(Date.now() + Number(expirationDays) * 24 * 60 * 60 * 1000).toLocaleDateString()}
                      </p>
                    )}
                  </div>
                ) : (
                  <div className="w-full px-3 py-2 border border-gray-200 rounded-lg bg-gray-50 text-gray-500 text-sm flex items-center">
                    <svg className="w-4 h-4 mr-2 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    Link will never expire
                  </div>
                )}
              </div>

              <div className="flex space-x-3 pt-4">
                <button
                  type="button"
                  onClick={() => {
                    setShowCreateModal(false);
                    setError('');
                    setLongUrl('');
                    setCustomSlug('');
                    setUseCustomSlug(false);
                    setExpirationDays('');
                    setUseExpiration(false);
                  }}
                  className="flex-1 px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={creating}
                  className="flex-1 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50"
                >
                  {creating ? 'Creating...' : 'Create'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* QR Code Designer Modal */}
      {showQRModal && selectedLinkForQR && (
        <QRCodeDesigner
          url={`http://127.0.0.1:5000/${selectedLinkForQR}`}
          onClose={() => {
            setShowQRModal(false);
            setSelectedLinkForQR(null);
          }}
        />
      )}
      </div>
    </div>
  );
};

export default Dashboard;
