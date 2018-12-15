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


################################################
#### Read audio features #####################
##############################################
import glob
import numpy as np


ROOT_Dir = os.getcwd()
genres_path = glob.glob(ROOT_Dir+'/frames/*/')
for genre_path in genres_path:
    videos = glob.glob(genre_path+'/*/')
    for video in videos:
        audio_feat_file = glob.glob(video+'audio/*.npy')
        file_name = audio_feat_file[0].split('/')[-1].split('.')[0]
        read_numpy_file = np.load(audio_feat_file[0])
        length_file = read_numpy_file.shape[0]
        genre =file_name.split('_')[0]
        video_id = file_name.split('_')[1]
        os.makedirs(ROOT_Dir+'/Features_processing/'+genre+'/'+video_id+'/'+'audio_feats/')
        print ("Printing Length of Each File")
        print (length_file)
        print ("***************************")
        for i in range(length_file):
            feat  =read_numpy_file[i]
            cat_str=''
            for k in range(5-len(str(i+1))):
                cat_str=cat_str+'0'    
            frame_id = genre+'_'+video_id+'_'+cat_str+str(i+1)+'.npy'
            feat = read_numpy_file[i]
            save_path = ROOT_Dir+'/Features_processing/'+genre+'/'+video_id+'/'+'audio_feats/'+frame_id
            np.save(save_path,feat)
