import numpy as np
import plotly.express as px
import streamlit as st

import utility as ut


st.set_page_config(layout="wide")

# slidebar

st.sidebar.title('India Analysis')

area_option = st.sidebar.selectbox('Select Area Wise',['Overall India','State','District'])

if area_option == 'Overall India' :
    pass

elif area_option == 'State':
    state_option = st.sidebar.selectbox('Select State Wise',ut.get_state_name())

elif area_option == 'District':
    district_option = st.sidebar.selectbox('Select District Wise',ut.get_district_name())

primary_option = st.sidebar.selectbox('Select Primary option',ut.get_primary_parameter())
secondary_option = st.sidebar.selectbox('Select Secondary option',ut.get_secondary_parameter())
chart_option = st.sidebar.multiselect('select chart',ut.get_chart())



btn_analyeze = st.sidebar.button('Analyeze')

if btn_analyeze :

    if primary_option == '' or secondary_option == '' :
        st.error('Please select options!')
    else :
        if area_option == 'Overall India':
            final_df = ut.df
            ut.display_overall(area_option,primary_option,secondary_option)
        elif area_option == 'State':
            final_df = ut.df[ut.df['State name'] == state_option]
            ut.display_overall(area_option,primary_option,secondary_option,state_option)
        elif area_option == 'District':
            final_df = ut.df[ut.df['District name'] == district_option]
            ut.display_overall(area_option,primary_option,secondary_option,district_option)

        ut.display_chart(chart_option,primary_option , secondary_option , final_df)
