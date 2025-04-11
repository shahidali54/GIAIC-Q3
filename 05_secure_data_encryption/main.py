import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate and store encryption key
if 'KEY' not in st.session_state:
    st.session_state.KEY = Fernet.generate_key()

cipher = Fernet(st.session_state.KEY)

# Initialize session state for storage
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

# Hash passkey using SHA-256
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt plain text
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt and validate
def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)

    for data in st.session_state.stored_data.values():
        if data["encrypted_text"] == encrypted_text and data["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    
    st.session_state.failed_attempts += 1
    return None

# UI Starts
st.title("🛡️ Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to Secure Storage App")
    st.markdown("Store and retrieve encrypted data securely using a unique passkey.")

elif choice == "Store Data":
    st.subheader("📂 Store Your Data")
    user_data = st.text_area("Enter your secret data:")
    passkey = st.text_input("Set a passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            encrypted = encrypt_data(user_data)
            hashed = hash_passkey(passkey)
            st.session_state.stored_data[encrypted] = {
                "encrypted_text": encrypted,
                "passkey": hashed
            }
            st.success("✅ Data encrypted and saved securely!")
            st.text_area("Here's your Encrypted Text (save it to retrieve later):", value=encrypted, height=100)
        else:
            st.error("⚠️ Please provide both data and passkey.")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    
    if st.session_state.failed_attempts >= 3:
        st.warning("🔒 Too many failed attempts. Please reauthorize.")
        st.switch_page("Login")

    encrypted_input = st.text_area("Paste your Encrypted Text:")
    passkey_input = st.text_input("Enter your Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey_input:
            decrypted = decrypt_data(encrypted_input, passkey_input)

            if decrypted:
                st.success("✅ Decryption Successful!")
                st.write("🔓 Decrypted Data:")
                st.code(decrypted)
            else:
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {remaining}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("Redirecting to Login...")
                    st.st.rerun()
        else:
            st.error("⚠️ Please enter both encrypted data and passkey.")

elif choice == "Login":
    st.subheader("🔑 Reauthorize Access")
    master_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if master_pass == "admin123": 
            st.session_state.failed_attempts = 0
            st.success("✅ Reauthorized. Try again now.")
        else:
            st.error("❌ Wrong master password.")
