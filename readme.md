# Quickstart

This code can be run to best match photos to videos that may contain those photos. After executing the desired script, matches.txt will be updated with the photo and video matches.

## Setup

- **Version:** Python 3.9.17
- **Dependencies:**
  - `pip install opencv-python`
  - _(optional progress bar)_ `pip install tqdm`
  - `os & shutil: Used for file and directory operations.`

## Execution

Run the desired script with Python:

> python 4_progressbar.py

## Methodology

The code has undergone multiple iterations that build upon each other up until the latest 4th iteration:

1. **Threshold Matching (1_templatematching.py)**:
   - Basic implementation with a threshold of .95 to match.
2. **Best Match Score (2_bestmatching.py)**:
   - Matches the highest score instead of relying on a fixed threshold.
   - Introduced the concept of storing matches in folders, not just in a text file.
3. **Resized Frame Matching (3_resizedmatching.py)**:
   - Resizes each frame of the video to match the screenshot resolution.
   - Uses the native `cv2` resize function. While it seems safe, there's potential for bugs.
4. **Progress Bar Implementation (4_progressbar.py)**:
   - Incorporates all the features from the Resized Frame Matching version but with an added progress bar for a better user experience.

## Conclusion

- This method currently picks the best match from the videos instead of using a matching threshold. This is optimized for accuracy and completeness but comes at the cost of requiring the code to traverse the entire set of videos with no early exit condition.
