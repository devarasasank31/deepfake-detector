import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.face_utils import detect_faces
from utils.metadata_utils import extract_metadata
from utils.gpt_explainer import get_gpt_feedback

st.title("🕵️ Deepfake Detector")

uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded:
    st.image(uploaded, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Detecting faces..."):
        faces = detect_faces(uploaded)
        st.write(f"✅ Faces Detected: {len(faces)}")

    # 🔁 Rewind the file so it can be read again
    uploaded.seek(0)

    with st.spinner("Extracting metadata..."):
        metadata = extract_metadata(uploaded)
        st.json(metadata)

    with st.spinner("Asking Gemini to analyze..."):
        feedback = get_gpt_feedback(faces, metadata)
        st.markdown("### 🧠 Gemini Feedback")
        st.write(feedback)
