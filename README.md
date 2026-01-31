# QR Code Generator - Documentation

## Project Overview
The **QR Code Generator** is a modern desktop application built using Python's Tkinter framework. It allows users to generate high-quality QR codes from any text or URL data and save them locally with custom filenames.

---

## Features
- **Instant Generation**: Create QR codes instantly by clicking the "Generate QR" button.
- **Dynamic Preview**: Features a live preview area where the QR code scales automatically when the window is resized.
- **Custom Saving**: Securely save QR codes in `.png` or `.jpg` formats using a standard system file dialog.
- **Modern UI**: A clean, professional interface with a responsive layout and helpful status updates.
- **Error Handling**: Built-in validation to handle empty inputs and processing errors gracefully.

---

## Requirements
To run this project, you need Python installed on your system along with the following libraries:
- `qrcode`: For generating the QR code data.
- `Pillow (PIL)`: For image manipulation and display within Tkinter.
- `opencv-python`: (Optional/Residual) Used for potential future scanning capabilities.

---

## Installation Guide

1. **Clone the Project**:
   Ensure all files (`main.py`, `requirements.txt`) are in one folder.

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

### 1. Generating a QR Code
- Launch the application by running `python main.py`.
- Type your text or website URL into the **"Data / URL"** input field.
- Click the **"Generate QR 🚀"** button. The QR code will appear in the preview area.

### 2. Resizing the Window
- You can maximize or drag the corners of the window to resize it.
- The QR code image will dynamically adjust its size to fit the new dimensions.

### 3. Saving the QR Code
- Click the **"Save QR 💾"** button.
- A file explorer window will open.
- Navigate to your desired folder, type your preferred name for the file, and click **Save**.

---

## Technical Details
- **Framework**: Tkinter (Python Standard Library)
- **Styling**: Ttk (Themed Tkinter) using the 'clam' theme for a consistent look.
- **Image Handling**: Uses `Image.Resampling.LANCZOS` for high-quality scaling during window resizing.
- **Architecture**: Class-based structure for better maintainability and code organization.

---

## License
This project is open-source and free to used for personal or commercial purposes.
