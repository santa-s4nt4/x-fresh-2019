from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D, Input
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
from keras.callbacks import CSVLogger

n_categories = 26
batch_size = 32
train_dir = ''
validation_dir = ''
file_name = 'x-fresh'

base_model = VGG16(
    include_top=False,
    weights="imagenet",
    input_shape=None
)
base_model.summary()

'''
base_model = VGG16(weights='imagenet', include_top=False,
                   input_tensor=Input(shape=(224, 224, 3)))

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
prediction = Dense(n_categories, activation='softmax')(x)
model = Model(inputs=base_model.input, output=prediction)

for layer in base_model.layer[:15]:
    layer.trainable = False

model.compile(optimizer=SGD(lr=0.0001, momentum=0.9),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

validation_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True
)

hist = model.fit_generator(train_generator,
                           epochs=200,
                           verbose=1,
                           validation_data=validation_generator,
                           callbacks=[CSVLogger(file_name + '.csv')])


model.save(file_name+'.h5')
'''
