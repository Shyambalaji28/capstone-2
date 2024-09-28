import json
import os
import pandas as pd
import mysql.connector
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image

#Aggregated Transaction
path="C:/Users/ADMIN/Desktop/data science projects/pulse/data/aggregated/transaction/country/india/state/"
agg_state=os.listdir(path)
column={'State':[],'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for state in agg_state:
    state_path=path+state+"/"
    agg_year=os.listdir(state_path)
    for year in agg_year:
        year_path=state_path+year+"/"
        agg_quar=os.listdir(year_path)
        for quar in agg_quar:
            quar_path=year_path+quar
            data=open(quar_path,"r")    
            T=json.load(data)
            for d in T['data']['transactionData']:
                name=d['name']
                count=d['paymentInstruments'][0]['count']
                amount=float(d['paymentInstruments'][0]['amount'])
                column['Transaction_type'].append(name)
                column['Transaction_count'].append(count)
                column['Transaction_amount'].append(amount)
                column['State'].append(state)
                column['Year'].append(year)
                column['Quarter'].append(int(quar.strip('.json')))
Agg_Trans=pd.DataFrame(column)
Agg_Trans['State']=Agg_Trans['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar islands' )
Agg_Trans['State']=Agg_Trans['State'].str.replace('-', ' ')
Agg_Trans['State']=Agg_Trans['State'].str.title()
Agg_Trans['State']=Agg_Trans['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')
Agg_Trans['Transaction_amount'] = Agg_Trans['Transaction_amount'].astype(float)


#Aggregated User
path1="C:/Users/ADMIN/Desktop/data science projects/pulse/data/aggregated/user/country/india/state/"
agg_state=os.listdir(path1)
column1={'State':[],'Year':[],'Quarter':[],'Brand':[], 'Count':[], 'Percentage':[]}
for state in agg_state:
    state_path=path1+state+"/"
    agg_year=os.listdir(state_path)
    for year in agg_year:
        year_path=state_path+year+"/"
        agg_quar=os.listdir(year_path)
        for quar in agg_quar:
            quar_path=year_path+quar
            data=open(quar_path,"r")    
            U=json.load(data)
            try:
                 if U['data']['usersByDevice'] is not None:
                    for d in U['data']['usersByDevice']:
                        Brand=d['brand']
                        Count=d['count']
                        Percentage=d['percentage']
                        column1['Brand'].append(Brand)
                        column1['Count'].append(Count)
                        column1['Percentage'].append(Percentage)
                        column1['State'].append(state)
                        column1['Year'].append(year)
                        column1['Quarter'].append(int(quar.strip('.json')))
            except KeyError:
                    pass
Agg_User=pd.DataFrame(column1)
# Agg_User['State'] = Agg_User['State'].astype(str) 
Agg_User['State']=Agg_User['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar islands' )
Agg_User['State']=Agg_User['State'].str.replace('-', ' ')
Agg_User['State']=Agg_User['State'].str.title()
Agg_User['State']=Agg_User['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


# Map Transaction
path2="C:/Users/ADMIN/Desktop/data science projects/pulse/data/map/transaction/hover/country/india/state/"
agg_state=os.listdir(path2)
column2={'State':[],'Year':[],'Quarter':[],'district':[], 'Transaction_count':[], 'Transaction_amount':[]}
for state in agg_state:
    state_path=path2+state+"/"
    agg_year=os.listdir(state_path)
    for year in agg_year:
        year_path=state_path+year+"/"
        agg_quar=os.listdir(year_path)
        for quar in agg_quar:
            quar_path=year_path+quar
            data=open(quar_path,"r")    
            MT=json.load(data)
            for d in MT['data']['hoverDataList']:
                name=d['name']
                count=d['metric'][0]['count']
                amount=float(d['metric'][0]['amount'])
                column2['district'].append(name)
                column2['Transaction_count'].append(count)
                column2['Transaction_amount'].append(amount)
                column2['State'].append(state)
                column2['Year'].append(year)
                column2['Quarter'].append(int(quar.strip('.json')))
Map_Trans=pd.DataFrame(column2)
Map_Trans['State']=Map_Trans['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar islands' )
Map_Trans['State']=Map_Trans['State'].str.replace('-', ' ')
Map_Trans['State']=Map_Trans['State'].str.title()
Map_Trans['State']=Map_Trans['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')
Map_Trans['Transaction_amount'] = Map_Trans['Transaction_amount'].astype(float)


#Map User
path3="C:/Users/ADMIN/Desktop/data science projects/pulse/data/map/user/hover/country/india/state/"
agg_state=os.listdir(path3)
column3={'State':[],'Year':[],'Quarter':[],'district':[], 'registeredUsers':[],'appOpens':[]}
for state in agg_state:
    state_path=path3+state+"/"
    agg_year=os.listdir(state_path)
    for year in agg_year:
        year_path=state_path+year+"/"
        agg_quar=os.listdir(year_path)
        for quar in agg_quar:
            quar_path=year_path+quar
            data=open(quar_path,"r")    
            MU=json.load(data)
            
           
            try:
                for d in MU['data']['hoverData'].items():
                        district=d[0]
                        registeredUsers=d[1]['registeredUsers']
                        appOpens=d[1]['appOpens']
                        column3['district'].append(district)
                        column3['registeredUsers'].append(registeredUsers)
                        column3['appOpens'].append(appOpens)
                        column3['State'].append(state)
                        column3['Year'].append(year)
                        column3['Quarter'].append(int(quar.strip('.json')))
            except:
                    pass
Map_User=pd.DataFrame(column3)
Map_User['State']=Map_User['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar islands' )
Map_User['State']=Map_User['State'].str.replace('-', ' ')
Map_User['State']=Map_User['State'].str.title()
Map_User['State']=Map_User['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


# TOP Transaction
path4="C:/Users/ADMIN/Desktop/data science projects/pulse/data/top/transaction/country/india/state/"
agg_state=os.listdir(path4)
column4={'State':[],'Year':[],'Quarter':[],'district':[], 'Transaction_count':[], 'Transaction_amount':[]}
for state in agg_state:
    state_path=path4+state+"/"
    agg_year=os.listdir(state_path)
    for year in agg_year:
        year_path=state_path+year+"/"
        agg_quar=os.listdir(year_path)
        for quar in agg_quar:
            quar_path=year_path+quar
            data=open(quar_path,"r")    
            TT=json.load(data)
            try:
                for M in TT['data']['districts']:
                    entityName=M['entityName']
                    count=M['metric']['count']
                    amount=float(M['metric']['amount'])
                    column4['district'].append(entityName)
                    column4['Transaction_count'].append(count)
                    column4['Transaction_amount'].append(amount)
                    column4['State'].append(state)
                    column4['Year'].append(year)
                    column4['Quarter'].append(int(quar.strip('.json')))
            except:
                pass
Top_trans=pd.DataFrame(column4)
Top_trans['State']=Top_trans['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar islands' )
Top_trans['State']=Top_trans['State'].str.replace('-', ' ')
Top_trans['State']=Top_trans['State'].str.title()
Top_trans['State']=Top_trans['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')
Top_trans['Transaction_amount'] = Top_trans['Transaction_amount'].astype(float)


path5="C:/Users/ADMIN/Desktop/data science projects/pulse/data/top/user/country/india/state/"
agg_state=os.listdir(path5)
column5={'State':[],'Year':[],'Quarter':[],'district':[], 'registeredUsers':[]}
for state in agg_state:
    state_path=path5+state+"/"
    agg_year=os.listdir(state_path)
    for year in agg_year:
        year_path=state_path+year+"/"
        agg_quar=os.listdir(year_path)
        for quar in agg_quar:
            quar_path=year_path+quar
            data=open(quar_path,"r")    
            TU=json.load(data)
            try:
                for U in TU['data']['districts']:
                    district=U['name']
                    registeredUsers=U['registeredUsers']
                    column5['district'].append(district)
                    column5['registeredUsers'].append(registeredUsers)
                    column5['State'].append(state)
                    column5['Year'].append(year)
                    column5['Quarter'].append(int(quar.strip('.json')))
            except:
                pass
Top_User=pd.DataFrame(column5)
Top_User['State']=Top_User['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar islands' )
Top_User['State']=Top_User['State'].str.replace('-', ' ')
Top_User['State']=Top_User['State'].str.title()
Top_User['State']=Top_User['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


#My SQL connections
#Agg Trans
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shyam@28",
        database="phonepaydata"
    )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Agg_Trans(State VARCHAR(255) , Year int, Quarter int,Transaction_type VARCHAR(255), Transaction_count bigint,  Transaction_amount bigint)")    
for index, row in Agg_Trans.iterrows():
        sql = "INSERT IGNORE INTO Agg_Trans (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (row['State'], row['Year'], row['Quarter'], row['Transaction_type'], row['Transaction_count'], row['Transaction_amount'])
        mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()

#Agg USer
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shyam@28",
        database="phonepaydata"
    )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Agg_User(State VARCHAR(255) , Year int, Quarter int,Brand VARCHAR(255), Count bigint,  Percentage decimal(5,5))")    
for index, row in Agg_User.iterrows():
        sql = "INSERT IGNORE INTO Agg_User (State, Year, Quarter, Brand, Count, Percentage) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (row['State'], row['Year'], row['Quarter'], row['Brand'], row['Count'], row['Percentage'])
        mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()

#Map Trans
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shyam@28",
        database="phonepaydata"
    )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Map_Trans(State VARCHAR(255) , Year int, Quarter int, district VARCHAR(255),Transaction_count bigint, Transaction_amount bigint)")    
for index, row in Map_Trans.iterrows():
        sql = "INSERT IGNORE INTO Map_Trans (State, Year, Quarter, district, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (row['State'], row['Year'], row['Quarter'], row['district'], row['Transaction_count'], row['Transaction_amount'])
        mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()

#Map user

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shyam@28",
        database="phonepaydata"
    )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Map_User(State VARCHAR(255) , Year int, Quarter int,registeredUsers bigint, appOpens bigint)")    
