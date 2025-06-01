import seaborn as sns
import matplotlib.pyplot as plt


sns.set_style('white')  # or use 'whitegrid' for gridlines
plt.style.use('default')  # ensures no extra background tint

# Load dataset
tips = sns.load_dataset('tips')

# Plot with polynomial regression of order 3
sns.regplot(
    x='total_bill',
    y='tip',
    data=tips,
    order=3,
    scatter_kws={'color': 'green', 's': 30},  # s increases dot size
    line_kws={'color': 'red', 'linewidth': 3}
)

plt.title('Regression with parameter k = 3')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.tight_layout()
plt.show()
