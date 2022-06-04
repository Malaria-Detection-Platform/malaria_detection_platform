from distutils.command.upload import upload
from django.db import models
from django.conf import settings
import shutil
import glob 
from .mlFunc import one,two,three,four,five
import os
from PIL import Image
# Create your models here.

class malaria(models.Model):
    cellImage = models.ImageField(upload_to='cellImages')
    result = models.CharField(max_length=200, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)

    def save(self, *args, **kwargs):
        cellimage = str(self.cellImage)
        cell = Image.open(self.cellImage)
        #cellimage = "Trip 017 Day 1 19-10-05 Image 15 add_1.png"
        # print(os.path.join(settings.BASE_DIR,'media','cellImage',str(cellimage)))
        # src_path = os.path.join(settings.BASE_DIR,'media','cellImage',str(cellimage))
        dst_path = os.path.join(settings.BASE_DIR,'media','img',str(cellimage))
        cell.save(dst_path, 'PNG')
        print("saved to media/img")
        one.binarymaskgeneration()
        two.maskresize()
        newname = three.contours()
        four.crop()
        result = five.classify()
        print("this is the result")
        print(result)
        self.result = result
        os.remove(os.path.join(settings.BASE_DIR,"media","contours",str(newname)))
        os.remove(os.path.join(settings.BASE_DIR,"media","img",str(cellimage)))
        os.remove(os.path.join(settings.BASE_DIR,"media","predict",str(cellimage)))
        if(os.path.exists(os.path.join(settings.BASE_DIR,"media","crops",str(cellimage)))):
            os.remove(os.path.join(settings.BASE_DIR,"media","crops",str(cellimage)))
        # print("removed")
        # print(os.path.join(settings.BASE_DIR,"media","contours"))
        # print(glob.glob(os.path.join(settings.BASE_DIR,"media","contours")))
        # files = glob.glob(os.path.join(settings.BASE_DIR,"media","contours"))
        # for f in files:
        #     os.remove(f)    
        # files = glob.glob(os.path.join(settings.BASE_DIR,"media","img"))
        # for f in files:
        #     os.remove(f)    
        # files = glob.glob(os.path.join(settings.BASE_DIR,"media","predict"))
        # for f in files:
        #     os.remove(f)    
        # files = glob.glob(os.path.join(settings.BASE_DIR,"media","crops"))
        # for f in files:
        #     os.remove(f)    
        return super().save(*args, **kwargs)