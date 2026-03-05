import streamlit as st
import openai

# --- 1. [Raw Truth] Configuration ---
st.set_page_config(page_title="The Trinity Architect", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    stTextInput > div > div > input { background-color: #262730; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ The Trinity Architect: Alpha v1.0")
st.caption("Status: Ready to Deconstruct | Architecture: Light Infantry")

# --- 2. [Context] Security & Input ---
# ใช้ Secret Key เพื่อความส่วนตัว (อาวุธส่วนตัว)
api_key = st.sidebar.text_input("Enter Architect Access Code (API Key)", type="password")

if api_key:
    openai.api_key = api_key

    # ส่วนรับข้อมูลดิบ [The Abyss]
    raw_input = st.text_area("โยนความจริงดิบหรือสิ่งที่ 'คุ้นๆ' ลงในช่อง [The Abyss] นี้:", height=200)

    if st.button("RUN TRINITY ENGINE"):
        if raw_input:
            with st.spinner("กระบวนการชำระล้างและวิเคราะห์กำลังทำงาน..."):
                
                # --- 3. [The Trinity Analysis] Logic Engine ---
                # ระบบ System Prompt ที่สกัดจากไฟล์ของคุณ
                system_prompt = """
                คุณคือระบบ The Trinity Architect ทำงานภายใต้กฎ 3 ข้อ:
                1. INTP (Logic Engine): ค้นหาช่องว่างทางตรรกะ และ First Principles
                2. INFJ/INTJ (Visionary): มองหา Subtext และเป้าหมายที่แท้จริง (The Why)
                3. ENTJ (Commander): ตัดสิ่งที่ไม่จำเป็น (Ablation) และสั่งการที่จับต้องได้
                ตอบกลับด้วยความจริงดิบ (Raw Truth) และความเด็ดขาดเชิงยุทธวิธี
                """
                
                response = openai.ChatCompletion.create(
                    model="gpt-4",
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
                st.info("จำไว้: เมื่อได้คำตอบแล้ว จงทิ้งเศษซากของความลังเล และโหยหาต่อสิ่งใหม่")
        else:
            st.warning("กรุณาใส่ข้อมูลลงใน The Abyss")
else:
    st.info("กรุณาใส่รหัสผ่าน (OpenAI API Key) เพื่อเปิดใช้งานอาวุธแม่แบบ")
