# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 21:10:26 2022

@author: Rob https://github.com/rdzudzar
"""

import streamlit as st

import matplotlib.colors
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import cmasher as cmr
from colorspacious import cspace_converter

#from viscm import viscm
import time

from functions import make_procreate_swatches
import plotly.graph_objects as go

# To be able to call figure in st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

def page_make_colormaps():
    
        
    
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("") 
    st.sidebar.write("")
    
    
    st.markdown("<h1 style='text-align: center;'> Color Extractor</h1>", 
                unsafe_allow_html=True)
    
    

    def colormap_figure(cmap):
        """
        Plot for colormap. 

        Parameters
        ----------
        cmap : String. Cmap.
            Needs to be colormap name.

        Returns
        -------
        None.
        Function is pased to streamlit.pyplot

        """
        
        
        # To be able to call figure in st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        
        # Figure size appropriate to the size of the button
        fig, ax = plt.subplots(figsize=(7,1.32)) #7,1.4 loads faster
    
        # Getting 256 values
        x = np.linspace(0, 1, 256)[None, :]
        
        cmap_range = cmr.get_sub_cmap(cmap, 
                                 cmap_color_span[0], 
                                 cmap_color_span[1])
        
        # Show colormap
        ax.imshow(x, aspect='auto',
                  cmap = cmap_range)
      
        # Turn off the X and Y axes
        ax.set_axis_off()
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        
    def swatcheslike(cmap):
        """
        This function will show a swatches like graph with the little colored
        sqares - containing the extracted colors from the colormap.

        Parameters
        ----------
        cmap : String. Cmap.
            Needs to be colormap name.

        Returns
        -------
        None.
        Function is pased to streamlit.pyplot

        """
        # Number of individual colors
        swatches_number = num_of_swatches
        
        # This will determine how many rows of swatches will be shown
        # on the plot (1, 2, or 3), as each row contains max 10 swatches
        if (swatches_number >=0) and (swatches_number <= 10):
            m, n = 1, swatches_number
        elif (swatches_number >=10) and (swatches_number <= 20):
            m, n = 2, 10
        elif (swatches_number >=20) and (swatches_number <= 30):
            m, n = 3, 10

        # Creating array of evenly spaced values.  
        arr = np.arange(0, swatches_number)
        
        # Need to format array and sort how will the colors appear
        # m, n will be determined based on the selected number of colors
        Z = np.pad(arr.astype(float), (0, m*n - arr.size), 
               mode='constant', constant_values=np.nan).reshape(m,n)
        
        #To take the order as they appear on cmap, left to right
        if (swatches_number >=0) and (swatches_number <= 10):
            m, n = 1, swatches_number
            b = [Z[0]]
        elif (swatches_number >=10) and (swatches_number <= 20):
            m, n = 2, 10
            b = [Z[1], Z[0]]
        elif (swatches_number >=20) and (swatches_number <= 30):
            m, n = 3, 10
            b = [Z[2], Z[1], Z[0]]
        
        
        # Create figure
        fig, ax = plt.subplots()

        # Pass colormap - connect to the cmap range
        cmap_range = cmr.get_sub_cmap(cmap, 
                                 cmap_color_span[0],
                                 cmap_color_span[1])        

        # Create a pseudocolor plot with a non-regular rectangular grid
        ax.pcolor(b, edgecolors='k', linewidths=4, 
                        cmap=cmap_range)
        
        ax.set_aspect('equal')
        ax.tick_params(which='both', axis="x",direction="in", size=0.1)
        ax.tick_params(which='both', axis="y",direction="in", size=0.1)
        
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])
        
        fig.tight_layout()    
    
    def swatcheslike_plotly(colors):
        """
        This function will show a swatches-like graph with colored squares using Plotly.

        Parameters
        ----------
        colors : List of strings
            Hexadecimal color codes.

        Returns
        -------
        None.
        """

        #colors.sort()          # Sort the colors to ensure consistent order
        colors = colors#[::-1]  # Reverse the colors
        
        # Determine the number of colors
        swatches_number = len(colors)


        # Determine the number of rows and columns for the grid
        m, n = 3, 10

        fig = go.Figure()

        # Specify the positions of the colored squares
        for i, color in enumerate(colors):
            row = i // 10  # Determine the row
            col = i % 10   # Determine the column
            # Calculate the coordinates for the rectangle

            x = [col * (1 / n), (col + 1) * (1 / n), (col + 1) * (1 / n), col * (1 / n), col * (1 / n)]
            y = [1 - (row + 1) * (1 / m), 1 - (row + 1) * (1 / m), 1 - row * (1 / m), 1 - row * (1 / m), 1 - (row + 1) * (1 / m)]
            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='lines',
                line=dict(color='black', width=4),
                fill='toself',
                fillcolor=color,
                name=color,
                hoverinfo='text',  # Display hover info
                hovertext=f'Hex: {color}',  # Hover text with hexadecimal color code
                showlegend=False
            ))

        # Update layout
        fig.update_layout(
            width=700,
            height=200,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1]),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1]),
            margin=dict(l=0, r=0, t=0, b=0)
        )

        st.plotly_chart(fig)#, use_column_width=True)


    def pick_hex(cmap):
        """
        Takes N equally spaced colors from the created colormap and
        returns their HEX-values. Using CMasher function cmr.take_cmap_colors

        Parameters
        ----------
        cmap : String. Cmap.
            Needs to be colormap name.

        Returns
        -------
        colors_hex : List. 
            List of HEX colors.

        """
        colors_hex = cmr.take_cmap_colors(cmap, num_of_swatches, 
                                      cmap_range=(cmap_color_span[0], 
                                                  cmap_color_span[1]),
                                      return_fmt='hex')
        
        return colors_hex    
    
    
    def check_lightness_curve(created_cmap):
        """
        Function that takes created colormap and shows its lightness curve.
        Obtained from: https://matplotlib.org/stable/tutorials/colors/colormaps.html
        
        Returns
        -------
        None.
        Function is pased to streamlit.pyplot

        """
        
        # Made colormap will be registered as mycmap
        colormap = created_cmap
        # Indices to step through colormap
        x = np.linspace(0.0, 1.0, 256)
        
        fig, ax = plt.subplots(figsize=(4, 4))
        # Get RGB values for colormap and convert the colormap in
        # CAM02-UCS colorspace.  lab[0, :, 0] is the lightness.
        rgb = cm.get_cmap(created_cmap)(x)[np.newaxis, :, :3]
        lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
        
        # So reverse the order so that color start with low lightness
        y_ = lab[0, ::-1, 0]
        c_ = x[::-1]

        ax.scatter(x, y_, c=c_, cmap=created_cmap, s=300, linewidths=0.0)
        ax.set_ylabel('Lightness $L^*$', fontsize=12)
        ax.tick_params(which='both', axis="x",direction="in")
        ax.tick_params(which='both', axis="y",direction="in")


#    def see_viscm(cmap):
#        """
#        Function that takes created colormap and puts it into viscim package,
#        to give colormap quality overview.
#
#        Parameters
#        ----------
#        cmap : String. Cmap.
#            Needs to be colormap name.
#
#        Returns
#        -------
#        None.
#        Function is pased to streamlit.pyplot
#
#        """
#        
#        #Evaluate goodness of colormap using viscmm
#        viscm(cmap)
#        fig = plt.gcf()
#        fig.set_size_inches(12, 7)


    def get_code(name_procreate):
        """
        Prints out the python formatted code

        Parameters
        ----------
        name_procreate : String from streamlit input text.
            Will be colormaps name.
            
        Returns
        -------
        None.
        Prints out code on the page.

        """
        
        # Generate name if the input is empty
        if name_procreate == "":
            name_procreate = 'mycmap'
        elif name_procreate == " ":
            name_procreate = 'mycmap'
        
        # Create code for python script
        generate_cmap_code = f"""
# -*- coding: utf-8 -*-
# Generated using Color Extractor:
# https://github.com/rdzudzar/ColorExtractor
# {time.strftime("%Y%m%d_%H%M%S")}
# --- 

import matplotlib # v3.4.3
import matplotlib.pyplot as plt
import numpy as np #v1.20.3

# Add #colors and create colormap
created_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("{name_procreate}",
                                {c_hex})

# Register name of your colormap
plt.register_cmap("{name_procreate}", created_cmap)


# Get colors from the cmap
x = np.linspace(0, 1, 256)[None, :]

# See how colormap looks like
fig, ax = plt.subplots(figsize=(7,1.32))

ax.imshow(x, aspect='auto',
          cmap = "{name_procreate}")
  
# Turn off the X and Y axes
ax.set_axis_off()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

plt.show()

"""
        
        st.code(f"{generate_cmap_code}")    

        return generate_cmap_code

    def py_file_downloader(py_file_text, name_procreate):
        """
        Takes created python string which will contain infor of created
        colormap.

        Parameters
        ----------
        py_file_text : String.
            Created python code with f-strings to place in HEX colors.
        name_procreate : String from streamlit input text.
            Will be colormaps name.

        Returns
        -------
        None.
        Parses output to the streamlit's download button.

        """
    
        # Generate name if the input is empty
        if name_procreate == "":
            name_procreate = 'mycmap'
        elif name_procreate == " ":
            name_procreate = 'mycmap'
        
        # Streamlit's download button
        st.sidebar.download_button(
                label="Download .py file",
                data=f"{py_file_text}",
                file_name=f"{name_procreate}_CoEx.py",
                mime="application/octet-stream"
                )
        
        return name_procreate
    
    # Streamlit's number input which will contain number of colors for cmap
    number_of_colors = st.number_input("How many colors you want to use to\
                                       create colormap?",
                                      value = 2,
                                      max_value=4,
                                      min_value=2)
    # Streamlit's range slider - for colormap range
    cmap_color_span = st.slider('colormap range',
                            value = [0.0,1.0],
                            step = 0.1,
                            key = 'Range')
            

    # Check the selected number of colors for colormap, created colorpickers
    # for them, and combine them to colormap
    if number_of_colors == 2:
        st.info("Click on the color pickers (swatches) and choose your colors:")
        one, two = st.columns(2)
        with one:
            c1 = st.color_picker('First color:', "#1554cb")
            st.write(c1)
        with two:
            c2 = st.color_picker('Second color:', "#fbfb82")
            st.write(c2)
        # Create cmap
        created_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("mycmap", [c1,c2])
        # Save selected HEX
        c_hex = [c1, c2]
        
    # Same as above, just with 3 clors
    elif number_of_colors == 3:
        st.info("Click on the color pickers (swatches) and choose your colors:")
        one, two, three = st.columns(3)
        with one:
            c1 = st.color_picker('First color:', "#2d7f07")
            st.write(c1)
        with two:
            c2 = st.color_picker('Second color:', "#eae1c7")
            st.write(c2)
        with three:
            c3 = st.color_picker('Third color:', "#2307a6")
            st.write(c3)
        created_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("mycmap", [c1,c2,c3])
        # Collec hex colors for py code
        c_hex = [c1, c2, c3]
        
    # Same as above, just with 4 colors
    elif number_of_colors == 4:
        st.info("Click on the color pickers (swatches) and choose your colors:")
        one, two, three, four = st.columns(4)
        with one:
            c1 = st.color_picker('First color:', "#ffffff")
            st.write(c1)
        with two:
            c2 = st.color_picker('Second color:', "#86b166")
            st.write(c2)
        with three:
            c3 = st.color_picker('Third color:', "#6c3885")
            st.write(c3)
        with four:
            c4 = st.color_picker('Fourth color:', "#050a29")
            st.write(c4)
        created_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("mycmap", [c1,c2,c3,c4])
        # Collec hex colors for py code
        c_hex = [c1, c2, c3, c4] 
    
    # There will be User warning that this cmap is already registered, it's ok
    #plt.register_cmap("mycmap", created_cmap)
    st.pyplot(colormap_figure(created_cmap))
        
    
    # Press the button to get the python code and 
    #   download hyperlink option
    if st.checkbox('Generate Python Code With My colormap'):

        st.info("""
             **Python script** with your colormap. 
             **Download** option on the left.
            """)
        # Take colormap name from the input
        name_procreate = st.sidebar.text_input('Name your colormap', value="")

        # Create .py code and download        
        py_file_downloader(f"{get_code(name_procreate)}", name_procreate)
    
        # Show lightness graph and viscm output
        light = st.checkbox("Check lightness curve.")
        if light:
            
            #st.write("Below is evaluation of your colormap with [**viscm**](https://github.com/matplotlib/viscm/tree/v0.9).\
            #         Perceptually uniform sequential colormap should appear as \
            #             two straight lines on the two upper left (derivative) plots.")
            #st.pyplot(see_viscm('mycmap'))
    
            st.write("For sequential colormaps, the lightness value increases/decreases\
             monotonically, [**Read More**](https://matplotlib.org/stable/tutorials/colors/colormaps.html).")
    
            one, two = st.columns([2,1])
            
            with one:
                
                st.pyplot(check_lightness_curve(created_cmap))
    
    # Show extracted #hex colors and swatches graph
    cr = st.checkbox("Extract colors from my colormap")
    if cr:
        num_of_swatches = st.number_input("How many colors you want to extract?",
                                          value = 30,
                                          max_value=30)
        st.write('Hex colors from created colormap are printed below. \
                 If you want to test them for color blindness,\
                     you can save your image and import it into [**Coblis**](http://www.color-blindness.com/coblis-color-blindness-simulator/).')
            
        #st.pyplot(swatcheslike(created_cmap))
        swatcheslike_plotly(pick_hex(created_cmap))
        st.info("Download this as a Procreate swatches file - on the left sidebar.")
        st.write("You can copy HEX colors to clipboard (hover over the list) \
                 and adjust them on the 'Adjust Extracted Colors' page;\
                 or download palette as a Procreate .swatches file - see sidebar.")
        st.write(pick_hex(created_cmap))
        
        st.sidebar.write("")
        st.sidebar.write("")
        # Make procreate swatches file
        make_procreate_swatches(pick_hex(created_cmap))




    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    