# libraries
import seaborn as sns
import pandas as pd
import numpy as np

# Create a dataset
df = pd.DataFrame(np.random.random((10, 10)), columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])

# plot a heatmap
sns.heatmap(df, xticklabels=4)