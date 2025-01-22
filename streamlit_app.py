import streamlit as st
from scipy.stats import norm
st.header("additives")
import pandas
import csv
"Data provided are very rough averages of a few brands, and may contain dyes that are not present in a specific brand. Exact values are unknown, but some data is available on https://www.kaggle.com/datasets/sujaykapadnis/certified-food-dye-levels-in-food-samples"
standards=st.selectbox("Enter standards to compare",["USFDA","JECFA","EFSA"])
limits=[7.5,4,7,0.1,6]
if standards=="USFDA":
  limits=[5,3.75,7,2.5,12]
if standards=="EFSA":
  limits[4]=12.5
x=pandas.read_csv("additives.csv")
try:
  weight=float(st.text_input("Enter body weight in kg, defaults to 60"))
except:
  weight=60
limits=[i*weight for i in limits]
y=st.text_input("Enter number of unique food items to test")
if y:
  additives=[0,0,0,0,0]
  sd=[0,0,0,0,0]
  dic=["Yellow 5","Yellow 6","Red 40","Red 3","Blue 1"]
  for i in range(int(y)):
    z=st.selectbox("Enter food item "+str(i+1),x["Food"].values.tolist())
    num=st.text_input(f"Enter quantity of food item {i+1} consumed in a day in g")
    if num:
      num=float(num)
      target=x[x["Food"]==z]
      target=list(target.iloc[0])
      for j in range(1,6):
        additives[j-1]+=num*target[j]
        sd+=num*target[j+5]**2
  sd=[i**0.5 for i in sd]
  for i in range(5):
    st.write(f"{dic[i]}: Mean: {additives[i]}, SD: {sd[i]}")
    if additives[i]>limits[i]:
      st.write("Mean of above additive exceeds daily limit of",limits[i],"mg by",additives[i]-limits[i],"mg")
    if sd[i]>0:
      zscore=(additives[i]-limits[i])/sd[i]
      st.write("Probability of exceeding limit of above additive, assuming normal distribution, is",norm.cdf(zscore)*100,"%")
    st.write("___")
