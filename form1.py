# Core Pkgs
import streamlit as st
import pandas as pd
import datetime

def main():
	st.title("NCD Project Task Master")
	menu = ["Home","Creat Task","Update task","views"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Creat Task")

		# Task Creater
		# Combine forms + columns
		with st.form("my_form"):
				
			date1 = st.date_input(  "Task Assign Date",  datetime.date(2023, 3, 3))
			taskassign = st.selectbox("task",["Anayat","Ravinder","Abhishakh","Kashif","Sohobhit","sanjay Bema;","sanjay Sinha"])
			taskdes =   st.text_area('Enter brief task: ')
			date2 = st.date_input(  "Task end Date",  datetime.date(2023, 3, 3))
						     
			submit_task = st.form_submit_button(label='submit')			     
						     
			     			
	if submit_button:
			st.success("Thaks You have submited Task")

		
	else:
		st.subheader("Home")






if __name__ == '__main__':
	main()
