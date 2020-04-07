from sklearn.metrics.pairwise import pairwise_distances
from sklearn import manifold
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_MDS(distance, label):
    mds = manifold.MDS(n_components=2, dissimilarity='precomputed')
    data = mds.fit_transform(distance)
    i = 0
    temp = []
    for row in data:
        t = {}
        t['x'] = row[0]
        t['y'] = row[1]
        t['cluster'] = label[i]
        temp.append(t)
        i += 1
    mds_data = pd.DataFrame(temp)
    sns.scatterplot(x="x", y="y", hue="cluster",data=mds_data,palette="muted")
    plt.show()
    return mds_data

def gain_mds_data(data):
    scaler = StandardScaler()
    label = data['quality']
    train = scaler.fit_transform(data.drop(columns=['quality']))
    Euc_distance = pairwise_distances(X=train, metric="euclidean")
    Cor_distance = pairwise_distances(X=train, metric="correlation")
    Euc_mds_data = plot_MDS(Euc_distance, label)
    Cor_mds_data = plot_MDS(Cor_distance, label)
    return Euc_mds_data, Cor_mds_data

raw_data = pd.read_csv("/Users/yuchenma/Desktop/wine.csv")
random_sampling_data = pd.read_csv("/Users/yuchenma/Desktop/random_sampling_data.csv")
random_sampling_data = random_sampling_data.drop(columns=['Unnamed: 0'])
stratified_sampling_data = pd.read_csv("/Users/yuchenma/Desktop/stratified_sampling_data.csv")
stratified_sampling_data = stratified_sampling_data.drop(columns=['Unnamed: 0'])

raw_Euc_mds_data, raw_Cor_mds_data = gain_mds_data(raw_data)
random_Euc_mds_data, random_Cor_mds_data = gain_mds_data(random_sampling_data)
stratified_Euc_mds_data, stratified_Cor_mds_data = gain_mds_data(stratified_sampling_data)


raw_Euc_mds_data.to_csv("/Users/yuchenma/Desktop/raw_Euc_mds_data.csv")
raw_Cor_mds_data.to_csv("/Users/yuchenma/Desktop/raw_Cor_mds_data.csv")

random_Euc_mds_data.to_csv("/Users/yuchenma/Desktop/random_Euc_mds_data.csv")
random_Cor_mds_data.to_csv("/Users/yuchenma/Desktop/random_Cor_mds_data.csv")

stratified_Euc_mds_data.to_csv("/Users/yuchenma/Desktop/stratified_Euc_mds_data.csv")
stratified_Cor_mds_data.to_csv("/Users/yuchenma/Desktop/stratified_Cor_mds_data.csv")