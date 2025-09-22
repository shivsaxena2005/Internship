
print("Hello! I am ChatBot 🤖. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()   # take input and convert to lowercase

    if (user_input == "hi" or user_input == "hello"):
        print("Bot: Hello! How can I help you today?")

    elif ("your name" in user_input):
        print("Bot: I am a simple rule-based chatbot!")

    elif ("how are you" in user_input):
        print("Bot: I'm doing well, thank you! How are you?")

    elif ("weather" in user_input):
        print("Bot: I can't check the weather right now, but I hope it's nice outside!")

    elif ("bye" in user_input):
        print("Bot: Goodbye! Have a great day! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Can you rephrase?")
