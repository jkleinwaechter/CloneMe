import globals
import os
from intents import basicCall, basicCallWithSlot, getHelp, handleSessionEndRequest


# Make sure you list main.entryPoint as your entry point in your Lambda configuration page
def entryPoint(event, context):

    # See if environment string has debug turned on.
    if 'debug' in os.environ:
        globals.debug = True

    # Security check to ake sure that we are being called by the exepcted Alexa skill
    presentedId = event["session"]["application"]["applicationId"]
    if (globals.skillID != presentedId):
        if globals.debug is True:
            print "Invalid Application id %s. Expected %s" % (presentedId, globals.skillID)
        raise ValueError("Invalid Application ID")

    #
    # New Session Request
    #
    if event["session"]["new"]:
        if globals.debug is True:
            print "New Session Request"  # Stubbed here in case we do something eventually with this
        onSessionStarted(event["request"]["requestId"], event["session"])
    #
    # Launch Request
    #
    if event["request"]["type"] == "LaunchRequest":
        if globals.debug is True:
            print "Launch Request"
        return onLaunch(event["request"], event["session"], event["context"])

    #
    # Intent Request
    #
    elif event["request"]["type"] == "IntentRequest":
        if globals.debug is True:
            print "Intent Request"
        return onIntent(event["request"], event["session"], event["context"])
    #
    # Session End Request
    #
    elif event["request"]["type"] == "SessionEndedRequest":  # stubbed here in case we do something eventually with this
        if globals.debug is True:
            print "Session End Request"
        return onSessionEnded(event["request"], event["session"])


################################################################################
# onSessionStarted - New Session Request Handler
#   Input:
#       request - "request" object as provided by Alexa JSON request
#       session - "session" object as provided by Alexa JSON request
#   Output:
#       none
################################################################################
def onSessionStarted(request, session):
    if globals.debug is True:
        print "Starting new session."


################################################################################
# onIntent - Intent Requst Handler
#   Input:
#       request - "request" object as provided by Alexa JSON request
#       session - "session" object as provided by Alexa JSON request
#       context - "context" as provided by Alexa JSON reuest
#   Output:
#       none
################################################################################
def onIntent(request, session, context):
    intent = request["intent"]  # passed on to functions that have slots
    intentName = intent["name"]
    system = context["System"]

    if globals.debug is True:
        print "_______________________________________________________________"
        print "starting %s()" % intentName
        print "_______________________________________________________________"

    if intentName == "BasicCall":
        return basicCall(system)
    elif intentName == "BasicCallWithSlot":
        return basicCallWithSlot(system, intent)
    elif intentName == "AMAZON.HelpIntent":
        return getHelp(request, session)
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")


################################################################################
# onLaunch - Launch Requst Handler.
#   Input:
#       request - request object from Alexa
#       session - session object from Alexa
#       contexxt = context object from Alexa
#   Output:
#       none
################################################################################
def onLaunch(request, session, context):
    system = context["System"]
    # Currently configured so that if a user launcehs our app, we will do the same
    # as invoking the app intent with no parameters
    return basicCall(system)


################################################################################
# onSessionEnded - Session End Request Handler for nomral endings
#   Input:
#       request - "request" object as provided by Alexa JSON request
#       session - "session" object as provided by Alexa JSON request
#   Output:
#       none
################################################################################
def onSessionEnded(request, session):
    if globals.debug is True:
        print "Ending session."