for index, row in Map_User.iterrows():
        sql = "INSERT IGNORE INTO Map_User (State, Year, Quarter, registeredUsers, appOpens) VALUES (%s, %s, %s, %s, %s)"
        val = (row['State'], row['Year'], row['Quarter'], row['registeredUsers'], row['appOpens'])
        mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()

#Top Trans

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shyam@28",
        database="phonepaydata"
    )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Top_trans(State VARCHAR(255) , Year int, Quarter int, district VARCHAR(255),Transaction_count bigint, Transaction_amount bigint)")    
for index, row in Top_trans.iterrows():
        sql = "INSERT IGNORE INTO Top_trans (State, Year, Quarter, district, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (row['State'], row['Year'], row['Quarter'], row['district'], row['Transaction_count'], row['Transaction_amount'])
        mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()


#Top user

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shyam@28",
        database="phonepaydata"
    )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Top_User(State VARCHAR(255) , Year int, Quarter int,district VARCHAR(255), registeredUsers bigint)")    
for index, row in Top_User.iterrows():
        sql = "INSERT IGNORE INTO Top_User (State, Year, Quarter, district, registeredUsers) VALUES (%s, %s, %s, %s, %s)"
        val = (row['State'], row['Year'], row['Quarter'], row['district'], row['registeredUsers'])
        mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()


