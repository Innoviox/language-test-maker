import tensorflow as tf

import glob, imageio, numpy as np, os, PIL, time
from tensorflow.keras import layers, datasets

import matplotlib.pyplot as plt

from tqdm import trange

# (train_imgs, train_labs), (test_imgs, test_labs) = tf.keras.datasets.mnist.load_data()

# train_imgs = train_imgs.reshape(train_imgs.shape[0], 28, 28, 1).astype('float32')
# train_imgs = (train_imgs - 127.5) / 127.5 # Normalize the images to [-1, 1]

(train_imgs, train_labs), (test_imgs, test_labs) = datasets.cifar10.load_data()
train_imgs = train_imgs.reshape(train_imgs.shape[0], 32, 32, 3).astype('float32')
n = 127.5
train_imgs, test_imgs = (train_imgs - n) / n, (test_imgs - n) / n # normalize


BUFFER_SIZE = 60000
BATCH_SIZE  = 256

train_dataset = tf.data.Dataset.from_tensor_slices(train_imgs).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

def make_generator_model():
    model = tf.keras.Sequential()

    model.add(layers.Dense(8*8*256, use_bias=False, input_shape=(100,)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Reshape((8, 8, 256)))

    model.add(layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(3, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))

    model.summary()

    return model

def make_discriminator_model():
    model = tf.keras.Sequential()

    model.add(layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[32, 32, 3]))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Flatten())
    model.add(layers.Dense(1))

    return model

generator     = make_generator_model()
discriminator = make_discriminator_model()

cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)

def discriminator_loss(real, fake):
    real_loss = cross_entropy(tf.ones_like(real), real)
    fake_loss = cross_entropy(tf.zeros_like(fake), fake)
    return real_loss + fake_loss

def generator_loss(fake):
    return cross_entropy(tf.ones_like(fake), fake)

gen_opt = tf.keras.optimizers.Adam(1e-4)
disc_opt = tf.keras.optimizers.Adam(1e-4)

checkpt_dir = './training_checkpoints_2'
checkpt_pref = os.path.join(checkpt_dir, 'ckpt')
checkpt = tf.train.Checkpoint(generator_optimizer=gen_opt,
                              discriminator_optimizer=disc_opt,
                              generator=generator, discriminator=discriminator)

checkpt.restore(tf.train.latest_checkpoint(checkpt_dir))

EPOCHS = 50
noise_dim = 100
num_examples_to_generate = 16

seed = tf.random.normal([num_examples_to_generate, noise_dim])

@tf.function
def train_step(images):
    noise = tf.random.normal([BATCH_SIZE, noise_dim])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)

        real_out = discriminator(images, training=True)
        fake_out = discriminator(generated_images, training=True)

        gen_loss = generator_loss(fake_out)
        disc_loss = discriminator_loss(real_out, fake_out)

    grads_gen = gen_tape.gradient(gen_loss, generator.trainable_variables)
    grads_disc = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

    gen_opt.apply_gradients(zip(grads_gen, generator.trainable_variables))
    disc_opt.apply_gradients(zip(grads_disc, discriminator.trainable_variables))

def gen_imgs(model, epoch, test):
    predictions = model(test, training=False)

    fig = plt.figure(figsize=(4, 4))

    for i in range(predictions.shape[0]):
        plt.subplot(4, 4, i+1)
        plt.imshow(predictions[i, :, :, 0] * n + n, cmap='inferno')
        plt.axis('off')

    plt.savefig('image3_at_epoch_{:04d}.png'.format(epoch))
    plt.close()
    # plt.show()

def train(dataset, epochs):
    for epoch in trange(epochs):
        start = time.time()

        for batch in dataset:
            train_step(batch)

        gen_imgs(generator, epoch, seed)
        
        checkpt.save(file_prefix=checkpt_pref)

    gen_imgs(generator, epoch, seed)

# train(train_dataset, EPOCHS)
gen_imgs(generator, 50, seed)

anim_file = 'dcgan.gif'

with imageio.get_writer(anim_file, mode='I') as writer:
  filenames = glob.glob('image3*.png')
  filenames = sorted(filenames)
  last = -1
  for i,filename in enumerate(filenames):
    frame = 2*(i**0.5)
    if round(frame) > round(last):
      last = frame
    else:
      continue
    image = imageio.imread(filename)
    writer.append_data(image)
  image = imageio.imread(filename)
  writer.append_data(image)
