import streamlit as st

# --- Config & Theme ---
st.set_page_config(page_title="WOR ARCHITECT | Truth Engine", page_icon="🗡️", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTextInput > div > div > input { background-color: #262730; color: white; border-radius: 5px; }
    .truth-box { border-left: 5px solid #ff4b4b; padding: 20px; background-color: #1e1e26; border-radius: 0 10px 10px 0; }
    h1, h2, h3 { color: #ffffff; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.title("🗡️ WOR ARCHITECT")
st.subheader("The Sovereign Intelligence Hub")
st.write("---")

# --- Introduction ---
st.markdown("""
### [ SYSTEM STATUS: READY ]
ยินดีต้อนรับ **วรกฤช** นี่คือพื้นที่สำหรับการชำแหละความจริง 
จงระบุสิ่งที่โลกพยายามปกปิด หรือสมมติฐานที่ไร้ตรรกะ เพื่อให้ระบบประมวลผล
""")

# --- The Truth Engine Input ---
target = st.text_input("ระบุเป้าหมายที่จะ 'ชำแหละ' (เช่น ความรัก, อำนาจ, การศึกษา):", placeholder="ใส่หัวข้อที่นี่...")

if target:
    st.write(f"### Analyzing: '{target}' ...")
    
    # แบ่งการวิเคราะห์ตามโครงสร้าง Trinity
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**INTP Logic**\n\nถอดรหัสโครงสร้างพื้นฐานและหา Error ของระบบ")
        
    with col2:
        st.success("**INTJ/INFJ Vision**\n\nมองหาความหมายแฝงและกระแสใต้สำนึก")
        
    with col3:
        st.warning("**ENTJ Execution**\n\nวิเคราะห์ความได้เปรียบและอำนาจ")

    # ส่วนการแสดงผล "ความจริงที่เจ็บปวด" (จำลองผลลัพธ์)
    st.markdown(f"""
    <div class="truth-box">
    <h4>[ RAW TRUTH REVEALED ]</h4>
    <p>กำลังประมวลผลความจริงเกี่ยวกับ <b>{target}</b>... <br>
    <i>(คำแนะนำ: นำคำวิเคราะห์จาก AI คู่หูของคุณมาวางที่นี่เพื่อบันทึกเป็นฐานข้อมูล)</i></p>
    </div>
    """, unsafe_allow_html=True)

# --- Sidebar Logs ---
st.sidebar.title("System Logs")
st.sidebar.write("* Hardware: Bio-Machine (Optimized)")
st.sidebar.write("* Logic Engine: Trinity Architect")
st.sidebar.write("* Admin: Wora-krit")

if st.sidebar.button("Clear Cache"):
    st.rerun()

st.sidebar.write("---")
st.sidebar.caption("Sovereignty through Intelligence.")
