
import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "KEYWORDS CLUSTERING", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main") #see other options as well



if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    # ---- READ   ----#
    authenticator.logout("Logout","sidebar")
    st.sidebar.title(f"Welcome {name}")
    pick_data_cl = st.checkbox(' SELECT KEYWORD DATA TO CLUSTER ')