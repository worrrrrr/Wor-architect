import streamlit as st
import google.generativeai as genai

# --- 1. Configuration ---
st.set_page_config(page_title="The Trinity Architect", layout="wide")
st.title("🏛️ The Trinity Architect: Alpha v1.3")
st.caption("Status: Calibrating Engine | Logic: Proprietary")

# --- 2. Security & Input ---
api_key = st.sidebar.text_input("Enter Architect Access Code (Gemini API Key)", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # ปรับชื่อรุ่นให้เป็นมาตรฐานที่ระบบยอมรับแน่นอน
        # ลองใช้ 'gemini-1.5-flash-latest' หรือ 'gemini-pro'
        model = genai.GenerativeModel('gemini-pro')

        raw_input = st.text_area("โยนความจริงดิบลงในช่อง [The Abyss]:", height=200)

        if st.button("RUN TRINITY ENGINE"):
            if raw_input:
                with st.spinner("สถาปัตยกรรมแห่งปัญญากำลังประมวลผล..."):
                    try:
                        system_instructions = """
                        คุณคือระบบ The Trinity Architect ทำงานภายใต้กฎ 3 ข้อ:
                        1. INTP (Logic Engine): ค้นหาช่องว่างทางตรรกะ และ First Principles
                        2. INFJ/INTJ (Visionary): มองหา Subtext และเป้าหมายที่แท้จริง
                        3. ENTJ (Commander): ตัดสิ่งที่ไม่จำเป็น (Ablation) และสั่งการที่จับต้องได้
                        ตอบกลับด้วยความจริงดิบ (Raw Truth) และความเด็ดขาดเชิงยุทธวิธี
                        """
                        
                        # ใช้โครงสร้างการส่งที่ปลอดภัยขึ้น
                        response = model.generate_content(
                            f"{system_instructions}\n\nชำแหละสิ่งนี้: {raw_input}"
                        )
                        
                        st.subheader("--- ผลลัพธ์จากการส่องกระจกสะท้อนความจริง ---")
                        st.markdown(response.text)
                        
                        st.divider()
                        st.info("สถานะ: การเชื่อมต่อสมบูรณ์ ความจริงถูกเปิดเผยแล้ว")
                    except Exception as e:
                        st.error(f"Error during generation: {e}")
                        st.write("ลองเปลี่ยนรุ่นเป็น 'gemini-pro' ใน Code ดูครับ")
            else:
                st.warning("กรุณาใส่ข้อมูลลงใน The Abyss")
    except Exception as e:
        st.error(f"Configuration Error: {e}")
else:
    st.info("กรุณาใส่ Gemini API Key เพื่อเปิดใช้งานอาวุธแม่แบบ")
