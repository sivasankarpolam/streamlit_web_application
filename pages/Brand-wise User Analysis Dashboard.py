import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv(r'Agg_User.csv')

st.title("Brand-wise User Analysis Dashboard")

st.subheader("Business Problem Statement")
st.write("This dashboard helps in analyzing brand-wise transaction trends for PhonePe services. "
         "The objective is to identify top-performing brands, examine market penetration, and "
         "extract actionable insights for brand promotion and strategic decision-making.")


st.sidebar.header("Filter Options")
brand_filter = st.sidebar.multiselect('Select Brands', options=df['Agg_User_Brands'].unique(), default=df['Agg_User_Brands'].unique())
quarter_filter = st.sidebar.multiselect('Select Quarters', options=df['Quarter'].unique(), default=df['Quarter'].unique())
Year_filter= st.sidebar.multiselect('Select Years',options=df["Year"].unique(),default=df['Year'].unique())
State_filter= st.sidebar.multiselect('Select States',options=df["State"].unique(),default=df['State'].unique())

df_filtered = df[(df['Agg_User_Brands'].isin(brand_filter)) & (df['Quarter'].isin(quarter_filter)) & (df['Year'].isin(Year_filter)) & (df['State'].isin(State_filter))]


st.header('Brand-wise User Count and Market Share')
user_count_by_brand = df_filtered.groupby('Agg_User_Brands')['Agg_User_Count'].sum().reset_index()
user_percentage_by_brand = df_filtered.groupby('Agg_User_Brands')['Agg_User_Percentage'].mean().reset_index()

fig_user_count = px.bar(user_count_by_brand, x='Agg_User_Brands', y='Agg_User_Count', 
                               title='Total User Count by Brand',
                               labels={'user_count': 'User Count'})
st.plotly_chart(fig_user_count)

fig_market_share = px.pie(user_percentage_by_brand, values='Agg_User_Percentage', names='Agg_User_Brands', 
                          title='Market Share by Brand (%)')
st.plotly_chart(fig_market_share)

st.header('Quarterly User Trends')
user_trends = df_filtered.groupby(['Agg_User_Brands', 'Quarter'])['Agg_User_Count'].sum().reset_index()

fig_user_trends = px.bar(user_trends, x='Quarter', y='Agg_User_Count', color='Agg_User_Brands', 
                                 title='Quarterly User Trends by Brand')
st.plotly_chart(fig_user_trends)

# Yearly Brand Performance (Year can be updated if you have multi-year data)
st.header('Yearly Brand Performance')

Usercount_and_year = df_filtered.groupby(['Agg_User_Brands', 'Year'])['Agg_User_Count'].sum().reset_index()

fig_yearly_performance = px.bar(Usercount_and_year, x='Agg_User_Brands', y='Agg_User_Count', color='Year', 
                                title="Yearly Brand Performance")
st.plotly_chart(fig_yearly_performance)

st.header("State Wise Brand Performance")

Usercount_and_state =df_filtered.groupby(['Agg_User_Brands','State'])['Agg_User_Count'].sum().reset_index()

fig_state_performance = px.bar(Usercount_and_state, x='Agg_User_Brands',y='Agg_User_Count',color='State',title="State Wise Brand Performance")

st.plotly_chart(fig_state_performance)



# Summary Insights
st.header("Key Insights")
st.write(f"Total Users by User Count: {df_filtered['Agg_User_Count'].sum()}")
top_brand = df_filtered.groupby('Agg_User_Brands')['Agg_User_Count'].sum().idxmax()
st.write(f"Top Brand by User Count: {top_brand}")
st.write(f"Top Brand Market Share: {user_percentage_by_brand[user_percentage_by_brand['Agg_User_Brands'] == top_brand]['Agg_User_Percentage'].values[0]/100:.2%}")

# Footer
st.write("This expanded analysis provides deeper insights into the brand-wise performance of PhonePe transactions, "
         "offering actionable insights on market dynamics, growth, and correlation trends. "
         "PhonePe can leverage these findings to refine their marketing strategies and focus on key brands or emerging markets.")



# 