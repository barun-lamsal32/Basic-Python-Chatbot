# Display welcome message
print("----------Welcome to chatbot AI----------")
print("You can ask me basic question, and type bye if you want to exit")

# Import required modules
import datetime
import time   # (not used now, but kept as-is)

# Get the current hour from system time
presenthour = datetime.datetime.now().hour

# Ask user for their name
name = input("\nHi!,What's your name: ")

# If user types bye as name, exit immediately
if name.lower() == "bye":
    print("---------Thank You!---------")
    exit()

# Greet user based on current time
elif 1 <= presenthour <= 11:
    print("Good Morning!,", name)

elif 12 <= presenthour <= 15:
    print("Good Afternoon!,", name)

elif 16 <= presenthour <= 19:
    print("Good Evening!,", name)

else:
    print("Good Night!,", name)

# Dictionary containing questions and their responses
responses = {
    "hello": "Hello! How can I help?",
    "hey": "Hey! How can I help?",
    "hi": "Hi! How can I help?",
    "good morning": "Good morning!",
    "good evening": "Good Evening!",
    "good afternoon": "Good Afternoon!",
    "what is your name": "I am a chatbot.",
    "what is your name?": "I am a chatbot.",
    "what's your name": "I am a chatbot.",
    "what's your name?": "I am a chatbot.",
    "who are you": "I’m your assistant.",
    "who are you?": "I’m your assistant.",
    "what can you do?": "I can chat with you",
    "what can you do": "I can chat with you",
    "motivate me": "Keep building small things,Discipline and consstency is the key for sucess,You just need to be 1% better than yesterday",
    "What's next?": "Ask me anything."
}

# Function to generate reply based on user input
def rplyfunc(userinput):
    # Convert input to lowercase for matching
    userinput = userinput.lower()

    # Loop through all stored questions
    for que in responses:
        # Check if stored question exists in user input
        if que in userinput:
            return responses[userinput]

    # Default reply if no match is found
    return ("I can't answer it,I am still learning")

# Infinite loop to keep chatbot running
while True:
    # Safety check (not really needed, but kept as-is)
    if name.lower() == "bye":
        break

    # Ask user for a question
    ui = input("\nAsk a question or type bye to exit: ")

    # Exit condition
    if ui.lower() == "bye":
        break

    # Get chatbot reply
    response = rplyfunc(ui)

    # Print chatbot reply
    print("AI reply: ", response)

# Exit message
print("---------Thank You!---------")
