from django.shortcuts import render_to_response, RequestContext
import api.call

# Create your views here.
def index(request, candidateId):
    # instantiate calls.Call object
    apiCall = api.call.Call()
    
    '''
    Verify username is an integer
    Make API call to get the profile information for a Candidate.
    Pass in candidateId
    JSON array will be returned
    '''
    if int(candidateId):
        profile = apiCall.getProfile(candidateId)
    else:
        profile = {"errorCode":True, 'errorMsg':'User not found.'}

    #profile = apiCall.getProfile(username)  
    
    # return data to template   
    return render_to_response('candidate_index.html', {'profileData': profile}, context_instance = RequestContext(request))