import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import streamlit as st

uploaded_file  = r'task1/tips.csv'
data = pd.read_csv(uploaded_file)


st.title("My First Streamlit App")


st.header('Data overview')
st.write("first data row of the dataset! ")


st.dataframe(data.head())

st.header('Summary of statistics of  the dataset')

st.dataframe(data.describe())

st.header('Data Visualization')
st.write("Here is a bar chart of the dataset!")
x_axis = st.selectbox("X_axis" , data.columns)
y_axis = st.selectbox("y_axis" , data.columns)

plot_types = st.radio('Select a type of plot', ['scatter plot' , 'bar', 'line', 'hist'])


if plot_types == 'scatter plot':
    st.subheader(f"Scatter plot of {x_axis} vs {y_axis}")
    fig = plt.figure(figsize=(10,6))
    sns.scatterplot(x=x_axis , y=y_axis , data=data)
    st.pyplot(fig)
elif plot_types == 'bar':
    st.subheader( f"Bar plot of {x_axis} vs {y_axis}")
    fig = plt.figure(figsize=(10,6))
    sns.barplot(x=x_axis , y=y_axis , data=data)
    st.pyplot(fig)
elif plot_types == 'line':
    st.subheader( f"Line plot of {x_axis} vs {y_axis}")
    fig = plt.figure(figsize=(10,6))
    sns.lineplot(x=x_axis , y=y_axis , data=data)
    st.pyplot(fig)
    
elif plot_types == 'hist':
    st.subheader ( f"Histogram of {y_axis}")
    fig = plt.figure(figsize=(10,6))
    sns.histplot(x=x_axis , data=data)
    st.pyplot(fig)
    
    
st.header('Correlation Matrix HeatMap' )
if st.button('Gnerate Heatmap'):
    fig = plt.figure(figsize=(10,6))
    sns.heatmap(data.corr(numeric_only=True), annot=True , cmap='coolwarm')
    st.pyplot(fig)

st.write('your data is ready to be used for analysis!')


