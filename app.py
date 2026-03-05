import streamlit as st
import google.generativeai as genai

# --- 1. Configuration ---
st.set_page_config(page_title="The Trinity Architect", layout="wide")
st.title("🏛️ The Trinity Architect: Alpha v1.4")
st.caption("Status: Forced Calibration | Engine: Gemini 1.5 Flash")

# --- 2. Security & Input ---
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # ใช้ชื่อรุ่นที่ระบุเจาะจงและเป็นปัจจุบันที่สุด
        model = genai.GenerativeModel('gemini-1.5-flash-latest') 

        raw_input = st.text_area("โยนความจริงดิบลงในช่อง [The Abyss]:", height=200)

        if st.button("RUN TRINITY ENGINE"):
            if raw_input:
                with st.spinner("ระบบกำลังชำระล้างข้อมูลดิบ..."):
                    try:
                        system_instructions = """
                        คุณคือระบบ The Trinity Architect:
                        1. INTP: ค้นหาช่องว่างทางตรรกะ และ First Principles
                        2. INFJ/INTJ: มองหา Subtext และเป้าหมายที่แท้จริง
                        3. ENTJ: ตัดสิ่งที่ไม่จำเป็น (Ablation) และสั่งการที่จับต้องได้
                        ตอบกลับด้วยความจริงดิบ (Raw Truth) และความเด็ดขาดเชิงยุทธวิธี
                        """
                        
                        response = model.generate_content(
                            f"{system_instructions}\n\nชำแหละสิ่งนี้: {raw_input}"
                        )
                        
                        st.subheader("--- ผลลัพธ์จากการส่องกระจกสะท้อนความจริง ---")
                        st.markdown(response.text)
                        
                        st.divider()
                        st.info("Status: Online | No more excuses.")
                    except Exception as e:
                        st.error(f"Error during generation: {e}")
            else:
                st.warning("กรุณาใส่ข้อมูลลงใน The Abyss")
    except Exception as e:
        st.error(f"Configuration Error: {e}")
else:
    st.info("กรุณาใส่ Gemini API Key เพื่อเปิดใช้งานอาวุธแม่แบบ")
