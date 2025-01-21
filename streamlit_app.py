import streamlit as st
st.title("additives")
limits={}#dictionary for limits for additives
x=pandas.read_csv("additives.csv")
y=int(st.text_input("Enter number of unique food items to test"))
additives=[0,0]
dic={0:"E101",1:"E102"}
for i in range(y):
  z=st.selectbox("Enter food item "+str(i),x["Food"].values.tolist())
  num=int(st.text_input("Enter quantity"))
  target=x[x["Food"]==z]
  target=list(target[0])
  for j in range(1,len(target()):
    additives[j-1]+=num*target[j]
for i in range():
  st.write(additives[i],"of",dic[i])
