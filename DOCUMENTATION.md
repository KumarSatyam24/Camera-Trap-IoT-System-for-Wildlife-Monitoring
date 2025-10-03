# Camera Trap IoT System for Wildlife Monitoring - Complete Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Hardware Requirements](#hardware-requirements)
4. [Software Dependencies](#software-dependencies)
5. [Installation Guide](#installation-guide)
6. [Configuration](#configuration)
7. [Usage](#usage)
8. [Code Documentation](#code-documentation)
9. [Troubleshooting](#troubleshooting)
10. [Performance Optimization](#performance-optimization)
11. [Security Considerations](#security-considerations)
12. [Future Enhancements](#future-enhancements)
13. [Contributing](#contributing)
14. [License](#license)

## Project Overview

The Camera Trap IoT System is an intelligent wildlife monitoring solution that combines edge computing, computer vision, and IoT technologies to create an automated surveillance system for wildlife research and conservation efforts.

### Key Features
- **Motion Detection**: PIR sensor-based motion detection for power efficiency
- **AI-Powered Object Recognition**: YOLOv8 integration for real-time animal and human detection
- **Remote Monitoring**: Telegram bot integration for instant alerts and image sharing
- **Energy Efficient**: Sleep mode between detections to conserve battery
- **Weatherproof Design**: Suitable for outdoor deployment
- **Edge Computing**: Local processing reduces dependency on internet connectivity

### Use Cases
- Wildlife research and monitoring
- Anti-poaching surveillance
- Biodiversity studies
- Property security in rural areas
- Conservation photography
- Animal behavior research

## System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   PIR Sensor    │────│  Raspberry Pi    │────│   Camera Module │
│  (Motion Det.)  │    │   (Main Unit)    │    │  (Image Capture)│
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              │
                    ┌──────────────────┐
                    │   YOLOv8 Model   │
                    │ (Object Detection)│
                    └──────────────────┘
                              │
                              │
                    ┌──────────────────┐
                    │  Telegram Bot    │
                    │ (Alert System)   │
                    └──────────────────┘
```

### Data Flow
1. PIR sensor detects motion
2. System wakes up and captures image using camera
3. YOLOv8 processes image for object detection
4. System filters detected objects for relevant wildlife/humans
5. If relevant objects found, sends alert via Telegram
6. System returns to sleep mode

## Hardware Requirements

### Essential Components
| Component | Specification | Purpose |
|-----------|---------------|---------|
| Raspberry Pi | Pi 4B (4GB+ recommended) | Main processing unit |
| Camera Module | Pi Camera v2 or v3 | Image capture |
| PIR Sensor | HC-SR501 or similar | Motion detection |
| MicroSD Card | 32GB Class 10+ | Storage |
| Power Supply | 5V 3A or battery pack | Power |

### Optional Components
- **Weatherproof Case**: IP65 rated enclosure
- **Solar Panel**: For remote deployment
- **External Storage**: USB drive for local image storage
- **LED Indicators**: Status indication
- **Temperature Sensor**: Environmental monitoring

### Wiring Diagram
```
PIR Sensor:
  VCC  -> 5V (Pin 2)
  GND  -> Ground (Pin 6)
  OUT  -> GPIO 4 (Pin 7)

Camera Module:
  Connect via CSI port on Raspberry Pi

Optional LED:
  Anode -> GPIO 18 (Pin 12)
  Cathode -> Ground via 220Ω resistor
```

## Software Dependencies

### System Requirements
- Raspberry Pi OS (Bullseye or later)
- Python 3.8+
- Minimum 2GB free space

### Python Libraries
```bash
# Core libraries
opencv-python>=4.5.0
torch>=1.11.0
torchvision>=0.12.0
ultralytics>=8.0.0
telepot>=12.7
RPi.GPIO>=0.7.0

# Additional utilities
Pillow>=8.0.0
numpy>=1.21.0
```

### System Packages
```bash
# Camera support
sudo apt-get install python3-picamera2
sudo apt-get install libcamera-apps

# OpenCV dependencies
sudo apt-get install libopencv-dev
sudo apt-get install python3-opencv
```

## Installation Guide

### Step 1: System Preparation
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Enable camera interface
sudo raspi-config
# Navigate to: Interface Options > Camera > Enable

# Reboot
sudo reboot
```

### Step 2: Install Dependencies
```bash
# Install Python package manager
sudo apt-get install python3-pip

# Install system packages
sudo apt-get install python3-opencv libopencv-dev
sudo apt-get install libcamera-apps python3-picamera2

# Install Python libraries
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip3 install ultralytics telepot RPi.GPIO opencv-python Pillow numpy
```

### Step 3: Download Project
```bash
# Clone repository
git clone https://github.com/KumarSatyam24/Camera-Trap-IoT-System-for-Wildlife-Monitoring.git
cd Camera-Trap-IoT-System-for-Wildlife-Monitoring

# Make script executable
chmod +x code.py
```

### Step 4: Hardware Setup
1. Connect PIR sensor to GPIO 4
2. Attach camera module to CSI port
3. Secure all connections
4. Test hardware with basic scripts

## Configuration

### Telegram Bot Setup
1. **Create Bot**:
   - Message @BotFather on Telegram
   - Use `/newbot` command
   - Save the bot token

2. **Get Chat ID**:
   - Message your bot
   - Visit: `https://api.telegram.org/bot<TOKEN>/getUpdates`
   - Find your chat ID in the response

3. **Update Configuration**:
   ```python
   TOKEN = "your_bot_token_here"
   CHAT_ID = "your_chat_id_here"
   ```

### System Configuration Options

```python
# PIR Sensor Configuration
PIR_PIN = 4              # GPIO pin for PIR sensor
DETECTION_DELAY = 2      # Seconds between detections

# Camera Configuration
IMAGE_RESOLUTION = (1920, 1080)  # Image resolution
IMAGE_QUALITY = 90       # JPEG quality (1-100)

# Detection Configuration
CONFIDENCE_THRESHOLD = 0.5  # YOLO confidence threshold
TARGET_OBJECTS = [          # Objects to detect
    "person", "dog", "cat", "cow", "horse", 
    "sheep", "elephant", "bear", "zebra"
]

# Power Management
SLEEP_DURATION = 30      # Sleep between checks (seconds)
MAX_DAILY_ALERTS = 50    # Limit alerts per day
```

## Usage

### Basic Operation
```bash
# Start the system
python3 code.py

# Run in background
nohup python3 code.py &

# Check if running
ps aux | grep python3
```

### Advanced Usage

#### Scheduled Operation
Create a cron job for automated start:
```bash
# Edit crontab
crontab -e

# Add entry (start at boot)
@reboot /usr/bin/python3 /path/to/code.py

# Or scheduled operation (6 AM to 10 PM)
0 6 * * * /usr/bin/python3 /path/to/code.py
0 22 * * * pkill -f code.py
```

#### Service Configuration
Create systemd service for better management:
```bash
# Create service file
sudo nano /etc/systemd/system/camera-trap.service
```

Service file content:
```ini
[Unit]
Description=Camera Trap Wildlife Monitoring
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/Camera-Trap-IoT-System-for-Wildlife-Monitoring
ExecStart=/usr/bin/python3 /home/pi/Camera-Trap-IoT-System-for-Wildlife-Monitoring/code.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable camera-trap.service
sudo systemctl start camera-trap.service
```

## Code Documentation

### Main Functions

#### `capture_image()`
Captures image using libcamera and returns file path.

**Returns**: `str` - Path to captured image file

**Example Usage**:
```python
image_path = capture_image()
print(f"Image saved to: {image_path}")
```

#### `send_telegram_alert(image_path, detected_objects)`
Sends alert message and image to Telegram.

**Parameters**:
- `image_path` (str): Path to image file
- `detected_objects` (list): List of detected object names

**Example Usage**:
```python
objects = ["person", "dog"]
send_telegram_alert("image.jpg", objects)
```

### Code Flow Analysis

1. **Initialization Phase**:
   - GPIO setup for PIR sensor
   - Telegram bot initialization
   - YOLO model loading

2. **Detection Loop**:
   - Monitor PIR sensor state
   - Trigger on motion detection
   - Capture and process image
   - Send alerts if targets detected

3. **Cleanup Phase**:
   - GPIO cleanup on exit
   - Graceful shutdown handling

### Error Handling

The system includes basic error handling for:
- Camera initialization failures
- Network connectivity issues
- File I/O errors
- GPIO access problems

## Troubleshooting

### Common Issues

#### Camera Not Working
```bash
# Check camera connection
vcgencmd get_camera

# Test camera
libcamera-still -o test.jpg --nopreview

# Enable legacy camera support if needed
sudo raspi-config > Advanced Options > Camera
```

#### PIR Sensor Issues
```bash
# Test GPIO
gpio readall

# Check wiring
# Ensure proper power supply (5V)
# Verify ground connection
```

#### YOLO Model Loading Issues
```bash
# Check disk space
df -h

# Reinstall ultralytics
pip3 uninstall ultralytics
pip3 install ultralytics

# Download model manually
python3 -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

#### Telegram Connection Issues
```bash
# Test bot token
curl https://api.telegram.org/bot<TOKEN>/getMe

# Check internet connectivity
ping telegram.org

# Verify firewall settings
sudo ufw status
```

### Performance Issues

#### Slow Detection
- Use smaller YOLO model (yolov8n.pt)
- Reduce image resolution
- Increase detection delay
- Consider hardware acceleration

#### High Power Consumption
- Optimize sleep intervals
- Use hardware power management
- Implement battery monitoring
- Consider solar charging

## Performance Optimization

### Hardware Optimization
- **Enable GPU**: Use GPU acceleration for YOLO
- **Overclock**: Safely overclock Pi for better performance
- **Cooling**: Ensure adequate cooling for sustained operation
- **Storage**: Use fast SD card (Class 10+)

### Software Optimization
```python
# Optimize YOLO settings
model = YOLO("yolov8n.pt")
model.overrides['conf'] = 0.6  # Higher confidence threshold
model.overrides['imgsz'] = 640  # Smaller input size

# Memory management
import gc
gc.collect()  # Force garbage collection after processing

# Batch processing for multiple images
results = model(image_list)  # Process multiple images at once
```

### Network Optimization
- Compress images before sending
- Implement retry logic for failed transmissions
- Cache alerts during network outages
- Use webhook instead of polling for Telegram

## Security Considerations

### Data Protection
- **Encryption**: Encrypt stored images
- **Access Control**: Secure SSH access to Pi
- **Token Security**: Protect Telegram bot tokens
- **Network Security**: Use VPN for remote access

### Privacy Compliance
- **Data Retention**: Implement automatic deletion of old images
- **Anonymization**: Blur human faces if required
- **Consent**: Ensure proper signage for monitored areas
- **Compliance**: Follow local wildlife monitoring regulations

### Implementation Example
```python
# Secure token storage
import os
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Image encryption
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_image(image_path):
    with open(image_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    return encrypted_data
```

## Future Enhancements

### Planned Features
1. **Machine Learning Improvements**:
   - Custom trained models for specific wildlife
   - Behavior analysis capabilities
   - Species identification enhancement

2. **Hardware Additions**:
   - Night vision capability
   - Weather station integration
   - GPS tracking for mobile deployment

3. **Software Features**:
   - Web dashboard for monitoring
   - Database integration for data analysis
   - Mobile app development
   - Cloud storage integration

4. **Advanced Analytics**:
   - Animal counting algorithms
   - Movement pattern analysis
   - Biodiversity metrics
   - Time-lapse generation

### Implementation Roadmap
- **Phase 1**: Basic functionality (completed)
- **Phase 2**: Enhanced detection and web interface
- **Phase 3**: Advanced analytics and mobile app
- **Phase 4**: Multi-device network and cloud integration

## Contributing

### Development Setup
```bash
# Fork the repository
git fork https://github.com/KumarSatyam24/Camera-Trap-IoT-System-for-Wildlife-Monitoring.git

# Create development branch
git checkout -b feature/new-feature

# Install development dependencies
pip3 install -r requirements-dev.txt
```

### Code Style Guidelines
- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings for functions
- Include type hints where appropriate
- Write unit tests for new features

### Contribution Process
1. Create feature branch
2. Implement changes
3. Add tests
4. Update documentation
5. Submit pull request

## License

This project is licensed under the MIT License. See LICENSE file for details.

### Third-Party Licenses
- **YOLOv8**: AGPL-3.0 License
- **OpenCV**: Apache 2.0 License
- **PyTorch**: BSD 3-Clause License
- **Telepot**: MIT License

## Support and Contact

For support, questions, or contributions:
- **GitHub Issues**: Use for bug reports and feature requests
- **Email**: [Contact the maintainer]
- **Documentation**: Keep this file updated with changes
- **Community**: Join discussions in the repository

---

**Last Updated**: October 2025
**Version**: 1.0.0
**Maintainer**: KumarSatyam24