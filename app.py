import streamlit as st
from openai import OpenAI

# --- 1. [Raw Truth] Configuration ---
st.set_page_config(page_title="The Trinity Architect", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    stTextInput > div > div > input { background-color: #262730; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ The Trinity Architect: Alpha v1.1")
st.caption("Status: System Upgraded | Logic: OpenAI V1 Engine")

# --- 2. [Context] Security & Input ---
api_key = st.sidebar.text_input("Enter Architect Access Code (API Key)", type="password")

if api_key:
    # สร้าง Client แบบใหม่ (V1 Syntax)
    client = OpenAI(api_key=api_key)

    raw_input = st.text_area("โยนความจริงดิบลงในช่อง [The Abyss]:", height=200)

    if st.button("RUN TRINITY ENGINE"):
        if raw_input:
            with st.spinner("กำลังส่องกระจกสะท้อนความจริง..."):
                try:
                    # --- 3. [The Trinity Analysis] Logic Engine ---
                    system_prompt = """
                    คุณคือระบบ The Trinity Architect ทำงานภายใต้กฎ 3 ข้อ:
                    1. INTP (Logic Engine): ค้นหาช่องว่างทางตรรกะ และ First Principles
                    2. INFJ/INTJ (Visionary): มองหา Subtext และเป้าหมายที่แท้จริง
                    3. ENTJ (Commander): ตัดสิ่งที่ไม่จำเป็น (Ablation) และสั่งการที่จับต้องได้
                    ตอบกลับด้วยความจริงดิบ (Raw Truth) และความเด็ดขาดเชิงยุทธวิธี
                    """
                    
                    response = client.chat.completions.create(
                        model="gpt-4o", # อัปเกรดเป็นรุ่นที่ฉลาดและคุ้มค่ากว่า
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": f"ชำแหละสิ่งนี้: {raw_input}"}
                        ]
                    )
                    
                    analysis = response.choices[0].message.content

                    # --- 4. [Ablation & Output] ---
                    st.subheader("--- ผลลัพธ์จากการส่องกระจกสะท้อนความจริง ---")
                    st.markdown(analysis)
                    
                    st.divider()
                    st.info("จำไว้: ความจริงอาจเจ็บปวด แต่ความลวงนั้นอันตรายกว่า")
                except Exception as e:
                    st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
        else:
            st.warning("กรุณาใส่ข้อมูลลงใน The Abyss")
else:
    st.info("กรุณาใส่รหัสผ่าน (API Key) เพื่อเปิดใช้งานอาวุธแม่แบบ")
