import streamlit as st
import string
import random
import re

# Set page configuration
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="centered"
)

# Initialize session state for dark mode
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False  # Default is Light Mode

# Toggle Dark Mode Button
if st.button("🌙 Dark Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode  # Toggle state
 
# Custom CSS for full dark mode
dark_style = """
    <style>
    body, .main, .stApp {
        background-color: #121212 !important;
        color: #FFFFFF !important;
    }
    .stTextInput > div > div > input, .stCode {
        background-color: #333 !important;
        color: #fff !important;
    }
    .stButton > button {
        background-color: #444 !important;
        color: white !important;
        border: 1px solid white !important;
    }
    .stSlider > div {
        background-color: #444 !important;
    }
    .stMarkdown, .stTitle, .stHeader {
        color: #FFFFFF !important;
    }
    .stTabs [role="tab"], label {
        color: white !important;
    }
    </style>
"""

light_style = """
    <style>
    body, .main, .stApp {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    .stTextInput > div > div > input, .stCode {
        background-color: #FFF !important;
        color: #000 !important;
    }
    .stButton > button {
        background-color: #EEE !important;
        color: black !important;
        border: 1px solid black !important;
    }
    .stSlider > div {
        background-color: #ddd !important;
    }
    .stMarkdown, .stTitle, .stHeader {
        color: #000000 !important;
    }
    .stTabs [role="tab"], label {
        color: black !important;
    }
    </style>
"""

# Apply Dark Mode if enabled
if st.session_state.dark_mode:
    st.markdown(dark_style, unsafe_allow_html=True)
else:
    st.markdown(light_style, unsafe_allow_html=True)

# Title and description
st.title("🔒 Password Strength Meter")
st.markdown("### Check your password strength or generate a secure one!")

def check_password_strength(password):
    """Calculate password strength score and return feedback"""
    score = 0
    feedback = []
    
    # List of common passwords
    common_passwords = ["123456", "password", "qwerty", "abc123", "password1"]
    
    if password in common_passwords:
        return "Very Weak", ["❌ Your password is too common! Try a stronger one."]
    
    # Length check
    if len(password) >= 8:
        score += 2
        feedback.append("✅ Length is good.")
    else:
        feedback.append("❌ Should be at least 8 characters long.")
    
    # Check for numbers
    if re.search(r"\d", password):
        score += 2
        feedback.append("✅ Should include at least one number.")
    else:
        feedback.append("❌ Should include at least one number.")
    
    # Check for uppercase
    if re.search(r"[A-Z]", password):
        score += 2
        feedback.append("✅ Should include at least one uppercase letter.")
    else:
        feedback.append("❌ Should include at least one uppercase letter.")
    
    # Check for lowercase
    if re.search(r"[a-z]", password):
        score += 2
        feedback.append("✅ Should include at least one lowercase letter.")
    else:
        feedback.append("❌ Should include at least one lowercase letter.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
        feedback.append("✅ Should include at least one special character.")
    else:
        feedback.append("❌ Should include at least one special character.")
    
    strength_labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return strength_labels[min(score // 2, 4)], feedback

def generate_password(length=12):
    """Generate a strong random password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Create two tabs
tab1, tab2 = st.tabs(["Check Password", "Generate Password"])

with tab1:
    # Password input
    password = st.text_input("Enter your password", type="password")
    
    if password:
        strength, feedback = check_password_strength(password)
        
        # Display strength meter
        strength_colors = {"Very Weak": "#ff4444", "Weak": "#ffbb33", "Moderate": "#ffeb3b", "Strong": "#00C851", "Very Strong": "#007E33"}
        
        st.markdown(f"""
            <div class="password-strength" style="background-color: {strength_colors[strength]};">
                <h3 style="color: white; margin: 0;">Strength: {strength}</h3>
            </div>
        """, unsafe_allow_html=True)

        # Display feedback
        st.markdown("### Password Analysis:")
        for item in feedback:
            st.markdown(item)

with tab2:
    st.markdown("### Generate a Strong Password")
    
    # Password length slider
    length = st.slider("Password Length", min_value=8, max_value=32, value=12)
    
    if st.button("Generate Password"):
        generated_password = generate_password(length)
        st.code(generated_password)

# Footer
st.markdown("--------------------------------")
st.markdown("Made with ❤️ by Shahid Ali")
<<<<<<< HEAD

=======

>>>>>>> d7cc499768b54f50cc3151e63c11a84e76875ada
