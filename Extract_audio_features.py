import os
import glob
from shutil import copyfile
from audioset.extract_high_level_features import Extract_feats


ROOT_dir = os.getcwd()



weight_file='./audioset/vggish_model.ckpt'
pca_params = './audioset/vggish_pca_params.npz'
genrers = glob.glob(ROOT_dir+'/frames/*/')
for genre in genrers:
    all_videos = glob.glob(genre+'/*/')
    for video in all_videos:
        audio_path = glob.glob(video+'/audio/*.wav')
        outfile = audio_path[0].split('.')[0]+'.npy'
        Extract_feats(audio_path[0],outfile,weight_file,pca_params)
        print('Done--->'+audio_path[0])
