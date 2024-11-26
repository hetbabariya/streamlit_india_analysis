import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv(r"C:\Users\hetba\Downloads\Download Data\indian_census\merge_india_census.csv")



def get_state_name():
    state_names = df['State name'].unique().tolist()
    return state_names

def get_district_name():
    district_names = df['District name'].tolist()
    return district_names

def get_primary_parameter():
    primary_para = df.columns
    primary_para = primary_para.insert(0,'')
    return primary_para

def get_secondary_parameter():
    secondary_para = df.columns
    secondary_para = secondary_para.insert(0,'')
    return secondary_para

def get_dataframe(option , primary , secondary,other_opt = None):
    if option == 'Overall India':
        final_df = df[ list(dict.fromkeys([ 'State name' ,'District name', primary , secondary]))]
    elif option == 'State':
        final_df =  df[df['State name'] == other_opt].loc[ : ,list(dict.fromkeys(['State name','District name', primary , secondary]))]
    elif option == 'District':
        final_df = df[df['District name'] == other_opt].loc[ : ,list(dict.fromkeys(['State name','District name', primary , secondary]))]

    return final_df

def display_overall(option , primary , secondary,other_opt = None) :
    st.title(f'{option.capitalize()} Analysis')
    df = get_dataframe(option , primary , secondary,other_opt)
    st.dataframe(df)
    display_summary(df , secondary)

def display_state(option , primary , secondary,other_opt = None):
    st.title(f'{other_opt.capitalize()} Analysis')
    df = get_dataframe(option , primary , secondary,other_opt)
    st.dataframe(df)
    display_summary(df , secondary)

def display_district(option , primary , secondary,other_opt = None):
    st.title(f'{other_opt.capitalize()} Analysis')
    df = get_dataframe(option , primary , secondary,other_opt)
    st.dataframe(df)
    display_summary(df , secondary)


def display_summary(df , secondary):

    st.subheader('Summary')
    col1 , col2 , col3 , col4 = st.columns(4)

    with col1:
        st.metric( 'Min' , round(df[secondary].min()))
    with col2:
        st.metric( 'Max' , round(df[secondary].max()))
    with col3:
        st.metric( 'Std' , round(df[secondary].std()))
    with col4:
        st.metric( 'Mean' , round(df[secondary].mean()))


def get_chart():
    chart_types = [
    'Bar Chart',
    'Scatter Plot',
]
    return chart_types


def display_chart(chart_list , primary , secondary , final_df):
    st.title('Charts')

    for chart in chart_list :


        if chart == 'Bar Chart':
            st.subheader(chart)
            fig_bar = px.bar(final_df, x=primary, y=secondary)
            st.plotly_chart(fig_bar, key=f"bar_{primary}_{secondary}_{chart}")


        elif chart == 'Scatter Plot':
            st.subheader(chart)
            fig = px.scatter(final_df, x=primary, y=secondary, color=secondary)
            st.plotly_chart(fig, key=f"scatter_{primary}_{secondary}_{chart}")


    try :
        fig = px.scatter_mapbox(final_df, lat="Latitude", lon="Longitude", size=primary, color=secondary,
                                zoom=4, size_max=35, mapbox_style="carto-positron", width=1200, height=700)
        st.plotly_chart(fig, use_container_width=True, key=f"mapbox_numeric_{primary}_{secondary}_{chart}")
    except TypeError as e :
        fig = px.scatter_mapbox(final_df, lat="Latitude", lon="Longitude",  color=secondary,
                                zoom=4, size_max=35, mapbox_style="carto-positron", width=1200, height=700)
        st.plotly_chart(fig, use_container_width=True, key=f"mapbox_numeric_{primary}_{secondary}_{chart}")