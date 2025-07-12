import os
import time
import cv2
import torch
import telepot
import RPi.GPIO as GPIO
from datetime import datetime
from ultralytics import YOLO


# PIR Sensor Setup
PIR_PIN = 4 # Updated to GPIO 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)


# Telegram Setup
TOKEN = "YOUR_TELEGRAM"
CHAT_ID = "YOUR_CHAT_ID"
# Replace with your actual Telegram bot token and chat ID
bot = telepot.Bot(TOKEN)


# Load YOLOv8 model
model = YOLO("yolov8n.pt") # Using a small, fast model
# Function to send a Telegram alert


def send_telegram_alert(image_path, detected_objects):
    message = f"Detected: {', '.join(detected_objects)}"
    bot.sendMessage(CHAT_ID, message)
    bot.sendPhoto(CHAT_ID, open(image_path, "rb"))
# Function to capture image using libcamera
def capture_image():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = f"detected_{timestamp}.jpg"
    os.system(f"libcamera-still -o {image_path} --nopreview")
    return image_path


# Main loop
print("Waiting for motion...")
while True:
    if GPIO.input(PIR_PIN): # Motion detected
        print("Motion detected! Capturing image...")
        image_path = capture_image()
        
        # Run YOLO detection
        results = model(image_path)
        detected_objects = [model.names[int(obj)] for obj in results[0].boxes.cls]
        # Filter for animals and humans
        relevant_objects = [obj for obj in detected_objects if obj in ["person","dog", "cat", "cow", "horse", "sheep", "elephant"]]
        if relevant_objects:
            print(f"Detected: {', '.join(relevant_objects)}")
            send_telegram_alert(image_path, relevant_objects)
        else:
            print("No relevant object detected.")
        time.sleep(2) # Avoid rapid triggering
GPIO.cleanup()