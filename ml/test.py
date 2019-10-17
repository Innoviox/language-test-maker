import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import tensorflow as tf

from tensorflow.keras import datasets, layers, models
from tqdm import tqdm

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

(train_imgs, train_labs), (test_imgs, test_labs) = datasets.cifar10.load_data()
train_imgs, test_imgs = train_imgs / 255, test_imgs / 255 # normalize

##train_labs = []
##for i in tqdm(_train_labs):
##    x = [0] * len(class_names)
##    x[i[0]] = 1
##    train_labs.append(x)
##
##test_labs = []
##for i in tqdm(_test_labs):
##    x = [0] * len(class_names)
##    x[i[0]] = 1
##    test_labs.append(x)

# CNN: input tensor is (image height, image width, color channels)

##model = models.Sequential()
##model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
##model.add(layers.MaxPooling2D((2, 2)))
##model.add(layers.Conv2D(64, (3, 3), activation='relu'))
##model.add(layers.MaxPooling2D((2, 2)))
##model.add(layers.Conv2D(64, (3, 3), activation='relu'))
##
##model.add(layers.Flatten())
##model.add(layers.Dense(64, activation='relu'))
##model.add(layers.Dense(len(class_names), activation='softmax'))

model = models.Sequential()
# model.add(layers.Input((1,)))
# model.add(layers.Dense(len(class_names), activation='softmax'))
model.add(layers.Dense(64*3*64, activation='relu', input_shape=(1,)))
model.add(layers.BatchNormalization())
model.add(layers.LeakyReLU())
# model.add(layers.Flatten())
model.add(layers.Reshape((64, 3, 64)))

model.add(layers.Conv2DTranspose(64, (3, 3), strides=(1, 1), padding='same', use_bias=False))
# model.add(layers.BatchNormalization())
# model.add(layers.LeakyReLU())

# model.add(layers.Conv2DTranspose(32, (3, 3), strides=(1, 1), padding='same', use_bias=False))

# model.add(layers.Permute((64, 3, 3), input_shape=(1024,)))
# model.add(layers.Dense(64, (3, 3), activation='relu'))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(train_labs, train_imgs, epochs=10, validation_data=(test_labs, test_imgs))

# test_loss, test_acc = model.evaluate(test_imgs, test_labs, verbose=2)
# print(test_acc)
