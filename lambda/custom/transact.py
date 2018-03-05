from json import loads, dumps
import time
import requests
import globals
from exceptionTypes import ExProviderFailure, ExInsufficientPermission


################################################################################
# performAlexaTransaction
#   Input:
#       endpoint - url of the REST endpoint
#       apiToken - API access token as provided by the original JSON request from Alexa
#       post - True if transaction is a Post. Otherwise a get (default)
#       dictBody - The body of the request(optional)
#   Output:
#       List object with all items on the list
#   Raises:
#       ExProviderFailure - something went wrong in the communication
#       ExInsufficientPermission - Skill does not have necessary permissions
################################################################################
def performAlexaTransaction(endpoint, apiToken, post=False, dictBody={}):

    # form header
    header = {'Authorization': "Bearer " + apiToken, 'Accept': 'application/json'}

    # Make the Alexa API call
    try:
        start = time.time()
        if dictBody == {}:
            if post is True:
                jsonResponse = requests.post(endpoint, headers=header)
            else:
                jsonResponse = requests.get(endpoint, headers=header)

            if globals.debug is True:
                print "______________OUR REQUEST____________________"
                print "Http header: %s" % header
                print "Endpoint: %s" % endpoint
                if post is True:
                    print "Post operation"
                else:
                    print "Get operation"
                print "jsonBody: n/a"
                print "_____________________________________________"
        else:
            jsonBody = dumps(dictBody)  # Convert payload dictionary to JSON
            if globals.debug is True:
                print "______________OUR REQUEST____________________"
                print "Http header: %s" % header
                print "Endpoint: %s" % endpoint
                if post is True:
                    print "Post operation"
                else:
                    print "Get operation"
                print "jsonBody: %s" % str(jsonBody)
                print "_____________________________________________"

            if post is True:
                jsonResponse = requests.post(endpoint, headers=header, data=jsonBody)
            else:
                jsonResponse = requests.get(endpoint, headers=header, data=jsonBody)

        globals.alexaTime = int((time.time() - start) * 1000)
        if globals.debug is True:
            print "Call took: %s ms" % globals.alexaTime

    except requests.exceptions.TooManyRedirects:
        raise ExProviderFailure("Too many redirects.")
    except requests.exceptions.ConnectionError:
        raise ExProviderFailure("Connection Error")
    except requests.exceptions.Timeout:
        raise ExProviderFailure("Timeout")
    except requests.exceptions.ConnectionError:
        raise ExProviderFailure("Could not connect.")
    except requests.exceptions.RetryError:
        raise ExProviderFailure("Retry failure")
    else:
        # if jsonResponse.status_code == requests.codes.ok:  # If result is good, convert to Dict and return
        if jsonResponse.ok is True:
            dictReturn = loads(jsonResponse.text)
            if globals.debug is True:
                print "______________ALEXA RESPONSE_________________"
                print dictReturn
                print "_____________________________________________"
            return dictReturn
        elif jsonResponse.status_code == 403:  # Forbidden (403) - indicates that the user has not enabled permissions.
            raise ExInsufficientPermission("Alexa device not allowing access to lists")
        else:
            raise ExProviderFailure("Alexa could not process request: " + str(jsonResponse.status_code) + " : " + jsonResponse.text)
