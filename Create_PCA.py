import numpy as np
from sklearn.decomposition import PCA
import os
feature_vec_file ='/srv/home/noorfathima/database_videos2/allimagefeatures2'
Lines = [line.rstrip('\n') for line in open(feature_vec_file,'r')]
Feature_matrix = []
for i in range(len(Lines)):
    line = Lines[i]
    feat_text=line.split(' ')[1][1:-1].split(',')
    file_name = line.split(' ')[0]
    if not len(feat_text):
        print('Not processing --->'+file_name)
    dumm_vec = np.zeros((1,4096))
    for k in range(4096):
        dumm_vec[0,k] = str(feat_text[k])
    Feature_matrix.append(dumm_vec[0,:])



Final_feature_mat=np.asarray(Feature_matrix)
X = Final_feature_mat
n_samples = X.shape[0]
pca = PCA()
X_transformed = pca.fit_transform(X)
# We center the data and compute the sample covariance matrix.
X_centered = X - np.mean(X, axis=0)
cov_matrix = np.dot(X_centered.T, X_centered) / n_samples
eigenvalues = pca.explained_variance_
if not os.path.exists('pca_params/'):
   os.mkdir('pca_params/')

np.save('pca_params/eigenvals.npy',eigenvalues)
np.save('pca_params/eigenvecs.npy',pca.components_)
X_mean = np.mean(X, axis=0)
np.save('pca_params/mean.npy',X_mean)
