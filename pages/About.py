import streamlit as st

st.set_page_config(
    # page_title="About",
    page_icon="🎬"

)

st.write("# About")
st.write("#### I'm a passionate coder and science enthusiast with a keen interest in technology. At 15, I've already delved into various programming languages, including Python, HTML, CSS, C++, Flask, and Flutter, ML and DL. As a Linux user, I enjoy exploring the intricacies of operating systems and customizing my computing experience.\n\nBeyond the digital realm, I'm an active individual who participates in various sports and extracurricular activities. I'm a badminton player, football enthusiast, and chess aficionado. Additionally, I'm a Cuber, solving Rubik's Cubes with speed and precision. My passion for knowledge extends to quizzing, where I enjoy testing my mental agility and expanding my understanding of diverse subjects.\n\nCurrently, I'm fascinated by the world of machine learning algorithms and deep learning. I'm eager to explore the potential of these technologies to solve real-world problems and make a positive impact on society.\n\nAs a young coder, I'm excited to continue learning and growing in the ever-evolving field of technology. I'm committed to using my skills to create innovative solutions that benefit others.")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 