"""
OCR App - Camera & Image File Text Recognition
Equivalent to the Tesseract.js HTML app, using:
  - pytesseract for OCR
  - OpenCV for camera capture
  - tkinter for GUI
  - Pillow for image handling

Requirements:
    pip install pytesseract pillow opencv-python
    Also install Tesseract OCR engine:
      - Windows: https://github.com/UB-Mannheim/tesseract/wiki
      - macOS:   brew install tesseract
      - Linux:   sudo apt install tesseract-ocr
"""

import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import threading
import cv2
import pytesseract
from PIL import Image, ImageTk
import numpy as np


class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tesseract OCR - File & Camera")
        self.root.geometry("860x780")
        self.root.configure(bg="#f5f5f5")

        self.cap = None
        self.camera_active = False
        self.current_frame = None
        self._camera_loop_id = None

        self._build_ui()
        self.root.bind("<space>", self.on_space)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # ── UI ──────────────────────────────────────────────────────────────────

    def _build_ui(self):
        title = tk.Label(self.root, text="Tesseract OCR — File & Camera",
                         font=("Arial", 18, "bold"), bg="#f5f5f5", fg="black")
        title.pack(pady=(16, 4))

        # ── Upload section ──
        upload_frame = tk.LabelFrame(self.root, text="Option 1: Upload Image",
                                     font=("Arial", 11), bg="#f5f5f5", padx=10, pady=8, fg="black")
        upload_frame.pack(fill="x", padx=20, pady=6)

        tk.Button(upload_frame, text="Choose Image File…",
                  command=self.upload_image,
                  font=("Arial", 11), padx=10, pady=5).pack(side="left")
        self.upload_label = tk.Label(upload_frame, text="No file selected",
                                     bg="#f5f5f5", fg="#666", font=("Arial", 10))
        self.upload_label.pack(side="left", padx=10)

        # ── Camera section ──
        cam_frame = tk.LabelFrame(self.root, text="Option 2: Camera Input",
                                  font=("Arial", 11), bg="#f5f5f5", padx=10, pady=8,  fg="black")
        cam_frame.pack(fill="x", padx=20, pady=6)

        btn_row = tk.Frame(cam_frame, bg="#f5f5f5")
        btn_row.pack(anchor="w")
        self.start_btn = tk.Button(btn_row, text="Start Camera",
                                   command=self.start_camera,
                                   font=("Arial", 11), padx=10, pady=5, bg="#4CAF50", fg="black")
        self.start_btn.pack(side="left", padx=(0, 6))
        self.stop_btn = tk.Button(btn_row, text="Stop Camera",
                                  command=self.stop_camera,
                                  font=("Arial", 11), padx=10, pady=5, bg="#f44336", fg="black",
                                  state="disabled")
        self.stop_btn.pack(side="left", padx=(0, 6))
        self.capture_btn = tk.Button(btn_row, text="Capture & OCR  [SPACE]",
                                     command=self.capture_and_ocr,
                                     font=("Arial", 11), padx=10, pady=5, bg="#2196F3", fg="black",
                                     state="disabled")
        self.capture_btn.pack(side="left")

        self.cam_status = tk.Label(cam_frame,
                                   text="Press 'Start Camera', then SPACE (or the button) to capture.",
                                   bg="#f5f5f5", fg="#666", font=("Arial", 10, "italic"))
        self.cam_status.pack(anchor="w", pady=(4, 0))

        # ── Video preview ──
        self.video_label = tk.Label(self.root, bg="#333", width=640, height=360)
        self.video_label.pack(pady=6)
        self.video_label.pack_forget()   # hidden until camera starts

        # ── OCR result ──
        result_frame = tk.LabelFrame(self.root, text="OCR Result",
                                     font=("Arial", 11), bg="#f5f5f5", padx=10, pady=8,  fg="black")
        result_frame.pack(fill="both", expand=True, padx=20, pady=(6, 16))

        self.result_box = scrolledtext.ScrolledText(result_frame, font=("Courier", 11),
                                                    wrap="word", bg="#f0f0f0", fg="black", height=10)
        self.result_box.pack(fill="both", expand=True)
        self.set_result("Text will appear here…")

        copy_btn = tk.Button(result_frame, text="Copy to Clipboard",
                             command=self.copy_result, font=("Arial", 10), padx=8, pady=3)
        copy_btn.pack(anchor="e", pady=(4, 0))

    # ── Helpers ─────────────────────────────────────────────────────────────

    def set_result(self, text):
        self.result_box.config(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.insert("1.0", text)
        self.result_box.config(state="disabled")

    def copy_result(self):
        text = self.result_box.get("1.0", "end").strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(text)

    def run_ocr_thread(self, pil_image):
        """Run pytesseract in a background thread so the UI stays responsive."""
        def task():
            self.set_result("Processing…")
            try:
                text = pytesseract.image_to_string(pil_image).strip()
                self.set_result(text if text else "No text detected.")
            except Exception as e:
                self.set_result(f"OCR Error: {e}")
        threading.Thread(target=task, daemon=True).start()

    # ── File upload ──────────────────────────────────────────────────────────

    def upload_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff *.webp"), ("All files", "*.*")])
        if not path:
            return
        self.upload_label.config(text=path.split("/")[-1])
        img = Image.open(path)
        self.run_ocr_thread(img)

    # ── Camera ───────────────────────────────────────────────────────────────

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Camera Error", "Could not access the camera.")
            return
        self.camera_active = True
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.capture_btn.config(state="normal")
        self.video_label.pack(pady=6)
        self.cam_status.config(text="Camera active. Press SPACE (or button) to capture.")
        self._update_camera()

    def _roi_box(self, w, h):
        """Return (x1, y1, x2, y2) for the centered 75% ROI box."""
        box_w, box_h = int(w * 0.75), int(h * 0.75)
        x1 = (w - box_w) // 2
        y1 = (h - box_h) // 2
        return x1, y1, x1 + box_w, y1 + box_h

    def _update_camera(self):
        if not self.camera_active:
            return
        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame
            frame_mirrored = cv2.flip(frame, 1)

            # Draw ROI rectangle on a display copy
            h, w = frame_mirrored.shape[:2]
            x1, y1, x2, y2 = self._roi_box(w, h)
            display = frame_mirrored.copy()
            cv2.rectangle(display, (x1, y1), (x2, y2), (0, 200, 255), 2)

            rgb = cv2.cvtColor(display, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb)
            img.thumbnail((640, 360))
            imgtk = ImageTk.PhotoImage(img)
            self.video_label.config(image=imgtk, width=img.width, height=img.height)
            self.video_label.image = imgtk   # prevent GC
        self._camera_loop_id = self.root.after(30, self._update_camera)

    def stop_camera(self):
        self.camera_active = False
        if self._camera_loop_id:
            self.root.after_cancel(self._camera_loop_id)
        if self.cap:
            self.cap.release()
            self.cap = None
        self.video_label.pack_forget()
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.capture_btn.config(state="disabled")
        self.cam_status.config(text="Camera stopped.")
        self.set_result("Camera stopped.")

    def capture_and_ocr(self):
        if self.current_frame is None:
            return
        # Use the original (non-mirrored) frame for OCR
        h, w = self.current_frame.shape[:2]
        x1, y1, x2, y2 = self._roi_box(w, h)
        roi = self.current_frame[y1:y2, x1:x2]
        pil_image = Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
        self.run_ocr_thread(pil_image)

    def on_space(self, event):
        if self.camera_active:
            self.capture_and_ocr()

    def on_close(self):
        self.camera_active = False
        if self.cap:
            self.cap.release()
        self.root.destroy()


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()