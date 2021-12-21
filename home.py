# -*- coding: utf-8 -*-
import streamlit as st
import PIL
from PIL import Image, ImageOps
# importing predicting color function
from color_classifier import predict_color
from PIL import Image

# display image with the size and rgb color


def display_image():
    img = Image.new("RGB", (200, 200), color=(Red, Green, Blue))
    img = ImageOps.expand(img, border=1, fill='black')  # border to the img
    st.image(img, caption='RGB Color')


if __name__ == "__main__":
    hide_st_style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    st.sidebar.title("About")
    st.sidebar.info(
        "The 11 Classes system provide are *Red, Green, Blue, Yellow, Orange, Pink, Purple, Brown, Grey, Black and White.* However, the color of urine only focus on colors; *Yellow, Red, Orange, Green, Brown, Purple*. \n\n"
        "Please refer the pee color information have been given. For more information [click here](https://www.medicalnewstoday.com/articles/324469) for details.\n\n"
    )

    st.title('Identify Your Pee Color using Classifier')

    image = Image.open('pee-colors.jpg')
    st.image(image, caption='Pee color information')

    st.header("Select RGB values")
    
    Red = st.number_input(label="(R) RED value: ", min_value=0,
                          max_value=255, value=0, key="red")
    Green = st.number_input(label="(G) GREEN value: ",
                            min_value=0, max_value=255, value=0, key="green")
    Blue = st.number_input(label="(B) value: ", min_value=0,
                           max_value=255, value=0, key="blue")

    st.write('Red: {}, Green: {}, Blue: {}'.format(Red, Green, Blue))
    display_image()
    result = ""
    if st.button("Predict"):
        result = predict_color(Red, Green, Blue)
        st.success('The Color is {}!'.format(result))
        if ((format(result)=='Red') or (format(result)=='Pink'))
            st.success('Blood in urine, eating beetroor or blacberries')
        if format(result)=='Green' 
            st.succeess('Drugs containing phenol, some antidepressants, dyes in food and certain infection')
        if ((format(result)=='Yellow') or (format(result)=='White'))
            st.success('You are well hydrated')
        if format(result)=='Orange'
            st.success('Having dehydration, certain drugs and medications and dietary factors such as eating lots of carrots')
        if format(result)=='Purple'   
            st.success('Porphyria, a rare metabolic disorder')
        if format(result)=='Brown'   
            st.success('certain antipsychotic drugs, certain antibiotics')
                       
