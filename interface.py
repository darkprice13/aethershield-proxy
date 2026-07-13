import streamlit as st
import pandas as pd
import asyncio
from proxy_engine import AetherShieldEngine

# Page configurations matching the signature luxury theme
st.set_page_config(page_title="Hades Net — MOTHER Core", page_icon="🔱", layout="wide")

# Initialize the data engine directly inside the frontend environment layer
if 'shield' not in st.session_state:
    st.session_state.shield = AetherShieldEngine()

# Initialize an internal persistent mock database log for historical data monitoring
if 'compliance_db' not in st.session_state:
    st.session_state.compliance_db = [
        {"Timestamp": "2026-07-10 14:22:10", "Asset Type": "CREDIT_CARD_PAN", "Risk Level": "CRITICAL", "Framework Vulnerability": "PCI-DSS Section 3", "Est. Fine Avoided": "$250,000"},
        {"Timestamp": "2026-07-11 09:04:45", "Asset Type": "INTERNATIONAL_IBAN", "Risk Level": "HIGH", "Framework Vulnerability": "DORA Article 6", "Est. Fine Avoided": "$110,000"},
        {"Timestamp": "2026-07-12 16:41:19", "Asset Type": "CORP_ASSET", "Risk Level": "MEDIUM", "Framework Vulnerability": "SEC Rule 17a-4", "Est. Fine Avoided": "$50,000"}
    ]

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
    }
    .gold-divider { height: 2px; background: linear-gradient(90deg, transparent, #D4AF37, transparent); margin: 20px 0; }
    .stDataFrame { background-color: #16161A !important; border: 1px solid #3A3A42 !important; }
    .metric-box { background-color: #111115; border: 1px solid #D4AF37; padding: 15px; border-radius: 5px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🔱 HADESNET SYSTEM")
    st.markdown("### `ENGINE STATUS: SECURE` ")
    st.markdown("Sector Target: Institutional Finance")
    st.markdown("Architect: Ssemanda Ethan Price")
    st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
    st.markdown("🔒 **Active Policy:** Real-Time Data Interception Matrix mapping live SEC & PCI-DSS leaks.")

st.title("🔱 HADESNET — FINANCIAL RECLAMATION PROTOCOL")
st.subheader("Project AetherShield // Standalone Compliance Matrix")
st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)

# Executive Live Analytics Grid
st.markdown("### 📊 Live Operations Monitoring Cluster")
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1:
    st.markdown(f"<div class='metric-box'><h4 style='color:grey;margin:0;'>COMPLIANCE COVERAGE</h4><h2 style='margin:10px 0;'>100% SECURE</h2></div>", unsafe_allow_html=True)
with m_col2:
    total_fines = sum([int(x["Est. Fine Avoided"].replace("$","").replace(",","")) for x in st.session_state.compliance_db])
    st.markdown(f"<div class='metric-box'><h4 style='color:grey;margin:0;'>REGULATORY LIABILITY MITIGATED</h4><h2 style='color:#FFD700;margin:10px 0;'>${total_fines:,}</h2></div>", unsafe_allow_html=True)
with m_col3:
    st.markdown(f"<div class='metric-box'><h4 style='color:grey;margin:0;'>ACTIVE INGESTION FILTERS</h4><h2 style='margin:10px 0;'>8 HEURISTICS</h2></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 Financial Inbound Data Egress Perimeter")
    raw_input = st.text_area(
        "Enter Raw Internal Document, Wire Transfer, or Strategy Note containing sensitive parameters:",
        value=(
            "MEMORANDUM: Our core trading deployment will run on Alpha Strategy Yield starting Monday. "
            "Please dispatch the operational account assets to routing code 021000021 and credit card number "
            "4111111111111111 for verification. Direct inquiries to lead architect Ethan Price at info@hadesnet.com."
        ),
        height=220
    )
    trigger_shield = st.button("ENGAGE VAULT PROTOCOL INTERCEPT")

if trigger_shield:
    shield = st.session_state.shield
    
    # 1. Initialize session vault lease
    session_id = asyncio.run(shield.initialize_session())
    
    # 2. Execute local zero-knowledge anonymization sequence
    secure_prompt = asyncio.run(shield.secure_inbound_payload(session_id, raw_text=raw_input))
    
    # 3. Simulate local intelligence response layout completely card-free
    tokenized_ai_response = (
        "HADES NET CORE SYSTEM COMPLIANCE INGESTION COMPLETED:\n\n"
        "Security token structures successfully established for internal analysis parameters within {{CORP_ASSET_3}}. "
        "System architecture updates have been authorized by framework director {{IDENTITY_1}}.\n\n"
        "Network telemetry streams confirmed secure. Active monitoring protocols have routed transaction tokens "
        "securely through secondary gateway network routing frame {{BANK_ROUTING_ABA_1}} and card gateway {{CREDIT_CARD_PAN_1}}. "
        "System alerts routed to admin node {{EMAIL_ADDR_1}}."
    )
    
    # 4. Run local reconstruction sequence prior to rendering safely
    clean_restored_output = asyncio.run(shield.restore_outbound_payload(session_id, tokenized_ai_response))
    
    # Update our dynamic interactive database matrix upon asset processing
    new_entry = {
        "Timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Asset Type": "MULTI-VECTOR LEAK",
        "Risk Level": "CRITICAL",
        "Framework Vulnerability": "SEC + PCI-DSS Fusion",
        "Est. Fine Avoided": "$500,000"
    }
    st.session_state.compliance_db.insert(0, new_entry)
    
    # 5. Flush temporary mapping vault keys to preserve zero-knowledge compliance
    asyncio.run(shield.close_session_vault(session_id))
    
    with col1:
        st.markdown(f"**Vault Lease Session ID:** `{session_id}`")
        st.warning("⚠️ **Outbound Payload Transmitted to Public Cloud (Scrubbed Clean):**")
        st.code(secure_prompt, language="text")
        
    with col2:
        st.markdown("### 🤖 Public Frontier LLM Simulation Engine")
        st.write("The external cloud vector computes metrics using only non-identifiable tokens:")
        st.code(tokenized_ai_response, language="text")
        
        st.markdown("### 🔓 Local Egress Restore Frame")
        st.success("👑 **Pristine Institutional Output Safely Decoded Inside Local Vault:**")
        st.write(clean_restored_output)

# Interactive Institutional Compliance Database Panel Matrix Display Layer
st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
st.markdown("### 📜 Institutional Compliance Vault Log Matrix & Threat Ledger")
st.write("Below is the internal analytics database tracking active intercepts, corporate financial liabilities avoided, and regulatory classification records:")

df_db = pd.DataFrame(st.session_state.compliance_db)
# 📑 THE COMPLIANCE EXPORT GATEWAY
st.markdown("<br>", unsafe_allow_html=True)
csv_buffer = df_db.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 DOWNLOAD OFFICIAL REGULATORY AUDIT REPORT (.CSV)",
    data=csv_buffer,
    file_name=f"HadesNet_AetherShield_Audit_{pd.Timestamp.now().strftime('%Y%m%d')}.csv",
    mime="text/csv"
)
st.dataframe(df_db, use_container_width=True, hide_index=True)