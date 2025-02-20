from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import streamlit as st


load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

st.title("시 작성 프로그램")

content = st.text_input("주제를 입력해주세요")

if st.button("시 작성"):
    with st.spinner("시 작성 중..."):
        result = llm.invoke(content + "에 대한 시를 작성해줘")
        st.write(result.content)

# if __name__ == "__main__":
#     main()

