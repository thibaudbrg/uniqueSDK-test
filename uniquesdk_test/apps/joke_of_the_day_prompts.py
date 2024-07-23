# joke_of_the_day_prompts.py

# System prompt to instruct the model
JOKE_OF_THE_DAY_SYSTEM_PROMPT = """
You are a highly creative and humorous assistant whose job is to generate jokes to lighten up the user's day. 
Your jokes should be clever, witty, and family-friendly. Always ensure your jokes are appropriate for all audiences.
"""

# Trigger prompt to start the joke generation
JOKE_OF_THE_DAY_TRIGGER_PROMPT = """
{USERMESSAGE}
You: That's a good one! How about this for a laugh?
{PERSON}: Oh, I can't wait to hear it!
"""

# Example jokes for reference or direct use
EXAMPLE_JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you get if you cross a snowman and a vampire? Frostbite!",
    "Why don’t skeletons fight each other? They don’t have the guts."
]

def get_random_joke():
    import random
    return random.choice(EXAMPLE_JOKES)
