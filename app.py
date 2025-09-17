# app.py

import streamlit as st
import google.generativeai as genai

# --- Configuration ---
# Set up the page configuration for your app
st.set_page_config(
    page_title="AI Educator's Toolkit",
    page_icon="📚",
    layout="centered", # 'centered' or 'wide'
)

# --- API Key and Model Setup ---
# Configure the Gemini API with the key from secrets
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error configuring the AI model. Please check your API key. Error: {e}")
    st.stop() # Stop the app if the API key is not found or invalid

# --- The App's User Interface ---
st.title("👨‍🏫 AI Educator's Toolkit")
st.write("Your AI co-pilot for lesson planning. Fill in the details below to generate a custom lesson plan.")

# --- Lesson Plan Generator ---
st.header("Lesson Plan Generator")

# Get user inputs
topic = st.text_input("Topic:", placeholder="e.g., The Water Cycle")
grade_level = st.text_input("Grade Level:", placeholder="e.g., 4th Grade")
time_limit = st.text_input("Time Limit (in minutes):", placeholder="e.g., 45 minutes")

# The button to trigger the AI
if st.button("Generate Lesson Plan"):
    if not topic or not grade_level or not time_limit:
        st.warning("Please fill in all the fields to generate a lesson plan.")
    else:
        # --- Prompt Engineering ---
        # This is where you tell the AI what you want it to do
        prompt = f"""
        You are an expert curriculum developer for K-12 education. Your task is to create a detailed lesson plan.

        Topic: {topic}
        Grade Level: {grade_level}
        Time Limit: {time_limit} minutes

        The lesson plan must include the following sections:
        1.  **Learning Objective:** What will students be able to do by the end of the lesson?
        2.  **Materials Needed:** A list of all required materials.
        3.  **Hook/Engagement (5-10 minutes):** A creative activity to capture students' interest at the start.
        4.  **Main Activity/Instruction (20-30 minutes):** The core teaching part of the lesson, with step-by-step instructions.
        5.  **Wrap-Up & Assessment (5-10 minutes):** An activity to review the concepts and check for understanding.

        Please format the output in a clear, organized, and professional manner using markdown.
        """

        # --- AI Call and Display ---
        try:
            with st.spinner("Your AI co-pilot is crafting the perfect lesson plan..."):
                response = model.generate_content(prompt)
                st.divider()
                st.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred while generating the content: {e}")


# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info("This app was created by Zachary Groves.")