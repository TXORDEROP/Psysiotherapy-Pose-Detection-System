Physiotherapy Pose Detection System

🚑 A real-time physiotherapy exercise monitoring system using Computer Vision and Machine Learning.
The system detects, classifies, and evaluates physiotherapy poses via a standard webcam, providing immediate feedback to users through an intuitive Tkinter GUI.

📌 Features

🔹 Automated Pose Recognition – Detects and classifies physiotherapy poses in real-time.

🔹 Correctness Assessment – Distinguishes between correct and incorrect poses with feedback.

🔹 Real-Time Feedback – Provides corrective instructions instantly via GUI.

🔹 Self-Guided Rehabilitation – Reduces dependency on therapists.

🔹 User & Admin Management – Simple login/registration system with SQLite3 database.

🔹 Modular Architecture – Easily extendable for new poses or models.

🏗️ System Architecture

Video Input: Captured from webcam.

Pose Detection: OpenPose detects keypoints.

Feature Extraction: Joint angles/distances computed.

Pose Classification: Logistic Regression model classifies as Correct/Incorrect.

Feedback Generation: GUI provides real-time corrective feedback.

Database: SQLite3 stores users, datasets, and model weights.

⚙️ Tech Stack

Language: Python 3.8

Libraries/Frameworks:

OpenCV

OpenPose

Scikit-learn

Tkinter

SQLite3

OS: Windows 10 (64-bit)

IDE: VS Code / Spyder

📊 Algorithms

OpenPose – Extracts body keypoints from frames.

Logistic Regression – Classifies poses as Correct/Incorrect.

Alternative Options: Mediapipe, Random Forest, CNN, LSTM (for future work).

🧪 Testing

✔️ Unit Testing – Modules (Video, Keypoints, Classification, Feedback).
✔️ Integration Testing – Ensures smooth pipeline.
✔️ System Testing – Verified under different conditions (lighting, angles).
✔️ Acceptance Testing – Validated with physiotherapy exercises like Trikonasana, Gripping Pose, etc.

🚀 How to Run

Clone this repo:

git clone https://github.com/TXORDEROP/Psysiotherapy-Pose-Detection-System.git
cd Psysiotherapy-Pose-Detection-System


Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows


Install dependencies:

pip install -r requirements.txt


Run the system:

python main.py

📂 Project Structure
├── dataset/                # Pose dataset (excluded in .gitignore due to size)
├── src/                    # Source code
│   ├── gui/                # Tkinter GUI files
│   ├── ml/                 # Machine learning models
│   ├── utils/              # Helper functions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignore venv, datasets, cache

📈 Results

✅ Pose classification accuracy: >85%

✅ Real-time processing speed: <100 ms per frame

✅ Successfully tested on multiple physiotherapy poses

🔮 Future Scope

📱 Mobile deployment using Mediapipe.

⏳ Sequential pose analysis using LSTM / Transformers.

☁️ Cloud-based analytics & remote physiotherapy sessions.

📡 Integration with wearable sensors for enhanced accuracy.
