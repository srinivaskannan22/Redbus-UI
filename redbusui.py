import streamlit as st
import pandas as pd
import streamlit_pandas as sp

st.set_page_config(
    page_title="Red-Bus Details",
    page_icon="png-transparent-redbus-in-india-ticket-discounts-and-allowances-bus-text-logo-india.png",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)


@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

file = "tenstate.csv"
df = load_data()
create_data = {
                "name": "text",
                "type": "multiselect",
                "route-collected": "text"}

all_widgets = sp.create_widgets(df, create_data, ignore_columns=["s_no","departure_time","arrival_time","duration","seats_available"])
res = sp.filter_df(df, all_widgets)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("Red-Bus Details")
st.header("All-Bus")
st.write(df)
st.header("Filter-Bus")
st.write(res)
