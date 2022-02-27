|logo|

Distribution Analyser 
=====================

|MIT licensed|

# ColorExtractor
Color Extractor is a Web App that allows you to extract palettes of colors from 
various colormaps and create your own colormaps.

At the moment Color Extractor contains 253 imported colormaps from 6 different 
Python packages. In adition, you can create an infinite combinations of your own colormaps.

How to use
----------
Here is a link to YouTube for Color Extractor walkthrough.


Main options:
=============
- `Extract colors from colormaps` - Interactively explore and extract palette of colors from various colormaps.
- `Make your own colormap` - Interactively select colors and create your own colormap. 
- `Adjust extracted colors` - Interactively adjust your selected palette of colors.

Extract colors from colormap
----------------------------

- Select colormap page.
    - There are 6 colormap pages available
    - See References for each colormap page
- Extract palette of colors from a colormap by clicking on colormap's button.
- Use slider and number input to adjust selected colormap.
- Copy HEX colors to clipboard and/or download palette as a Procreate .swatches file.
- Inspect each colormap with viscm.

Make your own colormap
----------------------

- Select how many colors you want to combine into a colormap.
- Click on the color pickers to select desired colors.
- You can generate python code with your colormap
    - Copy code to clipboard and/or download .py code
- You can extract palette of colors from your colormap
    - Chose number of colors you want to extract
    - Copy HEX colors to clipboard and/or download palette as a Procreate .swatches file.
- You can inspect your colormap with viscm

Adjust extracted colors
-----------------------

- Input a list of comma separated HEX colors
- Click on individual color pickers to interactively adjust/change each of your colors
- Copy HEX colors to clipboard and/or download palette as a Procreate .swatches file.


Use Color Extractor localy
--------------------------------

Clone repository and run locally with Streamlit https://streamlit.io/:
::

    $ git clone https://github.com/rdzudzar/ColorExtractor.git
    $ cd ColorExtractor
    $ streamlit run main.py


Structure
---------

.. code-block:: raw
   
   Color Extractor
   
   ├── main.py                  # Color Extractor page container
   ├── page_intro.py            # 1st Page in the Main app
   ├── page_extract_colors.py   # 2nd Page in the Main app and colormap page container
   ├── page_make_colormaps.py   # 3rd Page in the Main app
   ├── page_adjust_colors.py    # 4th Page in the Main app
   ├── functions.py             # Functions for extracting colors from colormaps
   
   ├── page_cmasher.py          # CMasher page container
   ├── page_cmocean.py          # Cmocean page container
   ├── page_colorcet.py         # Colorcet page container
   ├── page_crameri.py          # Crameri page container
   ├── page_matplotlib.py       # Matplotlib page container
   ├── page_svivis.py           # SciVisColor page container

   ├── README.rst
   ├── requirements.txt         # List of used packages
   └── LICENSE
   │
   ├── Images
   │   ├── CoEx_logo.png        # App logo
   │   └── 7 other .png         # Images used on the introduction page

Community guidelines
--------------------

**Color Extractor** is an open-source and free-to-use, provided under the MIT licence.
If you like Color Extractor, please share it, star repo and feel free to open issues for any bugs/requests.

.. |MIT licensed| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/rdzudzar/ColorExtractor/blob/main/LICENSE
   :alt: MIT License

.. |logo| image:: https://github.com/rdzudzar/ColorExtractor/blob/main/Images/CoEx_logo.png
   :target: https://github.com/rdzudzar/DistributionAnalyser
   :alt: DA logo