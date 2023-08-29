import cv2
import os
import shutil


def match_screenshot_to_video(screenshot_path, video_path):
    screenshot = cv2.imread(screenshot_path, cv2.IMREAD_COLOR)
    if screenshot is None:
        print(f"Warning: Unable to load screenshot: {screenshot_path}")
        return 0.0, None

    vid_cap = cv2.VideoCapture(video_path)
    if not vid_cap.isOpened():
        print(f"Warning: Unable to open video: {video_path}")
        return 0.0, None

    best_match_score = 0.0
    while True:
        ret, frame = vid_cap.read()
        if not ret:
            break

        res = cv2.matchTemplate(frame, screenshot, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)
        best_match_score = max(best_match_score, max_val)

    return best_match_score, video_path


video_directory = "./videos/"
photo_directory = "./photos/"

videos = [os.path.join(video_directory, video) for video in os.listdir(video_directory)]
screenshots = [
    os.path.join(photo_directory, photo) for photo in os.listdir(photo_directory)
]

if os.path.exists("matches"):
    shutil.rmtree("matches")
os.makedirs("matches")


match_count = 0
with open("matches.txt", "w") as f:
    for screenshot in screenshots:
        best_match_video = None
        best_score = 0.0

        for video in videos:
            match_score, matched_video = match_screenshot_to_video(screenshot, video)
            if match_score > best_score:
                best_score = match_score
                best_match_video = matched_video

        match_count += 1
        match_folder = os.path.join("matches", str(match_count))
        os.makedirs(match_folder)
        shutil.copy(screenshot, match_folder)
        shutil.copy(best_match_video, match_folder)

        print(
            f"Best match for {screenshot} is {best_match_video} with score {best_score:.2f}"
        )
        f.write(
            f"Screenshot {screenshot} best matches with video {best_match_video} with score {best_score:.2f}\n"
        )

print("Process completed.")
