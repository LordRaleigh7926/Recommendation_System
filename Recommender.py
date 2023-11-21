import streamlit as st
from main import get_Rec, row_names
from PIL import Image

st.set_page_config(
    # page_title="Movie Recommender",
    page_icon="🎬"
)

img = Image.open("pic.jpg")

# st.image(img,"Photo by charlesdeluvio on Unsplash")
st.write("# Movie Recommender")
selection = st.selectbox(label="Choose a Movie", options=row_names)
st.divider()

if selection:
    for k,i in enumerate(row_names):
        if i == selection:
            selection = k
            break
    listOfMovies = get_Rec(selection)
    print(listOfMovies)

    for i,k in enumerate(listOfMovies[0]):

        name = row_names[k]
        comma = name.find(",")

        if comma != -1:
            index_of_bracket = name.find("(")
            c = name[comma+2:index_of_bracket]
            d = name[:comma]
            name = c+d+" "+name[index_of_bracket:]

        if  i == 0:
            st.write(f"### Recommendations for {name}:\n")
        else:
            st.write(f"{i}. {name}")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 