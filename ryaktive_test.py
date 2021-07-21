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



"""
## Batch elements and input widgets
"""

    
# Forms can be declared using the 'with' syntax
with st.form(key='my_form'):
    name = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='Submit')
    
# st.form_submit_button returns True upon form submit
if submit_button:
    st.write(f'Hello {name}')


"""
## Insert elements in order
"""
st.text('This will appear first')
# Appends some text to the app.

my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

my_slot2 = st.empty()
# Appends another empty slot.

st.text('This will appear last')
# Appends some more text to the app.

my_slot1.text('This will appear second')
# Replaces the first empty slot with a text string.

my_slot2.line_chart(np.random.randn(20, 2))
# Replaces the second empty slot with a chart.


"""
## Animate elements
"""

progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()


"""
## Append data to a table or chart
"""


# Get some data.
data = np.random.randn(10, 2)

# Show the data as a chart.
chart = st.line_chart(data)

# Wait 2 seconds, so the change is clearer.
time.sleep(2)

# Grab some more data.
data2 = np.random.randn(10, 2)

# Append the new data to the existing chart.
chart.add_rows(data2)

import pandas as pd 
import numpy as np
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt


# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Draw the dataframe

x = 10
'x', x  # <-- Draw the string 'x' and then the value of x


st.write('Hello, *World!* :sunglasses:')

st.write(1234)
st.write(pd.DataFrame({    
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))


# st.write('1 + 1 = ', 2)
# st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')


st.header('This is header')

st.subheader('This is subheader')


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})



genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")
    
    
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)


age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


from datetime import time
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)



from datetime import datetime

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)


start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

number = st.number_input('Insert a number')
st.write('The current number is ', number)
