import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level'],
        color='blue',
        s=20,
        alpha=0.6
    )
    # Create first line of best fit
    res_all = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )
    slope_all = res_all.slope
    intercept_all = res_all.intercept

    years_extended = pd.Series(range(df['Year'].min(), 2051))
    sea_level_extended = intercept_all + slope_all * years_extended

    ax.plot(
        years_extended,
        sea_level_extended,
        color='red',
        label='Fit: 1880-2050'
    )
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(
        df_2000['Year'],
        df_2000['CSIRO Adjusted Sea Level']
    )
    slope_2000 = res_2000.slope
    intercept_2000 = res_2000.intercept

    years_2000 = pd.Series(range(2000, 2051))
    sea_level_2000 = intercept_2000 + slope_2000 * years_2000

    ax.plot(
        years_2000,
        sea_level_2000,
        color='green',
        label='Fit: 2000-2050'
    )
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    # Save plot and return fig
    fig.savefig('sea_level_plot.png')
    return fig
