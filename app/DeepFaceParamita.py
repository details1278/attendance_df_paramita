from deepface import DeepFace
from statistics import fmean

import logging,traceback

def df_extract_face(img):
  try : 
    face_obj = DeepFace.extract_faces(img_path= img)
    if face_obj is None :
      return None
    else : 
      return face_obj
  except : 
    return None

def df_verify(img, listImg):
  try :
    # declare empty accrcy
    accrcy = 0.0
    fmeanResult = 0.0

    #loop by images already stored in the database
    listDist = []
    listImg2 = []
    if len(listImg) < 10 :
      listImg = listImg[:len(listImg)]
    else :
      listImg = listImg[:10] # set to take n data only

    face_obj_img = df_extract_face(img)
    if face_obj_img is None:
        return {
          'code' : 400,
          'result' : False,
          'message' : "Face not detected in the image provided."
          }
    else : 
      for imgs in listImg:
        face_obj = df_extract_face(imgs)
        if face_obj is None : 
          continue
        else : 
          listImg2.append(imgs)
      if len(listImg2) == 0:
        listImg2.append(img) # append clock in image if listImg2 is empty
      for imgs in listImg2:
        result = DeepFace.verify(
            img1_path = img,
            img2_path = imgs,
            model_name = 'VGG-Face',
            distance_metric = 'cosine',
            detector_backend = 'opencv',
            normalization = 'VGGFace',
            # threshold= 0.68 # default threshold for cosine metric         
        )
        if result['distance'] < 0 and result['verified'] == True:
          # update distance as 0.0 if verified = True and distance below zero
          result['distance'] = 0.0
        listDist.append(result['distance'])

      if len(listDist) > 0 :
        fmeanResult = fmean(listDist)
        accrcy  = (1 - fmeanResult) * 100      
      else:
        accrcy = 0.0

      if accrcy <= 35:
        return {
          'code' : 200,
          'accuracy' : accrcy,
          'results' : False
          }
      else : 
        return {
          'code' : 200,
          'accuracy' : accrcy,
          'results' : True
          } # successful face recognition if result > 60%
  except Exception as ex :
    return {
      'code' : 400,
      'result' : False,
      'message' : str(ex)
    }