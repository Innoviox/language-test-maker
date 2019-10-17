import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_imgs, train_labs), (test_imgs, test_labs) = datasets.cifar10.load_data()
train_imgs, test_imgs = train_imgs / 255, test_imgs / 255 # normalize

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

if False:
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)

        plt.imshow(train_imgs[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labs[i][0]])

    plt.show()


# CNN: input tensor is (image height, image width, color channels)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(train_imgs, train_labs, epochs=10, validation_data=(test_imgs, test_labs))

if False:
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')

    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.5, 1])
    plt.legened(loc='lower right')

# test_loss, test_acc = model.evaluate(test_imgs, test_labs, verbose=2)
# print(test_acc)
