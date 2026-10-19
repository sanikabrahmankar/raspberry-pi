# Raspberry Pi Rocket Camera Payload

A lightweight Python script for Raspberry Pi designed to automatically record flight video and capture a high-resolution image during a rocket launch mission using the standard `libcamera` utilities.

## Features

 Power-On/Launch Delay: Includes an initial startup delay (`time.sleep(5)`) to allow system stability after power-on.
 Automated Video Recording: Uses `libcamera-vid` to capture a 10-second high-definition video segment (`flight_video.h264`).
 High-Resolution Image Capture: Uses `libcamera-still` to take a snapshot image (`apogee_image.jpg`) at 1920x1080 resolution.
 Autonomous Execution: Designed to run headless on a Raspberry Pi camera payload board without user intervention during flight.

## Prerequisites & Hardware Requirements

 Raspberry Pi (Model 3, 4, 5, or Zero W/2W) running Raspberry Pi OS (Bullseye or newer).
 Raspberry Pi Camera Module (v1, v2, v3, or HQ Camera) connected via CSI ribbon cable.
 libcamera tools installed (pre-installed on official Raspberry Pi OS images).

## Usage

1. Clone or copy the script onto your Raspberry Pi:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
   cd YOUR-REPO-NAME