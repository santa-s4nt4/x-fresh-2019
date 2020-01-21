import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, VGG16
from keras.models import Model
from annoy import AnnoyIndex

img_dir_path = 'dataset/All/'
annoy_model_path = 'model/x-fresh.ann'
annoy_dim = 4096

base_model = VGG16(weights="imagenet")
model = Model(inputs=base_model.input,
              outputs=base_model.get_layer("fc2").output)

annoy_model = AnnoyIndex(annoy_dim)

for i in range(1, 2156):
    img_path = img_dir_path + str(i) + '.jpg'
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    fc2_features = model.predict(x)

    annoy_model.add_item(i, fc2_features[0])
    print(img_path, 'saved')

annoy_model.build(2155)
annoy_model.save(annoy_model_path)
