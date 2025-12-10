import React, { useState, useRef } from 'react';
import { QRCodeSVG } from 'qrcode.react';
import html2canvas from 'html2canvas';
import { Download, Palette, Image as ImageIcon, X } from 'lucide-react';

interface QRCodeDesignerProps {
  url: string;
  onClose: () => void;
}

interface QRStyle {
  name: string;
  fgColor: string;
  bgColor: string;
  level: 'L' | 'M' | 'Q' | 'H';
  style?: string;
}

const QR_TEMPLATES: QRStyle[] = [
  { name: 'Classic', fgColor: '#000000', bgColor: '#FFFFFF', level: 'M' },
  { name: 'Ocean Blue', fgColor: '#0891B2', bgColor: '#E0F2FE', level: 'M' },
  { name: 'Purple Dream', fgColor: '#7C3AED', bgColor: '#F3E8FF', level: 'M' },
  { name: 'Sunset', fgColor: '#DC2626', bgColor: '#FEF2F2', level: 'M' },
  { name: 'Forest', fgColor: '#059669', bgColor: '#D1FAE5', level: 'M' },
  { name: 'Midnight', fgColor: '#1E293B', bgColor: '#F1F5F9', level: 'H' },
  { name: 'Neon Pink', fgColor: '#EC4899', bgColor: '#FCE7F3', level: 'M' },
  { name: 'Gold', fgColor: '#D97706', bgColor: '#FEF3C7', level: 'M' },
];

const QRCodeDesigner: React.FC<QRCodeDesignerProps> = ({ url, onClose }) => {
  const [selectedTemplate, setSelectedTemplate] = useState<QRStyle>(QR_TEMPLATES[0]);
  const [customFgColor, setCustomFgColor] = useState('#000000');
  const [customBgColor, setCustomBgColor] = useState('#FFFFFF');
  const [size, setSize] = useState(300);
  const [useCustomColors, setUseCustomColors] = useState(false);
  const qrRef = useRef<HTMLDivElement>(null);

  const currentStyle = useCustomColors
    ? { ...selectedTemplate, fgColor: customFgColor, bgColor: customBgColor }
    : selectedTemplate;

  const downloadQR = async (format: 'png' | 'svg') => {
    if (!qrRef.current) return;

    if (format === 'svg') {
      const svgElement = qrRef.current.querySelector('svg');
      if (!svgElement) return;

      const svgData = new XMLSerializer().serializeToString(svgElement);
      const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
      const svgUrl = URL.createObjectURL(svgBlob);
      const downloadLink = document.createElement('a');
      downloadLink.href = svgUrl;
      downloadLink.download = `qrcode-${Date.now()}.svg`;
      document.body.appendChild(downloadLink);
      downloadLink.click();
      document.body.removeChild(downloadLink);
      URL.revokeObjectURL(svgUrl);
    } else {
      const canvas = await html2canvas(qrRef.current, {
        backgroundColor: currentStyle.bgColor,
        scale: 2,
      });
      const pngUrl = canvas.toDataURL('image/png');
      const downloadLink = document.createElement('a');
      downloadLink.href = pngUrl;
      downloadLink.download = `qrcode-${Date.now()}.png`;
      document.body.appendChild(downloadLink);
      downloadLink.click();
      document.body.removeChild(downloadLink);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-gray-200">
          <div>
            <h2 className="text-2xl font-bold text-gray-900">QR Code Designer</h2>
            <p className="text-sm text-gray-500 mt-1">Customize and download your QR code</p>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <X className="h-6 w-6 text-gray-500" />
          </button>
        </div>

        <div className="p-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {/* Left: Preview */}
            <div className="space-y-6">
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
                  <ImageIcon className="h-5 w-5" />
                  Preview
                </h3>
                <div
                  ref={qrRef}
                  className="flex items-center justify-center p-8 rounded-xl border-2 border-gray-200"
                  style={{ backgroundColor: currentStyle.bgColor }}
                >
                  <QRCodeSVG
                    value={url}
                    size={size}
                    fgColor={currentStyle.fgColor}
                    bgColor={currentStyle.bgColor}
                    level={currentStyle.level}
                    includeMargin={true}
                  />
                </div>
              </div>

              {/* Download Buttons */}
              <div className="space-y-3">
                <button
                  onClick={() => downloadQR('png')}
                  className="w-full flex items-center justify-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl font-semibold hover:from-blue-700 hover:to-purple-700 transition-all shadow-lg"
                >
                  <Download className="h-5 w-5" />
                  Download PNG
                </button>
                <button
                  onClick={() => downloadQR('svg')}
                  className="w-full flex items-center justify-center gap-2 px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-xl font-semibold hover:from-purple-700 hover:to-pink-700 transition-all shadow-lg"
                >
                  <Download className="h-5 w-5" />
                  Download SVG
                </button>
              </div>
            </div>

            {/* Right: Customization */}
            <div className="space-y-6">
              {/* Templates */}
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
                  <Palette className="h-5 w-5" />
                  Templates
                </h3>
                <div className="grid grid-cols-2 gap-3">
                  {QR_TEMPLATES.map((template) => (
                    <button
                      key={template.name}
                      onClick={() => {
                        setSelectedTemplate(template);
                        setUseCustomColors(false);
                      }}
                      className={`p-4 rounded-xl border-2 transition-all ${
                        selectedTemplate.name === template.name && !useCustomColors
                          ? 'border-blue-500 bg-blue-50'
                          : 'border-gray-200 hover:border-gray-300'
                      }`}
                    >
                      <div className="flex items-center gap-3">
                        <div
                          className="w-12 h-12 rounded-lg border-2"
                          style={{
                            backgroundColor: template.bgColor,
                            borderColor: template.fgColor,
                          }}
                        />
                        <span className="text-sm font-medium text-gray-900">
                          {template.name}
                        </span>
                      </div>
                    </button>
                  ))}
                </div>
              </div>

              {/* Custom Colors */}
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4">Custom Colors</h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Foreground Color
                    </label>
                    <div className="flex gap-3">
                      <input
                        type="color"
                        value={customFgColor}
                        onChange={(e) => {
                          setCustomFgColor(e.target.value);
                          setUseCustomColors(true);
                        }}
                        className="h-12 w-20 rounded-lg border-2 border-gray-300 cursor-pointer"
                      />
                      <input
                        type="text"
                        value={customFgColor}
                        onChange={(e) => {
                          setCustomFgColor(e.target.value);
                          setUseCustomColors(true);
                        }}
                        className="flex-1 px-4 py-2 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none"
                        placeholder="#000000"
                      />
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Background Color
                    </label>
                    <div className="flex gap-3">
                      <input
                        type="color"
                        value={customBgColor}
                        onChange={(e) => {
                          setCustomBgColor(e.target.value);
                          setUseCustomColors(true);
                        }}
                        className="h-12 w-20 rounded-lg border-2 border-gray-300 cursor-pointer"
                      />
                      <input
                        type="text"
                        value={customBgColor}
                        onChange={(e) => {
                          setCustomBgColor(e.target.value);
                          setUseCustomColors(true);
                        }}
                        className="flex-1 px-4 py-2 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none"
                        placeholder="#FFFFFF"
                      />
                    </div>
                  </div>
                </div>
              </div>

              {/* Size */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Size: {size}px
                </label>
                <input
                  type="range"
                  min="200"
                  max="500"
                  step="50"
                  value={size}
                  onChange={(e) => setSize(Number(e.target.value))}
                  className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
                />
                <div className="flex justify-between text-xs text-gray-500 mt-1">
                  <span>200px</span>
                  <span>500px</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QRCodeDesigner;
