# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 22:37:20 2022

@author: Rob
"""

import streamlit as st


def page_references():
    
    # App
    st.markdown("<h1 style='text-align: center;'> Color Extractor</h1>", 
                unsafe_allow_html=True)

    st.write(""" **Color Extractor** uses a sample of publicly available python
             packages that contain, or are made for, colormaps. At the moment
             Color Extractor contains 253 imported colormaps.""")   
             
             
    st.markdown("<h3 style='text-align: left;'> CMasher colormaps</h3>", 
                unsafe_allow_html=True)
    
    st.write("""The [**CMasher**](https://cmasher.readthedocs.io/) package provides a collection of scientific 
             colormaps which are all designed to be perceptually uniform 
             sequential; made by Ellert van der Velden. Most of CMasher colormaps are color-vision deficiency
             (CVD; color blindness) friendly.""")   

    st.write(""" Publication: [van der Velden, (2020). CMasher: Scientific colormaps for making accessible, informative and 'cmashing' plots. Journal of Open Source Software, 5(46), 2004](https://doi.org/10.21105/joss.02004)""")
             

    
    st.markdown("<h3 style='text-align: left;'> Cmocean colormaps</h3>", 
                unsafe_allow_html=True)
    
    st.markdown("""[**Cmocean**](https://cran.r-project.org/web/packages/cmocean/vignettes/cmocean.html) 
                are color palettes for oceanography, developed for python by Kristen Thyng. Cmocean palettes are perceptually uniform.""")
    st.markdown(""" Publication:
                [K. M., Greene, C. A., Hetland, R. D., Zimmerle, H. M., & DiMarco, S. F. (2016). True colors of oceanography. Oceanography, 29(3), 10.](https://tos.org/oceanography/assets/docs/29-3_thyng.pdf)
                    """)
    
    st.markdown("<h3 style='text-align: left;'> Colorcet colormaps</h3>", 
                unsafe_allow_html=True)
    
    st.markdown("""[**Colorcet**](https://colorcet.holoviz.org/) is a collection of perceptually acccurate 256-color colormaps for use with Python plotting programs. 
                The continuous maps were constructed by Peter Kovesi. """)
    st.markdown(""" Publication: 1) [Glasbey, van der Heijden, Toh, & Gray (2007).](https://strathprints.strath.ac.uk/30312/1/colorpaper_2006.pdf); 2) [Kovesi, 2015](https://arxiv.org/pdf/1509.03700.pdf)""")
    
    st.markdown("<h3 style='text-align: left;'> Crameri colormaps</h3>", 
                unsafe_allow_html=True)
    
    st.markdown("""[**Crameri**](https://www.fabiocrameri.ch/colourmaps/) is a suite of scientific, colour-vision deficiency friendly and perceptually uniform colour maps, made by Fabio Crameri.""")
    st.markdown(""" Publication: 1) [Crameri, F. 2018](https://zenodo.org/record/5501399#.YhofgJZxVjE); 2) [Crameri, F., G.E. Shephard, and P.J. Heron, 2020](https://www.nature.com/articles/s41467-020-19160-7).""")
    
    st.markdown("<h3 style='text-align: left;'> Matplotlib colormaps</h3>", 
                unsafe_allow_html=True)
    
    st.markdown("""[**Matplotlib**](https://matplotlib.org/) is a comprehensive library for creating static, animated, and interactive visualizations in Python.\
                Matplotlib has a number of built-in colormaps, you can read more [**here.**](https://matplotlib.org/stable/tutorials/colors/colormaps.html) """)
    
    st.markdown("<h3 style='text-align: left;'> SciVisColor colormaps</h3>", 
                unsafe_allow_html=True)
    
    st.markdown("""[**SciVisColor**](https://sciviscolor.org/) is a hub for research and resources related to color in scientific visualization. SciVisColor draws on expertise from the arts, computer science, data science, geoscience, mathematics, and the scientific visualization community to create tools and guides that enhance scientists’ ability to extract knowledge from their data.""")
    st.markdown("""Color Extractor uses SciVisColors imported to Python through [**ProPlot**](https://proplot.readthedocs.io/en/latest/colormaps.html) package. """)