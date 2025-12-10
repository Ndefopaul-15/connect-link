import React from 'react';

interface LogoProps {
  className?: string;
  showText?: boolean;
}

const Logo: React.FC<LogoProps> = () => {
  return (
    <div className="flex flex-col">
      <span className="text-3xl font-black tracking-tight leading-none text-white"
            style={{ 
              fontFamily: 'system-ui, -apple-system, sans-serif',
              letterSpacing: '-0.02em',
              textShadow: '0 2px 10px rgba(0, 0, 0, 0.3)'
            }}>
        Connect
      </span>
      <span className="text-3xl font-black tracking-tight leading-none text-white -mt-1"
            style={{ 
              fontFamily: 'system-ui, -apple-system, sans-serif',
              letterSpacing: '-0.02em',
              textShadow: '0 2px 10px rgba(0, 0, 0, 0.3)'
            }}>
        Link
      </span>
    </div>
  );
};

export default Logo;
