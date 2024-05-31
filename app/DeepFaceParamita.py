from deepface import DeepFace
import pandas as pd
import numpy as np
import sys
from statistics import fmean

import logging,traceback

def df_verify(img, listImg):
  try :
    #loop by images already stored in the database
    listDist = []
    if len(listImg) < 10 :
      listImg = listImg[:len(listImg)]
    else :
      listImg = listImg[:10] # set to take n data only
    for imgs in listImg:
      result = DeepFace.verify(
          img1_path = img,
          img2_path = imgs,
          model_name = 'VGG-Face',
          distance_metric = 'cosine',
          detector_backend = 'opencv',
          # threshold= 0.68 # default threshold for cosine metric         
      )
      listDist.append(result['distance'])
      
    fmeanResult = fmean(listDist)
    accrcy  = (1 - fmeanResult) * 100
    if accrcy <= 60 :
      return {
        'code' : 200,
        'results' : False
        }
    else : 
      return {
        'code' : 200,
        'results' : True
        } # successful face recognition if result > 60%
  except Exception as ex :
    return {
      'code' : 400,
      'result' : False,
      'message' : str(ex)
    }