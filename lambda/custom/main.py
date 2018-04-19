'''----------------------------------------------------------------------------------------------
This is the main entry function and distributor for all Alexa invocations
----------------------------------------------------------------------------------------------'''

import globals
import os
from intents import basicCall, basicCallWithSlot, getHelp, handleSessionEndRequest


def entryPoint(event, context):
    '''----------------------------------------------------------------------------------------------
    The main entry point for an AWS Lambda function. Make usre you ist main.entryPoint as the starting
    point on your AWS page.

    Parameters
    ----------
        event : dict
            AWS event data. The dictionary representation of the Alexa JSON Request object
        context : dict
            AWS Lambda context object (unused)

    Returns
    -------
        dictionary
            The Alexa JSON Response object

    Notes
    -----
        https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html
        https://developer.amazon.com/docs/custom-skills/request-and-response-json-reference.html

    ----------------------------------------------------------------------------------------------'''

    # See if environment string has debug turned on.
    if 'debug' in os.environ:
        globals.debug = True

    # Security check to ake sure that we are being called by the exepcted Alexa skill
    if globals.skillID == '':
        if globals.debug is True:
            print 'SkillId checking disabled. Please add the skill id to globals.py to ensure secure calling.'
    else:
        presentedId = event['session']['application']['applicationId']
        if (globals.skillID != presentedId):
            if globals.debug is True:
                print 'Invalid Application id %s. Expected %s' % (presentedId, globals.skillID)
            raise ValueError('Invalid Application ID')

    #
    # New Session Request
    #
    if event['session']['new']:
        if globals.debug is True:
            print 'New Session Request'  # Stubbed here in case we do something eventually with this
        onSessionStarted(event['request']['requestId'], event['session'])
    #
    # Launch Request
    #
    if event['request']['type'] == 'LaunchRequest':
        if globals.debug is True:
            print 'Launch Request'
        return onLaunch(event['request'], event['session'], event['context'])

    #
    # Intent Request
    #
    elif event['request']['type'] == 'IntentRequest':
        if globals.debug is True:
            print 'Intent Request'
        return onIntent(event['request'], event['session'], event['context'])
    #
    # Session End Request
    #
    elif event['request']['type'] == 'SessionEndedRequest':  # stubbed here in case we do something eventually with this
        if globals.debug is True:
            print 'Session End Request'
        return onSessionEnded(event['request'], event['session'])


def onSessionStarted(request, session):
    '''----------------------------------------------------------------------------------------------
    Process an Alexa New Session Request

    Parameters
    ----------
    request : dictionary
        The 'request' section of the Alexa JSON Request object
    session : dictionary
        The 'session' section of the Alexa JSON Request object

    Returns
    -------
    none

    ----------------------------------------------------------------------------------------------'''
    if globals.debug is True:
        print 'Starting new session.'


def onIntent(request, session, context):
    '''----------------------------------------------------------------------------------------------
    Process an Alexa Intent Request

    Parameters
    ----------
        request : dictionary
            The 'request' section of the Alexa JSON Request object
        session : dictionary
            The 'session' section of the Alexa JSON Request object
        context : dictionary
            The 'context' section of the Alexa JSON Request object

    Returns
    -------
        dictionary
            The Alexa JSON Response object

    Raises
    ------
        ValueError
            Invalid intent
    ----------------------------------------------------------------------------------------------'''

    intent = request['intent']  # passed on to functions that have slots
    intentName = intent['name']
    system = context['System']

    if globals.debug is True:
        print '_______________________________________________________________'
        print 'starting %s()' % intentName
        print '_______________________________________________________________'

    if intentName == 'BasicCall':
        return basicCall(system)
    elif intentName == 'BasicCallWithSlot':
        return basicCallWithSlot(system, intent)
    elif intentName == 'AMAZON.HelpIntent':
        return getHelp(request, session)
    elif intentName == 'AMAZON.CancelIntent' or intentName == 'AMAZON.StopIntent':
        return handleSessionEndRequest()
    else:
        raise ValueError('Invalid intent')


def onLaunch(request, session, context):
    '''----------------------------------------------------------------------------------------------
    Process an Alexa Launch Request. This is used when an Alexa skill is invoked with no parameters

    Parameters
    ----------
        request : dictionary
            The 'request' section of the Alexa JSON Request object
        session : dictionary
            The 'session' section of the Alexa JSON Request object
        context : dictionary
            The 'context' section of the Alexa JSON Request object

    Returns
    -------
        dictionary
            The Alexa JSON Response object

    ----------------------------------------------------------------------------------------------'''

    system = context['System']
    # Currently configured so that if a user launcehs our app, we will do the same
    # as invoking the app intent with no parameters
    return basicCall(system)


def onSessionEnded(request, session):
    '''----------------------------------------------------------------------------------------------
    Process an Alexa Session End Request. Not to be confused with a Stop or Cancel event.

    Parameters
    ----------
        request : dictionary
            The 'request' section of the Alexa JSON Request object
        session : dictionary
            The 'session' section of the Alexa JSON Request object

    Returns
    -------
        dictionary
            The Alexa JSON Response object

    ----------------------------------------------------------------------------------------------'''
    if globals.debug is True:
        print 'Ending session.'
