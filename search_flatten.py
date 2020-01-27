import os
import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, VGG16
from keras.models import Model
from annoy import AnnoyIndex

annoy_model_path = 'model/x-fresh-flatten.ann'
search_img_path = input("\n>> 入力したい画像ファイルのPATH ： ")
annoy_dim = 25088

base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input,
              outputs=base_model.get_layer('flatten').output)

loaded_model = AnnoyIndex(annoy_dim)
loaded_model.load(annoy_model_path)

img_path = search_img_path
img = image.load_img(img_path, target_size=(224, 224))

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

flatten_features = model.predict(x)

items = loaded_model.get_nns_by_vector(
    flatten_features[0], 3, search_k=-1, include_distances=False)
print(items[0])
print(items[1])
print(items[2])
