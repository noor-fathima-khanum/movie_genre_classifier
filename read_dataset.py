import numpy as np
import os
import glob


class_lables = {'action':0,'animation':1,'drama':2,'horror':3,'periodfilm':4,'romantic':5}
num_classes = len(class_lables)

data_path = '/srv/home/noorfathima/database_videos2/classifier3/feats'


def read_dataset(folder_path):
    all_npy_files = glob.glob(folder_path+'/*.npy')
    features = []
    labels = []
    print ("XXXXXXXXXXXXXXXXXXXXXXXX")
    for numpy_file in all_npy_files:
        #print (all_npy_files[0])
        print (numpy_file)
        feature_matrix = np.load(numpy_file).T  ### Taking transpose to make time dimesion is x-axis
        print ("Before Transpose",(np.load(numpy_file)).shape)
        print ("After Transpose",feature_matrix.shape)
        label = class_lables[folder_path.split('/')[-2]]
        dummy_vec = np.zeros((1,num_classes))
        dummy_vec[0][label]=1.0
        labels.append(dummy_vec[0])
        features.append(feature_matrix)
    print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    return features,labels
        

    
    
all_class_folders = glob.glob(data_path+'/*/')
Full_features =[]
Full_labels = []
i=0
for class_folder in all_class_folders:
    features_mat,label_matrix = read_dataset(class_folder)
    if i==0:
        Full_features = np.asarray(features_mat)
        Full_labels = np.asarray(label_matrix)
    else:
        Full_features = np.concatenate((Full_features,np.asarray(features_mat)))
        Full_labels = np.concatenate((Full_labels, np.asarray(label_matrix)))
    i=i+1
    print(i)

print (Full_features.shape)
print (Full_labels.shape)
np.save('features.npy',Full_features)
np.save('labels.npy',Full_labels)
