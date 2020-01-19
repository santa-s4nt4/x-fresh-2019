import os
import keras
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = 1000000000

classes = ["Abstract_Expressionism",
           "Action_painting",
           "Analytical_Cubism",
           "Art_Nouveau",
           "Baroque",
           "Color_Field_Painting",
           "Contemporary_Realism",
           "Cubism",
           "Early_Renaissance",
           "Expressionism",
           "Fauvism",
           "High_Renaissance",
           "Impressionism",
           "Mannerism_Late_RenaissanceMinimalism",
           "Naive_Art_Primitivism",
           "New_Realism",
           "Northern_Renaissance",
           "Pointillism",
           "Pop_Art",
           "Post_Impressionism",
           "Realism",
           "Rococo",
           "Romanticism",
           "Symbolism",
           "Synthetic_Cubism",
           "Ukiyo_e"]

nb_classes = len(classes)

img_width = 150
img_height = 150

train_data_dir = 'dataset/01train'
validation_data_dir = 'dataset/02test'

nb_train_samples = 7000
nb_validation_samples = 1000

batch_size = 100

nb_epoch = 20

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    zoom_range=0.2,
    horizontal_flip=True
)

validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    color_mode='rgb',
    classes=classes,
    class_mode='categorical',
    batch_size=batch_size,
    shuffle=True
)

validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    color_mode='rgb',
    classes=classes,
    class_mode='categorical',
    batch_size=batch_size,
    shuffle=True
)

keras.applications.vgg16.VGG16(include_top=True, weights='imagenet',
                               input_tensor=None, input_shape=None, pooling=None, classes=1000)


input_tensor = Input(shape=(img_width, img_height, 3))
vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

top_model = Sequential()
top_model.add(Flatten(input_shape=vgg16.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(nb_classes, activation='softmax'))

vgg_model = Model(input=vgg16.input, output=top_model(vgg16.output))

for layer in vgg_model.layers[:15]:
    layer.trainable = False

vgg_model.compile(loss='categorical_crossentropy',
                  optimizer=optimizers.SGD(lr=1e-3, momentum=0.9),
                  metrics=['accuracy'])

history = vgg_model.fit_generator(
    train_generator,
    samples_per_epoch=nb_train_samples,
    nb_epoch=nb_epoch,
    validation_data=validation_generator,
    nb_val_samples=nb_validation_samples)

# resultsディレクトリを作成
result_dir = 'results'
if not os.path.exists(result_dir):
    os.mkdir(result_dir)

vgg_model.save_weights(os.path.join(result_dir, 'Final.h5'))

vgg_model.save(os.path.join(result_dir, 'VGGtake1.h5')


plt.plot(history.history["acc"], label="acc", ls="-", marker="o")
plt.plot(history.history["val_acc"], label="val_acc", ls="-", marker="x")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(loc="best")
plt.savefig('Final.png')
plt.show()
