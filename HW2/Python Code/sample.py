import pandas as pd
from sklearn.cluster import KMeans
import random
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
N_cluster = 7
raw_data = pd.read_csv("/Users/yuchenma/Desktop/wine.csv")

# ====================================================================================
# random sampling
# ====================================================================================
random_sampling_data = raw_data.sample(frac=0.3, replace=True, random_state=1)


# ====================================================================================
# stratified sampling
# ====================================================================================
MSE = []
for k in range(1, 16):
    kmeans = KMeans(n_clusters=k).fit(raw_data)
    kmeans.fit(raw_data)
    MSE.append(sum(np.min(cdist(raw_data, kmeans.cluster_centers_,'euclidean'), axis=1)) / raw_data.shape[0])

i = 1
temp = []
for item in MSE:
    t = {}
    t['x'] = i
    t['y'] = item
    temp.append(t)
    i += 1
mse_data = pd.DataFrame(temp)

sns.set()
fig = plt.figure(figsize=(10, 5))
plt.plot(range(1,16), MSE, 'bx-',color="m")
plt.xlabel('K')
plt.ylabel('MSE')
plt.title('Elbow Plot')
plt.show()

clustering = KMeans(n_clusters=N_cluster).fit(raw_data)
clustering.fit(raw_data)
raw_data['label'] = clustering.labels_
temp = []
for i in range(N_cluster):
    temp.append(raw_data.loc[random.sample(list(raw_data[raw_data['label'] == i].index),
                                                         (int)(len(raw_data[raw_data['label'] == i])*0.3))])
stratified_sampling_data = pd.concat(temp)
del stratified_sampling_data['label']

# ====================================================================================
# Two sampling data export
# ====================================================================================
print(random_sampling_data.shape)
print(stratified_sampling_data.shape)

random_sampling_data.to_csv("/Users/yuchenma/Desktop/random_sampling_data.csv")
stratified_sampling_data.to_csv("/Users/yuchenma/Desktop/stratified_sampling_data.csv")
mse_data.to_csv("/Users/yuchenma/Desktop/mse_data.csv")
