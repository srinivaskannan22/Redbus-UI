import mysql.connector
import pandas as pd
import streamlit as st
import pandas as pd
import streamlit_pandas as sp
 
conn = mysql.connector.connect(

    host="localhost",

    user="root",

    port="3306",

    password="seenu2218",

    database="red_bus"

)

table_name='bus_details'
database="red_bus"
cursor = conn.cursor()

writer = cursor 

query = "SELECT * FROM bus_details"

query2 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND TABLE_SCHEMA = '{database}' ORDER BY ORDINAL_POSITION"

writer.execute(query)

view = cursor.fetchall()

data=pd.DataFrame(view)

writer.execute(query2)
s=cursor.fetchall()
data=pd.DataFrame(view)
flat_list = [item[0] for item in s]
#flat_list_1=['s_no','route-collected','name','type','arrival_time','departure_time','duration','price','seats_available','rating']
data.columns=flat_list
data=data.set_index('s_no')


st.set_page_config(
    page_title="Red-Bus Details",
    page_icon="png-transparent-redbus-in-india-ticket-discounts-and-allowances-bus-text-logo-india.png",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)

create_data = {
                "name": "text",
                "type": "multiselect",
                "route-collected": "multiselect"}

all_widgets = sp.create_widgets(data, create_data, ignore_columns=["departure_time","arrival_time","duration","seats_available"])
res = sp.filter_df(data, all_widgets)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("Red-Bus Details")
st.header("All-Bus")
st.write(data)
st.header("Filter-Bus")
st.write(res)

