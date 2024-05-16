from deepface import DeepFace
import pandas as pd
import numpy as np
import os

import logging,traceback

#
# FUNCTION DEEPFACE VERIFY
#
def deepface_verify(img1_path, img2_path):
  try :
    if not img1_path :
      raise ValueError('Attendance image path is empty')
    else :
      result = DeepFace.verify(
        img1_path = img1_path,
        img2_path = img2_path,
        model_name = 'VGG-Face',
        distance_metric = 'euclidean_l2',
        detector_backend = 'opencv',
      )

      return result
  except (RuntimeError, TypeError, NameError) as ex:
    return "Value error occured. Exception message: {}".format(ex)
  except Exception as ex:
    logging.error(traceback.format_exc())

def deepface_dist( img1, listImg): #need fix args 1
  listDistance = list()
  try :
    #to do, loop by images
    for img in listImg :
      print("Attendance image : {}, db image : {} ".format(img1,img))
      dist = deepface_verify(img1, img)
      listDistance.append(dist['distance'])
      print("Verified : {} \n Distance : {} \n Threshold {} ".format(dist['verified'],dist['distance'],dist['threshold']))
    return listDistance
  except Exception as ex:
    logging.error(traceback.format_exc())
    return "Exception message : {} ".format(ex)
  
  img_path = ''
listImg = []
listDist = []

def df_verify(img, listImg):
  try :
    #loop by images
    for imgs in listImg:
      result = DeepFace.verify(
          img1_path = img,
          img2_path = imgs,
          model_name = 'VGG-Face',
          distance_metric = 'euclidean_l2',
          detector_backend = 'opencv',
      )
      listDist.append(result['distance'])
    print('List Dist : {} '.format(len(listDist)))
  except Exception as ex :
    logging.error(traceback.format_exc())
    return "Exception message : {} ".format(ex)