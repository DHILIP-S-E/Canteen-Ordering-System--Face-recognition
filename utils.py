import cv2
import face_recognition
import numpy as np
import os
import pickle
from PIL import Image
import streamlit as st

# Create necessary directories
FACES_DIR = os.path.join(os.path.dirname(__file__), 'faces')
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(FACES_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

ENCODINGS_FILE = os.path.join(DATA_DIR, 'encodings.pkl')

def capture_face():
    """Capture a single frame from webcam and detect face"""
    try:
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            return None, "Error: Could not access webcam"
        
        # Read a single frame
        ret, frame = cap.read()
        cap.release()
        
        if not ret:
            return None, "Error: Could not capture image"
        
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect face locations
        face_locations = face_recognition.face_locations(rgb_frame)
        
        if not face_locations:
            return None, "Error: No face detected"
        
        if len(face_locations) > 1:
            return None, "Error: Multiple faces detected"
        
        return rgb_frame, "Success"
        
    except Exception as e:
        return None, f"Error: {str(e)}"

def save_image(image, username):
    """Save captured image to faces directory"""
    try:
        if not os.path.exists(FACES_DIR):
            os.makedirs(FACES_DIR)
        
        image_path = os.path.join(FACES_DIR, f"{username}.jpg")
        
        # Convert numpy array to PIL Image
        pil_image = Image.fromarray(image)
        pil_image.save(image_path)
        
        return image_path
    
    except Exception as e:
        raise Exception(f"Error saving image: {str(e)}")

def get_face_encoding(image):
    """Get face encoding from image"""
    try:
        # Convert image to 8-bit RGB if needed
        if isinstance(image, np.ndarray):
            # Ensure 8-bit RGB format
            if image.dtype != np.uint8:
                image = (image * 255).astype(np.uint8)
            # Ensure RGB format
            if len(image.shape) == 2:  # Grayscale
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            elif image.shape[2] == 4:  # RGBA
                image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
            elif image.shape[2] == 3:  # Might be BGR
                if not isinstance(image, np.ndarray) or image.dtype != np.uint8:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Get face encoding
        face_encodings = face_recognition.face_encodings(image)
        
        if not face_encodings:
            return None
            
        return face_encodings[0]
        
    except Exception as e:
        st.error(f"Error getting face encoding: {str(e)}")
        return None

def save_encoding(username, encoding):
    """Save face encoding to encodings file"""
    try:
        # Load existing encodings
        encodings = {}
        if os.path.exists(ENCODINGS_FILE):
            with open(ENCODINGS_FILE, 'rb') as f:
                encodings = pickle.load(f)
        
        # Add new encoding
        encodings[username] = encoding
        
        # Save updated encodings
        with open(ENCODINGS_FILE, 'wb') as f:
            pickle.dump(encodings, f)
            
    except Exception as e:
        raise Exception(f"Error saving encoding: {str(e)}")

def verify_face(image):
    """Verify face against stored encodings"""
    try:
        if not os.path.exists(ENCODINGS_FILE):
            return None, "No registered faces found"
        
        # Load stored encodings
        with open(ENCODINGS_FILE, 'rb') as f:
            stored_encodings = pickle.load(f)
        
        if not stored_encodings:
            return None, "No registered faces found"
        
        # Get encoding of the captured image
        face_encoding = get_face_encoding(image)
        if face_encoding is None:
            return None, "Could not encode face"
        
        # Compare with stored encodings
        for username, stored_encoding in stored_encodings.items():
            # Compare faces with tolerance of 0.6
            match = face_recognition.compare_faces([stored_encoding], face_encoding, tolerance=0.6)[0]
            if match:
                return username, "Success"
        
        return None, "Face not recognized"
        
    except Exception as e:
        return None, f"Error during verification: {str(e)}"