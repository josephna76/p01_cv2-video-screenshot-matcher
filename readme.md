# Quickstart

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

The code has undergone multiple iterations, each providing a different method of template matching:

1. **1_templatematching.py**:
   - The first iteration.
   - Basic implementation with a threshold of .95 to match.
2. **2_bestmatching.py**:

   - The second iteration.
   - Matches the highest score instead of relying on a fixed threshold.
   - Introduced the concept of storing matches in folders, not just in a text file.

3. **3_resizedmatching.py**:

   - Resizes each frame of the video to match the screenshot resolution.
   - Uses the native `cv2` resize function. While it seems safe, there's potential for bugs.

4. **4_progressbar.py**:
   - Same as `3_resizedmatching.py` but with an added progress bar for better UX during execution.

## Conclusion

- This method currently picks the best match from the videos instead of using a matching threshold. This is optimized for accuracy and completeness but comes at the cost of requiring the code to traverse the entire set of videos with no early exit condition.
