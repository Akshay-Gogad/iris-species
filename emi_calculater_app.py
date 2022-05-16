import streamlit as st

def calculate_emi(p,n,r):
  emi = round(p*(r/100)*(1+r/100)**n/((1+r/100)**n-1),3)
  st.write("EMI Calculater",emi)


st.title("EMI Calculater")
principle = st.slider('Loan Ammount',1000.0,100000.0)
tenure = st.slider('Tenure in years',1,30)
roi = st.slider('Rate of Interest',1,15)
n = tenure*12
r = roi/12

if st.button('Calculate'):
  calculate_emi(principle,n,r)

def calculate_outstanding_bal(p,n,r,m):
  balance = round((p * ((1+r/100)**n - (1+r/100)**m) )/ ((1+r/100)**n - 1),3)
  st.write("Balance =",balance)

st.title("EMI Calculater")
principle = st.slider('Loan Ammount',1000.0,100000.0)
tenure = st.slider('Tenure in years',1,30)
roi = st.slider('Rate of Interest',1,15)
period = st.slider('Period after to check loan balance in month',1,tenure*12)
n = tenure*12
r = roi/12

emi_button = st.button('Calculate EMI')
balance_button = st.button('Calculate Outstanding loan balance')

if emi_button:
  calculate_emi(principle,n,r)
elif balance_button:
  calculate_outstanding_bal(principle,n,r,period)
