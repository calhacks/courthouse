ANNOTATOR_ID = 'annotator_id'
SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"

# Setting
# keys
# SETTING_WAVE = '0' # boolean
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
# these can be overridden via the config file
DEFAULT_WELCOME_MESSAGE = '''
Welcome to the judging portion of the hackathon.

**Please read this important message carefully before continuing.**

Courthouse is a fully automated judging system that both 
tells you where to go and collects your votes.

You will be able to judge your floor's projects on Courthouse.

The system is based on the model of pairwise comparison. You'll start off by
looking at a single submission, and then for every submission after that,
you'll decide whether it's better or worse than the one you looked at
**immediately beforehand**.

If at any point, you can't find a particular submission, you can click the
'Skip' button and you will be assigned a new project. **Please don't skip
unless absolutely necessary.**

Courthouse makes it really simple for you to submit votes, but please think hard
before you vote. **Once you make a decision, you can't take it back**.
'''.strip()

DEFAULT_EMAIL_SUBJECT = '[IMPORTANT] Hackathon Judging Information'

DEFAULT_EMAIL_BODY = '''
Hi {name},

Thanks for volunteering at the hackathon!

Judging will be done using Courthouse, an online platform for expo judging built
by the Cal Hacks team. 

To access the system, visit {link}.

DO NOT SHARE this email with others, as it contains your personal magic link.

Once you're in, please take the time to read the welcome message and
instructions before continuing.
'''.strip()

DEFAULT_CLOSED_MESSAGE = '''
The judging system is currently closed. Reload the page to try again.
'''.strip()

DEFAULT_DISABLED_MESSAGE = '''
Your account is currently disabled. Reload the page to try again.
'''.strip()

DEFAULT_LOGGED_OUT_MESSAGE = '''
You are currently logged out. Open the magic link emailed to you to get started.
'''.strip()

DEFAULT_WAIT_MESSAGE = '''
We couldn't find a project for you to judge.

Wait for a little bit and reload the page to try again.

If you've looked at all the projects already, then you're done.
'''.strip()
