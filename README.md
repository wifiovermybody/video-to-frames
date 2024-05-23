
A simple and efficient Python script to extract frames from a video file using `ffmpeg`.

## Prerequisites

- **ffmpeg**: Make sure `ffmpeg` is installed on your system. You can check if it’s installed by running `ffmpeg -version` in the terminal. If it's not installed, download it from [here](https://ffmpeg.org/download.html).
- **ffmpeg-python**: Install the `ffmpeg-python` library:
  ```bash

  pip install ffmpeg-python

Usage
Save the script below to a file, for example, extract_frames.py.

Make the script executable (optional but recommended on Unix-like systems):

bash
Copy code
chmod +x extract_frames.py
Run the script: Open a terminal, type python3 (including the space), then drag your video file into the terminal to add its path automatically. Press Enter to run the script:

bash
Copy code
python3 /path/to/extract_frames.py /path/to/your/video.mp4
