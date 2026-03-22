# Motion Detection System (OpenCV)

A real-time motion detection system built from scratch using OpenCV and Python.
No pretrained models — pure computer vision techniques.

## How it works

The system compares consecutive webcam frames to detect motion. When movement
is detected above a certain size threshold, it highlights the region with a
bounding box and fills the motion mask.

## Pipeline
```
Webcam ──► Frame Difference ──► Blur ──► Threshold ──► Dilate/Erode ──► Contours ──► Display
```

### Step by step

1. **Frame differencing** — computes the absolute difference between two
   consecutive frames to isolate what changed
2. **Gaussian blur** — smooths the difference to reduce pixel-level noise
3. **Grayscale + threshold** — converts to binary (black/white) based on
   pixel intensity change
4. **Dilation + erosion** — morphological operations that close gaps and
   remove small artifacts
5. **Contour detection** — finds the outlines of moving regions
6. **Filtering** — ignores contours smaller than 5000px² to avoid false
   positives from noise

## Run it
```bash
pip install opencv-python numpy
python detect.py
```

## Skills demonstrated

- Real-time video processing with OpenCV
- Frame differencing for motion isolation
- Image preprocessing: Gaussian blur, grayscale conversion, thresholding
- Morphological operations: dilation and erosion
- Contour detection and bounding box rendering
- Noise filtering with area thresholding
