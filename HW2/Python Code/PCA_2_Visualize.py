import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
raw_data = pd.read_csv("/Users/yuchenma/Desktop/wine.csv")
random_sampling_data = pd.read_csv("/Users/yuchenma/Desktop/random_sampling_data.csv")
random_sampling_data = random_sampling_data.drop(columns=['Unnamed: 0'])
stratified_sampling_data = pd.read_csv("/Users/yuchenma/Desktop/stratified_sampling_data.csv")
stratified_sampling_data = stratified_sampling_data.drop(columns=['Unnamed: 0'])

def gain_dataset(data):
    label = data['quality']
    train = pd.DataFrame(scaler.fit_transform(data.drop(columns=['quality'])))
    return train,label

raw_train,raw_label = gain_dataset(raw_data)
random_train,random_label = gain_dataset(random_sampling_data)
stratified_train,stratified_label = gain_dataset(stratified_sampling_data)


def plot_PCA(train, label):
    pca = PCA(n_components=2)
    pc_2 = pca.fit_transform(train)
    pc_data = pd.DataFrame(data=pc_2, columns=['pc1', 'pc2'])
    pc_data = pd.concat([pc_data, label], axis=1)
    fig = plt.figure(figsize = (5,5))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('pc1', fontsize = 15)
    ax.set_ylabel('pc2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    targets = [3, 4, 5, 6, 7, 8]
    colors = sns.color_palette("cubehelix", 6)
    for target, color in zip(targets,colors):
        index = pc_data['quality'] == target
        ax.scatter(pc_data.loc[index, 'pc1']
                   , pc_data.loc[index, 'pc2']
                   , c = color
                   , s = 10)
    ax.legend(targets)
    ax.grid()
    plt.show()
    return pc_data

raw_pc_data = plot_PCA(raw_train, raw_label)
random_pc_data = plot_PCA(random_train, random_label)
stratified_pc_data = plot_PCA(stratified_train, stratified_label)

raw_pc_data.to_csv("/Users/yuchenma/Desktop/raw_pc_data.csv")
random_pc_data.to_csv("/Users/yuchenma/Desktop/random_pc_data.csv")
stratified_pc_data.to_csv("/Users/yuchenma/Desktop/stratified_pc_data.csv")
