import streamlit as st
import requests


def send_request(code, max_length):
    api_url = 'https://main-code-gpt-python-scy6500.endpoint.ainize.ai/generate'
    files = {
        'code': (None, code),
        'max_length': (None, max_length),
    }
    response = requests.post(api_url, files=files)
    status_code = response.status_code

    return status_code, response


st.title("CodeGPT-Python Demo")
st.header("Generate python code using CodeGPT model")

length_slider = st.sidebar.slider("Max length", 0, 300)

code = st.text_input("Type Base Code", "def add(a, b):")
if st.button("Submit"):
    if length_slider == 0:
        st.warning("Please define the max length")
    else:
        status_code, response = send_request(code, length_slider)
        if status_code == 200:
            prediction = response.json()
            st.success(prediction["result"])
        else:
            st.error(str(status_code) + " Error")