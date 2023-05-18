
def create_

# Create a list of consecutive integers
integers = range(len(prices))

plt.figure(figsize=(16, 8))

# Plot a scatterplot
plt.scatter(y=prices, x=integers, c='red', alpha=0.5)
plt.show()

-----
# Import the zscores function
from scipy.stats import zscore

# Find the zscores of prices
scores = zscore(prices)

# Check if the absolute values of scores are over 3
is_over_3 = abs(scores)>3

# Use the mask to subset prices
outliers = prices[is_over_3]

print(len(outliers))s