import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Reshape
from tensorflow.keras.layers import Conv2D, UpSampling2D
from tensorflow.keras.layers import LeakyReLU, Dropout
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.optimizers import Adam, SGD, RMSprop
from tensorflow.keras import backend as ktf
import os

import time
import numpy as np
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.vgg19 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
import os
import glob
import sys


for p in sys.path:
  print (p)
model = VGG19(weights='imagenet', include_top=True)
#model.summary()
print ("****************TENSORFLOW VERSION***********")
print (tf.__version__)

print("KERAS VERSION:", tf.keras.__version__)


base_model = VGG19(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)

ROOT_dir=os.getcwd()

gnres = glob.glob(ROOT_dir+'/frames/*/')

final_array=[]
dummy=[]
print ("***")

for gnre in gnres:
    all_videos=glob.glob(gnre+'/*/')
    for video in all_videos:
        all_images=glob.glob(video+'/frames/*.jpg')
        for x in all_images:
            #x=all_images[1]
            outfile=x.split('.')[0]+'.txt'
            splitslash=((x.split('/')[-1]).split('.'))[0]
            print (splitslash)
            img = image.load_img(x,target_size=(224, 224))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img = preprocess_input(img)
            fc2_features = model.predict(img)
            final_features=[]
            final_features.append(outfile)
            final_features.append(fc2_features)
            list_features=fc2_features.tolist()
            print (len(list_features[0]))
            #np.savetxt(outfile,fc2_features)
            outF=open(outfile,"w")
            outF.write(str(splitslash))
            outF.write(' ')
            lst=map(str,list_features)
            line=",".join(lst)
            outF.write(line)
            outF.write('\n')
            #np.savetxt(outfile,list_features,delimiter=',')
            dummy=[splitslash,list_features]
            final_array.append(dummy)
            dummy=[]
            outF.close()

#np.savetxt('final_vecs_numpy',final_array)

with open('final_vecs.txt',"w") as myfile:
    for item in final_array:
       filename="".join(map(str,item[0]))
       lst=map(str,item[1])
       line=",".join(lst)
       myfile.write(filename)
       myfile.write(' ')
       myfile.write(line)
       myfile.write("\n")

myfile.close()
       


#finaloutF=open('final_vecs.txt',"w")
#finaloutF.write(str(final_array))
#finaloutF.close()

# pre-process the image
#img = image.load_img('/home/noor/ann_project/project/youtube-8m-videos-frames/frames/action/048/frames/action_048_frame_00039.jpg', target_size=(224, 224))
#img = image.img_to_array(img)
#img = np.expand_dims(img, axis=0)
#img = preprocess_input(img)
#model = Model(input=base_model.input, output=base_model.get_layer('fc2').output)
#fc2_features = model.predict(img)
#print (fc2_features)
#print ("Feature vector dimensions: ",fc2_features.shape)
