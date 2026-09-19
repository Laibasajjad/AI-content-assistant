import os
import streamlit as st
import google.generativeai as genai

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Content Assistant",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for Styling and Animations ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main Container Padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header Animation */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .main-header {
        animation: fadeInDown 0.8s ease-out;
        text-align: center;
        margin-bottom: 2rem;
    }

    .main-header h1 {
        background: linear-gradient(135deg, #FF4B4B 0%, #FF8F8F 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 2.8rem;
    }

    /* Card Box Animation */
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .output-card {
        animation: fadeInUp 0.6s ease-out;
        background-color: #1e1e2e;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #313244;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        color: #cdd6f4;
        margin-top: 1rem;
    }

    /* Button Glow Effect */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FF4B4B 0%, #FF7676 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.3);
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.5);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- Header Section ---
st.markdown(
    """
    <div class="main-header">
        <h1>✨ AI Content Assistant</h1>
        <p style="color: #a6adc8; font-size: 1.1rem;">Generate tailored, ready-to-post social media content powered by Gemini</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- Sidebar: API Configuration ---
with st.sidebar:
    st.header("⚙️ Configuration")

    # API Key Handling (Secret or Input)
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        api_key = st.text_input("Enter Gemini API Key:", type="password")
        st.caption(
            "Get your key from [Google AI Studio](https://aistudio.google.com/)."
        )
    else:
        st.success("API Key detected from environment!")

    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown(
        "- Be specific with your **Topic** for better results.\n"
        "- Match your **Tone** to the chosen **Platform**.\n"
        "- Try different audiences to tailor the messaging."
    )

# --- Main Layout: Input Form & Output Area ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Post Parameters")

    platform = st.selectbox(
        "Target Platform",
        [
            "LinkedIn",
            "Instagram",
            "Twitter / X",
            "Facebook",
            "YouTube Community",
            "Threads",
        ],
    )

    content_type = st.selectbox(
        "Content Type",
        [
            "Educational Post",
            "Promotional / Sales",
            "Storytelling / Personal",
            "Product Announcement",
            "Industry Insights / Tips",
            "Question / Engagement Hook",
        ],
    )

    topic = st.text_area(
        "Topic / Key Points",
        placeholder="e.g., 5 essential productivity tips for remote software engineers...",
        height=100,
    )

    target_audience = st.text_input(
        "Target Audience",
        placeholder="e.g., Small business owners, Software developers, Gen Z students",
    )

    tone = st.selectbox(
        "Tone of Voice",
        [
            "Professional & Authoritative",
            "Casual & Friendly",
            "Engaging & Witty",
            "Inspirational & Motivational",
            "Urgent & Persuasive",
            "Informative & Direct",
        ],
    )

    generate_btn = st.button("🚀 Generate Content")

with col2:
    st.subheader("🎯 Generated Output")

    if generate_btn:
        if not api_key:
            st.error(
                "Please provide a Gemini API key in the sidebar to proceed."
            )
        elif not topic:
            st.warning("Please enter a topic or key points for the content.")
        else:
            with st.spinner("✨ Crafting your perfect post..."):
                try:
                    # Configure Gemini API
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel("gemini-1.5-flash")

                    # Structured Prompt Construction
                    prompt = f"""
                    You are an expert social media manager and copywriter. Create a complete, highly engaging social media post based on the following parameters:

                    - **Platform**: {platform}
                    - **Content Type**: {content_type}
                    - **Topic**: {topic}
                    - **Target Audience**: {target_audience if target_audience else "General Audience"}
                    - **Tone**: {tone}

                    **Requirements**:
                    1. Format the output specifically for {platform} (respect character limits, readability, and structural best practices for this platform).
                    2. Include an attention-grabbing Hook.
                    3. Provide clear, value-driven Main Body content tailored to the audience.
                    4. Add a strong Call to Action (CTA).
                    5. Include 5-10 highly relevant and trending hashtags.

                    **Output Structure**:
                    ---
                    ### 🎯 Post Title / Hook
                    [Hook here]

                    ### 📝 Caption / Content
                    [Main Post Content]

                    ### 🏷️ Relevant Hashtags
                    [Hashtags]
                    ---
                    """

                    response = model.generate_content(prompt)
                    output_text = response.text

                    # Render output inside animated card container
                    st.markdown(
                        f"""
                        <div class="output-card">
                            {output_text}
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )

                    # Copy-friendly text box
                    st.markdown("---")
                    st.text_area(
                        "Plain Text (Easy Copy):",
                        value=output_text,
                        height=250,
                    )

                except Exception as e:
                    st.error(f"An error occurred while generating content: {e}")
    else:
        st.info("Fill in the parameters on the left and click **Generate Content** to see the magic!")