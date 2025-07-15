import re

# Calculator functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error: Division by zero!" if y == 0 else x / y

# Rule-based chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()

    # === Friendly Chat ===
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I assist you today for calculations? "
    elif "how are you" in user_input:
        return "I'm doing well! Thanks for asking. How can I help you?"
    elif "your name" in user_input:
        return "I'm Meghana's smart calculator chatbot."
    elif "help me" in user_input or "assist me" in user_input:
        return "I can chat with you or calculate! Try typing things like 'add 5 and 3' or 'how are you?'"
    
    # === Calculator Logic ===
    elif "add" in user_input:
        numbers = re.findall(r'\d+\.?\d*', user_input)
        if len(numbers) >= 2:
            return f"The result is {add(float(numbers[0]), float(numbers[1]))}"

    elif "subtract" in user_input:
        numbers = re.findall(r'\d+\.?\d*', user_input)
        if len(numbers) >= 2:
            return f"The result is {subtract(float(numbers[1]), float(numbers[0]))}"

    elif "multiply" in user_input:
        numbers = re.findall(r'\d+\.?\d*', user_input)
        if len(numbers) >= 2:
            return f"The result is {multiply(float(numbers[0]), float(numbers[1]))}"

    elif "divide" in user_input:
        numbers = re.findall(r'\d+\.?\d*', user_input)
        if len(numbers) >= 2:
            return f"The result is {divide(float(numbers[0]), float(numbers[1]))}"

    # === Exit ===
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! It was nice chatting with you! 👋"

    # === Default ===
    else:
        return "Sorry, I didn't understand that. Try typing 'add 2 and 3' or 'how are you?'"

# Chat loop
print("🤖 Welcome to Meghana's Smart Chatbot! Type something like 'add 2 and 3' or 'how are you?' (Type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if "exit" in user_input.lower():
        print("Chatbot:", chatbot_response(user_input))
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
