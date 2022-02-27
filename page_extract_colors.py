# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:44:23 2022

@author: Rob https://github.com/rdzudzar
"""

import streamlit as st

# Individual colormap pages
from page_cmasher import page_cmasher
from page_matplotlib import page_matplotlib
from page_crameri import page_crameri
from page_cmocean import page_cmocean
from page_scivis import page_scivis
from page_colorcet import page_colorcet
from page_references import page_references

def page_extract_colors():
    
    """
    Register pages to Extract Colors:
        page_introduction - contains page with images and brief explanations
        page_colorextractor - contains functions that allows color extraction
                            from various colormaps
    """

    pages = {
        "CMasher colormaps": page_cmasher,
        "Cmocean colormaps": page_cmocean,
        "Colorcet colormaps": page_colorcet,
        "Crameri colormaps": page_crameri, 
        "Matplotlib colormaps": page_matplotlib,
        "SciVisColor colormaps": page_scivis,
        "References": page_references
        }

    # Sidebar notes
    st.sidebar.title("Available colormaps")

    # Radio buttons to select desired option
    page = st.sidebar.radio("Select:", tuple(pages.keys()))
                                
    # Display the selected page with the session state
    pages[page]()
    
    
