# Camera Trap IoT System for Wildlife Monitoring

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B-red.svg)](https://www.raspberrypi.org/)

An intelligent IoT-based camera trap system that combines edge computing, computer vision, and IoT technologies to create an automated wildlife monitoring solution. The system uses Raspberry Pi, PIR motion sensors, and YOLOv8 AI for real-time animal and human detection with instant Telegram alerts.

## 🌟 Key Features

- **🎯 Motion Detection**: PIR sensor-based motion detection for power efficiency
- **🤖 AI-Powered Recognition**: YOLOv8 integration for real-time animal and human identification  
- **📱 Remote Monitoring**: Telegram bot integration for instant alerts and image sharing
- **⚡ Energy Efficient**: Smart sleep modes and optimized processing
- **🌧️ Weather Resistant**: Designed for outdoor deployment
- **🔧 Edge Computing**: Local AI processing reduces cloud dependency
- **📊 Comprehensive Logging**: Detailed system monitoring and analytics

## 🎯 Use Cases

- Wildlife research and biodiversity monitoring
- Anti-poaching surveillance systems  
- Conservation photography and documentation
- Property security in remote areas
- Animal behavior research
- Ecological impact studies

## 📸 System Overview

The system operates on an event-driven model:
1. PIR sensor detects motion and wakes up the system
2. Camera captures high-resolution images
3. YOLOv8 AI model processes images for object detection
4. System filters results for target wildlife/humans
5. Relevant detections trigger Telegram alerts with images
6. System returns to low-power sleep mode

## 🛠️ Hardware Requirements

### Essential Components
- **Raspberry Pi 4B** (4GB+ RAM recommended)
- **Pi Camera Module** (v2 or v3)
- **PIR Motion Sensor** (HC-SR501)
- **MicroSD Card** (32GB+ Class 10)
- **Power Supply** (5V 3A) or battery pack
- **Jumper Wires** and breadboard

### Optional Components  
- Weatherproof enclosure (IP65 rated)
- Solar panel for remote deployment
- Status LED indicators
- Temperature/humidity sensors
- GPS module for location tracking

## 🚀 Quick Start

### 1. Hardware Setup
```bash
# Connect PIR sensor to Raspberry Pi
PIR VCC  → Pi Pin 2 (5V)
PIR GND  → Pi Pin 6 (Ground)
PIR OUT  → Pi Pin 7 (GPIO 4)

# Connect camera module to CSI port
```

### 2. Software Installation
```bash
# Clone repository
git clone https://github.com/KumarSatyam24/Camera-Trap-IoT-System-for-Wildlife-Monitoring.git
cd Camera-Trap-IoT-System-for-Wildlife-Monitoring/Camera-Trap-IoT-System-for-Wildlife-Monitoring

# Install dependencies
sudo apt-get update && sudo apt-get install -y python3-pip libcamera-apps
pip3 install -r requirements.txt

# Enable camera interface
sudo raspi-config
# Interface Options → Camera → Enable
```

### 3. Configuration
```bash
# Create environment file
cp .env.example .env

# Edit configuration
nano .env

# Add your Telegram credentials:
TELEGRAM_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### 4. Run System
```bash
# Test run
python3 code.py

# Or use enhanced version with more features
python3 code_enhanced.py

# Run as service (see INSTALLATION.md for details)
sudo systemctl start camera-trap.service
```

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [**DOCUMENTATION.md**](./DOCUMENTATION.md) | Complete system documentation and user guide |

## 🔧 Configuration Options

The system supports extensive customization through environment variables:

```bash
# Detection Settings
PIR_PIN=4                    # GPIO pin for PIR sensor
CONFIDENCE_THRESHOLD=0.6     # YOLO detection confidence
DETECTION_DELAY=2           # Seconds between detections

# Image Settings  
IMAGE_WIDTH=1920            # Capture resolution width
IMAGE_HEIGHT=1080           # Capture resolution height
IMAGE_QUALITY=90            # JPEG quality (1-100)

# Alert Settings
MIN_ALERT_INTERVAL=300      # Minimum seconds between alerts
MAX_DAILY_ALERTS=50         # Maximum alerts per day

# Logging
LOG_LEVEL=INFO              # Logging verbosity
LOG_FILE=camera_trap.log    # Log file location
```

## 🎯 Target Detection

The system can detect and classify the following objects:
- **Humans**: Person detection for security monitoring
- **Large Mammals**: Elephant, horse, cow, bear, zebra
- **Medium Mammals**: Dog, sheep, deer, wolf  
- **Small Mammals**: Cat, fox, rabbit
- **Custom Objects**: Easily configurable for specific species

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Detection Latency | 3-5 seconds |
| Power Consumption | 1.5-2.5W |
| Detection Range | 3-7 meters |
| Battery Life | 8-12 hours (10Ah) |
| Image Resolution | Up to 4K |
| Model Accuracy | >90% (YOLOv8) |

## 🌍 Deployment Examples

### Research Station Monitoring
- Solar-powered remote deployment
- 24/7 wildlife activity logging
- Multi-species biodiversity studies
- Long-term behavioral research

### Anti-Poaching Surveillance  
- Perimeter monitoring systems
- Human detection alerts
- Night vision capabilities
- Network of connected sensors

### Conservation Photography
- Automated wildlife documentation
- Non-invasive monitoring
- High-quality image capture
- Species identification and counting

## 🤝 Contributing

We welcome contributions! Please see our contribution guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip3 install -r requirements-dev.txt

# Run tests
python3 -m pytest tests/

# Format code
black . && flake8 .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Ultralytics** for the YOLOv8 object detection framework
- **Raspberry Pi Foundation** for the amazing hardware platform
- **OpenCV** community for computer vision tools
- **Wildlife conservation organizations** for inspiration and requirements

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/KumarSatyam24/Camera-Trap-IoT-System-for-Wildlife-Monitoring/issues)
- 📧 **Email**: [Contact the maintainer]
- 📖 **Documentation**: Check the docs folder for detailed guides

---

**Made with ❤️ for wildlife conservation**

*Helping protect and monitor wildlife through innovative IoT and AI technology*
