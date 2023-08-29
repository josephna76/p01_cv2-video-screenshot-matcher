import cv2
import os


def match_screenshot_to_video(screenshot_path, video_path):
    print(f"Matching {screenshot_path} with {video_path}")

    screenshot = cv2.imread(screenshot_path, cv2.IMREAD_COLOR)

    if screenshot is None:
        print(f"Warning: Unable to load screenshot: {screenshot_path}")
        return False

    vid_cap = cv2.VideoCapture(video_path)
    if not vid_cap.isOpened():
        print(f"Warning: Unable to open video: {video_path}")
        return False

    frame_count = 0
    while True:
        ret, frame = vid_cap.read()
        if not ret:
            print(f"Finished processing all frames of {video_path}")
            break

        frame_count += 1
        if frame_count % 100 == 0:  # Print every 100 frames for progress tracking
            print(f"Processed {frame_count} frames in {video_path}")

        res = cv2.matchTemplate(frame, screenshot, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        if max_val > 0.95:
            print(f"Match found in {video_path} for {screenshot_path}")
            return True

    print(f"No match found in {video_path} for {screenshot_path}")
    return False


video_directory = "./videos/"
photo_directory = "./photos/"

videos = [os.path.join(video_directory, video) for video in os.listdir(video_directory)]
screenshots = [
    os.path.join(photo_directory, photo) for photo in os.listdir(photo_directory)
]

with open("matches.txt", "w") as f:
    for screenshot in screenshots:
        print(f"Processing screenshot: {screenshot}")
        match_found = False
        for video in videos:
            if match_screenshot_to_video(screenshot, video):
                f.write(f"Screenshot {screenshot} matches with video {video}\n")
                match_found = True
                break  # Assuming each screenshot matches only one video, exit loop after first match
        if not match_found:
            print(f"Warning: No match found for screenshot: {screenshot}")

print("Process completed.")