#Streamlit 
#Aggregate transaction sorting w.r.t year
def Transaction_amount_count_y(df,Years):
    tacy=df[df['Year'] .astype(int)== Years]

    tacy.reset_index(drop=True, inplace=True)
    tacyg=tacy.groupby('State')[["Transaction_count","Transaction_amount"]].sum()
    tacyg.reset_index(inplace=True)
    col1,col2=st.columns(2)



    with col1:
      
        fig_amount = px.bar(tacyg, x="State",y="Transaction_amount",title=f"{Years}TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650)
        st.plotly_chart(fig_amount)
      # st.plotly_chart.show(fig_amount)
    with col2:
    
        fig_count = px.bar(tacyg, x="State",y="Transaction_count",title=f"{Years}TRANSACTION COUNT",
                            color_discrete_sequence=px.colors.sequential.Bluered_r,height=650,width=650)
        st.plotly_chart(fig_count)
        
      # st.plotly_chart.show(fig_count)
    col1,col2=st.columns(2)
    with col1:
        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data1=json.loads(response.content)
        State=[]
        for feature in data1["features"]:
            State.append(feature["properties"]["ST_NM"])
        State.sort()

        fig_india_1=px.choropleth(tacyg,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_amount",
                                    color_continuous_scale="Rainbow",range_color=(tacyg["Transaction_amount"].min(),
                                                                                tacyg["Transaction_amount"].max()),
                                                                                hover_name="State",title=f"{Years} Transaction Amount" ,
                                                                                fitbounds="locations",height=600,width=600)
        #,fig_india_1.update_geos(visible=False))
        fig_india_1.update_geos(visible=False)
        st.plotly_chart(fig_india_1)
    with col2:
        fig_india_2=px.choropleth(tacyg,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_count",
                                    color_continuous_scale="Rainbow",range_color=(tacyg["Transaction_count"].min(),
                                                                                tacyg["Transaction_count"].max()),
                                                                                hover_name="State",title=f"{Years} Transaction Count" ,
                                                                                fitbounds="locations",height=600,width=600)
        #,fig_india_1.update_geos(visible=False))
        fig_india_2.update_geos(visible=False)
        st.plotly_chart(fig_india_2)

    return tacyg

# CODE FOR TRANSACTION TYPE #
def aggre_trans_type(df, state):
    # Filter the DataFrame by the selected state
    tacy = df[df['State'] == state]

    tacy.reset_index(drop=True, inplace=True)
    
    # Check available columns
    print(tacy.columns)
    
    # Group by the correct column name
    tacyg = tacy.groupby('Transaction_type')[["Transaction_count", "Transaction_amount"]].sum()
    tacyg.reset_index(inplace=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_pie_1 = px.pie(data_frame=tacyg, names="Transaction_type", values="Transaction_amount",
                           width=600, title=f"{state.upper()} TRANSACTION_AMOUNT", hole=0.5)
        st.plotly_chart(fig_pie_1)
    
    with col2:
        fig_pie_2 = px.pie(data_frame=tacyg, names="Transaction_type", values="Transaction_count",
                           width=600, title=f"{state.upper()} TRANSACTION_COUNT", hole=0.5)
        st.plotly_chart(fig_pie_2)
    
    return tacyg

#In accordance to Quarter

def  Transaction_amount_count_yq(df,quarter):
   tacy=df[df['Quarter'].astype(int) == quarter]

   tacy.reset_index(drop=True, inplace=True)
   tacyg=tacy.groupby('State')[["Transaction_count","Transaction_amount"]].sum()
   tacyg.reset_index(inplace=True)
   col1,col2=st.columns(2)




   with col1:
      
        fig_amount = px.bar(tacyg, x="State",y="Transaction_amount",title=f"{quarter}Quarter TRANSACTION AMOUNT",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650)
        # fig_amount.show()
        st.plotly_chart(fig_amount)
   with col2:
      
        fig_count = px.bar(tacyg, x="State",y="Transaction_count",title=f"{quarter}Quarter TRANSACTION COUNT",
                                color_discrete_sequence=px.colors.sequential.Bluered_r,height=650,width=650)
        # fig_count.show()
      
        st.plotly_chart(fig_count)
   url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
   response= requests.get(url)
   data1=json.loads(response.content)
   State=[]
   for feature in data1["features"]:
      State.append(feature["properties"]["ST_NM"])
   State.sort()
   col1,col2=st.columns(2)
   with col1:

        fig_india_3=px.choropleth(tacyg,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_amount",
                                    color_continuous_scale="Rainbow",range_color=(tacyg["Transaction_amount"].min(),
                                                                                tacyg["Transaction_amount"].max()),
                                                                                hover_data="State",title=f"{quarter} Quarter Transaction Amount" ,
                                                                                fitbounds="locations",height=600,width=600)
        #,fig_india_1.update_geos(visible=False))
        fig_india_3.update_geos(visible=False)
        st.plotly_chart(fig_india_3)

   with col2:

        fig_india_4=px.choropleth(tacyg,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_count",
                                    color_continuous_scale="Rainbow",range_color=(tacyg["Transaction_count"].min(),
                                                                                tacyg["Transaction_count"].max()),
                                                                                hover_data="State",title=f" {quarter} Quarter Transaction Count" ,
                                                                                fitbounds="locations",height=600,width=600)
        #,fig_india_1.update_geos(visible=False))
        fig_india_4.update_geos(visible=False)
        st.plotly_chart(fig_india_4)
        return tacyg

# Transaction_amount_count_y(Agg_Trans,2)
        
#Agg user analysis w.r.t year
def Agg_user_data(df, year):
    # Ensure 'Year' column is of correct type
    df['Year'] = df['Year'].astype(int)
    
    # Filter and group data
    aguy = df[df['Year'] == year]
    aguyg = aguy.groupby('Brand')['Count'].sum().reset_index()
    
    # Plot with Plotly Express
    fig = px.bar(aguyg,
                 x='Brand',  # Use 'registeredUsers' as x-axis (horizontal bars)
                 y='Count',  # Use 'State' as y-axis
                 title=f"Brand and count for agg_user by {year}",
                 width=800,color_discrete_sequence=px.colors.sequential.haline_r)
    
    st.plotly_chart(fig)


#agg user analysing w.r.t quarter
def Agg_user_data_quarter(df, quarter):
    df['Quarter'] = df['Quarter'].astype(int)
    aguyq = df[df['Quarter'] == quarter]
    aguygq = aguyq.groupby('Brand')['Count'].sum().reset_index()
    figQ = px.bar(aguygq,
                 x='Brand', 
                 y='Count',  
                 title=f"Quarter {quarter} Brand and count for agg_user",
                 width=800,color_discrete_sequence=px.colors.sequential.haline_r)
    
    st.plotly_chart(figQ)

#user data w r t state
def aggre_user_state(df,state):
    aguygs=df[df['State'] == state]
    aguygs.reset_index(drop=True, inplace=True)
    #col1,col2=st.columns(2)
    
    #with col1:
    fig_line_1 = px.line(data_frame = aguygs, x = "Brand",y = "Count",hover_data= "Percentage",
                            width = 1000,title=f"{state} Brand count w.r.t percentage",markers=True)
    #fig_line_1.show()
    st.plotly_chart(fig_line_1)



#MAP TRANSACTION w.r.t.years


def  Map_transaction_amount_count_y(df,Years):
   tacymap=df[df['Year'].astype(int) == Years]

   tacymap.reset_index(drop=True, inplace=True)
   tacygmap=tacymap.groupby('State')[["Transaction_count","Transaction_amount"]].sum()
   tacygmap.reset_index(inplace=True)
   col1,col2=st.columns(2)



   with col1:
      
        map_fig_amount = px.bar(tacygmap, x="State",y="Transaction_amount",title=f"{Years} MAP TRANSACTION AMOUNT",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650)
        # map_fig_amount()
        st.plotly_chart(map_fig_amount)
   with col2:
      
        map_fig_count = px.bar(tacygmap, x="State",y="Transaction_count",title=f"{Years} MAP TRANSACTION COUNT",
                                color_discrete_sequence=px.colors.sequential.Bluered_r,height=650,width=650)
        # map_fig_count()
      
        st.plotly_chart(map_fig_count)
   url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
   response= requests.get(url)
   data1=json.loads(response.content)
   State=[]
   for feature in data1["features"]:
      State.append(feature["properties"]["ST_NM"])
   State.sort()

   Map_fig_india_1=px.choropleth(tacygmap,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_amount",
                              color_continuous_scale="Rainbow",range_color=(tacygmap["Transaction_amount"].min(),
                                                                           tacygmap["Transaction_amount"].max()),
                                                                           hover_data="State",title=f"{Years} MAP Transaction Amount" ,
                                                                           fitbounds="locations",height=600,width=600)
   #,fig_india_1.update_geos(visible=False))
   Map_fig_india_1.update_geos(visible=False)
   st.plotly_chart(Map_fig_india_1)

   Map_fig_india_2=px.choropleth(tacygmap,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_count",
                              color_continuous_scale="Rainbow",range_color=(tacygmap["Transaction_count"].min(),
                                                                           tacygmap["Transaction_count"].max()),
                                                                           hover_data="State",title=f"{Years} MAP Transaction Count" ,
                                                                           fitbounds="locations",height=600,width=600)
   #,fig_india_1.update_geos(visible=False))
   Map_fig_india_2.update_geos(visible=False)
   st.plotly_chart(Map_fig_india_2)

# Map_transaction_amount_count_y(Map_Trans,2020)


#map transaction w.r.t.state and districts#
def Map_trans_type(df,state):
    tacymap=df[df['State'] == state]

    tacymap.reset_index(drop=True, inplace=True)
    # tacymap
    tacygmap=tacymap.groupby('district')[["Transaction_count","Transaction_amount"]].sum()
    tacygmap.reset_index(inplace=True)
    # tacyg

    fig_pie_1 = px.pie(data_frame = tacygmap, names = "district",values = "Transaction_amount",
                        width = 600,title=f"{state.upper()} TRANSACTION_AMOUNT" , hole=0.5)
    st.plotly_chart(fig_pie_1)

    fig_pie_2 = px.pie(data_frame = tacygmap, names = "district",values = "Transaction_count",
                        width = 600,title=f"{state.upper()} TRANSACTION_COUNT" , hole=0.5)
    st.plotly_chart(fig_pie_2)
# Map_trans_type(Map_Trans, 'West Bengal')


#Map Trans w.r.t Quarter
#Map transaction w.r.t.quarter#
def  Map_Transaction_amount_count_yq(df,quarter):
   tacymap=df[df['Quarter'] == quarter]

   tacymap.reset_index(drop=True, inplace=True)
   tacygmap=tacymap.groupby('State')[["Transaction_count","Transaction_amount"]].sum()
   tacygmap.reset_index(inplace=True)
   col1,col2=st.columns(2)
   with col1:
      
    fig_amount_quat1 = px.bar(tacygmap, x="State",y="Transaction_amount",title=f"{quarter}Quarter TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650)
    
    st.plotly_chart(fig_amount_quat1)
   with col2:
      
    fig_count_quat2 = px.bar(tacygmap, x="State",y="Transaction_count",title=f"{quarter}Quarter TRANSACTION COUNT",
                            color_discrete_sequence=px.colors.sequential.Bluered_r,height=650,width=650)  
    st.plotly_chart(fig_count_quat2)


   url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
   response= requests.get(url)
   data1=json.loads(response.content)
   State=[]
   for feature in data1["features"]:
      State.append(feature["properties"]["ST_NM"])
   State.sort()
   col1,col2=st.columns(2)
   with col1:
     fig_india_1quat=px.choropleth(tacygmap,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_amount",
                              color_continuous_scale="Rainbow",range_color=(tacygmap["Transaction_amount"].min(),
                                                                           tacygmap["Transaction_amount"].max()),
                                                                           hover_data="State",title=f"{quarter} Quarter Transaction Amount" ,
                                                                           fitbounds="locations",height=600,width=600)
   #,fig_india_1.update_geos(visible=False))
     fig_india_1quat.update_geos(visible=False)
     st.plotly_chart(fig_india_1quat)
   
   with col2:
      fig_india_2quat=px.choropleth(tacygmap,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_count",
                              color_continuous_scale="Rainbow",range_color=(tacygmap["Transaction_count"].min(),
                                                                           tacygmap["Transaction_count"].max()),
                                                                           hover_data="State",title=f" {quarter} Quarter Transaction Count" ,
                                                                           fitbounds="locations",height=600,width=600)
   #,fig_india_1.update_geos(visible=False))
      fig_india_2quat.update_geos(visible=False)
      st.plotly_chart(fig_india_2quat)

# Map_Transaction_amount_count_yq(Map_Trans,2)

def Map_trans_quattype(df,state):
    tacymap=df[df['State'] == state]

    tacymap.reset_index(drop=True, inplace=True)
    # tacymap
    tacygmap=tacymap.groupby('district')[["Transaction_count","Transaction_amount"]].sum()
    tacygmap.reset_index(inplace=True)
    # tacyg

    fig_pie_1 = px.pie(data_frame = tacygmap, names = "district",values = "Transaction_amount",
                        width = 600,title=f"{state.upper()} TRANSACTION_AMOUNT" , hole=0.5)
    st.plotly_chart(fig_pie_1)

    fig_pie_2 = px.pie(data_frame = tacygmap, names = "district",values = "Transaction_count",
                        width = 600,title=f"{state.upper()} TRANSACTION_COUNT" , hole=0.5)
    st.plotly_chart(fig_pie_2)
#Map user analysis w.r.t year
def Map_user_data(df, year):
    # Ensure 'Year' column is of correct type
    df['Year'] = df['Year'].astype(int)
    
    # Filter and group data
    aguymuser = df[df['Year'] == year]
    aguygmuser = aguymuser.groupby('State')[["registeredUsers","appOpens"]].sum().reset_index()
    # Plot with Plotly Express
    figm = px.bar(data_frame=aguygmuser,
                 x='State',  # Use 'registeredUsers' as x-axis (horizontal bars)
                 y='registeredUsers',  # Use 'State' as y-axis
                 title=f"registered user and appopens for mapuser by {year}",
                 width=800,color_discrete_sequence=px.colors.sequential.haline_r,hover_name="registeredUsers")
    
    st.plotly_chart(figm)
#need to discuss shoaib for separe app a=opens
#Map user analysing w.r.t quarter
def Map_user_data_quarter(df, quarter):
    df['Quarter'] = df['Quarter'].astype(int)
    aguyqmuser = df[df['Quarter'] == quarter]  
    aguygqmuser = aguyqmuser.groupby('State')[["registeredUsers","appOpens"]].sum().reset_index()
    figQmu = px.bar(aguygqmuser,
                 x='State', 
                 y='registeredUsers',  
                 title=f"{df['Year'].min()} YEARS Quarter {quarter} for registered user and appopens",
                 width=800,color_discrete_sequence=px.colors.sequential.haline_r)
    
    st.plotly_chart(figQmu)
#need to discuss shoaib for separe app a=opens
#user data w r t state
def Map_user_data_state(df,state):
    aguygsmuser=df[df['State'] == state]
    aguygsmuser.reset_index(drop=True, inplace=True)
    col1,col2=st.columns(2)
    
    with col1:
     fig_line_1m = px.line(data_frame = aguygsmuser, x = "registeredUsers",y = "district",
                            width = 1000,title=f"{state.upper()} Brand count w.r.t percentage",markers=True)
    #fig_line_1.show()
     st.plotly_chart(fig_line_1m)
    with col2:
     fig_line_2m = px.line(data_frame = aguygsmuser, x = "appOpens",y = "district",
                            width = 1000,title=f"{state.upper()} Brand count w.r.t percentage",markers=True)
    #fig_line_2.show()
     st.plotly_chart(fig_line_2m)


def Top_Transaction_amount_count_y(df, years):
    df['Year'] = df['Year'].astype(int)
    tacytoptrans = df[df["Year"] == years]
    tacytoptrans.reset_index(drop=True, inplace=True)
    
    if tacytoptrans.empty:
        st.write("No data available for the selected year.")
        return
    
    tacygtoptrans = tacytoptrans.groupby("State")[["Transaction_count", "Transaction_amount"]].sum()
    tacygtoptrans.reset_index(inplace=True)
    
    col1, col2 = st.columns(2)
    with col1:    
        fig_amounttop = px.bar(tacygtoptrans, x="State", y="Transaction_amount", 
                               title=f"{years} TRANSACTION AMOUNT",
                               color_discrete_sequence=px.colors.sequential.Aggrnyl, height=650, width=650)
        st.plotly_chart(fig_amounttop)
    
    with col2:    
        fig_counttop = px.bar(tacygtoptrans, x="State", y="Transaction_count", 
                              title=f"{years} TRANSACTION COUNT",
                              color_discrete_sequence=px.colors.sequential.Bluered_r, height=650, width=650)
        st.plotly_chart(fig_counttop)
    
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(url)
    
    if response.status_code == 200:
        data1 = json.loads(response.content)
    else:
        st.write("Failed to load GeoJSON data.")
        return
    
    col1, col2 = st.columns(2)
    with col1:
        fig_india_1t = px.choropleth(tacygtoptrans, geojson=data1, locations="State", 
                                     featureidkey="properties.ST_NM", color="Transaction_amount",
                                     color_continuous_scale="Rainbow", 
                                     range_color=(tacygtoptrans["Transaction_amount"].min(),
                                                  tacygtoptrans["Transaction_amount"].max()),
                                     hover_data="State", title=f"{years} Transaction Amount",
                                     fitbounds="locations", height=600, width=600)
        fig_india_1t.update_geos(visible=False)
        st.plotly_chart(fig_india_1t)
    
    with col2:
        fig_india_2t = px.choropleth(tacygtoptrans, geojson=data1, locations="State", 
                                     featureidkey="properties.ST_NM", color="Transaction_count",
                                     color_continuous_scale="Rainbow", 
                                     range_color=(tacygtoptrans["Transaction_count"].min(),
                                                  tacygtoptrans["Transaction_count"].max()),
                                     hover_data="State", title=f"{years} Transaction Count",
                                     fitbounds="locations", height=600, width=600)
        fig_india_2t.update_geos(visible=False)
        st.plotly_chart(fig_india_2t)

def Top_trans_type(df,state):
    tacytop=df[df['State'] == state]
    tacytop.reset_index(drop=True, inplace=True)
    # tacy
    tacygtop=tacytop.groupby('State')[["Transaction_count","Transaction_amount"]].sum()
    tacygtop.reset_index(inplace=True)
    # tacyg
    col1,col2=st.columns(2)
    with col1:
        fig_pie_1t = px.pie(data_frame = tacygtop, names = "State",values = "Transaction_amount",
                            width = 600,title=f"{state.upper()} TRANSACTION_AMOUNT" , hole=0.5)
        st.plotly_chart(fig_pie_1t)
    with col2:
        fig_pie_2t = px.pie(data_frame = tacygtop, names = "State",values = "Transaction_count",
                            width = 600,title=f"{state.upper()} TRANSACTION_COUNT" , hole=0.5)
        st.plotly_chart(fig_pie_2t)
#In accordance to Quarter
def  Top_Transaction_amount_count_q(df,quarter):
   tacytop=df[df['Quarter'] == quarter]

   tacytop.reset_index(drop=True, inplace=True)
   tacygtop=tacytop.groupby('State')[["Transaction_count","Transaction_amount"]].sum()
   tacygtop.reset_index(inplace=True)
   col1,col2=st.columns(2)
   with col1:     
        fig_amounttq = px.bar(tacygtop, x="State",y="Transaction_amount",title=f"{quarter}Quarter TRANSACTION AMOUNT",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=650)        # fig_amount.show()
        st.plotly_chart(fig_amounttq)
   with col2:     
        fig_counttq1 = px.bar(tacygtop, x="State",y="Transaction_count",title=f"{quarter}Quarter TRANSACTION COUNT",
                                color_discrete_sequence=px.colors.sequential.Bluered_r,height=650,width=650)      
        st.plotly_chart(fig_counttq1)
   url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
   response= requests.get(url)
   data1=json.loads(response.content)
   State=[]
   for feature in data1["features"]:
      State.append(feature["properties"]["ST_NM"])
   State.sort()
   col1,col2=st.columns(2)
   with col1:
        fig_india_3tq=px.choropleth(tacygtop,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_amount",
                                    color_continuous_scale="Rainbow",range_color=(tacygtop["Transaction_amount"].min(),
                                                                                tacygtop["Transaction_amount"].max()),
                                                                                hover_data="State",title=f"{quarter} Quarter Transaction Amount" ,
                                                                                fitbounds="locations",height=600,width=600)
        #,fig_india_1.update_geos(visible=False))
        fig_india_3tq.update_geos(visible=False)
        st.plotly_chart(fig_india_3tq)
   with col2:
        fig_india_4tq=px.choropleth(tacygtop,geojson=data1,locations="State",featureidkey="properties.ST_NM",color="Transaction_count",
                                    color_continuous_scale="Rainbow",range_color=(tacygtop["Transaction_count"].min(),
                                                                                tacygtop["Transaction_count"].max()),
                                                                                hover_data="State",title=f" {quarter} Quarter Transaction Count" ,
                                                                                fitbounds="locations",height=600,width=600)
        #,fig_india_1.update_geos(visible=False))
        fig_india_4tq.update_geos(visible=False)
        st.plotly_chart(fig_india_4tq)
#top  quarter state sort
def Top_trans_type1(df,state):
    tacytop=df[df['State'] == state]
    tacytop.reset_index(drop=True, inplace=True)
    # tacy
    tacygtop=tacytop.groupby('State')[["Transaction_count","Transaction_amount"]].sum()
    tacygtop.reset_index(inplace=True)
    # tacyg
    col1,col2=st.columns(2)    
    with col1:
        fig_pie_1tqs = px.pie(data_frame = tacygtop, names = "State",values = "Transaction_amount",
                            width = 600,title=f"{state.upper()} TRANSACTION_AMOUNT" , hole=0.5)
        st.plotly_chart(fig_pie_1tqs)
    with col2:
        fig_pie_2tqs = px.pie(data_frame = tacygtop, names = "State",values = "Transaction_count",
                            width = 600,title=f"{state.upper()} TRANSACTION_COUNT" , hole=0.5)
        st.plotly_chart(fig_pie_2tqs)
#Top user analysis w.r.t year
def Top_user_data(df, year):
    # Ensure 'Year' column is of correct type
    df['Year'] = df['Year'].astype(int)    
    # Filter and group data
    aguymttop = df[df['Year'] == year]
    aguygmttop = aguymttop.groupby(["State","Quarter"]) ['registeredUsers'].sum().reset_index()    
    # Plot with Plotly Express
    figmt = px.bar(aguygmttop,
                 x='State',  # Use 'registeredUsers' as x-axis (horizontal bars)
                 y='registeredUsers',  # Use 'State' as y-axis
                 title=f"registered user topuser by {year}",
                 width=800,color_discrete_sequence=px.colors.sequential.haline_r)    
    st.plotly_chart(figmt)
#user data w r t state
def Top_user_state(df,state):
    aguygsmtop=df[df['State'] == state]
    aguygsmtop.reset_index(drop=True, inplace=True)
    #col1,col2=st.columns(2)    
    #with col1:
    fig_line_1mt = px.line(data_frame = aguygsmtop, x = "Quarter",y = "registeredUsers",
                            width = 1000,title=f"{state.upper()} registeredUsers",markers=True)
    #fig_line_1.show()
    st.plotly_chart(fig_line_1mt)
def top_chart_ta(table_name):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shyam@28",
            database="phonepaydata"
        )
    mycursor = mydb.cursor()
    Query1=f'''select state,sum(transaction_amount) As transaction_amount
                From {table_name}
                group by state
                order by transaction_amount Desc
                LIMIT 10;'''
    mycursor.execute(Query1)
    table_1=mycursor.fetchall()
    mydb.commit()
    DF_1=pd.DataFrame(table_1,columns=("state","transaction_amount"))
    col1,col2=st.columns(2)
    with col1:   
        Chart1 = px.bar(DF_1, x="state",y="transaction_amount",title="TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl,hover_name="state",height=650,width=650)
        st.plotly_chart(Chart1)
    Query2=f'''select state,sum(transaction_amount) As transaction_amount
                From {table_name}
                group by state
                order by transaction_amount 
                LIMIT 10;'''
    mycursor.execute(Query2)
    table_2=mycursor.fetchall()
    mydb.commit()
    DF_2=pd.DataFrame(table_2,columns=("state","transaction_amount"))
    with col2:   
        Chart2 = px.bar(DF_2, x="state",y="transaction_amount",title="TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl_r,hover_name="state",height=650,width=650)
        st.plotly_chart(Chart2)
    Query3=f'''select state,avg(transaction_amount) As transaction_amount
                From {table_name}
                group by state
                order by transaction_amount 
                LIMIT 10;'''
    mycursor.execute(Query3)
    table_3=mycursor.fetchall()
    mydb.commit()
    DF_3=pd.DataFrame(table_3,columns=("state","transaction_amount"))   
    Chart3 = px.bar(DF_3, x="state",y="transaction_amount",title="TRANSACTION AMOUNT",
                        color_discrete_sequence=px.colors.sequential.Bluered_r,hover_name="state",height=650,width=650)
    st.plotly_chart(Chart3)
# top_chart_ta("Map_Trans")

def top_chart_tc(table_name):

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shyam@28",
            database="phonepaydata"
        )
    mycursor = mydb.cursor()
    Query4=f'''select state,sum(transaction_count) As transaction_count
                From {table_name}
                group by state
                order by transaction_count Desc
                LIMIT 10;'''
    mycursor.execute(Query4)
    table_4=mycursor.fetchall()
    mydb.commit()
    DF_4=pd.DataFrame(table_4,columns=("state","transaction_count"))
    
        
    Chart4 = px.bar(DF_4, x="state",y="transaction_count",title="TRANSACTION COUNT",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl,hover_name="state",height=650,width=650)
    st.plotly_chart(Chart4)


    Query5=f'''select state,sum(transaction_count) As transaction_count
                From {table_name}
                group by state
                order by transaction_count 
                LIMIT 10;'''
    mycursor.execute(Query5)
    table_5=mycursor.fetchall()
    mydb.commit()
    DF_5=pd.DataFrame(table_5,columns=("state","transaction_count"))
        
    Chart5 = px.bar(DF_5, x="state",y="transaction_count",title="TRANSACTION COUNT",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl_r,hover_name="state",height=650,width=650)
    st.plotly_chart(Chart5)


    Query6=f'''select state,avg(transaction_count) As transaction_count
                From {table_name}
                group by state
                order by transaction_count 
                LIMIT 10;'''
    mycursor.execute(Query6)
    table_6=mycursor.fetchall()
    mydb.commit()
    DF_6=pd.DataFrame(table_6,columns=("state","transaction_count"))
        
    Chart6 = px.bar(DF_6, x="state",y="transaction_count",title="TRANSACTION COUNT",
                        color_discrete_sequence=px.colors.sequential.Bluered_r,hover_name="state",height=650,width=650)
    st.plotly_chart(Chart6)
# top_chart_tc("Map_Trans")
    
def top_chart_AU(table_name):

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shyam@28",
            database="phonepaydata"
        )
    mycursor = mydb.cursor()
    User_Query=f'''select state,sum(count) As count
                From {table_name}
                group by state
                order by count Desc
                LIMIT 10;'''
    mycursor.execute(User_Query)
    User_table=mycursor.fetchall()
    mydb.commit()
    User_DF=pd.DataFrame(User_table,columns=("state","count"))
    
        
    User_Chart = px.bar(User_DF, x="state",y="count",title="Count of Agg user",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl,hover_name="state",height=650,width=650)
    st.plotly_chart(User_Chart)

# top_chart_AU("Agg_User")    

def top_chart_MU(table_name):

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shyam@28",
            database="phonepaydata"
        )
    mycursor = mydb.cursor()
    registeredusers_Query=f'''select state,sum(registeredusers) As registeredusers
                From {table_name}
                group by state
                order by registeredusers Desc
                LIMIT 10;'''
    mycursor.execute(registeredusers_Query)
    registeredusers_table=mycursor.fetchall()
    mydb.commit()
    registeredusers_DF=pd.DataFrame(registeredusers_table,columns=("state","registeredusers"))
    
        
    registeredusers_chart = px.bar(registeredusers_DF, x="state",y="registeredusers",title="registeredusers ",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl,hover_name="state",height=650,width=650)
    st.plotly_chart(registeredusers_chart)

# top_chart_MU("Map_User")  
def top_chart_MUA(table_name):

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shyam@28",
            database="phonepaydata"
        )
    mycursor = mydb.cursor()
    Appopen_Query=f'''select state,sum(appopens) As appopens
                From {table_name}
                group by state
                order by appopens Desc
                LIMIT 10;'''
    mycursor.execute(Appopen_Query)
    Appopen_table=mycursor.fetchall()
    mydb.commit()
    Appopen_DF=pd.DataFrame(Appopen_table,columns=("state","appopens"))
    
        
    Appopen_Chart = px.bar(Appopen_DF, x="state",y="appopens",title="appopens ",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl,hover_name="state",height=650,width=650)
    st.plotly_chart(Appopen_Chart)
                               
