#Load classifier and assign to each crop the predicted species
import tensorflow as tf
from django.conf import settings
from tensorflow.python.keras.models import Model, load_model
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
from tqdm import tqdm


def classify():

    model = load_model(os.path.join(settings.BASE_DIR,'mlApi','mlFunc','models','LightNet_classification_mixed.hdf5'))

    model.compile(
        optimizer=tf.keras.optimizers.Adam(lr=1e-4),
        loss='categorical_crossentropy',
        metrics=['accuracy'],
   )


    # The right species of all crops from this test is Falciparum
    test_path = os.path.join(settings.BASE_DIR,'media','crops')


    test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255,
                                                                   samplewise_center=True,
                                                                   samplewise_std_normalization=True)  # preprocessing_function=preprocess_input

    file_list = os.listdir(test_path)
    plasmodium = ['Falciparum', 'Malariae', 'Ovale', 'Vivax','Negative']
    for file_name in file_list: #tqdm
    
        #original image reading
        #print(file_name)
        full_path = os.path.join(test_path, file_name)
        img= cv2.imread(full_path)
        img_rgb = cv2.resize(img, (224, 224), interpolation = cv2.INTER_LINEAR) 
        img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
        x = np.expand_dims(img_rgb, axis=0)
    
        test_iterator = test_datagen.flow(x,batch_size=1)
        x = test_iterator.next()
        result = model.predict(x, verbose=0)
    
        index = np.argmax(result,-1) # get class index of max value
        return (plasmodium[index[0]]) 