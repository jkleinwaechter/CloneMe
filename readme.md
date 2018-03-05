# Basic Alexa Skill Template for Python
Most of the templates within the Alexa Skills platform are in node.js. Those that are in python are fully formed apps that don't align with the new ASK CLI structure, leaving you the task of reforming that.

This is a bare bones template that you can use for python. It is a functioning skill (that does nothing useful) that provides the basic interaction functions required for a basic skill and is organized and populated with the elements required for using the ASK CLI.

There are several ways you can clone and own this. All of these require knowledge of how to setup an Alexa skill and also require you to have a working Amazon developer account as well as an AWS account. If you are not familiar with how to do this, check out this awesome CloudGuru [introductory course](https://acloud.guru/course/intro-alexa-free/dashboard).

Also note that if you elect options 2 or 3, you will need to install and have knowledge of using the Alexa Skill Kit Command Line Interface (ASK CLI) and have installed the Amazon Web Services Command Line Interface (AWS CLI). While this is more initial work, you will be one step closer to a fully automatable ASK development process.

  1. GitHub (manual)
  2. Alexa Skill Kit (ASK) Command Line Interface (CLI) template
  3. ASK CLI clone command
 
## 1. GitHub (manual)
If you don't want to learn the ASK CLI, this process can get you to a working skill. I recommend that you do learn the ASK CLI at some point as it will make the development process much easier.
### Steps

  1. Clone this repository
  2. Make the edits noted in the Edits section below
  3. Create your AWS Lambda function
  4. Zip up the lambda directory and upload it. Only include the files within the directory and not the directory itself!
  5. Create a new Alexa skill
  6. Copy the JSON within ./models/eh-US.json to the JSON editor of ASK model builder,
  7. Fill in the ARN of your lambda app into the Endpoint section of the ASK model builder

## 2. ASK CLI template
If you have already setup the ASK CLI, this is the easiest and fastest way to get started. You don't need to clone this library - the template will pick it up for you.

1. Change to the location where you want the project to exist.
2. Run the following ASK CLI command. Make sure you replace 'YourSkillName' with your project name. ```ask new --template CloneMe --url https://s3.amazonaws.com/jk-ask/templates.json --skill-name YourSkillName ``` 
3. Customize your skill to your satsifaction
4. **ask deploy** - this will send the model and code to the Alexa and Lambda servers.



## 3. ASK CLI clone command
This method is still a viable option, however it is rather outdated now that the ASK CLI new command has the template option noted above.

This option is used when you have already loaded the CloneMe projet into ASK and Lmabda and want to use it to create a new project from that base.

Once you have your skill in your system, I recommend leaving it as a template for your future apps. Customize it to how you want it and then you can use the clone command to replicate it.

These steps assume you have have [installed the ASK CLI](https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html)

### Steps
* 1. ***ask clone*** - from here select the CLoneMe project that you have previosuly loaded using one of the options above.
* 2. Make the edits noted in the Edits section below before republishing. Note that especially critical is the edits within the hidden directory *./.ask*.
* 3. ***ask deploy*** - This will commit your code the the servers.

See the [ASK CLI reference] (https://developer.amazon.com/docs/smapi/ask-cli-command-reference.html) for more information on command options.

## STRUCTURE
### Directory Structure
The code is organized to be in a format that can be used by the AWS CLI. This will be handy if you decide to go down that path later.

* **./lambda/**  - This contains the code that is placed in AWS Lambda. Note that the vast majority of code here are Python libraries that Lambda does not include. It is a rather painful process to determine what lbraries Lambda does not support, but these seem to be the most common ones. Most of these are only needed if you are making REST calls within your app. I would recommend keeping them until you decide you don't need them.
* **./models/** - This contains the JSON that is used in defining the interactionmodel within ASK.
* **./skill.json** - This file contains the publishing information for your application. When using the ASK CLU, it will populate all of the fields in the publishing section of the ASK developer console. 

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

## EDITS
When reusing this template, there are are a number of edits you will need to make before deploying your new skill.

### .ask/config
These edits are crucial when cloning a project. When you clone a project, these get set to point back to yoour existing lambda function. You need to change these to ensure that when you deploy, it goes in a s a new skill and function

* skill_id = ""
* was_cloned = false
* uri = "New Skill Name"

### skill.json
This is the manifest used for publishing. Fill it in accordingly
### models/en-US.json
This is the interaction model for your app. Fill it in accordingly
### lambda/custom/globals
* alexaSkillName = "Skill Name"
* skillID = "Your AMZN skill id"


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