# Set page configuration
st.set_page_config(page_title="Shyam PhonePe Data", page_icon="📊", layout="wide")
st.title("Shyam PhonePe Data Visualization and Exploration")

# Sidebar menu
with st.sidebar:
    select = option_menu("Main Menu", ["Welcome", "Data Insights", "Performance Charts"])

# Main content based on selected menu option
if select == "Welcome":
    tab1, = st.tabs(["Phonepe Info Page"])  # The comma unpacks the single-element tuple.
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.header("PHONEPE")
            st.subheader("INDIA'S BEST TRANSACTION APP")
            st.markdown("Phonepe is an Indian Digital Payments And Financial Technology Company")
            st.write("******FEATURES******")
            st.write("******Credit Card And Debit Card Linking******")
            st.write("******Bank Balance Check******")
            st.write("******Money Storage******")
            st.write("******Pin Authorisation******")
            st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
        with col2:
            # Specify the correct file path
            file_path = r"C:/Users/ADMIN/Desktop/images.jfif"
            if os.path.exists(file_path):
                st.image(Image.open(file_path), width=650)
            else:
                st.error(f"File not found: {file_path}")

    
elif select == "Data Insights":
    tab1, tab2, tab3 = st.tabs(["Aggregated Analysis", "Map Analysis", "Top Analysis"])

    with tab1:
        method = st.radio("Select the Method", ["Aggregated Transaction Analysis", "Aggregated User Analysis"])

        if method == "Aggregated Transaction Analysis":
            col1, col2 = st.columns(2)
            with col1:
                Years = st.slider("Select the year", int(Agg_Trans["Year"].min()), int(Agg_Trans["Year"].max()), int(Agg_Trans["Year"].min()), key="year_slider1")
            Transaction_amount_count_y(Agg_Trans, Years)
            col1, col2 = st.columns(2)
            with col1:
                state = st.selectbox("Select the state", Agg_Trans['State'].unique())
            aggre_trans_type(Agg_Trans, state)
            col1, col2 = st.columns(2)
            with col1:
                Quarters = st.slider("Select the Quarter", int(Agg_Trans["Quarter"].min()), int(Agg_Trans["Quarter"].max()), int(Agg_Trans["Quarter"].min()), key="Quarter_slider1")
            Transaction_amount_count_yq(Agg_Trans, Quarters)
            col1, col2 = st.columns(2)
            with col1:
                state_1 = st.selectbox("Select the state for Quarter", Agg_Trans["State"].unique())
            aggre_trans_type(Agg_Trans, state_1)

        elif method == "Aggregated User Analysis":
            col1, col2 = st.columns(2)
            with col1:
                year = st.slider("Select the year", int(Agg_User["Year"].min()), int(Agg_User["Year"].max()), int(Agg_User["Year"].min()), key="year_slider2")
            Agg_user_data(Agg_User, year)
            col1, col2 = st.columns(2)
            with col1:
                Quarters = st.slider("Select the Quarter", int(Agg_User["Quarter"].min()), int(Agg_User["Quarter"].max()), int(Agg_User["Quarter"].min()), key="Quarter_slider2")
            Agg_user_data_quarter(Agg_User, Quarters)
            col1, col2 = st.columns(2)
            with col1:
                state_2 = st.selectbox("Select the state", Agg_User["State"].unique())
            aggre_user_state(Agg_User, state_2)
    with tab2:
        method2 = st.radio("Select the Method", ["Map Transaction Analysis", "Map User Analysis"])

        if method2 == "Map Transaction Analysis":
            col1, col2 = st.columns(2)
            with col1:
                years = st.slider("Select the year", int(Map_Trans["Year"].min()), int(Map_Trans["Year"].max()), int(Map_Trans["Year"].min()),
                int(Map_Trans["Year"].min()), key="transaction_year_slider")
            Map_transaction_amount_count_y(Map_Trans, years)
            col1, col2 = st.columns(2)
            with col1:
                Map_state = st.selectbox("Select the state", Map_Trans["State"].unique(), key='state_selectbox_1')
            Map_trans_type(Map_Trans, Map_state)

            #     Map_state = st.selectbox("Select the state", Map_Trans["State"].unique())
            # Map_trans_type(Map_Trans,Map_state)
            col1, col2 = st.columns(2)
            with col1:
                Quarters = st.slider("Select the Quarter", int(Map_Trans["Quarter"].min()), int(Map_Trans["Quarter"].max()), int(Map_Trans["Quarter"].min()),
                              int(Map_Trans["Quarter"].min()), key="transaction_quarter_slider")
            Map_Transaction_amount_count_yq(Map_Trans, Quarters)
            col1, col2 = st.columns(2)
            with col1:
                Map_state1 = st.selectbox("Select the state for Quarter", Map_Trans["State"].unique(), key='state_selectbox_2' )
            Map_trans_quattype(Map_Trans,Map_state1)

        elif method2 == "Map User Analysis":
            col1, col2 = st.columns(2)
            with col1:
                year = st.slider("Select the year", int(Map_User["Year"].min()), int(Map_User["Year"].max()), int(Agg_User["Year"].min()),
                                int(Agg_User["Year"].min()), key="user_year_slider1")
            Map_user_data(Map_User, year)
            col1, col2 = st.columns(2)
            with col1:
                Quarters = st.slider("Select the Quarter", int(Map_User["Quarter"].min()), int(Map_User["Quarter"].max()), int(Map_User["Quarter"].min()),
                               int(Map_User["Quarter"].min()), key="user_quarter_slider2")
            Map_user_data_quarter(Map_User, Quarters)
            col1, col2 = st.columns(2)
            with col1:
                state = st.selectbox("Select the state", Map_User['State'].unique(), key="map_user_state_selectbox")
            Map_user_data_state(Map_User,state)

    with tab3:
        method3 = st.radio("Select the Method", ["Top Transaction Analysis", "Top User Analysis"])

        if method3 == "Top Transaction Analysis":
            col1, col2 = st.columns(2)
            with col1:
                years = st.slider("Select the year", int(Top_trans["Year"].min()), int(Top_trans["Year"].max()), int(Top_trans["Year"].min()),
                                  int(Top_trans["Year"].min()), key="top_trans_year_slider1")
            Top_Transaction_amount_count_y(Top_trans, years)
            col1, col2 = st.columns(2)
            with col1:
                Top_state = st.selectbox("Select the state", Top_trans["State"].unique(), key="top_state_selectbox1")
            Top_trans_type(Top_trans, Top_state)
            col1, col2 = st.columns(2)
            with col1:
                Quarters = st.slider("Select the Quarter", int(Top_trans["Quarter"].min()), int(Top_trans["Quarter"].max()), int(Top_trans["Quarter"].min()),
                                     int(Top_trans["Quarter"].min()), key="top_trans_quarter_slider2")
            Top_Transaction_amount_count_q(Top_trans, Quarters)
            col1, col2 = st.columns(2)
            with col1:
                Top_state1 = st.selectbox("Select the state for Quarter", Top_trans["State"].unique(),key="top_state1_selectbox2")
            Top_trans_type1(Top_trans, Top_state1)

        elif method3 == "Top User Analysis":
            col1, col2 = st.columns(2)
            with col1:
                year = st.slider("Select the year", int(Top_User["Year"].min()), int(Top_User["Year"].max()), int(Agg_User["Year"].min()),
                                 int(Agg_User["Year"].min()), key="top_user_year_slider")
            Top_user_data(Top_User, year)
            col1, col2 = st.columns(2)
            with col1:
                Top_User_state = st.selectbox("Select the state", Top_User['State'].unique(), key="top_user_state_selectbox")
            Top_user_state(Top_User, state)

