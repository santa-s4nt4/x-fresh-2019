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

img_weight, img_height = 150, 150
