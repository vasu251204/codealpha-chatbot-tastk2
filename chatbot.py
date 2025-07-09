import random
import time
from datetime import datetime

conversation_history = []

responses = {
    "greeting": ["Hi! Great to see you!", "Hello there!", "Hey, what's up?"],
    "how_are_you": ["I'm doing great, thanks!", "Feeling awesome, how about you?", "All good here! You?"],
    "farewell": ["Goodbye! Take care!", "See you later!", "Bye, have a nice day!"],
    "positive": ["That's awesome to hear!", "Glad you're feeling great!"],
    "negative": ["Oh, I'm sorry to hear that.", "Hope things get better soon!"],
    "default": ["Hmm, not sure about that one.", "Can you say that again?", "Let's try something else."]
}

positive_words = ["great", "awesome", "happy", "good"]
negative_words = ["sad", "bad", "terrible", "sorry"]

def log_conversation(user_input, bot_response):
    """Log conversation to a file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] User: {user_input}\n")
        log_file.write(f"[{timestamp}] Bot: {bot_response}\n")

def detect_sentiment(user_input):
    """Detect basic sentiment based on keywords"""
    user_input = user_input.lower()
    for word in positive_words:
        if word in user_input:
            return "positive"
    for word in negative_words:
        if word in user_input:
            return "negative"
    return None

def get_response(user_input, history):
    """Generate response based on user input and conversation history"""
    user_input = user_input.lower().strip()
    

    if not user_input:
        return "Please say something!"

    history.append(user_input)

    if user_input in ["bye", "exit", "quit"]:
        return random.choice(responses["farewell"])
    

    sentiment = detect_sentiment(user_input)
    if sentiment == "positive":
        return random.choice(responses["positive"])
    elif sentiment == "negative":
        return random.choice(responses["negative"])
 
    if "hello" in user_input or "hi" in user_input:
        if "hello" in history[-2:] or "hi" in history[-2:]:
            return "Hey, you already said hi! What's new?"
        return random.choice(responses["greeting"])
    elif "how are you" in user_input or "how you doing" in user_input:
        return random.choice(responses["how_are_you"])
    else:
        return random.choice(responses["default"])

def chatbot():
    """Main chatbot function"""
    print("Welcome to the Advanced Chatbot! Type 'bye', 'exit', or 'quit' to stop.")
    print("Try saying 'hello', 'how are you', or share how you're feeling!")
    
    while True:
        try:
            user_input = input("You: ")
            response = get_response(user_input, conversation_history)
            print("Bot:", response)
            
            log_conversation(user_input, response)
            
            if user_input.lower().strip() in ["bye", "exit", "quit"]:
                print("Chatbot shutting down. Check 'chat_log.txt' for conversation history.")
                break
                
        except KeyboardInterrupt:
            print("\nBot: Interrupted! Shutting down.")
            break
        except Exception as e:
            print(f"Bot: Oops, something went wrong: {e}")
            continue

if __name__ == "__main__":
    chatbot()