elif select == "Performance Charts":
    Question = st.selectbox("Select the Question", [
        "1.Transaction amount of Aggregate Transaction", 
        "2.Transaction count of Aggregate Transaction",
        "3.Transaction amount of Map Transaction",
        "4.Transaction count of Map Transaction",
        "5.Transaction amount of Top Transaction",
        "6.Transaction count of Top Transaction",
        "7.Transaction count of Aggregate User",
        "8.Registered User of Map User",
        "9.App open of Map User",
        "10.Registered User of Top User"
    ])
    if Question == "1.Transaction amount of Aggregate Transaction":
        st.subheader("Agg_trans_amt")
        top_chart_ta("Agg_Trans")
    elif Question == "2.Transaction count of Aggregate Transaction":
        st.subheader("Agg_trans_count")
        top_chart_tc("Agg_Trans")
    elif Question == "3.Transaction amount of Map Transaction":
        st.subheader("Map_trans_amount")
        top_chart_tc("Map_Trans")
    elif Question == "4.Transaction count of Map Transaction":
        st.subheader("Map_trans_count")
        top_chart_tc("Map_Trans")    
    elif Question == "5.Transaction amount of Top Transaction":
        st.subheader("Top_trans_amount")
        top_chart_tc("Top_trans")    
    elif Question == "6.Transaction count of Top Transaction":
        st.subheader("Top_trans_count")
        top_chart_tc("Top_trans")  
    elif Question == "7.Transaction count of Aggregate User":
        st.subheader("Agg_User_count") 
        top_chart_AU("Agg_User")  
    elif Question == "8.Registered User of Map User":
        st.subheader("Reg_User_count") 
        top_chart_MU("Map_User")          
    elif Question == "9.App open of Map User":
        st.subheader("App_User_count") 
        top_chart_MUA("Map_User")          
    elif Question == "10.Registered User of Top User":
        st.subheader("Reg_User_count of top")
        top_chart_MU("Top_User")









