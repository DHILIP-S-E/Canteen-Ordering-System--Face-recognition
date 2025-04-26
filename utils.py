import cv2
import face_recognition
import numpy as np
import os
import pickle
from PIL import Image
import streamlit as st
import numpy
# Create necessary directories
FACES_DIR = os.path.join(os.path.dirname(__file__), 'faces')
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(FACES_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

ENCODINGS_FILE = os.path.join(DATA_DIR, 'encodings.pkl')

def capture_face():
    """Capture a single frame from webcam and detect face"""
    cap = None
    preview = None
    try:
        # Try multiple camera indices (0, 1) in case default camera is not at index 0
        for camera_index in [0, 1]:
            try:
                if cap is not None:
                    cap.release()
                
                cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)  # Use DirectShow API on Windows
                
                if not cap.isOpened():
                    if camera_index == 1:  # If we've tried both cameras
                        return None, "Error: Could not access any webcam. Please ensure your webcam is connected and not in use by another application."
                    continue  # Try next camera
                
                # Set camera properties for better capture - use smaller resolution
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Reduced from 640
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # Reduced from 480
                cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)
                cap.set(cv2.CAP_PROP_CONTRAST, 150)
                cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75)
                
                # Create a placeholder for the webcam feed
                preview = st.empty()
                
                # Counter for successful face detections
                face_detected_count = 0
                max_attempts = 30  # Try for about 3 seconds
                
                for attempt in range(max_attempts):
                    ret, frame = cap.read()
                    
                    if not ret or frame is None:
                        continue
                    
                    try:
                        # Convert BGR to RGB for display and face detection
                        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        
                        # Show live preview
                        if preview is not None:
                            preview.image(rgb_frame, caption="Camera Preview", channels="RGB")
                        
                        # Detect face locations
                        face_locations = face_recognition.face_locations(rgb_frame)
                        
                        if face_locations:
                            face_detected_count += 1
                            if face_detected_count >= 3:  # Require 3 consecutive successful detections
                                if cap is not None:
                                    cap.release()
                                if preview is not None:
                                    preview.empty()
                                return rgb_frame, "Success"
                        else:
                            face_detected_count = 0  # Reset counter if face detection fails
                        
                    except (numpy.core._exceptions._ArrayMemoryError, MemoryError) as me:
                        # If we hit a memory error, try to free up resources and continue
                        if preview is not None:
                            preview.empty()
                        import gc
                        gc.collect()
                        continue
                    
                    import time
                    time.sleep(0.1)  # Small delay between frames
                
                if cap is not None:
                    cap.release()
                if preview is not None:
                    preview.empty()
                
                if camera_index == 1:  # If we've tried both cameras
                    return None, "Error: Could not detect a face. Please ensure good lighting, face the camera directly, and try again."
                
            except Exception as camera_error:
                if cap is not None:
                    cap.release()
                if preview is not None:
                    preview.empty()
                if camera_index == 1:
                    return None, f"Error with camera {camera_index}: {str(camera_error)}"
                continue
        
        return None, "Error: No working camera found."
        
    except Exception as e:
        if cap is not None:
            cap.release()
        if preview is not None:
            preview.empty()
        import traceback
        st.error(f"Detailed error: {traceback.format_exc()}")
        return None, f"Error accessing camera: {str(e)}. Please ensure your webcam is properly connected and not in use by another application."

    finally:
        # Make absolutely sure we release the camera
        if cap is not None:
            cap.release()
        if preview is not None:
            preview.empty()

def save_image(image, username):
    """Save captured image to faces directory"""
    try:
        if not os.path.exists(FACES_DIR):
            os.makedirs(FACES_DIR)
        
        image_path = os.path.join(FACES_DIR, f"{username}.jpg")
        
        # Ensure image is in correct format
        if isinstance(image, np.ndarray):
            # Convert numpy array to PIL Image
            pil_image = Image.fromarray(image.astype('uint8'))
            pil_image.save(image_path)
        else:
            # If already PIL Image
            image.save(image_path)
        
        return image_path
    
    except Exception as e:
        raise Exception(f"Error saving image: {str(e)}")

def get_face_encoding(image):
    """Get face encoding from image"""
    try:
        # Ensure image is in correct format for face_recognition
        if not isinstance(image, np.ndarray):
            image = np.array(image)
        
        # Convert to RGB if needed
        if len(image.shape) == 2:  # Grayscale
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        elif len(image.shape) == 3 and image.shape[2] == 4:  # RGBA
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        elif len(image.shape) == 3 and image.shape[2] == 3:  # BGR or RGB
            if not isinstance(image, np.ndarray) or image.dtype != np.uint8:
                image = image.astype(np.uint8)
        
        # Get face locations first
        face_locations = face_recognition.face_locations(image)
        if not face_locations:
            return None
            
        # Get face encodings
        face_encodings = face_recognition.face_encodings(image, face_locations)
        
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

def delete_face_data(username):
    """Delete face image and encoding for a user"""
    try:
        # Delete face image if it exists
        image_path = os.path.join(FACES_DIR, f"{username}.jpg")
        if os.path.exists(image_path):
            os.remove(image_path)
        
        # Remove encoding if it exists
        if os.path.exists(ENCODINGS_FILE):
            # Load existing encodings
            with open(ENCODINGS_FILE, 'rb') as f:
                encodings = pickle.load(f)
            
            # Remove user's encoding if it exists
            if username in encodings:
                del encodings[username]
                
            # Save updated encodings
            with open(ENCODINGS_FILE, 'wb') as f:
                pickle.dump(encodings, f)
                
        return True
    except Exception as e:
        raise Exception(f"Error deleting face data: {str(e)}")