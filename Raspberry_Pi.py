import os      # To execute Linux camera commands
import time    # To add delays

# Indicate that the camera payload software has started
print("Rocket camera payload started...")

# Delay after power-on / launch (in seconds)
time.sleep(5)

# Video Recording
# Record a video for 10 seconds
# -t 10000 : duration in milliseconds (10 seconds)
# -o       : output video file name
os.system("libcamera-vid -t 10000 -o flight_video.h264")

print("Video recording completed.")

# Short delay before capturing image
time.sleep(2)

# Image Capture
# Capture a high-resolution image
# -o : output image file name
# --width and --height : image resolution
os.system("libcamera-still -o apogee_image.jpg --width 1920 --height 1080")

print("Image captured successfully.")

# End of payload operation
print("Camera payload mission completed.")
