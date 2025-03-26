# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input:
        return "Hi there! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")
