import streamlit as st
import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import plotly.graph_objects as go

with open("styles.css", "r", encoding="utf-8") as f:
    spinner_css = f.read()

st.markdown(f'<style>{spinner_css}</style>', unsafe_allow_html=True)

plt.switch_backend("Agg")

def main():
    root_path = os.getcwd()
    st.title("Thống kê giao thông")

    uploaded_file = st.file_uploader("Chọn một video", type=["mp4"])
    if uploaded_file is not None:
        if st.button("Xử lý video"):

            spinner_markdown = st.markdown('<div class="custom-spinner-overlay"><div class="custom-spinner"></div></div>',
                                            unsafe_allow_html=True)

            response = requests.post("http://localhost:8080/process_video", files={"video": uploaded_file})
            if response.status_code == 200:
                spinner_markdown.empty()
                st.success(response.json()["result"])

                rate = response.json()["rate"]

                number_of_violator = response.json()["number_of_violator"]
                total_people = response.json()["total_people"]

                colors = ['#ff7f0e', '#1f77b4']

                data = pd.DataFrame({
                    'Category': ['Số người vi phạm', 'Tổng số ngời'],
                    'Value': [number_of_violator, total_people]
                })

                fig, ax = plt.subplots()
                ax.barh(data['Category'], data['Value'], color=colors)

                st.pyplot(fig)

                fig = go.Figure(data=[go.Pie(labels=["Tỉ lệ người vi phạm", "Tỉ lệ không vi phạm"], values=[rate, 1 - rate])])

                st.plotly_chart(fig)

                violator = response.json()["violator"]

                image_paths = []

                for path in violator:
                    image_paths.append(os.path.join(root_path + "\output_images", path))
                
                st.write("Ảnh người vi phạm")
                
                num_images = len(violator)
                num_columns = 3
                num_rows = (num_images + num_columns - 1) // num_columns

                for i in range(num_rows):
                    cols = st.columns(num_columns)
                    for j in range(num_columns):
                        index = i * num_columns + j
                        if index < num_images:
                            image = mpimg.imread(image_paths[index])
                            cols[j].image(image, caption="Ảnh " + f"{index}", use_column_width=True)

            else:
                st.error("Có lỗi xảy ra khi xử lý video.")
                spinner_markdown.empty()

if __name__ == "__main__":
    main()
