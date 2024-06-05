from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import requests

# import local files
from app.config import auth as Config
from app.config import exceptions as BusinessException
from app.config import url as url
from app import DeepFaceParamita as DFP

app = Flask(__name__)

#  { start request parser for face verification
parser_verify = reqparse.RequestParser()
parser_verify.add_argument(
    'userId',
    type = str,
    help = 'User ID cannot be empty.',
    required = True)

parser_verify.add_argument(
    'accessToken',
    type = str,
    help = 'Access token cannot be empty.',
    required = True)

parser_verify.add_argument(
    'imageUrl',
    type = str,
    help = 'Image URl cannot be empty.',
    required = True)
#  end request parser }

# set headers for api requests
headers = {
    "Content-Type": "application/json",
    "accept" : "application/json"
}

@app.route('/')
def index(): 
    return '''
        <h1>Hello, World!</h1>
        <h2>Paramita Ban</h2>
        <p>This is the attendance system for Paramita Ban</p>
    '''

@app.route('/face_verify', methods=['POST'])
# login and get refresh token
def face_verify():
    try:
        args = parser_verify.parse_args() # get input data from JSON body
        if request.method == 'POST':
            responseAbsence = requests.get(
                url= url.getPhotoAbsences(),
                auth= Config.BearerAuth(str(args['accessToken'])),
                headers= headers,
                params= {'userId':args['userId']}
            )
            JSONString = responseAbsence.json()
            # imageBaseUrl = JSONString['data']['imageBaseUrl'] # single image of the person
            imageBaseUrl = args['imageUrl'] # single image of the person
            imageAbsenceLast = JSONString['data']['imageAbsenceLast'] # recent 30 images
            
            if JSONString['statusCode'] == 200:
                result = DFP.df_verify(imageBaseUrl, imageAbsenceLast)
                return result
            else :
                raise BusinessException(str(JSONString['message'], JSONString['statusCode']))
        else:
            raise BusinessException('Method not allowed.', 405)
    except (Exception,ValueError,BusinessException) as ex:
        return {
            'code' : 500,
            'result' : False,
            'message' : str(ex)
        } # set return as false
    
if __name__ == "__main__":
    with app.app_context():
        app.run(host="0.0.0.0", port=5000, debug=True)