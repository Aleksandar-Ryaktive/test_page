import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import pydeck as pdk
from bokeh.plotting import figure
from PIL import Image
import time


st.title('Ryaktive Software Development Agency')

"""
We meet your expectations and beyond
"""

image = Image.open('ryaktive_logo.png')
           
st.image(image, caption='Ryaktive logo', width=400)        

"""
## Who we are
"""



st.write(
         
         '_Ryaktive_ is a software development agency. '         
         'We help you transform your big idea into reality. '        
         'We combine proven and up-to-date technologies, user experience (UX) '         
         'design techniques, data science methods, and agile methodologies to '         
         'quickly deliver scalable and beautifully crafted solutions '         
         'and products to our customers.'
         )

"""
## Our services

We build world-class software by focusing on user experience 
combined with data analytics to deliver engaging web and mobile apps.
If you are an entrepreneur and are looking for a technology partner 
to work with and implement your next big idea, look no further, 
we are the right technology partner. 
We are agile, and we understand the dynamic nature of startups. 
We will work with you from the very beginning and continue our partnership 
to ensure your success.
"""

"""
## Number of random values
"""

chart_data = pd.DataFrame(
     np.random.randn(8, 3),
     columns=['UX Design', 'Web Development', 'Data Analysis'])

st.line_chart(chart_data)



"""
## Our Team
"""


st.write(pd.DataFrame({
    'number': [1, 2, 3, 4, 5],
    'name': ['Husam Bamatrf', 'Hadis Alija', 'Aleksandar Anastasov', 'Tale Anevski', 'Nikola Matoski']
}))


"""
## Random map values
"""

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [41.9981, 21.4254],
    columns=['lat', 'lon'])

st.map(map_data)


"""
## Random bubble chart
"""

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)


#"""
### Random interactive table
#"""
#
#df = pd.DataFrame(
#    np.random.randn(50, 20),
#    columns=('col %d' % i for i in range(20)))
#st.dataframe(df.style.highlight_max(axis=0))  # Same as st.write(df)
#

"""
## Random bar chart
"""

chart_data = pd.DataFrame(
     np.random.randn(8, 3),
     columns=['UX Design', 'Web Development', 'Data Analysis'])

st.bar_chart(chart_data)


"""
Here’s a chart using a HexagonLayer and a ScatterplotLayer 
on top of the light map style:
"""

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=37.76,
         longitude=-122.4,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
))

"""
## Random checkbox
"""


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

"""
## Random selectbox for options
"""


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})


option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


"""
## Lay out your app
"""

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


"""
## Show progress
"""

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'



