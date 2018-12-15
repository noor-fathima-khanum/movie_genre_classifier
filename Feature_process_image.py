import numpy as np
from sklearn.decomposition import PCA
import os
import numpy as np
feature_vec_file = '/srv/home/noorfathima/database_videos2/allimagefeatures2'
Lines = [line.rstrip('\n') for line in open(feature_vec_file,'r')]
Feature_matrix = []
ROOT_Dir = os.getcwd()

if not os.path.exists('Features_processing/'):
    os.mkdir('Features_processing/')



for i in range(len(Lines)):
    line = Lines[i]
    file_name=line.split(' ')[0]
    feat_text=line.split(' ')[1][1:-1].split(',')
    if not len(feat_text):
        print('Not processing --->'+file_name)
    dumm_vec = np.zeros((1,4096))
    for k in range(4096):
        dumm_vec[0,k] = str(feat_text[k])
    split_name = file_name.split('_')
    genre=split_name[0]
    vide_id=split_name[1]
    frame_id=split_name[-1]
    save_img_feat_path=ROOT_Dir+'/Features_processing/'+genre+'/'+vide_id+'/'+'image_feats/'
    if not os.path.exists(save_img_feat_path):
        os.makedirs(save_img_feat_path)
    save_img_feat_name = genre+'_'+vide_id+'_'+frame_id+'.npy'
    save_img_feat_full_path=save_img_feat_path+save_img_feat_name
    np.save(save_img_feat_full_path,dumm_vec[0])
