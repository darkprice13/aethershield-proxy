import streamlit as st
import requests
import pandas as pd
import os

st.set_page_config(page_title="Hades Net — MOTHER Core", page_icon="🔱", layout="wide")

# 🌐 DYNAMIC ROUTING MATRIX
# Automatically checks for cloud environment variables, Streamlit secrets, or defaults to local dev
if "API_URL" in st.secrets:
    API_URL = st.secrets["API_URL"]
else:
    API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

# Ensure the trailing slash is stripped safely
API_URL = API_URL.rstrip("/")