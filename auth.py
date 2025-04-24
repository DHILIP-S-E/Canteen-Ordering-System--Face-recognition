import streamlit as st
from utils import capture_face, verify_face
from database.db_utils import DatabaseManager

def face_login():
    """Handle face login functionality"""
    st.title("Face Login")
    
    # Create centered columns for better layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 📸 Face Recognition Login")
        st.write("Please look at the camera and ensure good lighting")
        
        if st.button("Start Face Recognition"):
            with st.spinner("Capturing and verifying face..."):
                # Capture face
                image, message = capture_face()
                
                if "Error" in message:
                    st.error(message)
                    return
                
                # Show captured image
                st.image(image, caption="Captured Image", channels="RGB")
                
                # Verify face
                username, verify_message = verify_face(image)
                
                if username and verify_message == "Success":
                    # Get user role from database
                    db = DatabaseManager()
                    user_data = db.get_user(username)
                    
                    if user_data:
                        st.success(f"Welcome back, {username}!")
                        # Set session state
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        st.session_state.user_role = user_data['role']
                        st.rerun()
                    else:
                        st.error("User not found in database")
                else:
                    st.error(verify_message)
        
        st.markdown("---")
        st.markdown("### 🔑 Regular Login")
        st.write("Or use traditional login method")
        
        if st.button("Switch to Password Login"):
            st.session_state.login_method = "password"
            st.rerun()