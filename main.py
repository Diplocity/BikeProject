import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('US+Holiday+Dates+(2004-2021).csv')  # Replace with your actual filename

# Convert the 'Date' column to datetime format if it exists
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Streamlit dashboard layout
st.title('Bike Sharing Dashboard')

# Show basic statistics
st.header('Basic Statistics')
st.write(df.describe())

# Show missing values
st.header('Missing Values')
st.write(df.isnull().sum())

# Visualize number of trips per month
if 'Month' in df.columns:
    trips_per_month = df['Month'].value_counts().sort_index()
    st.subheader('Number of Trips per Month')
    fig1, ax1 = plt.subplots()
    trips_per_month.plot(kind='bar', color='green', ax=ax1)
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Number of Trips')
    ax1.set_title('Number of Trips per Month')
    st.pyplot(fig1)

# Visualize average trips per weekday
if 'WeekDay' in df.columns:
    avg_trips_per_weekday = df['WeekDay'].value_counts()
    st.subheader('Average Trips per Weekday')
    fig2, ax2 = plt.subplots()
    avg_trips_per_weekday.plot(kind='bar', color='purple', ax=ax2)
    ax2.set_xlabel('Weekday')
    ax2.set_ylabel('Number of Trips')
    ax2.set_title('Average Trips per Weekday')
    st.pyplot(fig2)
