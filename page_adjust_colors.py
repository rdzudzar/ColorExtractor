# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 21:06:31 2022

@author: Rob https://github.com/rdzudzar
"""

import streamlit as st
import re

from functions import make_procreate_swatches

def page_adjust_colors():
    
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")


    st.markdown("<h1 style='text-align: center;'> Color Extractor</h1>", 
                unsafe_allow_html=True)
    
    
    st.info("You can enter a list of HEX colors and adjust them.")
    
    input_hex = st.text_input(label='Paste below a comma separated HEX colors:',
                              placeholder="#FFFFFF")
    
    go = st.checkbox(label="Get individual color pickers from input HEX colors\
                     and download palette.")
    

    def create_swatches():
        """
        This function creates individual color pickers which will contain
        HEX colors obtained from the Streamlit's text input.

        Returns
        -------
        None.
        Sends information about HEX colors to Streamlit's components.
        
        """
        
        # initial inpput comma split
        initial_hex_list = input_hex.split(",")
        
        # Will contain hex codes from the input
        in_hex = []
        # Will contain hex codes from swatches - if one change swatch color
        # this list will be updated and the updated hex will be written out
        sw_hex = []
        # Create columns for swatches
        one, two, three, four, five, six, seven, eight, nine, ten = st.columns(10)
        
        # Go through initial_hex_list place each element into Swatch
                     
        for i, hexe in enumerate(initial_hex_list):
            # This clean is necessary when copying HEX from the cmap output
            b = hexe.strip(" ").strip("[").strip("   ").strip('"').strip("]").strip('" ')
    
            in_hex.append(b)
    
            # Check if HEX is a valid input
            check_hex = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', b)
            
            # If HEX is not a valid, report which one is not valid
            if check_hex == None:
                st.error(f"Your input: {b} is not a valid HEX color.")
            # Otherwise proceed with pickers
            else:
                
                # We have 3x10 columns, place hex codes into swatches
                # Label will contain number and hex code, this is useful in order
                # to avoid the same streamlit labels when hex codes are the same
                if (i==0 or i==10 or i==20) :
                    with one:
                        # Adding +1 so it starts from 1, as py starts from 0
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)
                        st.write(c)
    
                elif (i==1 or i==11 or i==21):
                    with two:
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)
                        st.write(c)
    
                elif (i==2 or i==12 or i==22):
                    with three:
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)
                        st.write(c)
    
                elif (i==3 or i==13 or i==23):
                    with four:
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)
                        st.write(c)
    
                elif (i==4 or i==14 or i==24):
                    with five:
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)
                        st.write(c)
    
                elif (i==5 or i==15 or i==25):
                    with six:
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)
                        st.write(c)
    
                elif (i==6 or i==16 or i==26):
                    with seven:
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)
                        st.write(c)
     
                elif (i==7 or i==17 or i==27):
                    with eight:
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)
                        st.write(c)
    
                elif (i==8 or i==18 or i==28):
                    with nine:
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)
                        st.write(c)
    
                elif (i==9 or i==19 or i==29):
                    with ten:
                        c = st.color_picker(f'{i+1}:', f'{in_hex[i]}')
                        sw_hex.append(c)                    
                        st.write(c)
        
        st.write("")
        st.write("")
        st.write("List of your selected hex colors. You can copy HEX colors to\
                 clipboard (hover over the list) or download palette as a\
                 Procreate .swatches file - on a sidebar.")
        st.write(sw_hex)
        
        # Make procreate swatches file
        make_procreate_swatches(sw_hex)
    
    if go:
        # To prevend the error when there is no input provided.
        if input_hex != '':
            
            st.write("")
            st.write("")
            st.write("Click on individual color picker to interactively change its\
                 color. A list of your updated HEX colors will appear below.")
                     
            create_swatches()
        else:
            st.write("Please enter a comma separated HEX colors first.")

        
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")   