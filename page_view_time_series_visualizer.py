import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import seaborn as sns

# Import data (Make sure to pase dates. Consider setting index column to date)
df = pd.read_csv(
    'fcc-forum-pageviews.csv',
    parse_dates=['date'],
    index_col='date'
)
# Clean data
lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)
df_clean = df[(df['value'] >= lower) & (df['value'] <= upper)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(
        df_clean.index,
        df_clean['value'],
        color='red',
        linewidth=1
    )
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for bar plot
    df_bar = df_clean.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar = df_bar.groupby(
        ['year', 'month'],
    )['value'].mean().unstack()
    months_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_bar = df_bar[months_order]
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar.plot(
        kind='bar',
        ax=ax
    )
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
    sns.boxplot(
        x='year', y='value', data=df_box, ax=axes[0],
        hue='year',
        palette='tab10',
        legend=False,
        fliersize=1
    )
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(
        x='month', y='value', data=df_box, ax=axes[1],
        order=month_order,
        hue='month',
        palette='Set2',
        legend=False,
        fliersize=1
    )
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    axes[0].set_ylim(0, 200000)
    axes[0].set_yticks(range(0, 200001, 20000))
    axes[0].tick_params(axis='y', labelrotation=0)

    axes[1].tick_params(axis='x', rotation=0, pad=6)
    fig.tight_layout()
    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
