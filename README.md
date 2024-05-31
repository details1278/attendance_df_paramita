# attendance_df_paramita
Attendance System for Paramita

Endpoint : /face_verify
1.  Body data ( JSON Format) : 
    {
        "userId": "example-user-id",
        "accessToken": "exampleAccessToken",
        "imageUrl" : "exampleImageUrl",
    }
2.  Expected Results :
    a. Success :
      {
        'code' : 200,
        'results' : True
      }
    b. Failed :
      {
        'code' : 200,
        'results' : False
      }
    c. Unexpected error from the Face Reco(bad input / image not detected / any unexpected results) : 
    {
        'error' : 400,
        'result' : False,
        'message' : "Example error"
    }
    d. Unexpected error () from API : 
    {
        'code' : 500,
        'result' : False,
        'message' : "Example error"
    }