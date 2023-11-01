import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st
import os
import plotly.graph_objects as go

df = pd.read_excel("D:/phy/df_melt.xlsx")
df = df.drop(["Unnamed: 0","variable"], axis=1)
df = df[df["value"]>0.5]
df_mean = df.groupby("SLOT").mean()

st.title("Laserwelding bead inspection result")
s1 = st.sidebar.selectbox(
    "Select one",
    [df["GAP"].unique()[0],df["GAP"].unique()[1],
     df["GAP"].unique()[2],df["GAP"].unique()[3],"All"]
)

rec = st.sidebar.slider(
    "adjust range",
    0,47,
    (1,35)
)

if s1 != "All":
    df_A = df[df["GAP"]==s1]
else:
    df_A = df

st.dataframe(df_A.head(5),use_container_width=True)
fig = px.strip(df_A,x="SLOT",y="value",color = "GAP")
fig.add_trace(go.Scatter(x=df_mean.index, y=df_mean["value"],line_color = "red"))
fig.add_hline(y=1.2, line_color = "red")
fig.add_vrect(x0=rec[0], x1=rec[1],opacity=0.15,fillcolor = "orange")
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
