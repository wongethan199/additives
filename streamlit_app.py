import streamlit as st
st.title("additives")
limits=[5,3.75,7,12]
x=pandas.read_csv("additives.csv")
y=int(st.text_input("Enter number of unique food items to test"))
additives=[0,0]
dic=["Yellow 5","Yellow 6","Red 40","Blue 1"]
for i in range(y):
  z=st.selectbox("Enter food item "+str(i),x["Food"].values.tolist())
  num=int(st.text_input("Enter quantity"))
  target=x[x["Food"]==z]
  target=list(target[0])
  for j in range(1,5):
    additives[j-1]+=num*target[j]
for i in range(4):
  st.write(additives[i],"of",dic[i])
  if additives[i]>limits[i]:
    st.markdown(":red[Above additive exceeds daily limit]")
