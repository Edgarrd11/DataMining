import scipy.stats.distributions as dist
import pandas as pd
import numpy as np
#Practica 4: Statistic Test
#Edgar Armando Ruiz Dorador 1990126


data = pd.read_csv("rf-clean-data.csv")
open = data[data["tourney_name"].isin( ["US Open","Australian Open"])]
ct = pd.crosstab( open.match_win_loss, open.tourney_name)
pct = pd.crosstab(open.match_win_loss, open.tourney_name).apply(lambda r:r/r.sum(),axis=1)

total_proportion_won = (open.match_win_loss == "W").mean()
num_us = open[open.tourney_name=="US Open"].shape[0]
num_aus = open[open.tourney_name=="Australian Open"].shape[0]
assert num_us*total_proportion_won>10, "Assumptions not met"
assert num_aus*total_proportion_won>10, "Assumptions not met"
assert num_us*(1-total_proportion_won)>10, "Assumptions not met"
assert num_aus*(1-total_proportion_won)>10, "Assumptions not met"

prop = open.groupby("tourney_name")["match_win_loss"].agg([lambda z: np.mean(z=="W"), "size"])
prop.columns = ['proportions_won','total_counts']
prop.head()
variance = total_proportion_won * (1 - total_proportion_won)
standard_error = np.sqrt(variance * (1 / prop.total_counts["US Open"] + 1 / prop.total_counts["Australian Open"]))
print("Sample Standard Error",standard_error)

# Calculate the test statistic
best_estimate = (prop.proportions_won["US Open"] - prop.proportions_won["Australian Open"])
print("The best estimate is",best_estimate)
hypothesized_estimate = 0
test_stat = (best_estimate-hypothesized_estimate) / standard_error
print("Computed Test Statistic is",test_stat)
# Calculate the  p-value
pvalue = 2*dist.norm.cdf(-np.abs(test_stat)) # Multiplied by two indicates a two tailed testing.
print("Computed P-value is", pvalue)
