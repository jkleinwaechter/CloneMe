import globals


##############################################################################################################
# These functions respresent all of the Alexa phrases that can be communicated for any exception processing
##############################################################################################################


################################################################################
#  insufficientPermisiion - need perms set
#   Input:
#       none
#   Output:
#       (string) - Response string
#################################################################################
def insufficientPermission():
    if globals.debug is True:
        print "Insufficient perms"
    return('I need to have permission to access your list.')


################################################################################
#  invalidItemNumber - item is not a number
#   Input:
#       none
#   Output:
#       (string) - Response string
#################################################################################
def invalidNumber():
    if globals.debug is True:
        print "Invalid number requested"
    return ('I\'m sorry, I do not recognize your request. I only understand numbers as an option. ')


################################################################################
#  help- provide help on the app
#   Input:
#       none
#   Output:
#       (string) - Response string
#################################################################################
def help():
    if globals.debug is True:
        print "Help requested - now with add txt"
        return ('You need help with ' + globals.alexaSkillName + ' and apparenly I haven"t written it yet')
