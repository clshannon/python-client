import requests

class Call:
    # Holds the API main site URL
    endpointHost = 'http://api-recruit-builders.papscnt.com:10088'
    
    # Holds specific API endpoint urls
    endpointProfile = '/api/profile/%s'
    endpointDashboard = '/api/dashboard/%s'
    endpointNotes = '/api/notes/%s'
    endpointSpecificNote = '/api/notes/%s/%d'
    endpointUsers = '/api/users';
    endpointGetUser = '/api/users/%s';
    endpointUserLogin = '/api/users/login';    
    
    """Holds the endpoint urls"""
    def __init__(self, method='GET'):
        self.method = method
        
    def doRequest(self, url):
        try:
            response = requests.get(url)
            return (response.json()) 
        except:
            # catastrophic error. bail.    
            return {"errorCode":404, 'errorMsg':'Bad URL. Try again.'}
        
    def getProfile(self, candidateId):
        url = self.endpointHost + self.endpointProfile % (candidateId)
        return self.doRequest(url)
        
    def getDashboard(self, userId):
        url = self.endpointDashboard % (userId)
        return self.doRequest(url)