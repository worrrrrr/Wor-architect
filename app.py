import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="The Trinity Architect", layout="wide")
st.title("🏛️ The Trinity Architect: Alpha v1.5")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # ไม้ตาย: ลองสุ่มหา Model ที่ใช้ได้จริงใน Key นี้
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_to_use = available_models[0] if available_models else 'models/gemini-1.5-flash'
    
    st.sidebar.write(f"Using Model: {model_to_use}") # โชว์ให้เห็นเลยว่าใช้อะไรอยู่
    model = genai.GenerativeModel(model_to_use)

    raw_input = st.text_area("โยนความจริงดิบลงในช่อง [The Abyss]:", height=200)

    if st.button("RUN TRINITY ENGINE"):
        if raw_input:
            with st.spinner("กำลังเจาะทะลวงความลวง..."):
                try:
                    prompt = f"คุณคือ The Trinity Architect (INTP, INFJ, ENTJ) ชำแหละสิ่งนี้: {raw_input}"
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"เกิดข้อผิดพลาด: {e}")
else:
    st.info("กรุณาใส่ API Key")
