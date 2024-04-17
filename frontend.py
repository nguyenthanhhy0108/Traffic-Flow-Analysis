import streamlit as st
import requests

# Streamlit UI
def main():
    st.title("Ứng dụng xử lý video")

    uploaded_file = st.file_uploader("Chọn một video", type=["mp4"])
    if uploaded_file is not None:
        if st.button("Xử lý video"):

            response = requests.post("http://localhost:8080/process_video", files={"video": uploaded_file})
            if response.status_code == 200:

                st.write("Kết quả xử lý:", response.json()["result"])
            else:
                st.error("Có lỗi xảy ra khi xử lý video.")

if __name__ == "__main__":
    main()
