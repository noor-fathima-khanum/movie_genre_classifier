import os
import glob
import numpy as np

ROOT_dir = os.getcwd()



##### Load PCA params
pca_params_folder = ROOT_dir+'/pca_params/'
pca_mean = np.load(pca_params_folder+'/mean.npy')[:]
pca_eigenvecs = np.load(pca_params_folder+'/eigenvecs.npy').T[:, :512]
pca_eigenvals = np.load(pca_params_folder+'/eigenvals.npy')[:512]


def apply_pca(frame_features):
    # Subtract mean
    feats = frame_features - pca_mean

    # Multiply by eigenvectors.
    feats = feats.reshape((1, 4096)).dot(pca_eigenvecs).reshape((512,))

    # Whiten
    feats /= np.sqrt(pca_eigenvals + 1e-4)
    return feats



if not os.path.exists(ROOT_dir+'/Store_feats/'):
    os.makedirs(ROOT_dir+'/Store_feats/')
    
All_genres = glob.glob(ROOT_dir+'/Features_processing/*/')
for genre in All_genres:
    all_vides = glob.glob(genre+'/*/')    
    dumm_vecs = np.zeros((1,640))
    for video in all_vides:
        #All_img_feats = sorted(glob.glob(video+'/image_feats/*.npy'))
        num_audio = sorted(glob.glob(video+'/audio_feats/*.npy'))
        num_img =   sorted(glob.glob(video+'/image_feats/*.npy'))
        if (len(num_audio)<len(num_img)):
           All_img_feats=sorted(glob.glob(video+'/audio_feats/*.npy'))
        else:
           All_img_feats=sorted(glob.glob(video+'/image_feats/*.npy'))
     
        Feat_matrix_video=[]
        #Feat_matrix_video_after_pca = []
        #Feat_matrix_video_before_pca = []
        for feat_vec in All_img_feats:
            name = feat_vec.split('/')[-1]
            feat_vec_np=np.load(video+'/image_feats/'+name)
            #feat_vec_np = np.load(feat_vec)
            pca_whitened_feat = apply_pca(feat_vec_np)
            audio_feat = np.load(video+'/audio_feats/'+name)
            full_feat = np.concatenate((pca_whitened_feat,audio_feat))
            Feat_matrix_video.append(full_feat)
            
            #Feat_matrix_video_before_pca.append(feat_vec_np)
            #Feat_matrix_video_after_pca.append(pca_whitened_feat)
        for k in range((143-len(Feat_matrix_video))):
            Feat_matrix_video.append(dumm_vecs[0])
        
        
        Feat_matrix_video_numpy=np.asarray(Feat_matrix_video)
        if np.asarray(Feat_matrix_video).shape[0] <= 143:
            Feat_matrix_video_numpy=np.asarray(Feat_matrix_video)[10:,:]
        else:
            Feat_matrix_video_numpy=np.asarray(Feat_matrix_video)[10:143,:]
         
        
        save_path = ROOT_dir+'/Store_feats/'+video.split('/')[-3]+'_'+video.split('/')[-2]+'.npy'
        np.save(save_path,Feat_matrix_video_numpy)
            
###############Test the feats
''''
All_feats = glob.glob(ROOT_dir+'/Store_feats/*.npy')
for file in All_feats:
    read_feat = np.load(file)
    print(read_feat.shape)
'''
#########################    
