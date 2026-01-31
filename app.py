import streamlit as st
import qrcode
from PIL import Image
import io

# Page Configuration
st.set_page_config(
    page_title="QR Code Studio",
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
    }
    div.stDownloadButton > button {
        width: 100%;
        background-color: #3498db !important;
        color: white !important;
        border: none;
        padding: 10px;
        font-weight: bold;
    }
    .qr-container {
        display: flex;
        justify-content: center;
        padding: 20px;
        background: white;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Premium QR Generator")
st.info("Fill the details below to create your custom branded QR Code.")

# Persistent Layout Containers
input_placeholder = st.container()
result_placeholder = st.container()

with input_placeholder:
    data = st.text_input("🔗 Enter your Link or Text:", placeholder="Paste your URL here...")
    custom_name = st.text_input("💾 Save as (Filename):", value="my_qrcode", help="Enter name without extension")
    
    if st.button("Generate QR Code Now 🚀"):
        if data:
            try:
                # Generate QR
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4
                )
                qr.add_data(data)
                qr.make(fit=True)
                
                img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
                
                # Use result placeholder to show content without shifting
                with result_placeholder:
                    st.markdown("---")
                    st.subheader("🎯 Your Generated QR Code")
                    
                    # Display Image
                    st.image(img, width=300)
                    
                    # Prepare Download
                    buf = io.BytesIO()
                    img.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    
                    # Extension check
                    final_name = f"{custom_name}.png" if not custom_name.endswith('.png') else custom_name
                    
                    st.download_button(
                        label=f"Download {final_name} 💾",
                        data=byte_im,
                        file_name=final_name,
                        mime="image/png"
                    )
                    st.success(f"Done! Ready to download as '{final_name}'")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
        else:
            st.warning("⚠️ Please enter some data first!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
