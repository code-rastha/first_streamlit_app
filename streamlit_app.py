import streamlit

streamlit.title("My New custom Healthy Diner")

streamlit.header(" Boba Juice")
streamlit.text(" 🥗🍞 Taro")
streamlit.text(" 🍞 Vanilla")
streamlit.text(" 🐔 All mix")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
