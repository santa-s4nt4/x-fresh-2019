import numpy as np
import os
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, VGG16
from keras.models import Model
from annoy import AnnoyIndex

# img_dir_path = 'dataset/All/'
img_dir_path = 'dataDrivenArt/bin/data/images/'
annoy_model_path = 'model/x-fresh-flatten.ann'
# annoy_dim = 4096 # fc2
annoy_dim = 25088

base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input,
              outputs=base_model.get_layer('flatten').output)

annoy_model = AnnoyIndex(annoy_dim)

for i in range(1, 3988):
    # img_path = img_dir_path + str(i) + '.jpg'
    img_path = "C:\\Users\\santa\\Desktop\\Python\\x-fresh\\dataDrivenArt\\bin\\data\\images\\{0:04d}.jpg".format(
        i + 0)
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    flatten_features = model.predict(x)

    annoy_model.add_item(i, flatten_features[0])
    print(img_path, 'saved')

annoy_model.build(3987)
annoy_model.save(annoy_model_path)
