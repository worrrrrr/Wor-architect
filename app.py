import streamlit as st
import google.generativeai as genai

# --- 1. SETTING & THEME (แต่งหน้าตาให้ 'สุนทร') ---
st.set_page_config(page_title="WOR ARCHITECT", page_icon="🗡️", layout="wide")

st.markdown("""
    <style>
    /* ปรับพื้นหลังและ Font */
    .main { background-color: #050505; color: #e0e0e0; }
    .stTextArea textarea { background-color: #111; color: #00ffcc; border: 1px solid #333; font-family: 'Courier New', monospace; }
    
    /* แต่งหัวข้อ */
    .title-text { font-family: 'serif'; font-size: 3rem; font-weight: bold; color: #ffffff; letter-spacing: 2px; }
    .subtitle-text { color: #888; font-style: italic; margin-bottom: 2rem; }
    
    /* กล่องคำตอบ (Truth Box) */
    .truth-box { 
        background-color: #0a0a0a; 
        border-left: 3px solid #00ffcc; 
        padding: 2rem; 
        border-radius: 0 10px 10px 0;
        box-shadow: 10px 10px 30px rgba(0,0,0,0.5);
    }
    .section-header { color: #00ffcc; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (ที่ใส่กุญแจ API) ---
with st.sidebar:
    st.markdown("### 🛠️ CONTROL PANEL")
    api_key = st.text_input("Gemini API Key", type="password", help="ไปเอา Key ได้ที่ Google AI Studio")
    st.write("---")
    st.caption("Admin: วรกฤช สุนทรธรรมนิติ")
    st.caption("Status: Hardware Optimized")

# --- 3. MAIN INTERFACE ---
st.markdown('<p class="title-text">🗡️ WOR ARCHITECT</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">The Sovereign Intelligence Hub | Alpha v1.6</p>', unsafe_allow_html=True)

# ช่องใส่ข้อมูล
raw_input = st.text_area("โยนความจริงดิบลงในช่อง [THE ABYSS]", height=200, placeholder="ระบุสิ่งที่ต้องการให้ 'กริช' เล่มนี้ชำแหละ...")

if st.button("EXECUTE TRINITY ENGINE"):
    if not api_key:
        st.error("ใส่ API Key ที่ Sidebar ก่อนครับ Admin")
    elif not raw_input:
        st.warning("The Abyss ว่างเปล่า... กรุณาใส่ข้อมูล")
    else:
        try:
            # เริ่มเชื่อมต่อ Gemini
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner("กริชกำลังทำงาน..."):
                # สั่ง AI ด้วย Trinity Logic
                prompt = f"""
                Analyze the following data as 'The Trinity Architect' for Admin 'วรกฤช':
                1. INTP Logic: Break it down to First Principles.
                2. INTJ/INFJ Vision: Find the hidden subtext/motives.
                3. ENTJ Execution: Give a cold, hard, actionable command.
                
                Data: {raw_input}
                """
                response = model.generate_content(prompt)
                
                # แสดงผลแบบสวยๆ
                st.markdown('<div class="truth-box">', unsafe_allow_html=True)
                st.markdown('<p class="section-header">[ RAW TRUTH REVEALED ]</p>', unsafe_allow_html=True)
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"System Error: {str(e)}")

# ฟุตเตอร์เท่ๆ
st.write("---")
st.caption("“Sovereignty through Intelligence.”")
