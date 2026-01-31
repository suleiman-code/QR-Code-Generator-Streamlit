# Premium QR Code Generator (Web App)

## Project Overview
The **Premium QR Code Generator** is a fast, modern, and responsive web application built with **Streamlit**. It allows users to generate high-quality QR codes for any URLs or text data directly from their browser, with the ability to download the result with a custom filename.

---

## Features
- **🌍 Universal Access**: Accessible from any device (Mobile, Tablet, Desktop) via a web browser.
- **⚡ Instant Generation**: Create QR codes in real-time with high error correction.
- **💾 Custom Filenames**: Choose your own name for the QR code file before downloading.
- **🎨 Premium UI**: Features a clean, professional, and stable interface with modern styling.
- **📱 Responsive Design**: The layout automatically adjusts to fit any screen size.
- **☁️ Cloud Ready**: Optimized for deployment on Streamlit Cloud or other web hosting platforms.

---

## Requirements
To run this project locally, you need Python installed along with the following libraries:
- `streamlit`: For the web interface and application logic.
- `qrcode`: For generating the QR code data.
- `Pillow (PIL)`: For handling and saving the QR code images.

---

## Installation Guide

1. **Clone/Download the Project**:
   Ensure all files (`app.py`, `requirements.txt`) are in your project directory.

2. **Setup Virtual Environment (Recommended)**:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Use

### 1. Launching the App
- Open your terminal in the project folder.
- Run the following command:
  ```bash
  streamlit run app.py
  ```
- The application will automatically open in your default web browser (usually at `http://localhost:8501`).

### 2. Generating a QR Code
- Enter your link or text in the **"🔗 Enter your Link or Text"** field.
- (Optional) Provide a custom name in the **"💾 Save as (Filename)"** field.
- Click the **"Generate QR Code Now 🚀"** button.

### 3. Downloading the QR Code
- Once generated, your QR code will appear on the screen.
- Click the **"Download [YourName].png 💾"** button.
- The file will be saved via your browser. 
  - *Tip: If you want to choose a specific folder every time, enable "Ask where to save each file before downloading" in your browser's download settings.*

---

## Technical Details
- **Backend Framework**: Streamlit (Python)
- **Image Processing**: Pillow (PIL)
- **QR Engine**: qrcode (Python library)
- **Design**: Customized CSS integration for a stable and premium user experience.

---

## Deployment
This application is ready to be deployed on **Streamlit Cloud** for free. Simply push the code to a GitHub repository and connect it to Streamlit Cloud to receive a public sharing link.

---

## License
This project is open-source and free to be used for personal or commercial purposes.
