# FaceSwapLive
🧑‍🔬 Live Face Swap with InsightFace

This project uses the InsightFace library to perform live face swap using your device's webcam.

📸 Description

The script detects faces in real-time via the webcam and swaps the detected face with a source face from an image that is loaded in advance.

It uses:

* insightface for face detection and analysis.

* An ONNX face swap model (inswapper_128.onnx).

* OpenCV for webcam handling and live result display.

📁 Project Structure
FaceSwapLive/
├── models/
│   └── inswapper_128.onnx        # ONNX model for face swap
├── source.jpg                    # Source image for face replacement
├── face_swap_live.py             # Main script (yours)
└── README.md                     # This file

⚙️ Requirements

* Python 3.7+

* InsightFace

* OpenCV (cv2)

* ONNX Runtime

Installation:

pip install insightface opencv-python onnxruntime

🚀 How to Use
1. Make sure you have a source image named source.jpg in the correct path.
2. Download the inswapper_128.onnx model and place it inside the models/ folder.
3. Run the script:
python face_swap_live.py
4. Press the q key to close the window.

⚠️ Warnings

* The script uses CPUExecutionProvider; if you have a compatible GPU, you can change this to improve performance.

* If no face is detected in the source image, the program will stop.

💡 Credits

Based on the amazing InsightFace library.
