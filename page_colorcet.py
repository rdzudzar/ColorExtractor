# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 23:21:41 2022

@author: Rob https://github.com/rdzudzar
"""

import streamlit as st


from functions import create_main_columns, get_hex, get_cmaps_from_origin,\
                        components, make_procreate_swatches


def page_colorcet():
    """
    Base of the colormap page. 
    Origin - name of the colormap page. 

    """
    
    # Colormap package
    origin = "colorcet"
    
        
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")

    
    # App
    st.markdown("<h1 style='text-align: center;'> Color Extractor</h1>", 
                unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center;'> Colorcet colormaps</h3>", 
                unsafe_allow_html=True)
    
    # Above the widgets
    st.info("**Click** on a colormap button to extract its colors:")
    

    # Getting colormap range values and number of extracted colors/swatches
    cmap_color_span, num_of_swatches = components()

    # All the colormap buttons
    buttons = create_main_columns(origin, cmap_color_span, num_of_swatches)

    # Obtain the list of the colormap names from the colormap package
    cmaps_input = get_cmaps_from_origin(origin)
    
    # Get them individual colors/pallete/swatches
    #get_hex(origin, cmaps_input, buttons, cmap_color_span, num_of_swatches)
    
    # Make procreate swatches file; Check the session state before
    #for i, but in enumerate(buttons):
    #    if buttons[i]:
    make_procreate_swatches(get_hex(origin, cmaps_input, buttons, cmap_color_span, num_of_swatches))