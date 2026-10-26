🎨 Real-Time Color Tracking with Python and OpenCV

A real-time computer vision project that detects blue and red objects using a webcam and tracks their movement by drawing a trail on the video screen.

📌 Features
🔵 Detects blue-colored objects.
🔴 Detects red-colored objects.
🎥 Uses a webcam for real-time tracking.
✏️ Draws a trail to follow the movement of the detected object.
🔄 Switches between blue and red tracking.
🧹 Clears the tracking trail whenever needed.
🛠️ Technologies Used
Python
OpenCV (cv2)
NumPy
📋 Requirements
Python 3.x
A working webcam
OpenCV
NumPy
📥 Installation

1. Clone this repository

bash
git clone https://github.com/YOUR-USERNAME/Test-Code.git


Replace YOUR-USERNAME with your GitHub username.

2. Open the project folder

bash
cd Test-Code


3. Install the required libraries

bash
pip install opencv-python numpy

▶️ How to Run

Run the Python script using:

bash
python color_tracking.py


A window will open showing the webcam feed and tracking the selected color.

⌨️ Keyboard Controls
Key	Action
C	Switch between blue and red
E	Erase the tracking trail
Q	Quit the program
⚙️ How It Works
Captures video from the webcam.
Converts each frame from BGR to HSV color space.
Detects the selected color using HSV thresholds.
Finds the largest detected contour.
Calculates the center of the detected object.
Draws a circle at the object's center and connects previous positions to create a tracking trail.
📁 Project Structure
text
Test-Code/
├── README.md
├── color_tracking.py
└── requirements.txt

🚀 Future Improvements
Track multiple objects simultaneously.
Add green and yellow color detection.
Improve detection under different lighting conditions.
Display the selected color on the screen.
Add mouse controls for selecting colors.
📄 License

No license has been specified for this project yet.

👨‍💻 Author

Created as a Python and OpenCV computer vision project.
