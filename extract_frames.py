import glob
import os
import random
from shutil import move


ROOT_dir = os.getcwd()
video_category  = glob.glob(ROOT_dir+'/videos/*/')
for category_path in video_category:
    category_name = category_path.split('/')[-2]
    create_dir = ROOT_dir+'/frames/'+category_name
    if not os.path.exists(create_dir):
        os.makedirs(create_dir)
    all_videos = glob.glob(category_path+'/*')
    n=0
    for video_file in all_videos:
        video_name = video_file.split('/')[-1].split('.')[0]
        create_rand_file = category_path+'/'+str(n)+str(random.randint(1,1000))+'.'+video_file.split('.')[-1]
        move(video_file,create_rand_file)
        n=n+1
    
    all_videos = glob.glob(category_path+'/*')    
    for video_file in all_videos:
        video_name = video_file.split('/')[-1].split('.')[0]
        print(video_name)
        create_folder = ROOT_dir+'/frames/'+category_name+'/'+video_name+'/frames/'
        if not os.path.exists(create_folder):
            os.makedirs(create_folder)
        create_folder_audio = ROOT_dir+'/frames/'+category_name+'/'+video_name+'/audio/'
        if not os.path.exists(create_folder_audio):
            os.makedirs(create_folder_audio)
        
        #os.system('ffmpeg -i '+video_file+' -r 1 '+' fps=0.960 '+ ROOT_dir+'/frames/'+category_name+'/'+video_name+'/frames/'+category_name+'_'+video_name+'_'+'frame_%05d.jpg')
        os.system('ffmpeg -i '+video_file+' -vf fps=1/0.960 '+ ROOT_dir+'/frames/'+category_name+'/'+video_name+'/frames/'+category_name+'_'+video_name+'_'+'frame_%05d.jpg')
        print('exracting frames----->'+video_file)
        #$FFMPEG -i "${video}" -f wav  $2/"${videoname}"/audio/audio.wav
        os.system('ffmpeg -i '+video_file+' -f wav '+ ROOT_dir+'/frames/'+category_name+'/'+video_name+'/audio/'+category_name+'_'+video_name+'_'+'audio.wav')
        print('extracting audio----->'+video_file)
