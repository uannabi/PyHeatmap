import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dataframe where the average value of the second column is higher than others:
df = pd.DataFrame(np.random.randn(10, 10) * 4 + 3)
df[1] = df[1] + 40

# If we do a heatmap, we just observe that one column has higher values than others:
sns.heatmap(df, cmap='viridis')
plt.show()

# Now if we normalize it by column:
df_norm_col = (df - df.mean()) / df.std()
sns.heatmap(df_norm_col, cmap='viridis')
plt.show()