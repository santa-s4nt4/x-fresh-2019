import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, VGG16
from keras.models import Model
from annoy import AnnoyIndex
