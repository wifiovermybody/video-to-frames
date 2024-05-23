## @wifiovermybody Script Collection

![Eye](https://github.com/wifiovermybody/video-to-frames/blob/main/eye.gif)
![Files](https://github.com/wifiovermybody/video-to-frames/blob/main/files.png)


## Video to Frames

A simple and efficient Python script to extract frames from a video file using `ffmpeg`. 
I've made this so it simply creates a folder next to your video file. Super simple and easy, hopefully easier than opening something like Premiere or Resolve.

## Prerequisites

- **ffmpeg-python**: Install the `ffmpeg-python` library:
  ```bash

  pip install ffmpeg-python

## Usage
Save the script below to a file, for example, extract_frames.py.

Make the script executable (optional but recommended on Unix-like systems):

  ```bash
chmod +x extract_frames.py

```
To run the script:
Open a terminal (eg. osx terminal), type python3 (including the space), drag your script in, then drag your video file into the terminal to add their paths in automatically. Press Enter to run the script. It should look something like below:

```bash

python3 /path/to/extract_frames.py /path/to/your/video.mp4

```

## Notes
A metadata file is created next to the file to show the fps and duration of clip

## Pro tips for OS X
You can get the file path quickly and easily by right clicking on an file and holding the `option ⌥` key. Where `copy` is usuaully is displayed, will now display an option to `copy <filename> as pathname`


 
