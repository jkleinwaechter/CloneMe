import re


################################################################################
# buildResponse - reate fully formed response card
#   Input:
#       session_attributes - The session_attributes of the
#           fully formed response card
#       speechlet_response - the voice portion of the
#           fully formed response card
#   Output:
#       Fully formed response card. This can be sent back to Alexa
################################################################################
def buildResponse(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }


################################################################################
# buildSpeechletResponse - build the response part of the response caard
#   Input:
#       title - text placed on title of card
#       output - the voice response that will also be used in the card body (SSML/w/o speak tags)
#       reprompt - text to use for open session that are not completed
#       shouldEndSession - Boolean indicating wheter to close session or not
#   Output:
#       Fully formed "response" portion of a card.  Note this is not the full card
################################################################################
def buildSpeechletResponse(title, output, reprompt="Knock Knock", shouldEndSession=True):

    # add the speak tag around the object so that the incoming text can be pure text or ssmal.
    voice = "<speak>" + output + "</speak>"  # Using SSML, but we will take care of encloising the string in a speak tag

    # Strip out ssml so we can print to the card
    cleanr = re.compile('<.*?>')
    cleanOutput = re.sub(cleanr, '', output)

    return {
        "outputSpeech": {
            "type": "SSML",
            "ssml": voice
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": cleanOutput
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt
            }
        },
        "shouldEndSession": shouldEndSession
    }


################################################################################
# buildPermsNeededResponse - Handle getting permissions from user
#   Input:
#       output - the string you would like read to the user in SSML.
#   Output:
#       Fully formed "response" portion of card. Note this is not the full card
################################################################################
def buildPermsNeededResponse(output):

    return {
        "outputSpeech": {
            "type": "Simple",
            "ssml": "You need permissions set in your Alexa app"
        },
        "card": {
            "type": "AskForPermissionsConsent",
            "permissions": ["read::alexa:household:list"]
        },
        # "shouldEndSession": True
    }
