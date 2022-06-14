import streamlit as st
import hydralit_components as hc

menu_data = [
    {'label':"Left End"},
    {'label':"Book"},
    {'label':"Component"},
    {'label':"Dashboard"},
    {'label':"Right End"},
]

menu_id = hc.nav_bar(menu_definition=menu_data)

st.info(f"{menu_id=}")
#when we import hydralit, we automatically get all of Streamlit



