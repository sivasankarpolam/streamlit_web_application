import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


df = pd.read_csv(r"Map_Trans.csv")

st.title("District-wise Transaction Analysis Dashboard")

st.subheader("Business Problem Statement")
st.write("This dashboard focuses on analyzing transaction trends across different districts "
         "The goal is to uncover which districts contribute the most to transaction volumes and amounts, and how this evolves over time.")

st.sidebar.header("Filter Options")
district_filter = st.sidebar.multiselect('Select District(s)', options=df['District'].unique(), default=df['District'].unique())
year_filter = st.sidebar.multiselect('Select Year(s)', options=df['Year'].unique(), default=df['Year'].unique())

df_filtered = df[(df['District'].isin(district_filter)) & (df['Year'].isin(year_filter))]

st.subheader("Transaction Trends Analysis")
districts = df['District'].unique()
selected_district = st.selectbox("Select District", districts)

filtered_data = df[df['District'] == selected_district]

# Plot Transaction Count and Amount
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(filtered_data['Quarter'], filtered_data['Dist_Transaction_Count'], color='g', width=0.4, label='Dist_Transaction_Count', alpha=0.6)

ax1.set_xlabel('Quarter')
ax1.set_ylabel('Dist_Transaction_Count', color='g')
ax2.set_ylabel('Dist_Transaction_Amount', color='b')
ax1.set_title(f'Transaction Trends for {selected_district}')


ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

st.pyplot(fig)



st.subheader("Yearly Total Transaction Amount")
yearly_data = df.groupby('Year').agg(total_transaction_amount=('Dist_Transaction_Amount', 'sum')).reset_index()

fig_yearly = px.bar(yearly_data, x='Year', y='total_transaction_amount', title='Total Transaction Amount by Year')
st.plotly_chart(fig_yearly)

st.header('District-wise Transaction Count and Amount')
transaction_count_by_district = df_filtered.groupby('District')['Dist_Transaction_Count'].sum().reset_index()
transaction_amount_by_district = df_filtered.groupby('District')['Dist_Transaction_Amount'].sum().reset_index()

fig_transaction_count = px.bar(transaction_count_by_district, x='District', y='Dist_Transaction_Count', 
                               title='Total Transaction Count by District',
                               labels={'Dist_Transaction_Count': 'Transaction Count'})
st.plotly_chart(fig_transaction_count)

fig_transaction_amount = px.bar(transaction_amount_by_district, x='District', y='Dist_Transaction_Amount', 
                                title='Total Transaction Amount by District (INR)',
                                labels={'Dist_Transaction_Amount': 'Transaction Amount'})
st.plotly_chart(fig_transaction_amount)


st.header('Quarterly Transaction Trends')
transaction_trends = df_filtered.groupby(['District', 'Quarter'])[['Dist_Transaction_Count', 'Dist_Transaction_Amount']].sum().reset_index()

fig_transaction_trends = px.line(transaction_trends, x='Quarter', y='Dist_Transaction_Count', color='District', 
                                 title='Quarterly Transaction Count by District')
st.plotly_chart(fig_transaction_trends)

st.header('Yearly District Performance')

transaction_amount_and_year = df_filtered.groupby(['District', 'Year'])[['Dist_Transaction_Count', 'Dist_Transaction_Amount']].sum().reset_index()

fig_yearly_performance = px.bar(transaction_amount_and_year, x='District', y='Dist_Transaction_Amount', color='Year', 
                                title="Yearly District-wise Transaction Amount (INR)")
st.plotly_chart(fig_yearly_performance)

st.header("Correlation Analysis: Transaction Count vs Transaction Amount")

correlation_data = df_filtered[['Dist_Transaction_Count', 'Dist_Transaction_Amount']].corr().iloc[0,1]
st.write(f"Correlation between Transaction Count and Transaction Amount: {correlation_data:.2f}")

fig_correlation = px.scatter(df_filtered, x='Dist_Transaction_Count', y='Dist_Transaction_Amount', color='District', 
                             title='Correlation Between Transaction Count and Transaction Amount')
st.plotly_chart(fig_correlation)

st.header('Growth Rate Analysis')
df_filtered['Growth_Rate'] = df_filtered.groupby('District')['Dist_Transaction_Amount'].pct_change() * 100
growth_rate_df = df_filtered[['District', 'Year', 'Quarter', 'Growth_Rate']].dropna()

fig_growth_rate = px.bar(growth_rate_df, x='District', y='Growth_Rate', color='Quarter', 
                         title='District-wise Quarterly Growth Rate (%)')
st.plotly_chart(fig_growth_rate)

st.header('District-wise Market Share Analysis')
market_share = df_filtered.groupby('District')['Dist_Transaction_Amount'].sum().reset_index()
total_amount = df_filtered['Dist_Transaction_Amount'].sum()
market_share['Market_Share'] = market_share['Dist_Transaction_Amount'] / total_amount * 100

fig_market_share = px.pie(market_share, values='Market_Share', names='District', 
                          title='Market Share by District (Transaction Amount)')
st.plotly_chart(fig_market_share)

st.header("Key Insights")
st.write(f"Total Transactions Analyzed: {df_filtered['Dist_Transaction_Count'].sum()}")
top_district = df_filtered.groupby('District')['Dist_Transaction_Count'].sum().idxmax()
st.write(f"Top District by Transaction Count: {top_district}")
st.write(f"Top District Transaction Amount: {transaction_amount_by_district[transaction_amount_by_district['District'] == top_district]['Dist_Transaction_Amount'].values[0]:,.2f} INR")


st.write("This dashboard provides actionable insights into district-wise transaction performance, helping stakeholders identify "
         "key trends and optimize strategies for market penetration and growth.")
