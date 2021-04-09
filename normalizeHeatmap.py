# libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dataframe where the average value of the second row is higher
df = pd.DataFrame(np.random.randn(10, 10) * 4 + 3)
df.iloc[2] = df.iloc[2] + 40

# If we do a heatmap, we just observe that one row has higher values than others:
sns.heatmap(df, cmap='viridis')
plt.show()

# Normalize it by row:
df_norm_row = df.apply(lambda x: (x - x.mean()) / x.std(), axis=1)

# And see the result
sns.heatmap(df_norm_row, cmap='viridis')
plt.show()