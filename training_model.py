#import keras
import tensorflow
import sklearn
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
import numpy as np
import pickle

batch_size = 10
num_classes = 6
epochs = 250


X_data = np.load('/srv/home/noorfathima/database_videos2/classifier3/features.npy')
Y_data = np.load('/srv/home/noorfathima/database_videos2/classifier3/labels.npy')
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.2, random_state=42)

print (X_data.shape)
#print (X_data[1])
#print (Y_data[1])

np.savetxt('Y_test.txt',Y_test)

input_shape = (640,133,1)
X_train = X_train.reshape(X_train.shape[0],640,133,1)
X_test = X_test.reshape(X_test.shape[0],640,133,1)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))


adadel=tensorflow.keras.optimizers.Adadelta(lr=0.0001, rho=0.95, epsilon=None, decay=0.7)
model.compile(loss=tensorflow.keras.losses.categorical_crossentropy,
              optimizer=adadel,
              metrics=['accuracy'])

history=model.fit(X_train, Y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1)

score = model.evaluate(X_test, Y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


values=[]
values=model.predict(X_test)
np.savetxt('Values.txt',values)

with open('trainHistoryDict', 'wb') as file_pi:
        pickle.dump(history.history, file_pi,protocol=2)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model.h5")
print("Saved model to disk")
