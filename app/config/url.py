# global var
host = 'https://be-core.paramitaban.com'

def getPhotoAbsences():
    ep = '/api/users/photo-absences'
    url = host + ep
    return url