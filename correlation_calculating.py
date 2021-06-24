saving=[43.42, 61.21, 62.99, 65.21, 65.14, 51.00, 62.32, 54.67, 31.54, 20.89, 15.11, 40.73]
saving_batch4=[37.20, 55.35, 56.15, 57.70, 56.96, 49.10, 55.60, 50.68, 29.20, 16.60, 06.79, 36.60]
repetetive_failure_rate=[61.46, 29.62, 31.91, 41.66, 58.70, 33.93, 26.97, 35.37, 36.70, 67.24, 67.92, 77.14]
failure_rates=[19.87, 6.85, 6.69, 6.91, 8.39, 9.23, 6.57, 8.97, 17.65, 32.78, 40.30, 24.09]
corrected_saving=[59.92, 69.30, 70.98, 73.17, 74.29, 60.21, 70.33, 64.15, 44.31, 36.98, 32.23, 57.86]
corrected_saving_batch4=[51.33, 62.66, 63.27, 64.75, 64.63, 57.97, 62.74, 59.46, 41.02, 29.39, 14.48, 51.99]



failure_spread=[]
for i in range(0,len(saving)):
    failure_spread.append(failure_rates[i]/repetetive_failure_rate[i])
from scipy import stats
print(stats.spearmanr(saving, failure_spread))
print(stats.spearmanr(saving, failure_rates))
print(stats.spearmanr(saving_batch4, failure_spread))
print(stats.spearmanr(saving_batch4, failure_rates))