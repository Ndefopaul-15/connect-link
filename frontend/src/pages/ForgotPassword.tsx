import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import toast from 'react-hot-toast';
import { ArrowLeft } from 'lucide-react';
import { authAPI } from '../services/api';
import Logo from '../components/Logo';
import NetworkBackground from '../components/NetworkBackground';

const ForgotPassword: React.FC = () => {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [emailSent, setEmailSent] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      await authAPI.forgotPassword(email);
      
      setEmailSent(true);
      toast.success('Password reset link sent to your email!', {
        duration: 5000,
        style: {
          background: '#10b981',
          color: '#fff',
        },
      });
    } catch (err: any) {
      toast.error(err.response?.data?.error || 'Failed to send reset link');
    } finally {
      setLoading(false);
    }
  };

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
            {emailSent ? 'Check Your Email' : 'Forgot Password?'}
          </h1>
          <p className="text-lg text-gray-300 font-medium">
            {emailSent 
              ? "We've sent you a password reset link" 
              : 'Enter your email to reset your password'}
          </p>
        </div>

        <div className="mt-8 glass-dark backdrop-blur-xl py-10 px-8 shadow-2xl rounded-2xl card-animate border border-white/20">
          {emailSent ? (
            <div className="text-center space-y-6">
              <div className="bg-green-500/20 border border-green-500/30 rounded-xl p-6">
                <svg className="mx-auto h-16 w-16 text-green-400 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                <p className="text-white text-lg font-semibold mb-2">Email Sent!</p>
                <p className="text-gray-300 text-sm">
                  We've sent a password reset link to <span className="font-bold text-blue-400">{email}</span>
                </p>
              </div>

              <div className="text-sm text-gray-300 space-y-2">
                <p>• Check your inbox and spam folder</p>
                <p>• Click the link in the email to reset your password</p>
                <p>• The link will expire in 1 hour</p>
              </div>

              <div className="pt-4">
                <button
                  onClick={() => setEmailSent(false)}
                  className="text-blue-400 hover:text-blue-300 font-semibold transition-colors"
                >
                  Didn't receive the email? Try again
                </button>
              </div>
            </div>
          ) : (
            <form className="space-y-6" onSubmit={handleSubmit}>
              <div>
                <label htmlFor="email" className="block text-sm font-semibold text-gray-200 mb-2 uppercase tracking-wide">
                  Email address
                </label>
                <input
                  id="email"
                  name="email"
                  type="email"
                  autoComplete="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="mt-1 appearance-none block w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent backdrop-blur-sm transition-all"
                  placeholder="you@example.com"
                />
              </div>

              <div className="pt-2">
                <button
                  type="submit"
                  disabled={loading}
                  className="w-full flex justify-center py-4 px-6 border border-transparent rounded-xl text-lg font-bold text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 transition-all btn-hover neon-glow shadow-2xl"
                >
                  {loading ? 'Sending...' : 'Send Reset Link'}
                </button>
              </div>
            </form>
          )}

          <div className="text-center pt-6 mt-6 border-t border-white/10">
            <Link 
              to="/login" 
              className="flex items-center justify-center space-x-2 text-gray-300 hover:text-white transition-colors font-medium"
            >
              <ArrowLeft className="h-4 w-4" />
              <span>Back to Login</span>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ForgotPassword;
