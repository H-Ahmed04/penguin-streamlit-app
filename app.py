import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import random

# Title
st.title("Hamdaan Ahmed")  # ← Replaced "Penguins Rock" with my name

# Load penguin dataset
df = sns.load_dataset("penguins").dropna()

# Add coordinates for mapping
island_coords = {
    "Biscoe": (-63.8, -63.4),
    "Dream": (-64.7, -62.9),
    "Torgersen": (-64.8, -64.1)
}

df["latitude"] = df["island"].map(lambda x: island_coords[x][0] + random.uniform(-0.1, 0.1))
df["longitude"] = df["island"].map(lambda x: island_coords[x][1] + random.uniform(-0.1, 0.1))

# Map plot
fig_map = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    color="species",
    color_discrete_map={"Adelie": "blue", "Chinstrap": "red", "Gentoo": "green"},
    title="This is a plot of penguins based on the color of their poop",
    zoom=5,
    mapbox_style="open-street-map"
)
st.plotly_chart(fig_map)

# Violin plot (SECOND PLOT)
fig_violin = px.violin(
    df,
    x="species",
    y="body_mass_g",
    color="sex",
    box=True,
    points="all"
)
fig_violin.update_layout(title="Penguin Body Mass by Species and Sex")
st.plotly_chart(fig_violin)
