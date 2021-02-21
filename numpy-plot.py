from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(size=100)

sns.displot(x,kind="hist",kde=True)

sns.set_theme(style="ticks")
df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")

plt.show()
