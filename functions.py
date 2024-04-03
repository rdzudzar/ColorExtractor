# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 22:34:52 2022

@author: Rob https://github.com/rdzudzar
"""

import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# For colormap overview
#from viscm import viscm

# Used colormap packages
import cmasher as cmr
import proplot as plot
import cmcrameri as cmc
import cmocean as cmo
import colorcet as cc

#from pyart.testing import get_test_data

# For Procreate swatches
import json
import zipfile
import io



# Ignore worning for many openned plots
plt.rcParams.update({'figure.max_open_warning': 0})

@st.cache_data()
def get_cmaps_from_origin(origin):
    """
    Making of lists of colormaps from individual packages in order to sort
    them as much as possible by a color. At the moment there are 253 colormaps.
    
    Parameters
    ----------
    origin : String
        Obtain origin of colormaps: cmasher, matplotlib, crameri, cmocean, 
                                    scivis.
    Returns
    -------
    colormap_names : List - colormap_names
        A list of colormaps from the package named in origin.

    """
    
    if origin == "cmasher":
        # A list of colormaop names (those that do not end with '_r' - as 
        # these are reversed), can be obtained with this code: 
        # colormap_names = [y for y in cmr.cm.cmap_d.keys() 
        #                 if not y.endswith('_r')]
        
        # Currated list of colormaps from origin
        colormap_names = ['flamingo','ember','sunburst',
                        'amber', 'fall', 'pepper','apple', 'heat', 'torch', 
                        'bubblegum','gothic','amethyst','voltage','gem', 
                        'cosmic','freeze', 'arctic','sapphire', 'ocean', 
                        'horizon', 'lavender','rainforest', 'swamp','toxic', 
                        'nuclear', 'emerald', 'jungle', 'lilac','ghostlight', 
                        'tree','eclipse', 'savanna','dusk','sepia','neutral',
                        'copper_s','copper', 'fusion','prinsenvlag','guppy',
                        'infinity_s', 'seasons_s','chroma','neon','tropical',
                        'holly','watermelon','infinity','seasons', 'pride',
                        'wildfire', 'iceburn','redshift','viola','emergency', 
                        'emergency_s', 'seaweed','waterlily']
        
    elif origin == "matplotlib":
        # List from:
        # https://matplotlib.org/stable/tutorials/colors/colormaps.html
        colormap_names = ['inferno', 'magma', 'spring', 'autumn', 'hot', 
                          'afmhot', 'gist_heat', 'copper', 'pink', 'Wistia',
                          'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 
                          'PuRd', 'RdPu', 'BuPu', 'Purples', 'GnBu', 'PuBu', 
                          'Blues', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn', 
                          'winter', 'viridis','summer','Greens', 
                          'gray', 'bone', 
                          'cividis', 'twilight', 'ocean', 'gist_earth', 
                          'terrain', 'gist_stern', 'gnuplot', 'gnuplot2', 
                          'CMRmap', 'cubehelix', 'brg',  'cool', 'rainbow', 
                          'jet', 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 
                          'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 
                          'bwr', 'seismic']
        
        
    elif origin == "crameri":
        
        # import crameri as cmc
        # colormap_names = [y for y in cmap if not y.endswith('_r') 
        #                 if y.startswith("cmc") if not y in remove 
        #                 if not y.endswith("S")]
        colormap_names = ['bilbao','lajolla', 'buda', 'acton','tokyo', 'bam', 
                          'bamO', 'vanimo', 'hawaii', 'roma', 'romaO', 'vik', 
                          'vikO', 'berlin', 'turku', 'batlowK', 'batlow', 
                          'batlowW', 'bamako', 'broc', 'brocO', 'cork', 
                          'tofino', 'corkO', 'imola', 'davos', 'nuuk', 'devon',
                          'oslo', 'lapaz', 'lisbon', 'oleron', 'bukavu', 'fes',
                          'grayC',]
        
    elif origin == "cmocean":
        
        # import cmocean as cmo
        # colormap_names = cmo.cm.cmapnames
        colormap_names = ['thermal', 'solar', 'matter','turbid', 'amp', 
                          'balance', 'curl', 'delta', 'dense', 'ice', 'haline',
                          'deep', 'tempo', 'rain', 'algae', 'speed', 'gray', 
                          'oxy', 'phase', 'topo', 'diff', 'tarn']
        
        
    elif origin == "scivis":

        # Imported via proplot
        colormap_names = ['blues1', 'blues2', 'blues3', 'blues4', 'blues5', 
                          'blues6', 'blues7', 'blues8', 'blues9', 'purples1', 
                          'purples2', 'purples3', 'greens1', 'greens2', 
                          'greens3', 'greens4', 'greens5', 'greens6', 
                          'greens7', 'greens8', 'reds1', 'reds2', 'reds3', 
                          'reds4', 'reds5', 'oranges1', 'oranges2', 'oranges3',
                          'oranges4', 'browns1', 'browns2', 'browns3', 
                          'browns4', 'browns5', 'browns6', 'browns7', 
                          'browns8', 'browns9']

    #elif origin == "pyart":
    #    
    #    colormap_names = ['LangRainbow12', 'HomeyerRainbow', "BuDOr18",  
    #                        "BuOr10", "BuOr12", "BuOr8", "BuDOr12", "BuDRd12","BuDRd18","BuOrR14",
    #                        "RdYlBu11b", 'balance',"Bu10", "Bu7",
    #                        "Gray5", "Gray9", "SymGray12", "BuGy8", "BlueBrown11", "BrBu10", "BrBu12",
    #                         "BuGr14", "GrMg16","Carbone11", "Carbone17",
    #                         "RRate11","StepSeq25","Theodore16"]

        
    elif origin == "colorcet":        
        colormap_names = ['cet_CET_D10',
                          'cet_diverging_isoluminant_cjm_75_c23',
                          'cet_isoluminant_cm_70_c39',
                          'cet_diverging_isoluminant_cjo_70_c25',
                          'cet_cwr',
                          'cet_cyclic_tritanopic_cwrk_40_100_c20',
                          'cet_cyclic_tritanopic_wrwc_70_100_c20',
                          'cet_bjy',
                          'cet_diverging_linear_protanopic_deuteranopic_bjy_57_89_c34',
                          'cet_bwy',
                          'cet_isolum',
                          'cet_CET_L10',
                          'cet_linear_protanopic_deuteranopic_kyw_5_95_c49',
                          'cet_bky',
                          'cet_cyclic_protanopic_deuteranopic_bwyk_16_96_c31',
                          'cet_cyclic_protanopic_deuteranopic_wywb_55_96_c33',
                          'cet_linear_protanopic_deuteranopic_kbjyw_5_95_c25',
                          'cet_linear_protanopic_deuteranopic_kbw_5_98_c40',
                          'cet_linear_protanopic_deuteranopic_kbw_5_95_c34',
                          'cet_kbc',
                          'cet_linear_tritanopic_kcw_5_95_c22',
                          'cet_blues',
                          'cet_CET_D13',
                          'cet_bgyw',
                          'cet_linear_bgy_10_95_c74',
                          'cet_linear_kbgoy_20_95_c57',
                          'cet_linear_kgy_5_95_c69',
                          'cet_diverging_gkr_60_10_c40',
                          'cet_diverging_gwr_55_95_c38',
                          'cet_CET_D2',
                          'cet_bmw',
                          'cet_bmy',
                          'cet_fire',
                          'cet_linear_worb_100_25_c53',
                          'cet_linear_wcmr_100_45_c42',
                          'cet_diverging_bkr_55_10_c35',
                          'cet_diverging_linear_bjr_30_55_c53',
                          'cet_diverging_bwr_20_95_c54',
                          'cet_linear_tritanopic_krjcw_5_95_c24',
                          'cet_linear_tritanopic_krjcw_5_98_c46',
                          'cet_linear_tritanopic_krw_5_95_c46',
                          'cet_dimgray']

    
    return colormap_names

#@st.cache(hash_funcs={matplotlib.figure.Figure: lambda _: None},
#                    allow_output_mutation=True,
#                    suppress_st_warning=True)


# adding time to live - ttl: cache objects will be removed after 5hours
# testing whether this will save app from reaching resource limits
#@st.cache(hash_funcs={matplotlib.figure.Figure: lambda _: None},
#                    allow_output_mutation=True,
#                    suppress_st_warning=True, ttl=5*3600)

# Will cache matplotlib and make it load much faster
# https://github.com/streamlit/streamlit/issues/3100
@st.cache_data(hash_funcs={matplotlib.figure.Figure: hash}, ttl=3600)
def colormap_figure(colormap, origin, cmap_color_span, num_of_swatches):
    """
    Get the origin of the colormap and greate a plot of colormap, using
    only 50 values so that the plots load faster.

    Parameters
    ----------
    colormap : String.
        Colormap name.
    origin : String
        Obtain origin of colormaps: cmasher, matplotlib, crameri, cmocean, 
                                    scivis.
    cmap_color_span : Streamlit widget.
        A range filter that is connected to the colormap range.
    num_of_swatches : Streamlit widget.
        A number input value whish says how many colors to extract from
        colormap.

    Returns
    -------
    None.
    Will be parsed to streamlit pyplot to show figure.

    """
    
    
    # To be able to call figure in st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)
   

    # Checking which package colormap belogns to, as their name is called with
    # prefix, so we need to add one correspondingly
    if origin == 'cmasher':
        cmap_range = cmr.get_sub_cmap('cmr.'+f"{colormap}", 
                             cmap_color_span[0], cmap_color_span[1])
        
    elif origin == 'cmocean':
        cmap_range = cmr.get_sub_cmap('cmo.'+f"{colormap}", 
                             cmap_color_span[0], cmap_color_span[1])
        
    elif origin == 'crameri':
        cmap_range = cmr.get_sub_cmap('cmc.'+f"{colormap}", 
                             cmap_color_span[0], cmap_color_span[1])

    #elif origin == 'pyart':
    #    cmap_range = cmr.get_sub_cmap('pyart_'+f"{colormap}", 
    #                         cmap_color_span[0], cmap_color_span[1])
        
    else:
        cmap_range = cmr.get_sub_cmap(f"{colormap}", 
                             cmap_color_span[0], cmap_color_span[1])
        
    # Figure hight will be similar to the hight of the button
    fig, ax = plt.subplots(figsize=(7,1.32)) 

    # Getting only 50 values here so that colormaps are loading faster
    x = np.linspace(0, 1, 50)[None, :]
    
    # Show colormap
    ax.imshow(x, aspect='auto',
              cmap = cmap_range)
  
    # Turn off the X and Y axes
    ax.set_axis_off()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    
    return fig
    

def create_main_columns(origin, cmap_color_span, num_of_swatches):
    """
    Create main app columns. 1) List of buttons with colormap name; 
    2) Colormaps for names listed in 1; 3) Colormaps for names listed in 4; 
    4) List of buttons with colormap names.

    Parameters
    ----------
    origin : String
        Obtain origin of colormaps: cmasher, matplotlib, crameri, cmocean, 
                                    scivis.
    cmap_color_span : Streamlit widget.
        A range filter that is connected to the colormap range.
    num_of_swatches : Streamlit widget.
        A number input value whish says how many colors to extract from
        colormap.

    Returns
    -------
    buttons : List
        List of streamlit buttons - contain colormaps, will be used to extract
        individual colors from colormaps when clicked on button.

    """
    

    # Create 4 columns
    one, two, three, four = st.columns(4)

    with one:
        # Check the size of the colormap list - take half so we can place
        # the first half of buttons and colormaps in column 1 and 2;
        # the econd half of buttons and colormaps will go to column 3 and 4
        # Name on the button shortened to 20 characters as colorcet are lengthy
        size = len(get_cmaps_from_origin(origin))/2
        buttons = []
        for ind, cmr_cmap in enumerate(get_cmaps_from_origin(origin)):
            if ind < size:
                cmr_cmap = st.button(f"{cmr_cmap}"[0:20], key=f'{cmr_cmap}')
                buttons.append(cmr_cmap)
                
    with two:
        for ind, cmr_cmap in enumerate(get_cmaps_from_origin(origin)):
            if ind < size:
                st.pyplot(colormap_figure(f"{cmr_cmap}", origin, 
                                          cmap_color_span, num_of_swatches))
    
    with four:

        for ind, cmr_cmap in enumerate(get_cmaps_from_origin(origin)):
            if ind >= size:
                cmr_cmap2 = st.button(f"{cmr_cmap}"[0:20], key=f"{cmr_cmap}")
                buttons.append(cmr_cmap2)
                
    with three:
        for ind, cmr_cmap in enumerate(get_cmaps_from_origin(origin)):
            if ind >= size:
                st.pyplot(colormap_figure(f"{cmr_cmap}", origin, 
                                          cmap_color_span, num_of_swatches))
                
    return buttons


def swatcheslike(cmp_name, origin, cmap_color_span, num_of_swatches):
    """
    This function will show a swatches like graph with the little colored
    sqares - containing the extracted colors from the colormap.

    Parameters
    ----------
    cmp_name : String.
        Colormap name.
    origin : String
        Obtain origin of colormaps: cmasher, matplotlib, crameri, cmocean, 
                                    scivis.
    cmap_color_span : Streamlit widget.
        A range filter that is connected to the colormap range.
    num_of_swatches : Streamlit widget.
        A number input value whish says how many colors to extract from
        colormap.

    Returns
    -------
    None.
    The figure will be parsed to the streamlit pyplot.

    """
        
    # This will determine how many rows of swatches will be shown
    # on the plot (1, 2, or 3), as each row contains max 10 swatches
    if (num_of_swatches >=0) and (num_of_swatches <= 10):
        m, n = 1, num_of_swatches
    elif (num_of_swatches >=10) and (num_of_swatches <= 20):
        m, n = 2, 10
    elif (num_of_swatches >=20) and (num_of_swatches <= 30):
        m, n = 3, 10

    # Creating array of evenly spaced values.  
    arr = np.arange(0, num_of_swatches)

    # Need to format array and sort how will the colors appear
    # m, n will be determined based on the selected number of colors
    Z = np.pad(arr.astype(float), (0, m*n - arr.size), 
           mode='constant', constant_values=np.nan).reshape(m,n)
    
    # To take the order as they appear on cmap, left to right
    if (num_of_swatches >=0) and (num_of_swatches <= 10):
        m, n = 1, num_of_swatches
        b = [Z[0]]
    elif (num_of_swatches >=10) and (num_of_swatches <= 20):
        m, n = 2, 10
        b = [Z[1], Z[0]]
    elif (num_of_swatches >=20) and (num_of_swatches <= 30):
        m, n = 3, 10
        b = [Z[2], Z[1], Z[0]]
    
    
    # Create fogure 
    fig, ax = plt.subplots()

    # Check the origin so we can add corresponding prefix to colormap name
    if origin == 'cmasher':
        cmap_range = cmr.get_sub_cmap('cmr.'+f"{cmp_name}", 
                             cmap_color_span[0], cmap_color_span[1])  
    elif origin == 'cmocean':
        cmap_range = cmr.get_sub_cmap('cmo.'+f"{st.session_state['button']}", 
                             cmap_color_span[0], cmap_color_span[1])
    elif origin == 'crameri':
        cmap_range = cmr.get_sub_cmap('cmc.'+f"{cmp_name}", 
                             cmap_color_span[0], cmap_color_span[1])        
    #elif origin == 'pyart':
    #    cmap_range = cmr.get_sub_cmap('pyart_'+f"{cmp_name}", 
    #                         cmap_color_span[0], cmap_color_span[1])  

    else:
        cmap_range = cmr.get_sub_cmap(f"{cmp_name}", 
                             cmap_color_span[0], cmap_color_span[1])   

    # Create a pseudocolor plot with a non-regular rectangular grid
    ax.pcolor(b, edgecolors='k', linewidths=4, 
                    cmap=cmap_range)
    
    ax.set_aspect('equal')
    ax.tick_params(which='both', axis="x",direction="in", size=0.1)
    ax.tick_params(which='both', axis="y",direction="in", size=0.1)
    
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    
    fig.tight_layout()
    
    
def pick_hex(cmp_name, origin, cmap_color_span, num_of_swatches):
    """
    Takes N equally spaced colors from the provided colormap cmap and 
    returns their HEX-values. Using CMasher function cmr.take_cmap_colors

    Parameters
    ----------
    cmp_name : String.
        Colormap name.
    origin : String
        Obtain origin of colormaps: cmasher, matplotlib, crameri, cmocean, 
                                    scivis.
    cmap_color_span : Streamlit widget.
        A range filter that is connected to the colormap range.
    num_of_swatches : Streamlit widget.
        A number input value whish says how many colors to extract from
        colormap.

    Returns
    -------
    colors_hex : (list of {tuple; str})
        The colors that were taken from the selected colormap.

    """
    
    
    if origin == 'cmasher':
        colors_hex = cmr.take_cmap_colors('cmr.'+f"{cmp_name}", num_of_swatches, 
                                  cmap_range=(cmap_color_span[0], 
                                              cmap_color_span[1]),
                                  return_fmt='hex')
    elif origin == 'cmocean':
        colors_hex = cmr.take_cmap_colors('cmo.'+f"{st.session_state['button']}", num_of_swatches, 
                                  cmap_range=(cmap_color_span[0], 
                                              cmap_color_span[1]),
                                  return_fmt='hex')
    elif origin == 'crameri':
        colors_hex = cmr.take_cmap_colors('cmc.'+f"{cmp_name}", num_of_swatches, 
                                  cmap_range=(cmap_color_span[0], 
                                              cmap_color_span[1]),
                                  return_fmt='hex')
    #elif origin == 'pyart':
    #    colors_hex = cmr.take_cmap_colors('pyart_'+f"{cmp_name}", num_of_swatches, 
    #                              cmap_range=(cmap_color_span[0], 
    #                                          cmap_color_span[1]),
    #                              return_fmt='hex')

    else:
        colors_hex = cmr.take_cmap_colors(f"{cmp_name}", num_of_swatches, 
                                  cmap_range=(cmap_color_span[0], 
                                              cmap_color_span[1]),
                                  return_fmt='hex')
    return colors_hex


#def get_me_viscm(origin, cmap_color_span):
#    
#    # Adding optional checkbox if someone wants to see viscim 
#    # overview of the selected colormap             
#    vi = st.checkbox("Evaluate colormap with viscm")
#    
#    if vi:    
#        st.write("Below is evaluation of your colormap with\
#                 [**viscm**](https://github.com/matplotlib/viscm/tree/v0.9).\
#                 Perceptually uniform sequential colormap should appear as\
#                two straight lines on the two upper left (derivative)\
#                plots.")
#        
#        # Check the origin of the colormap, and then parse colormap to the
#        # viscim
#        if origin == 'cmasher':
#            viscm_cmap_range = cmr.get_sub_cmap('cmr.'+f"{st.session_state['button']}", 
#                                 cmap_color_span[0], cmap_color_span[1])
#            viscm(viscm_cmap_range)
#            
#        elif origin == 'cmocean':
#            viscm_cmap_range = cmr.get_sub_cmap('cmo.'+f"{st.session_state['button']}", 
#                                 cmap_color_span[0], cmap_color_span[1])
#            viscm(viscm_cmap_range)
#            
#        elif origin == 'crameri':
#            viscm_cmap_range = cmr.get_sub_cmap('cmc.'+f"{st.session_state['button']}", 
#                                 cmap_color_span[0], cmap_color_span[1])
#            viscm(viscm_cmap_range)
#            
#        else:
#            viscm_cmap_range = cmr.get_sub_cmap(f"{st.session_state['button']}", 
#                                 cmap_color_span[0], cmap_color_span[1])
#            viscm(viscm_cmap_range)
#        
#        # Show viscim overview, selected size is ok
#        fig = plt.gcf()
#        fig.set_size_inches(12, 7)
#        st.pyplot(fig)

def get_hex(origin, cmp_name, buttons, cmap_color_span, num_of_swatches):
    """
    Function that will display plot with extracted colors from colormap based
    on the button that was clicked on. It will also display the HEX codes
    of the extracted colors.

    Parameters
    ----------
    origin : String
        Obtain origin of colormaps: cmasher, matplotlib, crameri, cmocean, 
                                    scivis.
    cmp_name : String.
        Colormap name.
    buttons : List
        List of streamlit buttons - contain colormaps, will be used to extract
        individual colors from colormaps when clicked on button.
    cmap_color_span : Streamlit widget.
        A range filter that is connected to the colormap range.
    num_of_swatches : Streamlit widget.
        A number input value whish says how many colors to extract from
        colormap.

    Returns
    -------
    None.

    """
    
    # Ussing streamlit session_state so that app remembers on which button
    # it was clicked when changing colormap range or number of extracted
    # colors.
    if 'button' not in st.session_state:
        #st.stop()
        st.session_state['button'] = 'No'
    
    for i, but in enumerate(buttons):
        if buttons[i]:
            st.session_state['button'] = cmp_name[i]
    
    # Try/Except is is to avoid key error on a first run where colormap is 
    # not selected
    try:
        # Parse to streamlit to write and plot selected colormap
        st.write(f"{st.session_state['button']} colormap was selected.")
        st.pyplot(swatcheslike(f"{st.session_state['button']}", origin, 
                               cmap_color_span, num_of_swatches))
    
        hexes = pick_hex(f"{st.session_state['button']}", origin, 
                         cmap_color_span, num_of_swatches)
        st.info("**Download** patelette as a Procreate .swatches file - on the left sidebar.")
        st.write("You can copy HEX colors to clipboard (hover over the list) \
                 and adjust them on the 'Adjust Extracted Colors' page;\
                 or download palette as a Procreate .swatches file - see sidebar.")
        st.write(f"{num_of_swatches} hex colors from selected\
                  {st.session_state['button']} colormap are:", hexes)        
        
        #get_me_viscm(origin, cmap_color_span)
        
    except KeyError:
        st.write("")
        
    try:
        return hexes
    except UnboundLocalError:
        hexes = ["#ffffff", "#ffffff"]
        return hexes



def make_procreate_swatches(sw_hex):
    """
    Function that will create Procreate swatches file from the provided HEX
    colors.

    Parameters
    ----------
    sw_hex : List
        List of HEX colors.

    Returns
    -------
    None.
    Parses created swatches file to streamlit's download button

    """
    
    # This check is so that the download swatches doesn't apper before a
    # colormap is selected. As default HEX are set to 2 white colors to
    # avoid error which appears upon loading cmap page if nothing is selected
    if sw_hex != ['#ffffff', '#ffffff']:
        # Text input which will be parsed as a swatches name
        name_procreate = st.sidebar.text_input('Name your palette', value="")
    
        # In case input name is empty
        if name_procreate == "":
            name_procreate = 'ColorExtractor'
        elif name_procreate == " ":
            name_procreate = 'ColorExtractor'

    
        # Extracting rgb and hsv from HEX to store in procreate file
        rgb_components = []
        hsv_components = []
        for ind, hex_color in enumerate(sw_hex):
            #  Get color HEX, RGB and RGBA codes
            c_rgb  = colors.to_rgb(hex_color)   #  HEX to RGB
            rgb_components.append(c_rgb)
            
            hsv_c = colors.rgb_to_hsv(rgb_components[ind]) # RGB to HSV
            hsv_components.append(hsv_c)
        
        # Individual swatches in format [{}]
        sw = []
        for ind, c in enumerate(sw_hex):
            dict_component = {
                "alpha" : 1,
                "origin" : 2,
                "colorSpace" : 0,
                "colorModel" : 0,
                "brightness" : hsv_components[ind][2],
                "components" : [
                    rgb_components[ind][0],
                    rgb_components[ind][1],
                    rgb_components[ind][2]
                    ],
                "version" : "5.0",
                "colorProfile" : "KzqhZFd5qeY0dE+vmwHpECsMm4j9bezteTTfhrlJr34=",
                "saturation" : hsv_components[ind][1],
                "hue" : hsv_components[ind][0]
                }
            sw.append(dict_component)
        
        # Prefix for Procreate
        swatches_content = {
            "name" : f"{name_procreate}_CoEx",
            "swatches" : sw
        }
        
        # Creating json format to parse it to the output so we can download file
        jsonString = json.dumps(swatches_content) #jsonData
        
        # Procreate data: data storred in Swatches.json, 
        # which is zipped but zip is .swatches
        # File/Swathes name will be obtained from input
        with io.BytesIO() as buffer: 
            with zipfile.ZipFile(buffer, 'w') as zip:
                zip.writestr("Swatches.json", jsonString)
            
            buffer.seek(0)
            
            # Streamlit's download button
            #with open(f"{name_procreate}.swatches", "rb") as fp:
            st.sidebar.download_button(
                    label="Download .swatches",
                    data=buffer,
                    file_name=f"{name_procreate}.swatches",
                    mime="application/octet-stream"
                    )
        st.sidebar.write("")
        st.sidebar.write("")

        
def components():
    """
    Creating streamlit widget that will control colormap range and number of
    extracted colors from colormap.

    Returns
    -------
    cmap_color_span : Streamlit widget.
        A range filter that is connected to the colormap range.
    num_of_swatches : Streamlit widget.
        A number input value whish says how many colors to extract from
        colormap.

    """
    # Two columns, first one with larger width then the second one
    one, two = st.columns([3,1])
    
    with one:
        # Streamlit's range slider            
        cmap_color_span = st.slider('Colormap range',
                            value = [0.0,1.0],
                            step = 0.1,
                            key = 'Range')
            
    with two:
        # Streamlit's number input 
        num_of_swatches = st.number_input("How many colors?",
                                          value = 30,
                                          min_value=1,
                                          max_value=30)
        
    return cmap_color_span, num_of_swatches
