# app.py# app.py

import streamlit as st
import google.generativeai as genai

# --- Configuration ---
st.set_page_config(
    page_title="AI Educator's Toolkit",
    page_icon="📚",
    layout="centered",
)

# --- API Key and Model Setup ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error configuring the AI model. Please check your API key in the secrets. Error: {e}")
    st.stop()

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
tool_choice = st.sidebar.radio("Choose a tool:", 
    ("Lesson Plan Generator", "Quiz Creator", "Concept Simplifier"))

st.sidebar.markdown("---")
st.sidebar.info("This app was created by Zachary Groves.")

# --- Main App Title ---
st.title("👨‍🏫 AI Educator's Toolkit")
st.write("Your AI co-pilot for classroom preparation. Choose a tool from the sidebar to get started.")
st.markdown("---")


# --- Tool 1: Lesson Plan Generator ---
if tool_choice == "Lesson Plan Generator":
    st.header("Lesson Plan Generator")
    st.write("Fill in the details below to generate a custom lesson plan.")

    topic = st.text_input("Topic:", placeholder="e.g., The Water Cycle")
    grade_level = st.text_input("Grade Level:", placeholder="e.g., 4th Grade")
    time_limit = st.text_input("Time Limit (in minutes):", placeholder="e.g., 45 minutes")

    if st.button("Generate Lesson Plan"):
        if not topic or not grade_level or not time_limit:
            st.warning("Please fill in all the fields.")
        else:
            prompt = f"""
            You are an expert curriculum developer. Create a detailed lesson plan.
            Topic: {topic}
            Grade Level: {grade_level}
            Time Limit: {time_limit} minutes

            Include these sections: Learning Objective, Materials Needed, Hook/Engagement, Main Activity, and Wrap-Up/Assessment.
            Format the output in a clear, organized manner using markdown.
            """
            try:
                with st.spinner("Crafting the perfect lesson plan..."):
                    response = model.generate_content(prompt)
                    st.divider()
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- Tool 2: Quiz Creator ---
elif tool_choice == "Quiz Creator":
    st.header("Quiz Creator")
    st.write("Paste any text below to generate a quiz. This is perfect for reading comprehension checks.")
    
    source_text = st.text_area("Paste your source text here:", height=200, placeholder="e.g., A chapter from a textbook or an article.")
    num_questions = st.number_input("Number of questions:", min_value=1, max_value=10, value=3)

    if st.button("Generate Quiz"):
        if not source_text:
            st.warning("Please paste some source text.")
        else:
            prompt = f"""
            You are a helpful teaching assistant. Based on the following text, generate {num_questions} unique multiple-choice questions with 4 possible answers each.
            Clearly indicate the correct answer for each question.

            Here is the source text:
            ---
            {source_text}
            ---
            """
            try:
                with st.spinner("Generating your quiz..."):
                    response = model.generate_content(prompt)
                    st.divider()
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- Tool 3: Concept Simplifier ---
elif tool_choice == "Concept Simplifier":
    st.header("Concept Simplifier")
    st.write("Enter a complex topic and the target audience to get a simple, easy-to-understand explanation.")

    complex_topic = st.text_input("Complex Topic:", placeholder="e.g., Photosynthesis or Karnaugh Maps")
    target_audience = st.text_input("Target Audience:", placeholder="e.g., a 5th grader, a high school student")

    if st.button("Simplify Concept"):
        if not complex_topic or not target_audience:
            st.warning("Please fill in all the fields.")
        else:
            prompt = f"""
            You are an expert educator who can explain anything simply.
            Explain the following complex topic as if you were talking to {target_audience}.
            Use an analogy to help clarify the concept.

            Topic: {complex_topic}
            """
            try:
                with st.spinner("Simplifying the concept..."):
                    response = model.generate_content(prompt)
                    st.divider()
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
st.sidebar.info("This app was created by Zachary Groves.")
