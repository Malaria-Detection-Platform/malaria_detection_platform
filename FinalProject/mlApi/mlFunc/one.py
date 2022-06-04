#Parasite Segmentation: binary mask generation 
import tensorflow as tf
from django.conf import settings
import segmentation_models as sm
import os
import cv2
import numpy as np
from tqdm import tqdm

def binarymaskgeneration():

    sm.set_framework('tf.keras')

    model = sm.Unet('vgg19',encoder_weights = None )
    model.load_weights(os.path.join(settings.BASE_DIR,'mlApi','mlFunc','models','vgg19_color_ntl_dataset12_shuffle_nocrops_augmented.hdf5'))

    model.compile(
        optimizer=tf.keras.optimizers.Adam(lr=1e-4),
        loss=sm.losses.bce_jaccard_loss,
        metrics=[sm.metrics.iou_score],
    )


    test_path = os.path.join(settings.BASE_DIR,'media','img')
    predict_path = os.path.join(settings.BASE_DIR,'media','predict')

    test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255,
                                                                   samplewise_center=True,
                                                                   samplewise_std_normalization=True)  # preprocessing_function=preprocess_input

    file_list = os.listdir(test_path)

    for file_name in tqdm(file_list):
    
        #original image reading
        full_path = os.path.join(test_path, file_name)
        img= cv2.imread(full_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_rgb = cv2.resize(img_rgb, (224, 224), interpolation = cv2.INTER_LINEAR) 
        x = np.expand_dims(img_rgb, axis=0)
    
        test_iterator = test_datagen.flow(x,batch_size=1)
        x = test_iterator.next()
        result = model.predict(x, verbose=0)
        result = np.squeeze(result, axis=0)
        result = np.where(result > 0.5, 255, 0)
        #save predicted mask
        full_path = os.path.join(predict_path, file_name)
        cv2.imwrite(full_path, result)