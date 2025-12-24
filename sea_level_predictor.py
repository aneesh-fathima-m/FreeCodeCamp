import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # Line of best fit for all data
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(1880, 2051)
    ax.plot(years_all, intercept1 + slope1 * years_all, 'r', label='Fit: 1880-2020')

    # Line of best fit for data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    ax.plot(years_recent, intercept2 + slope2 * years_recent, 'green', label='Fit: 2000-2020')

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save plot
    fig.savefig('sea_level_plot.png')
    return fig

# Uncomment to test
# draw_plot()
