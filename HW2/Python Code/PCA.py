import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn import preprocessing
import random
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
sns.set(style="white")

scaler = StandardScaler()
raw_data = pd.read_csv("/Users/yuchenma/Desktop/wine.csv")
random_sampling_data = pd.read_csv("/Users/yuchenma/Desktop/random_sampling_data.csv")
random_sampling_data = random_sampling_data.drop(columns=['Unnamed: 0'])
stratified_sampling_data = pd.read_csv("/Users/yuchenma/Desktop/stratified_sampling_data.csv")
stratified_sampling_data = stratified_sampling_data.drop(columns=['Unnamed: 0'])

def gain_dataset(data):
    label = data['quality']
    # train = data.drop(columns=['quality'])
    train = pd.DataFrame(scaler.fit_transform(data.drop(columns=['quality'])))
    return train,label

def show_scree_plot(data):
    pca = PCA()
    data_normalized = preprocessing.normalize(data, norm='l2')
    pca.fit(data_normalized)
    pca.explained_variance_ratio_ * 100
    scree_data = []
    count = 1
    for i in pca.explained_variance_ratio_ * 100:
        temp = {}
        temp['index'] = count
        temp['value'] = (i)
        count += 1
        scree_data.append(temp)
    scree_data = pd.DataFrame(scree_data)
    plot = sns.barplot(x='index', y='value', data=scree_data)
    for patch in plot.patches:
        plot.annotate(format(patch.get_height(), '.2f'), (patch.get_x() + patch.get_width() / 2., patch.get_height()),
                          ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    plt.show()
    return(scree_data)

raw_train,raw_label = gain_dataset(raw_data)
random_train,random_label = gain_dataset(random_sampling_data)
stratified_train,stratified_label = gain_dataset(stratified_sampling_data)
# ====================================================================================
# PCA for Orginal
# ====================================================================================

# plt.figure(figsize=(9,9))
# corr_matrix = raw_data.corr()
# mask = np.zeros_like(corr_matrix)
# mask[np.triu_indices_from(mask)] = True
# with sns.axes_style("white"):
#   p2 = sns.heatmap(corr_matrix, mask=mask, vmax=0.3, square=True, cmap="bone_r",annot=True)
# plt.show()
def gain_top_3_attr(train,label):
    data_scaled = pd.DataFrame(preprocessing.scale(train),columns = train.columns)
    pca_3 = PCA(n_components=3)
    temp = pca_3.fit_transform(data_scaled)
    result = pd.DataFrame(temp)
    result['quality'] = label
    return result

raw_pca_3 = gain_top_3_attr(raw_train,raw_label)
random_pca_3 = gain_top_3_attr(random_train,random_label)
stratified_pca_3 = gain_top_3_attr(stratified_train,stratified_label)

raw_pca_3.to_csv("/Users/yuchenma/Desktop/raw_pca_3.csv")
random_pca_3.to_csv("/Users/yuchenma/Desktop/random_pca_3.csv")
stratified_pca_3.to_csv("/Users/yuchenma/Desktop/stratified_pca_3.csv")
#
# raw_pca_result = show_scree_plot(raw_train)
# # ====================================================================================
# # PCA for random_sampling_data
# # ====================================================================================
# random_pca_result = show_scree_plot(random_train)
# # ====================================================================================
# # PCA for stratified_sampling_data
# # ====================================================================================
# stratified_pca_result = show_scree_plot(stratified_train)
#
#
#
# raw_pca_result.to_csv("/Users/yuchenma/Desktop/raw_pca_result.csv")
# random_pca_result.to_csv("/Users/yuchenma/Desktop/random_pca_result.csv")
# stratified_pca_result.to_csv("/Users/yuchenma/Desktop/stratified_pca_result.csv")