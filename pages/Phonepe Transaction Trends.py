import streamlit as st
import pandas as pd
import plotly.express as px


st.title("PhonePe Transaction Interactive Dashboard")

df = pd.read_csv('Agg_Trans.csv')



st.sidebar.header("Filter Options")
state_filter = st.sidebar.multiselect('Select States', options=df['State'].unique(), default=df['State'].unique())
year_filter = st.sidebar.slider('Select Year Range', int(df['Year'].min()), int(df['Year'].max()), (2020, 2021))

df_filtered = df[(df['State'].isin(state_filter)) & (df['Year'] >= year_filter[0]) & (df['Year'] <= year_filter[1])]


st.header('Phonepe Transaction Trends: State-wise Performance')

transaction_amount_and_state = df_filtered.groupby('State')['Agg_Transaction_Amount'].max().reset_index()
fig_statewise = px.bar(transaction_amount_and_state, x='State', y='Agg_Transaction_Amount', title="Max Transaction Amount by State")
st.plotly_chart(fig_statewise)

st.header('Phonepe Transaction Trends: Quarterly Performance')

transaction_amount_and_quarter = df_filtered.groupby('Quarter')['Agg_Transaction_Amount'].max().reset_index()
fig_quarterly = px.bar(transaction_amount_and_quarter, x='Quarter', y='Agg_Transaction_Amount', title="Max Transaction Amount by Quarter")
st.plotly_chart(fig_quarterly)

st.header('Yearly and State-wise Transactions')

transaction_amount_and_year_state = df_filtered.groupby(['State', 'Year'])['Agg_Transaction_Amount'].max().reset_index()
fig_year_state = px.bar(transaction_amount_and_year_state, x='State', y='Agg_Transaction_Amount', color='Year',
                        title="Max Transaction Amount by State and Year")
st.plotly_chart(fig_year_state)


st.header('Correlation Between Transaction Count and Amount')

fig_corr = px.scatter(df_filtered, x='Agg_Transaction_Count', y='Agg_Transaction_Amount', color='State',
                      title='Correlation Between Transaction Count and Amount')
st.plotly_chart(fig_corr)

st.header("Key Insights")

st.write(f"Total Transactions Analyzed: {df_filtered['Agg_Transaction_Count'].sum()}")
st.write(f"Highest Transaction Amount: {df_filtered['Agg_Transaction_Amount'].max()}")

# Footer
st.write("This dashboard provides insights into state-wise and quarterly performance for insurance transactions. "
         "These insights can be used to identify trends and optimize sales strategies for insurance services.")

