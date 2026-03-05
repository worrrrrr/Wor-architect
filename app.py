import streamlit as st
import google.generativeai as genai

# --- 1. Configuration ---
st.set_page_config(page_title="The Trinity Architect (Gemini Edition)", layout="wide")
st.title("🏛️ The Trinity Architect: Alpha v1.2")
st.caption("Status: Powered by Gemini Engine | Logic: Proprietary")

# --- 2. Security & Input ---
api_key = st.sidebar.text_input("Enter Architect Access Code (Gemini API Key)", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash') # หรือใช้ gemini-1.5-pro

    raw_input = st.text_area("โยนความจริงดิบลงในช่อง [The Abyss]:", height=200)

    if st.button("RUN TRINITY ENGINE"):
        if raw_input:
            with st.spinner("Gemini กำลังส่องกระจกสะท้อนความจริง..."):
                try:
                    system_instructions = """
                    คุณคือระบบ The Trinity Architect:
                    1. INTP (Logic Engine): ค้นหาช่องว่างทางตรรกะ และ First Principles
                    2. INFJ/INTJ (Visionary): มองหา Subtext และเป้าหมายที่แท้จริง
                    3. ENTJ (Commander): ตัดสิ่งที่ไม่จำเป็น (Ablation) และสั่งการที่จับต้องได้
                    ตอบกลับด้วยความจริงดิบ (Raw Truth) และความเด็ดขาดเชิงยุทธวิธี
                    """
                    
                    response = model.generate_content(f"{system_instructions}\n\nชำแหละสิ่งนี้: {raw_input}")
                    
                    st.subheader("--- ผลลัพธ์จากการส่องกระจกสะท้อนความจริง ---")
                    st.markdown(response.text)
                    
                    st.divider()
                    st.info("จำไว้: ความจริงคืออาวุธที่คมที่สุด")
                except Exception as e:
                    st.error(f"เกิดข้อผิดพลาด: {e}")
else:
    st.info("กรุณาใส่รหัสผ่าน (Gemini API Key) เพื่อเปิดใช้งานอาวุธแม่แบบ")
