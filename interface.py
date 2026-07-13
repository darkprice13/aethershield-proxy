import streamlit as st
import pandas as pd
import asyncio
from proxy_engine import AetherShieldEngine

# Page configurations matching the signature luxury theme
st.set_page_config(page_title="Hades Net — MOTHER Core", page_icon="🔱", layout="wide")

# SSO Identity Management Logic
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def check_identity():
    if st.session_state["access_token"] == "HADES-99-AX":
        st.session_state.authenticated = True
    else:
        st.error("🚫 INVALID CLEARANCE TOKEN. ACCESS DENIED.")

# Custom UI Luxury Styling Matrices
st.markdown("""
    <style>
    .main { background-color: #0A0A0C !important; color: #E6E8EA !important; }
    [data-testid="stSidebar"] { background-color: #111115 !important; border-right: 2px solid #D4AF37 !important; }
    h1, h2, h3 { color: #D4AF37 !important; font-family: 'Courier New', monospace !important; font-weight: 700 !important; }
    .stTextArea textarea { background-color: #16161A !important; color: #FFFFFF !important; border: 1px solid #3A3A42 !important; }
    .stButton>button { 
        background: linear-gradient(135deg, #FFD700 0%, #D4AF37 100%) !important; 
        color: #000000 !important; font-weight: bold !important; font-family: 'Courier New', monospace !important; width: 100%;
        border: none !important; padding: 10px !important;
    }
    .gold-divider { height: 2px; background: linear-gradient(90deg, transparent, #D4AF37, transparent); margin: 25px 0; }
    .metric-box { background-color: #111115; border: 1px solid #D4AF37; padding: 15px; border-radius: 5px; text-align: center; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# 🔱 SSO ACCESS GATEWAY SHIELD
if not st.session_state.authenticated:
    st.title("🔱 HADES NET // ACCESS GATEWAY")
    st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
    with st.container():
        st.info("SYSTEM CLASSIFICATION: TOP SECRET // CORPORATE SSO CLEARANCE REQUIRED")
        st.text_input("ENTER ENTERPRISE ACCESS TOKEN", type="password", key="access_token")
        st.button("AUTHORIZE PERIMETER ENTRY", on_click=check_identity)
    st.stop()

# --- COGNITIVE CORE INITIALIZATION ---
if 'shield' not in st.session_state:
    st.session_state.shield = AetherShieldEngine()

if 'current_session' not in st.session_state:
    # Safely spin up a persistent dynamic masking workspace vault
    st.session_state.current_session = asyncio.run(st.session_state.shield.initialize_session())

if 'compliance_db' not in st.session_state:
    st.session_state.compliance_db = [
        {"Timestamp": "2026-07-10 14:22:10", "Asset Type": "CREDIT_CARD_PAN", "Risk Level": "CRITICAL", "Framework Vulnerability": "PCI-DSS", "Est. Fine Avoided": "$250,000"},
        {"Timestamp": "2026-07-11 09:04:45", "Asset Type": "INTERNATIONAL_IBAN", "Risk Level": "HIGH", "Framework Vulnerability": "DORA Article 6", "Est. Fine Avoided": "$110,000"},
        {"Timestamp": "2026-07-12 16:41:19", "Asset Type": "CORP_ASSET", "Risk Level": "MEDIUM", "Framework Vulnerability": "NDA / IP Leak", "Est. Fine Avoided": "$85,000"}
    ]

# --- CONTROL SIDEBAR ---
with st.sidebar:
    st.markdown("## 🔱 HADESNET SYSTEM")
    st.markdown("### `IDENTITY: ETHAN PRICE` ")
    st.markdown(f"### `TRACE TRACE_ID: {st.session_state.current_session}`")
    st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
    if st.button("LOGOUT PERIMETER"):
        st.session_state.authenticated = False
        st.rerun()

# --- MASTER DASHBOARD DISPLAY ---
st.title("🔱 HADESNET — FINANCIAL RECLAMATION PROTOCOL")
st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)

# Performance Ledger Tiers
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1:
    st.markdown("<div class='metric-box'><h3>PROXY STREAM STATUS</h3><p style='color:#00FF66; font-size:24px; font-weight:bold; margin:0;'>ACTIVE INGESTION</p></div>", unsafe_allow_html=True)
with m_col2:
    st.markdown("<div class='metric-box'><h3>REGULATORY INTERCEPTS</h3><p style='color:#D4AF37; font-size:24px; font-weight:bold; margin:0;'>1,482 BLOCKS</p></div>", unsafe_allow_html=True)
with m_col3:
    st.markdown("<div class='metric-box'><h3>LIABILITY SECURED</h3><p style='color:#D4AF37; font-size:24px; font-weight:bold; margin:0;'>$445,000 USD</p></div>", unsafe_allow_html=True)

# Live Test Bench Intercept Framework
st.markdown("## 🛠️ LIVE METRIC INTERCEPT ENTRYWAY")
raw_input = st.text_area(
    "INBOUND RAW DATA STREAM (Include sensitive numbers or configurations to test the proxy filtration)", 
    height=120,
    value="Internal transaction batch notification: Processing settlement via routing node DE89370400440532013000 to cover liabilities associated with corporate execution."
)

if st.button("RUN PERIMETER INTERCEPT"):
    if raw_input:
        sanitized_result = asyncio.run(
            st.session_state.shield.secure_inbound_payload(st.session_state.current_session, raw_input)
        )
        st.session_state['last_sanitized_payload'] = sanitized_result
        st.success("🔒 EDGE FILTER COMPLETE: SENSITIVE STRINGS CONVERTED TO CRYPTOGRAPHIC PLACEHOLDERS")
    else:
        st.warning("Payload vector stream cannot be empty.")

# Show out-of-band proxy transformations if active
if 'last_sanitized_payload' in st.session_state:
    st.markdown("### 📡 OUTBOUND COMPLIANT STREAM (What the public LLM model sees):")
    st.code(st.session_state['last_sanitized_payload'], language="text")
    
    st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
    
    st.markdown("## 🔄 DE-TOKENIZATION OUTBOUND RESPONSE TEST")
    simulated_ai_reply = st.text_area(
        "SIMULATED RESPONSIVE INBOUND PAYLOAD", 
        value=f"Transaction validated for placeholder targets matching {st.session_state['last_sanitized_payload']}."
    )
    
    if st.button("RESTORE RESPONSES"):
        try:
            reconstructed_text = asyncio.run(
                st.session_state.shield.restore_outbound_payload(st.session_state.current_session, simulated_ai_reply)
            )
            st.markdown("### 🔓 DE-CRYPTED LOCAL CLEAR TEXT (What your internal user sees):")
            st.info(reconstructed_text)
        except Exception as err:
            st.error(f"Vault error restoring trace session metrics: {err}")

# Persistent Regulatory Audit Trail Table
st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
st.markdown("## 📊 HISTORICAL AUDIT & COMPLIANCE THREAT LEDGER")
st.dataframe(pd.DataFrame(st.session_state.compliance_db), use_container_width=True)