import streamlit as st
st.title("additives")
limits={}#dictionary for limits for additives
x=pandas.read_csv("additives.csv")
y=int(st.text_input("Enter number of unique food items to test"))
additives=[]
for i in range(y):
  z=st.selectbox("Enter food item "+str(i),x["Food"].values.tolist())
  num=int(st.text_input("Enter quantity))
  target=x[x["Food"]==z]
  #add values of additives
for i in range():
  st.write(additives[i],"of",dic[i])
