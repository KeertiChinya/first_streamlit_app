import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Braekfast Menu')
streamlit.text(' 🍞Omega 3 & 🥑 Blueberry Oatmeal')
streamlit.text('🐔Kale , Spanish &   🥣 Rocket Smoothie')
streamlit.text('🥗 Hard-Boiled 🐔 Free-Range Egg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
