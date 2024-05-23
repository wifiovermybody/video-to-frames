import ffmpeg
import os
import sys

def get_output_directory(base_dir, base_name):
    """
    Get the next available output directory name.

    :param base_dir: The directory where the video is stored.
    :param base_name: The base name of the video file.
    :return: The path to the next available output directory.
    """
    counter = 1
    output_dir = os.path.join(base_dir, f'{base_name}_outputframes')
    while os.path.exists(output_dir):
        output_dir = os.path.join(base_dir, f'{base_name}_{counter}_outputframes')
        counter += 1
    return output_dir

def extract_frames(video_path):
    """
    Extract every frame from a video file.

    :param video_path: Path to the video file.
    """
    if not os.path.exists(video_path):
        print(f"Error: The video file '{video_path}' does not exist.")
        sys.exit(1)

    # Get the video file name without extension and the directory it is stored in
    video_dir = os.path.dirname(video_path)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Get the next available output directory
    output_dir = get_output_directory(video_dir, video_name)
    output_pattern = os.path.join(output_dir, 'frame_%04d.png')

    # Create the output directory
    os.makedirs(output_dir)

    # Use ffmpeg to extract frames
    try:
        (
            ffmpeg
            .input(video_path)
            .output(output_pattern, start_number=0)
            .run(capture_stdout=True, capture_stderr=True)
        )
        print(f"Frames extracted to '{output_dir}' successfully.")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode('utf8')}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_video_file>")
        sys.exit(1)

    video_path = sys.argv[1]

    extract_frames(video_path)
