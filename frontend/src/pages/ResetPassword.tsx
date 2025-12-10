import React, { useState } from 'react';
import { useNavigate, useSearchParams, Link } from 'react-router-dom';
import toast from 'react-hot-toast';
import { Eye, EyeOff, CheckCircle } from 'lucide-react';
import { authAPI } from '../services/api';
import Logo from '../components/Logo';
import NetworkBackground from '../components/NetworkBackground';

const ResetPassword: React.FC = () => {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const token = searchParams.get('token');

  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (password !== confirmPassword) {
      setError('Passwords do not match');
      toast.error('Passwords do not match');
      return;
    }

    if (password.length < 6) {
      setError('Password must be at least 6 characters');
      toast.error('Password must be at least 6 characters');
      return;
    }

    if (!token) {
      setError('Invalid reset token');
      toast.error('Invalid reset token');
      return;
    }

    setLoading(true);

    try {
      await authAPI.resetPassword(token, password);
      
      setSuccess(true);
      toast.success('🎉 Password reset successful!', {
        duration: 5000,
        style: {
          background: '#10b981',
          color: '#fff',
        },
      });

      // Redirect to login after 3 seconds
      setTimeout(() => {
        navigate('/login');
      }, 3000);
    } catch (err: any) {
      const errorMsg = err.response?.data?.error || 'Failed to reset password';
      setError(errorMsg);
      toast.error(errorMsg);
    } finally {
      setLoading(false);
    }
  };

  if (!token) {
    return (
      <div className="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8" style={{ 
        background: 'linear-gradient(135deg, #0a1929 0%, #0f2337 50%, #1a3a52 100%)', 
        position: 'relative' 
      }}>
        <NetworkBackground />
        <div className="max-w-md w-full text-center" style={{ position: 'relative', zIndex: 10 }}>
          <div className="glass-dark backdrop-blur-xl py-10 px-8 shadow-2xl rounded-2xl border border-white/20">
            <h2 className="text-2xl font-bold text-white mb-4">Invalid Reset Link</h2>
            <p className="text-gray-300 mb-6">This password reset link is invalid or has expired.</p>
            <Link 
              to="/forgot-password"
              className="inline-block px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl font-semibold hover:from-blue-700 hover:to-purple-700 transition-all"
            >
              Request New Link
            </Link>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8" style={{ 
      background: 'linear-gradient(135deg, #0a1929 0%, #0f2337 50%, #1a3a52 100%)', 
      position: 'relative' 
    }}>
      <NetworkBackground />
      <div className="max-w-md w-full space-y-8" style={{ position: 'relative', zIndex: 10 }}>
        <div className="text-center">
          <div className="flex justify-center bounce-in">
            <Logo className="h-40 w-40 drop-shadow-2xl" />
          </div>
          <h1 className="mt-6 text-4xl font-bold text-white mb-2">
            {success ? 'Password Reset!' : 'Reset Password'}
          </h1>
          <p className="text-lg text-gray-300 font-medium">
            {success ? 'Your password has been updated' : 'Enter your new password'}
          </p>
        </div>

        <div className="mt-8 glass-dark backdrop-blur-xl py-10 px-8 shadow-2xl rounded-2xl card-animate border border-white/20">
          {success ? (
            <div className="text-center space-y-6">
              <div className="bg-green-500/20 border border-green-500/30 rounded-xl p-8">
                <CheckCircle className="mx-auto h-20 w-20 text-green-400 mb-4" />
                <p className="text-white text-xl font-bold mb-2">Success!</p>
                <p className="text-gray-300">
                  Your password has been reset successfully.
                </p>
              </div>

              <p className="text-sm text-gray-400">
                Redirecting to login page...
              </p>

              <Link
                to="/login"
                className="inline-block px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl font-semibold hover:from-blue-700 hover:to-purple-700 transition-all btn-hover neon-glow"
              >
                Go to Login
              </Link>
            </div>
          ) : (
            <form className="space-y-6" onSubmit={handleSubmit}>
              {error && (
                <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg shake">
                  {error}
                </div>
              )}

              <div>
                <label htmlFor="password" className="block text-sm font-semibold text-gray-200 mb-2 uppercase tracking-wide">
                  New Password
                </label>
                <div className="relative">
                  <input
                    id="password"
                    name="password"
                    type={showPassword ? "text" : "password"}
                    autoComplete="new-password"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="mt-1 appearance-none block w-full px-4 py-3 pr-12 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent backdrop-blur-sm transition-all"
                    placeholder="••••••••"
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-white transition-colors"
                  >
                    {showPassword ? <EyeOff className="h-5 w-5" /> : <Eye className="h-5 w-5" />}
                  </button>
                </div>
                <p className="mt-2 text-xs text-gray-400">Must be at least 6 characters</p>
              </div>

              <div>
                <label htmlFor="confirmPassword" className="block text-sm font-semibold text-gray-200 mb-2 uppercase tracking-wide">
                  Confirm New Password
                </label>
                <div className="relative">
                  <input
                    id="confirmPassword"
                    name="confirmPassword"
                    type={showConfirmPassword ? "text" : "password"}
                    autoComplete="new-password"
                    required
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    className="mt-1 appearance-none block w-full px-4 py-3 pr-12 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent backdrop-blur-sm transition-all"
                    placeholder="••••••••"
                  />
                  <button
                    type="button"
                    onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                    className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-white transition-colors"
                  >
                    {showConfirmPassword ? <EyeOff className="h-5 w-5" /> : <Eye className="h-5 w-5" />}
                  </button>
                </div>
              </div>

              <div className="pt-2">
                <button
                  type="submit"
                  disabled={loading}
                  className="w-full flex justify-center py-4 px-6 border border-transparent rounded-xl text-lg font-bold text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 transition-all btn-hover neon-glow shadow-2xl"
                >
                  {loading ? 'Resetting...' : 'Reset Password'}
                </button>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};

export default ResetPassword;
