# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:33:00 2022

@author: Rob https://github.com/rdzudzar
"""

import streamlit as st

def page_intro():
    
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    
    
    st.markdown("<h2 style='text-align: center;'> Welcome To </h2>", 
                unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'> Color Extractor</h1>", 
                unsafe_allow_html=True)
    
    st.markdown("At the moment **Color Extractor** contains **253** imported\
                colormaps from 6 different Python packages.\
                In adition, you can create an infinite combinations of your \
                own colormaps.")
    
    st.info("""
            There are three main features: \n
            - Extract colors from colormaps
            - Make your own colormap
            - Adjust extracted colors
            $←$ To start playing with the app, select an option on the 
            left sidebar.
            """)
            
    st.info("""
            - Here is a youtube link to the [Color Extractor\
                walkthrough](https://www.youtube.com/watch?v=6S0b7gFY36I&t=3s).
            - App snippets and brief descriptions ⮧
            """)
            

    image1 = "https://raw.githubusercontent.com/rdzudzar/ColorExtractor/main/Images/Extract1.png"
    image2 = "https://raw.githubusercontent.com/rdzudzar/ColorExtractor/main/Images/Extract2.png"
    image3 = "https://raw.githubusercontent.com/rdzudzar/ColorExtractor/main/Images/Adjust1.png"
    image4 = "https://raw.githubusercontent.com/rdzudzar/ColorExtractor/main/Images/Adjust2.png"
    image5 = "https://raw.githubusercontent.com/rdzudzar/ColorExtractor/main/Images/Make1.png"
    image6 = "https://raw.githubusercontent.com/rdzudzar/ColorExtractor/main/Images/Make2.png"
    image7 = "https://raw.githubusercontent.com/rdzudzar/ColorExtractor/main/Images/Make3.png"



    def make_line():
        """ Line divider between images. """
            
        line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                unsafe_allow_html=True)

        return line
    
    
    # Images and brief explanations.
    st.error('Extract colors from colormap')
    feature1, feature2 = st.columns([0.5,0.4])
    with feature1:
        st.image(image1, use_column_width=True)
    with feature2:
        st.warning('Select colormap page')
        st.info("""
                - A - Available colormap pages.
                - B - Change colormap range with slider, and select how many\
                    colors you want to extract (1-30).
                - C - Click on the colormap button to extract its colors.
                """)
    st.info("**References** - lists references to origin of used colormaps.")
    make_line()
    
    feature3, feature4 = st.columns([0.6,0.4])
    with feature3:        
        st.image(image2, use_column_width=True)
    with feature4:
        st.warning('After button click')
        st.info("""
                Scroll to the bottom of the page, your colors will appear.
                - A - Name your palette and download Procreate .swatches file.
                - B - Copy HEX colors to clipboard.
                - C - Examine quality of the colormap with viscm.
                """)
    
    make_line()
    

    st.error('Adjust selected colors')
    feature5, feature6 = st.columns([0.5,0.4])
    with feature5:
        st.image(image3, use_column_width=True)
    with feature6:
        st.warning('Paste in your HEX colors')
        st.info("""
                - Paste in a list of comma separated HEX colors.
                - Press Enter and click on the checkbox.
                """)
                
    make_line()
    
    feature7, feature8 = st.columns([0.6,0.4])
    with feature7:        
        st.image(image4, use_column_width=True)
    with feature8:
        st.warning('After checkbox is clicked')
        st.info("""
                - A - You can click on each color picker and change color.
                - B - You can copy to clipboard your new list of HEX colors.
                - C - Name your palette, press enter and click on the button\
                    to download Procreate .swatches file.
                """)
    
    make_line()
    
    st.error('Make your own colormap')
    feature9, feature10 = st.columns([0.5,0.4])
    with feature9:
        st.image(image5, use_column_width=True)
    with feature10:
        st.warning('Select properties')
        st.info("""
                - A - Select how many colors you want in colormap (2-4).
                - B - Adjust colormap range.
                - C - Click on the color pickers to select colors.
                - D - You can generate python code with your colormap, and you\
                    can also extract colors from your colormap.
                """)
                
                
    make_line()
    
    feature10, feature11 = st.columns([0.5,0.4])
    with feature10:
        st.image(image6, use_column_width=True)
    with feature11:
        st.warning('Checkbox: Extract colors')
        st.info("""
                - A - Select how many colors you want to extract (1-30).
                - B - Name your palette, press enter and click on the button\
                    to download Procreate .swatches file.
                - C - Copy HEX colors to clipboard. \ 
                    You maybe want to tweak some colors on the 'Adjust\
                        selected colors' page.
                """)
                
    make_line()
    
    feature12, feature13 = st.columns([0.5,0.4])
    with feature12:
        st.image(image7, use_column_width=True)
    with feature13:
        st.warning('Checkbox: Python file')
        st.info("""
                - A - Copy Python script to clipboard.
                - B - Name your Python script, press enter and click\
                        on the button to download .py file.
                - C - Click on checkbox if you want to examine quality of your\
                    colormap with viscm.
                """)
                
    make_line()
