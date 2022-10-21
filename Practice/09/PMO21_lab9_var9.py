import pandas as pd
import matplotlib.pyplot as plt

df_raw = pd.read_csv("Covid19.csv")
cyl_colors = {4:'tab:red', 5:'tab:green', 6:'tab:blue', 8:'tab:orange'}
df_raw['cyl_color'] = df_raw.Ail.map(cyl_colors)

df = df_raw[['Ail', 'Region']].groupby('Region').apply(lambda x: x.mean())
df.sort_values('Ail', ascending=False, inplace=True)
df.reset_index(inplace=True)
df_median = df_raw[['Ail', 'Region']].groupby('Region').apply(lambda  x: x.median())

fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
ax.hlines(y=df.index, xmin=0, xmax=1500, color='gray', alpha=0.5, linewidth=.5, linestyles='dashdot')

for i, make in enumerate(df.Region):
    df_make = df_raw.loc[df_raw.Region==make, :]
    ax.scatter(y=[i]*df_make.shape[0], x='Ail', data=df_make, s=25, edgecolors='gray', c='w', alpha=0.5)
    ax.scatter(y=i, x='Ail', data=df_median.loc[df_median.index==make, :], s=25, c='firebrick')

ax.text(1290, 23, "$red \; dots \; are \; the \: median$", fontdict={'size':10}, color='firebrick')

red_patch = plt.plot([],[], marker="o", ms=8, ls="", mec=None, color='firebrick', label="Median")
plt.legend(handles=red_patch)
ax.set_title('The number of Covid-19 time in the region per day', fontdict={'size':22})
ax.set_xlabel('Data for 06.12-11.12', alpha=0.7)
ax.set_yticks(df.index)
ax.set_yticklabels(df.Region.str.title(), fontdict={'horizontalalignment': 'right'}, alpha=0.7)
ax.set_xlim(1, 1500)
plt.xticks(alpha=0.7)
plt.gca().spines["top"].set_visible(False)    
plt.gca().spines["bottom"].set_visible(False)    
plt.gca().spines["right"].set_visible(False)    
plt.gca().spines["left"].set_visible(False)   
plt.grid(axis='both', alpha=.4, linewidth=.1)
plt.show()