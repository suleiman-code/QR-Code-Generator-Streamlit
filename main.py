import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
import cv2
import io
import os

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Premium QR Code Generator & Scanner")
        self.root.geometry("700x800")
        self.root.minsize(600, 700)
        self.root.configure(bg="#f0f2f5")

        # Variables
        self.qr_image = None
        self.current_qr_pil = None
        self.logo_path = None # Variable for optional logo image
        self.status_text = tk.StringVar(value="Ready")
        self.data_var = tk.StringVar()

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure LabelFrames
        style.configure("TLabelframe", background="#f0f2f5", padding=10)
        style.configure("TLabelframe.Label", background="#f0f2f5", font=("Segoe UI", 10, "bold"), foreground="#333")

        # Modern Button Styles
        style.configure("Generate.TButton", font=("Segoe UI", 10, "bold"), background="#2ecc71", foreground="white")
        style.map("Generate.TButton", background=[('active', '#27ae60')])
        
        style.configure("Save.TButton", font=("Segoe UI", 10, "bold"), background="#3498db", foreground="white")
        style.map("Save.TButton", background=[('active', '#2980b9')])

    def create_widgets(self):
        # Main Container
        main_frame = tk.Frame(self.root, bg="#f0f2f5", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")

        # Title
        title_label = tk.Label(main_frame, text="✨ QR Code Generator", font=("Segoe UI", 24, "bold"), bg="#f0f2f5", fg="#2c3e50")
        title_label.pack(pady=(0, 20))

        # Input Section
        input_frame = ttk.LabelFrame(main_frame, text=" Input Details ")
        input_frame.pack(fill="x", pady=10)

        tk.Label(input_frame, text="Data / URL:", bg="#f0f2f5", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.data_entry = ttk.Entry(input_frame, textvariable=self.data_var, font=("Segoe UI", 11))
        self.data_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.data_entry.focus()
        input_frame.columnconfigure(1, weight=1)

        # Action Buttons
        button_frame = tk.Frame(main_frame, bg="#f0f2f5")
        button_frame.pack(fill="x", pady=10)

        self.gen_btn = ttk.Button(button_frame, text="Generate QR 🚀", style="Generate.TButton", command=self.generate_qr)
        self.gen_btn.pack(side="left", expand=True, fill="x", padx=5)

        self.save_btn = ttk.Button(button_frame, text="Save QR 💾", style="Save.TButton", command=self.save_qr)
        self.save_btn.pack(side="left", expand=True, fill="x", padx=5)

        # Display Area
        self.display_frame = ttk.LabelFrame(main_frame, text=" QR Preview ")
        self.display_frame.pack(expand=True, fill="both", pady=10)

        self.qr_display = tk.Label(self.display_frame, text="No QR Generated", bg="white", relief="sunken")
        self.qr_display.pack(expand=True, fill="both", padx=10, pady=10)

        # Bind resize event for dynamic scaling
        self.display_frame.bind("<Configure>", self.on_resize)

        # Status Bar
        self.status_bar = tk.Label(self.root, textvariable=self.status_text, bd=1, relief="sunken", anchor="w", 
                                  bg="#ecf0f1", font=("Segoe UI", 9))
        self.status_bar.pack(side="bottom", fill="x")

    def on_resize(self, event):
        """Handle window resizing to scale the QR code."""
        if self.current_qr_pil:
            self.update_qr_display()

    def update_qr_display(self):
        """Updates the QR display based on current window/frame size."""
        if not self.current_qr_pil:
            return

        # Get current frame dimensions
        frame_width = self.display_frame.winfo_width() - 40
        frame_height = self.display_frame.winfo_height() - 40
        
        # Ensure minimum size for visibility
        size = max(min(frame_width, frame_height), 100)
        
        # Resize image for display
        display_img = self.current_qr_pil.copy()
        display_img.thumbnail((size, size), Image.Resampling.LANCZOS)
        
        self.qr_image = ImageTk.PhotoImage(display_img)
        self.qr_display.config(image=self.qr_image, text="")

    def update_status(self, message):
        if len(message) > 80:
            message = message[:77] + "..."
        self.status_text.set(message)
        self.root.update_idletasks()

    def generate_qr(self):
        data = self.data_var.get().strip()
        if not data:
            messagebox.showwarning("Empty Input", "Please enter some data or a URL to generate a QR code.")
            return

        try:
            self.update_status("🔄 Generating QR Code...")
            
            # Use Standard Error Correction
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            self.current_qr_pil = img
            self.update_qr_display()
            self.update_status(f"✅ Generated QR for: {data}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR: {str(e)}")
            self.update_status("❌ Error during generation")

    def save_qr(self):
        if self.current_qr_pil is None:
            messagebox.showwarning("No QR", "Please generate a QR code first.")
            return

        file_path = filedialog.asksaveasfilename(
            title="Save QR Code As",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )

        if file_path:
            try:
                self.current_qr_pil.save(file_path)
                messagebox.showinfo("Success", f"QR Code saved successfully to:\n{file_path}")
                self.update_status(f"💾 Saved to: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {str(e)}")
                self.update_status("❌ Save failed")


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
