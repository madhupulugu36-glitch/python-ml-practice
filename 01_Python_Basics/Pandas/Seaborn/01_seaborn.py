import seaborn as sns
import matplotlib.pyplot as plt

# 1. Lineplot
fmri = sns.load_dataset("fmri")
sns.lineplot(x = "timepoint", y="signal", hue="region", data=fmri)
plt.show()

# 2. Scatterplot
tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips)
plt.show()

# 3. Barplot
tips = sns.load_dataset("tips")

sns.barplot(x="day", y="total_bill", data=tips)
plt.show()

# 4. Boxplot
tips = sns.load_dataset("tips")

sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# 5. Histplot
tips = sns.load_dataset("tips")

sns.histplot(tips["total_bill"], kde=True)
plt.show()

# 6. Heatmap
tips = sns.load_dataset("tips")
corr = tips.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# 7. Pairplot
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.show()