
# 🛡️ Secure Data Encryption System (Python + Streamlit)

A secure, in-memory data storage and retrieval system built using **Streamlit** and **Fernet encryption**. Users can store encrypted data with a unique passkey and retrieve it securely using the same key.

---

## 🚀 Features

- 🔐 **AES Encryption** using Python's `cryptography` library (Fernet)
- 🧠 **Hashed Passkeys** using SHA-256 (secure comparison)
- 📂 **In-Memory Storage** (no external database required)
- 🚫 **Login Lock** after 3 failed decryption attempts
- ✅ **Simple Reauthorization** via Login page
- 🖥️ **User-friendly UI** with Streamlit

---

## 📸 UI Pages

1. **Home** – Welcome page with info  
2. **Store Data** – Encrypt and save text with a passkey  
3. **Retrieve Data** – Decrypt data using your passkey  
4. **Login** – Reauthorization after failed attempts

---

## 🧠 How it Works

### ✅ Data Storage
- Users input **secret text** and a **passkey**
- Passkey is **hashed (SHA-256)** for comparison
- Text is **encrypted** using **Fernet**
- Data is saved in memory:

```python
stored_data = {
    "encrypted_text": {
        "encrypted_text": "...",
        "passkey": "hashed_passkey"
    }
}
```

---

### 🔍 Data Retrieval
- Users paste the **encrypted text** and **passkey**
- If valid → shows decrypted text  
- If invalid → increases attempt counter

---

### 🔒 Security Mechanism
- 3 wrong passkey attempts = redirect to **Login Page**
- Master login password (demo): `admin123`
- Login resets `failed_attempts` to 0

---

## 🧪 Technologies Used

- **Python 3.8+**
- **Streamlit**
- **cryptography (Fernet)**
- **hashlib (SHA-256)**

---

## 📦 Future Improvements (Bonus Ideas)

- [ ] Store encrypted data in **JSON file** for persistence
- [ ] Replace `admin123` with environment-based secrets
- [ ] Add **username-based login** for multi-user storage
- [ ] Add **timestamp lockout** feature

---

## 💡 How to Run

```bash
pip install streamlit cryptography
streamlit run main.py
```

> `main.py` = your main Python file

---

## 🤝 Author

Developed as part of a Python assignment using Streamlit & Encryption concepts.
By Shahid Ali

---

🎉 **Happy Coding!** 😎
