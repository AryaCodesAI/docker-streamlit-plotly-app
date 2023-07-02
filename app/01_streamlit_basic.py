#import necessarry libraries
import pandas as pd 
import streamlit as st
import plotly.express as px

#concate into one data frame
df0 = pd.read_csv('../data/energy_data_chunk_0.csv')
df1 = pd.read_csv('../data/energy_data_chunk_1.csv')
df2 = pd.read_csv('../data/energy_data_chunk_2.csv')
df3 = pd.read_csv('../data/energy_data_chunk_3.csv')
df_energy = pd.concat([df0, df1, df2, df3], axis=0)
df_energy_sort = df_energy.sort_values(by='year')
dff_energy = df_energy_sort.reset_index()

#streamlit sidebar ui
st.title('Exploring Energy Dynamics: An Animated Analysis of International Energy Statistics')
st.write('This app retrieves data from [kaggle](https://www.kaggle.com/datasets/unitednations/international-energy-statistics?select=all_energy_statistics.csv). The Energy Statistics Database contains comprehensive energy statistics on the production, trade, conversion and final consumption of primary and secondary; conventional and non-conventional; and new and renewable sources of energy.')

with st.sidebar: 
    list_country = st.multiselect('Select Countries', options = df_energy.country_or_area.unique())
    mask_country = dff_energy.country_or_area.isin(list_country)
    dff = dff_energy[mask_country]
    
#vizualization
st.write('Animated Scatter Plot: Showing the change in relationships over time by animating the scatter plot.')
animated_plot = px.scatter(dff, x='quantity', y='category', animation_frame='year', color='country_or_area',
                           title='Energy Quantity vs. Category (Animated Scatter Plot)')
st.plotly_chart(animated_plot)

st.write('Line Plot: Visualizing the trends of energy quantity over time for a specific country or area.')
line_plot = px.line(dff, x='year', y='quantity', color='country_or_area', title='Energy Quantity Trends')
st.plotly_chart(line_plot)

st.write('3D Scatter Plot: Visualizing relationships between three variables (quantity, unit, year) using a 3D scatter plot.')
scatter_3d = px.scatter_3d(dff, x='quantity', y='unit', z='year', color='country_or_area',
                           title='Energy Quantity vs. Unit vs. Year (3D Scatter Plot)')
st.plotly_chart(scatter_3d)

st.write('Each of these visualizations will shed light on different aspects of the dataset, enabling us to derive actionable insights for businesses operating in the energy sector. The insights gained from our visualizations have far-reaching implications for strategic decision-making, resource allocation, policy formulation, and investment opportunities within the energy industry. By harnessing the power of data visualization, we can unlock the potential of the International Energy Statistics dataset and enable data-driven, evidence-based decision-making in the dynamic landscape of energy.')