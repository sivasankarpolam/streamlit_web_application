import streamlit as st

phonepe_logo_url = "image.png"


st.image(phonepe_logo_url,width=600) 




st.title("PhonePe Transaction Data Analysis Dashboard")

st.write(''' 
### What is PhonePe?
PhonePe is a digital payments platform that allows users to send and receive money, pay bills, buy insurance, and make online payments through UPI (Unified Payments Interface). With its growing range of financial services, including insurance, PhonePe is becoming a major player in India's fintech ecosystem, helping millions of users manage their financial transactions with ease.
''')

st.write('''
### Business Problem Statement:
**Analyzing Transaction Trends and User Engagement on Digital Platforms**

As PhonePe continues to expand its financial services, especially in the insurance sector, it becomes critical to leverage transaction and engagement data to derive key insights. The core challenge lies in understanding how various factors, including geography (state and district-wise performance), quarterly trends, and yearly performance, influence the growth and efficiency of transactions on the platform.

**This analysis will address the following key aspects:**
1. **State-wise Performance:** Identify how geographical factors influence transaction volume and revenue, helping businesses focus on underperforming regions and enhance strategy.
2. **District-wise Trends:** Uncover high-performing districts and analyze how transaction volumes and amounts change over time, identifying regions with high growth potential.
3. **Brand-wise Insights:** Analyze brand-specific transaction trends to identify top-performing brands, measure market penetration, and support strategic decision-making for brand promotion.
4. **User Engagement:** Solve the issue of districts with high registered users but low app engagement by correlating `Registered_users` and `App_opens`, and formulating targeted marketing strategies to boost engagement.
5. **Year-wise Trends:** In this analysis, we will examine how the transaction count and amount have changed year by year.
6. **Transactiontype-wise-Trends:** In this analysis, I examined which transaction types, such as peer-to-peer payments, merchant payments, etc., had the highest transaction volumes.
By addressing these factors, the analysis will help optimize the performance of PhonePe's transactions.
''')


