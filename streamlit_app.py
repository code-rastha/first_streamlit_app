import streamlit

streamlit.title("My New custom Healthy Diner")

streamlit.header(" Boba Juice")
streamlit.text(" 🥗🍞 Taro")
streamlit.text(" 🍞 Vanilla")
streamlit.text(" 🐔 All mix")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('fruit')

#lets put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
