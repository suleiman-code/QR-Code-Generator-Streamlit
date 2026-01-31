import streamlit as st
import qrcode
from PIL import Image
import io
import os

# Page Configuration
st.set_page_config(
    page_title="Premium QR Studio",
    page_icon="✨",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    div.stButton > button {
        width: 100%;
        background-color: #2ecc71 !important;
        color: white !important;
        border: none;
        padding: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #27ae60 !important;
        transform: scale(1.02);
    }
    div.stDownloadButton > button {
        width: 100%;
        background-color: #3498db !important;
        color: white !important;
        border: none;
        padding: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stDownloadButton > button:hover {
        background-color: #2980b9 !important;
        transform: scale(1.02);
    }
    .main-title {
        text-align: center;
        color: #2c3e50;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>✨ QR Code Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d;'>Create Professional, Colorful, and Specialized QR Codes</p>", unsafe_allow_html=True)

# --- Sidebar: Customization ---
st.sidebar.header("🎨 Design & Colors")
fg_color = st.sidebar.color_picker("Pick QR Code Color (Foreground)", "#000000")
bg_color = st.sidebar.color_picker("Pick Background Color", "#FFFFFF")

st.sidebar.markdown("---")
st.sidebar.header("⚙️ QR Settings")
print_mode = st.sidebar.toggle("🖨️ Print Optimized Mode", help="Enable this for high-resolution prints and posters.")

if print_mode:
    box_size = 25  # Ultra HD
    st.sidebar.info("🚀 Hyper-HD Mode Active")
else:
    box_size = st.sidebar.slider("QR Box Size", 5, 20, 10, help="Controls the size of the QR dots. Higher = Larger Image.")

# Border Thickness (Point) - Always adjustable
border_size = st.sidebar.slider("Border Thickness (Points)", 1, 20, 4, help="White margin around the QR code. Recommended: 4.")

# Automatically set Error Correction for better UX
error_correction = qrcode.constants.ERROR_CORRECT_H if print_mode else qrcode.constants.ERROR_CORRECT_M

# --- Initial State ---
if 'generated_qr' not in st.session_state:
    st.session_state.generated_qr = None
if 'qr_details' not in st.session_state:
    st.session_state.qr_details = ""
if 'qr_filename' not in st.session_state:
    st.session_state.qr_filename = ""

# --- Main App Logic ---
st.markdown("### 🛠️ Choose QR Type")
mode = st.radio("Select Mode:", ["🔗 Basic (Text/URL)", "📶 WiFi QR", "📞 Business Card"], horizontal=True)

final_qr_data = ""
final_filename = "my_qrcode"

if mode == "🔗 Basic (Text/URL)":
    data_input = st.text_input("Enter Link or Text:", placeholder="https://google.com")
    if data_input:
        if "." in data_input and not data_input.startswith(("http://", "https://", "mailto:", "tel:")):
            final_qr_data = "https://" + data_input
        else:
            final_qr_data = data_input
        final_filename = st.text_input("Save as (Filename):", value="text_qr")

elif mode == "📶 WiFi QR":
    st.info("📶 **WiFi Guide:** Uncheck 'Hidden' if you can see your WiFi name in your phone's list.")
    ssid = st.text_input("WiFi Name (SSID):", placeholder="Exact WiFi Name")
    password = st.text_input("WiFi Password:", type="password", placeholder="WiFi Password")
    security = st.selectbox("Security Type:", ["WPA", "WEP", "None"])
    hidden = st.checkbox("Hidden Network? (Usually No)")
    
    if ssid:
        esc_ssid = ssid.replace("\\", "\\\\").replace(";", "\\;").replace(":", "\\:").replace(",", "\\,").replace("\"", "\\\"")
        esc_pw = password.replace("\\", "\\\\").replace(";", "\\;").replace(":", "\\:").replace(",", "\\,").replace("\"", "\\\"")
        sec = "nopass" if security == "None" else security
        h_val = "true" if hidden else "false"
        final_qr_data = f"WIFI:T:{sec};S:{esc_ssid};P:{esc_pw};H:{h_val};;"
        final_filename = st.text_input("Save as (Filename):", value="wifi_qr")

elif mode == "📞 Business Card":
    st.info("🎯 **Tip:** Scan to save contact details directly to phone.")
    full_name = st.text_input("Full Name (e.g. Suleiman Ahmed):")
    phone = st.text_input("Phone Number:")
    email = st.text_input("Email:")
    org = st.text_input("Organization/Job:")
    
    if full_name:
        # Split name for N field (Lastname;Firstname)
        name_parts = full_name.strip().split()
        first_name = name_parts[0] if len(name_parts) > 0 else ""
        last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
        
        # Optimized vCard for Android/iOS parsing
        final_qr_data = (
            f"BEGIN:VCARD\n"
            f"VERSION:3.0\n"
            f"N:{last_name};{first_name};;;\n"
            f"FN:{full_name}\n"
            f"ORG:{org}\n"
            f"TEL;TYPE=CELL:{phone}\n"
            f"EMAIL:{email}\n"
            f"END:VCARD"
        )
        final_filename = st.text_input("Save as (Filename):", value="contact_qr")

st.markdown("---")

col_gen, col_clr = st.columns([3, 1])

with col_gen:
    generate_clicked = st.button("Generate Premium QR 🚀")

with col_clr:
    if st.button("Clear Design 🗑️"):
        st.session_state.generated_qr = None
        st.session_state.qr_details = ""
        st.rerun()

# Generation Logic
if generate_clicked:
    if final_qr_data:
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=error_correction,
                box_size=box_size,
                border=border_size
            )
            qr.add_data(final_qr_data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color=fg_color, back_color=bg_color).convert('RGB')
            
            # Save to Session State
            st.session_state.generated_qr = img
            st.session_state.qr_details = final_qr_data
            st.session_state.qr_filename = final_filename
            
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please fill in the required fields first!")

# Display current QR from session state
if st.session_state.generated_qr:
    st.markdown("---")
    col_img, col_info = st.columns([1, 1])
    
    with col_img:
        st.image(st.session_state.generated_qr, width=300, caption="Your QR Design")
    
    with col_info:
        st.success("🎯 QR Code Ready!")
        st.write("**Details:**")
        st.code(st.session_state.qr_details)
        
        # Prepare PNG Download
        buf_png = io.BytesIO()
        st.session_state.generated_qr.save(buf_png, format="PNG")
        byte_png = buf_png.getvalue()
        
        # Prepare PDF Download (Best for Printing)
        buf_pdf = io.BytesIO()
        # Convert RGB image to PDF
        st.session_state.generated_qr.save(buf_pdf, format="PDF", resolution=300.0)
        byte_pdf = buf_pdf.getvalue()
        
        dl_name_png = f"{st.session_state.qr_filename}.png"
        dl_name_pdf = f"{st.session_state.qr_filename}.pdf"
        
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            st.download_button(
                label=f"Download PNG 🖼️",
                data=byte_png,
                file_name=dl_name_png,
                mime="image/png"
            )
        with col_dl2:
            st.download_button(
                label=f"Download PDF (Print) �",
                data=byte_pdf,
                file_name=dl_name_pdf,
                mime="application/pdf"
            )

# Footer
st.markdown("<br><hr><p style='text-align: center;'>Built with ❤️ using Streamlit & Python</p>", unsafe_allow_html=True)
