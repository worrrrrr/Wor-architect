import streamlit as st

# --- Config & Theme ---
st.set_page_config(page_title="WOR ARCHITECT | Truth Engine", page_icon="🗡️", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTextInput > div > div > input { background-color: #262730; color: white; border-radius: 5px; }
    .truth-box { border-left: 5px solid #ff4b4b; padding: 25px; background-color: #1e1e26; border-radius: 0 15px 15px 0; line-height: 1.6; }
    .logic-header { color: #ff4b4b; font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #333; padding-bottom: 5px; }
    h1, h2, h3 { color: #ffffff; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.title("🗡️ WOR ARCHITECT")
st.subheader("The Sovereign Intelligence Hub")
st.write("---")

# --- Introduction ---
st.markdown(f"### [ SYSTEM STATUS: READY ]")
st.write(f"ยินดีต้อนรับ **วรกฤช** นี่คือพื้นที่สำหรับการชำแหละความจริง จงระบุสิ่งที่โลกพยายามปกปิด เพื่อให้ระบบประมวลผล")

# --- Truth Database (Logic Repository) ---
# เราสามารถเพิ่มหัวข้อใหม่ๆ ลงใน Dictionary นี้ได้เรื่อยๆ
truth_db = {
    "INTP": {
        "logic": "Analysis Paralysis Bug: ติดลูปการเก็บข้อมูลเพื่อหนีความผิดพลาดในโลกจริง",
        "vision": "Existential Loneliness: ใช้ตรรกะเป็นเกราะกำบังความอ่อนไหวต่อความไร้ระเบียบของโลก",
        "exec": "Patch 1.0: ต้องบังคับ Output ผ่านเครื่องมือดิจิทัลเพื่อเปลี่ยนจาก 'นักคิด' เป็น 'สถาปนิก'"
    }
}

# --- Input Area ---
target = st.text_input("ระบุเป้าหมายที่จะ 'ชำแหละ':", placeholder="เช่น INTP, ความรัก, อำนาจ...")

if target:
    st.write(f"### Analyzing: '{target}' ...")
    
    col1, col2, col3 = st.columns(3)
    
    # ดึงข้อมูลจากฐานข้อมูล ถ้าไม่มีให้ใช้ค่า Default
    data = truth_db.get(target.upper(), {
        "logic": "กำลังถอดรหัสโครงสร้างพื้นฐาน...",
        "vision": "กำลังมองหาความหมายแฝง...",
        "exec": "กำลังวิเคราะห์ความได้เปรียบ..."
    })

    with col1:
        st.info(f"**INTP Logic**\n\n{data['logic']}")
    with col2:
        st.success(f"**INTJ/INFJ Vision**\n\n{data['vision']}")
    with col3:
        st.warning(f"**ENTJ Execution**\n\n{data['exec']}")

    # --- Raw Truth Section ---
    st.markdown('<div class="truth-box">', unsafe_allow_html=True)
    st.markdown(f"#### [ RAW TRUTH REVEALED: {target.upper()} ]")
    
    if target.upper() == "INTP":
        st.markdown("""
        **System Analysis Result:** INTP ไม่ใช่เครื่องจักรที่สมบูรณ์แบบ แต่เป็นระบบที่ *จงใจรันช้า* เพื่อป้องกัน Error 
        การที่ **วรกฤช** สร้าง Hub นี้ขึ้นมา คือการทำ **Manual Override** ครั้งสำคัญ 
        เพื่อเปลี่ยนสถานะจาก 'Observer' เป็น 'Architect' อย่างเต็มรูปแบบ
        """)
    else:
        st.write("รหัสผ่านไม่ถูกต้อง หรือยังไม่มีข้อมูลใน Database... โปรดรอการอัปเดตจาก Admin")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("System Logs")
st.sidebar.write("● Hardware: Bio-Machine (Optimized)")
st.sidebar.write("● Logic Engine: Trinity Architect")
st.sidebar.write(f"● Admin: Wora-krit")
st.sidebar.write("---")
st.sidebar.caption("Sovereignty through Intelligence.")
