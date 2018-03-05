# Basic Alexa Skill Template for Python
Most of the templates within the Alexa Skills platform are in node.js. Those that are in python are fully formed apps that don't align with the new ASK CLI structure, leaving you the task of reforming that.

This is a bare bones template that you can use for python. It is a functioning skill, that does nothing useful other than providing the basic interaction functions required for a skill. It is organized and populated with the elements required for using the Alexa Skill Kit Command Line Interface (ASK CLI) automation commands. The opther advantage is that I have included optinal files to get you going in making HTTP/REST calls as that is a very common situation in many skills.

I am assuming you have a basic knowledge of setting up an Alexa environment, including associated Lambda functions. If not, I highly recommend this awesome CloudGuru [introductory course](https://acloud.guru/course/intro-alexa-free/dashboard). It is also expected that you have installed and configured your ASK CLI environment. If not, here's a great [step-by-step tutorial](https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html).

### A Note About Names
It is easy to get crossed up the the different naming conventions used in ASK development. There are basically three separate names:

* **Skill Name** - This is the name that will be used when you publish your skill. While it can be anything you want, it should be two or three words, separated by spaces. This is so that there is a close tie between your app name and the *Invocation Name*, discussed next.
* **Invocation Name** - This is the phrase that will be used to invoke your app by the user. In order to pas certification you will need to use two or more words, separated by a space and have no capitalization. Keep this short so that you don't burden the user. It is highly recommended that your *Skill Name* match your *Invocation Name*, without the capital letters, again to avoid confusing the user.
* **Function Name** - This is the name of the Lambda function that will host your skill's code. The function name must contain only letters, numbers, hyphens, or underscores. This makes it impossible for your *Skill Name*, *Invocation Name*, and *Function Name* to be the same words.

My personal convention is to simply remove the spaces from my *Skill Name* and then use camel case for the function name.
Defaults for this template:

* Skill Name: *My Skill*
* Invocation Name: *my skill*
* Function name: *mySkill*

This is ridiculous. Tell Amazon.

## ASK CLI template
Even though this is a GitHub repository, there is no need to clone this directory in the traditional fashion. It exists here to enable the ASK CLI to clone on to your system. Just follow the steps below.

1. Change directories to the location where you want the project to exist.
2. Run the following ASK CLI command. Make sure you replace 'Your Skill' with your *Skill Name*.
  * ```ask new --template CloneMe --url https://s3.amazonaws.com/jk-ask/templates.json --skill-name "my skill" ``` 
3. Make the following pre-deployment edits:

  * **./.ask/config** - Change the value associated "uri" to your *Function Name*.
  * **./skill.json** - Change the value associated with *"name"* to your *Invocation Name*. 
4. **ask deploy** - This will send the model and code to the Alexa and Lambda servers.
5. Make the following post-deployment edits:
  * **AWS Lambda** - Go to your skill's lambda instance and set 'Runtime' to *Python 2.7*, 'Handler' to *main.entryPoint*, and save. I told you Python wa a second class citizen.
  * **./lambda/custom.globals.py** - Two changes required here. Change the value associated with alexaSkillName to your *Skill Name*. Change the skillID to match your skill. You can copy and paste this from the *./.ask/config* file's *skill_id* attribute.

6. **ask deploy -t lambda** - This will cause your newly edited code to be put back in place on lambda

Now you can make all the changes to the model or the code on your local system. Whenever you are ready to put the changes on the server just **ask deploy**. Note that this will put everything and cause you to wait for the model to be built. Since this can sometimes be lengthy, if you are just replacing the code and not changing the model, just use **ask deploy -t lambda** instead. It will be much faster.

## STRUCTURE
### Directory Structure
The code is organized to be in a format that can be used by the AWS CLI. This will be handy if you decide to go down that path later.

* **./lambda/**  - This contains the code that is placed in AWS Lambda. Note that the vast majority of code here are Python libraries that Lambda does not include. It is a rather painful process to determine what lbraries Lambda does not support, but these seem to be the most common ones. Most of these are only needed if you are making REST calls within your app. I would recommend keeping them until you decide you don't need them.
* **./models/** - This contains the JSON that is used in defining the interactionmodel within ASK.
* **./skill.json** - This your your skill's manifest. It contains the publishing information for your application. When using the ASK CLI, it will populate all of the fields in the publishing section of the ASK developer console. 

### Lambda Files
* ***main.py*** - entry point for lambda execution. Everything routes from here. When you add new intents, you put the intent name in here and put tha corresponding handler function in intents.py

* ***intents.py*** - Place all of your intent handlers in here.I highly recommend keeping this file just for the entry ppints of all of the intents and placing corresponding business logice in a seaparate file.

* ***globals.py*** - All global variables

* ***responses.py*** - I put all of my output phrases in here so that I can always look at them and adjust the dialog to be consistent.

* ***exceptionTypes.py*** - This contains all of the exception classes used for Try/Except processing

* ***transact.py*** - This is an optional module that allows you to make rest calls back to Alexa. This is handy for list processing, retrieiving location information, and several other functions. It is not used by default. Just uncomment the include within intents.py to enable it.

The following are python modules that are added mostly so that you can use the Requests library to make API calls. If you use the transact.py file listed above to incorporate API calls, you will need these modules. If not, you may safely delete them.

* ***certifi/***
* ***chardet/***
* ***idna/***
* ***requests/***
* ***urllib3/***
* ***pkg_resources.py***


## Helpful ASK CLI commands

* **ask deploy**  (does everything)
* **ask deploy -t lambda**  (code only)
* **ask deploy -t model** (model only)
* **ask lambda log -f "CloneMe"** (retrieves latest log)
* **ask lambda log -f "CloneMe" --start-time "1monthago"**
* **ask api list-skills** (list all of your skills)
* **ask simulate -t "ask clone me"** (simulate a voice command)
* **ask simulate -f phrases.txt**  (file of phrases to test)

Note: set *ASK\_DEFAULT\_DEVICE\_LOCALE* environment variable to "en-US" in your shell startup script. If not, many of the ASK CLI commands will require you to use the --locale "en-US" flag on the command line.

For more information

[Installing the ASK CLI](https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html)

[ASK CLI reference] (https://developer.amazon.com/docs/smapi/ask-cli-command-reference.html)

[CloudGuru free introductory course for building Alexa skills](https://acloud.guru/course/intro-alexa-free/dashboard)

[Other Alexa templates from Amazon](https://github.com/alexa)
