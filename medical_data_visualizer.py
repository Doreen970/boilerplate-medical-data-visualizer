import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
print(df.head())
#print(df.columns)

# Add 'overweight' column
df['height'] /= 100 #convert height column to metres
df['BMI'] = df['weight'] / (df['height'] ** 2)
df['overweight'] = np.where(df['BMI'] > 25, 1, 0)
#print(df['overweight'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using pd.melt using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']]
    print(df_cat.head())
    df_cat = pd.melt(df_cat, var_name='variable', value_name='value')

    # Include the 'cardio' column from the original DataFrame 'df'
    df_cat['cardio'] = df['cardio']

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    print(df_cat.head(10))

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable', y='count', hue='value', col='cardio', data=df_cat, kind='bar')

    # Get the figure for the output
    fig = g.fig

    # Save the figure
    fig.savefig('catplot.png')

    return fig

draw_cat_plot()

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
