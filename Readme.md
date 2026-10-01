# 🔍 AI Vision Detector

A simple web app that detects objects in any image using **YOLOv8** and shows the result in a **Gradio** interface. Upload an image, and the app draws bounding boxes and lists how many of each object it found.

## ✨ Features

- Object detection with YOLOv8 (nano model, fast on CPU)
- Clean web UI built with Gradio
- Shows the annotated image plus a count of every detected object
- Works fully offline once the model file is downloaded

## 📁 Project Structure

```
AI_Vision_Detector/
├── app.py            # Gradio web app (run this)
├── detect.py         # YOLO detection logic
├── test.py           # Quick local test with an image window
├── downloads.py      # Downloads the YOLOv8 model
├── yolov8n.pt        # YOLOv8 nano model weights
├── requirements.txt  # Python dependencies
├── uploads/          # Uploaded/test images are saved here
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Vision_Detector.git
cd AI_Vision_Detector
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the model (only if `yolov8n.pt` is missing)

```bash
python downloads.py
```

### 5. Run the app

```bash
python app.py
```

Open the link shown in the terminal (usually http://127.0.0.1:7860) in your browser.

## 🧪 Quick test without the web UI

Put an image at `uploads/image.jpeg` and run:

```bash
python test.py
```

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- [Gradio](https://www.gradio.app/)
- [OpenCV](https://opencv.org/)

## 📌 How It Works

1. You upload an image in the Gradio interface.
2. `app.py` saves it to `uploads/input.jpg`.
3. `detect.py` runs YOLOv8 on it, draws boxes and counts each class.
4. The annotated image and the object counts are shown back in the UI.

## 📄 License

This project is open source. Add a license of your choice (for example MIT).

## 👤 Author

Made by SHIVAM VAGHASIYA — [GitHub](https://github.com/YOUR_USERNAME)