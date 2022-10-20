# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:30:00 2022

@author: Rob https://github.com/rdzudzar
"""

import streamlit as st

from page_intro import page_intro
from page_extract_colors import page_extract_colors
from page_adjust_colors import page_adjust_colors
from page_make_colormaps import page_make_colormaps


# Set the default elements on the sidebar
st.set_page_config(page_title='ColorExtractor')


image_logo = 'https://raw.githubusercontent.com/rdzudzar/ColorExtractor/main/Images/CoEx_logo.png'


st.sidebar.markdown("<h1 style='text-align: center; color: grey;'> \
                Color Extractor </h1>", unsafe_allow_html=True)
st.sidebar.image(image_logo, use_column_width=True)

st.sidebar.write(" ")

def main():
    """
    Register pages to Extract Colors:
        page_introduction - contains page with images and brief explanations
        page_colorextractor - contains functions that allows color extraction
                            from various colormaps
    """

    pages = {
        "Introduction": page_intro,
        "Extract colors from colormaps": page_extract_colors,
        "Make your own colormap": page_make_colormaps,
        "Adjust extracted colors": page_adjust_colors,

    }

    st.sidebar.title("Main options")

    # Radio buttons to select desired option
    page = st.sidebar.radio("Select:", tuple(pages.keys()))
                                
    # Display the selected page with the session state
    pages[page]()


    st.write("")
    st.write("")
    st.write("")
    
    st.sidebar.write("")
    st.sidebar.write("")

    
    # Write About    
    st.sidebar.header("About")
    st.sidebar.warning(
            """
            Color Extractor app is created and maintained by **Dr Robert Dzudzar**. 
            If you like this app please star its
            [**GitHub**](https://github.com/rdzudzar/ColorExtractor)
            repo, share it and feel free to open an issue if you find a bug 
            or if you want some additional features.
            """
    )


if __name__ == "__main__":
    main()