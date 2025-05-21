import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')
ibm = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (ibm > 25).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
        var_name='variable',
        value_name='value'
    )
    df_cat = (
        df_cat
        .groupby(['cardio', 'variable', 'value'], as_index=False)
        .size()
        .rename(columns={'size':'total'})
    )
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    cond1= df['ap_lo'] <= df['ap_hi']
    h_low, h_high = df['height'].quantile([0.025, 0.975])
    w_low, w_high = df['weight'].quantile([0.025, 0.975])
    cond2 = df['height'].between(h_low, h_high)
    cond3 = df['weight'].between(w_low, w_high)
    df_heat = df[cond1 & cond2 & cond3]
    corr = df_heat.corr()
    mask = np.triu(corr)
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        linewidth=.5,
        cmap='coolwarm',
        cbar_kws={'shrink': .5}
    )
    fig.savefig('heatmap.png')
    return fig
    
if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()
    print("Gráficos generados y guardados: catplot.png, heatmap.png")
