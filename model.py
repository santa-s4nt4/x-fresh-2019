import os
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
import numpy as np
import time

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
