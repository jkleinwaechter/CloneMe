import globals
import responses
from cards import buildResponse, buildSpeechletResponse
from exceptionTypes import ExIndexOutOfBounds
# from transact import performAlexaTransaction


################################################################################
# handleSessionEndRequest - Process "Cancel" intent
#   Input:
#       none
#   Output:
#       Parting phrase
################################################################################
def handleSessionEndRequest():
    card_title = globals.alexaSkillName
    speech = "Grazie."
    shouldEndSession = True

    return buildResponse({}, buildSpeechletResponse(card_title, speech, None, shouldEndSession))


################################################################################
# getHelp - If allowing sessions, process a session start
#   Input:
#       request - "request" object as provided by Alexa JSON request
#       session - "session" object as provided by Alexa JSON request
#   Output:
#       Response card - Fully formed response card
################################################################################
def getHelp(request, session):
    session_attributes = {}
    card_title = globals.alexaSkillName
    reprompt_text = ""
    shouldEndSession = True

    if globals.debug is True:
        print "User asked for help."
    return buildResponse(session_attributes, buildSpeechletResponse(card_title, responses.help(), reprompt_text, shouldEndSession))


#############################################################################################
# basicCall - This is the intent handler for a basic call with no slots
#   Input:
#       system - "system" as provided in the intent request
#   Output:
#       fully formed respone card
#############################################################################################
def basicCall(system):

    card_title = globals.alexaSkillName
    reprompt_text = ""
    shouldEndSession = True
    session_attributes = {}

    # Put in code or call that will eventually fill the string 'speech' with the proper response
    # Use performAlexaTransaction() if you want to make calls to Alexa (lists, userinfo etc.)
    speech = "This page left intentionally blank."  # Code or call goes here

    return buildResponse(session_attributes, buildSpeechletResponse(card_title, speech, reprompt_text, shouldEndSession))


################################################################################
# basicCallWithSlot - This is the intent handler for a basic call with a slot
#   Input:
#       system - "system" as provided in the intent request
#       intent - "intent" object as provided by Alexa JSON request
#   Output:
#       Response card - Fully formed response card
################################################################################
def basicCallWithSlot(system, intent):

    session_attributes = {}
    card_title = globals.alexaSkillName
    reprompt_text = "Knock knock"
    shouldEndSession = True

    # Put in code or call that will eventually fill the string 'speech' with the proper response
    # Use the example in getNumericSlot to process a slot
    try:
        # Use performAlexaTransaction() if you want to make calls to Alexa (lists, userinfo etc.)
        requestedNumber = getNumericSlot(intent)
    except ExIndexOutOfBounds:
        speech = responses.invalidNumber()
    else:
        speech = "User asked for number " + str(requestedNumber)
    return buildResponse(session_attributes, buildSpeechletResponse(card_title, speech, reprompt_text, shouldEndSession))


################################################################################
# getNumericSlot
#   Input:
#       intent - "intent" object as provided by Alexa JSON request
#   Output:
#       (integer) - An integer of the slot number to use in the array (1 based)
#           0 indicates out of bounds
#   Raises:
#       ExIndexOutofBounds - could not detect a value
#################################################################################
def getNumericSlot(intent):

    # INDEX is the slot named in the model - change to match yours
    if "INDEX" in intent["slots"]:
        slot = intent["slots"]["INDEX"]
        if "value" in slot:
            value = slot["value"]
            return int(value)
        else:
            print 'No "value" in slot'
            raise ExIndexOutOfBounds(intent)
    else:
        print 'No "INDEX" in slot'
        raise ExIndexOutOfBounds(intent)
