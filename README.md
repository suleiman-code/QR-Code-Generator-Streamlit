# Premium QR Code Generator (Web App)

## Project Overview
The **Premium QR Code Generator** is a fast, modern, and responsive web application built with **Streamlit**. It allows users to generate professional-grade QR codes for URLs, WiFi connection, and Business Cards directly from their browser.

---

## 🌟 Professional Features
- **🖼️ Multiple QR Modes**:
    - **🔗 Basic**: For any URL or Text (Auto-detects links).
    - **📶 WiFi QR**: Auto-connect to WiFi (Supports SSID, Password, and Hidden networks).
    - **📞 Business Card**: Modern vCard format to save contacts directly to mobile.
- **🎨 Design & Colors**: Fully customize the QR code and background colors.
- **🖨️ Print Optimized Mode**: One-click Hyper-HD resolution for high-quality printing.
- **📄 Dual Download Options**: Save your designs as **PNG** images or **PDF** files (best for printing).
- **⚙️ Advanced Controls**: Adjust QR dot size and border thickness (Points).
- **📱 Mobile Optimized**: Generated codes are formatted for 100% compatibility with native iOS and Android camera apps.

---

## 📋 Requirements
- `streamlit`: For the web interface.
- `qrcode`: For generating the QR data.
- `Pillow (PIL)`: For high-quality image processing and PDF conversion.

---

## 🚀 Installation Guide

1. **Clone the Project**:
   Ensure all files (`app.py`, `requirements.txt`) are in your folder.

2. **Setup Virtual Environment**:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Application**:
   ```bash
   streamlit run app.py
   ```

---

## 🛠️ How to Use

1. **Choose Mode**: Select between Basic, WiFi, or Business Card.
2. **Setup Design**: Use the Sidebar to pick colors and adjust size/thickness.
3. **Enable Print Mode**: If you plan to print the QR, toggle the **Print Optimized Mode** for maximum quality.
4. **Generate & Save**: Click **Generate**, then choose **PNG** for digital use or **PDF** for physical printing.

---

## ☁️ Deployment
This application is ready for free deployment on **Streamlit Cloud**. Push the code to GitHub and connect your repository to share your app with a public link.

---

## License
Open-source and free for personal and commercial use.
