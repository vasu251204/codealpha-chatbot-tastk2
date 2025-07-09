# codealpha-chatbot-tastk2
# Codealpha_tasks-python
Overview

This repository contains an advanced rule-based chatbot implemented in Python. The chatbot responds to user inputs like "hello," "how are you," and "bye" with predefined replies, while incorporating advanced features such as context awareness, sentiment detection, response variation, and conversation logging. It is designed to demonstrate key programming concepts including if-elif statements, functions, loops, and input/output handling.

Features





Context Awareness: Tracks conversation history to provide varied responses (e.g., avoids repeating greetings).



Sentiment Detection: Recognizes basic positive/negative sentiment based on keywords (e.g., "happy" or "sad").



Response Variation: Randomly selects from multiple response options for natural interaction.



Conversation Logging: Saves interactions with timestamps to chat_log.txt.



Robust Input Handling: Manages empty inputs, exceptions, and multiple exit commands ("bye," "exit," "quit").



Modular Design: Organized with functions for easy extension and maintenance.

Requirements





Python 3.6 or higher



No external dependencies required

Installation





Clone the repository:

git clone https://github.com/your-username/codealpha_task-chatbot.git
cd -chatbot



Ensure Python is installed:

python --version



Run the chatbot:

python chatbot.py

Usage





Launch the chatbot by running python 
chatbot.py.



Interact with the chatbot by typing phrases:





Greetings: "hello," "hi" → e.g., "Hi! Great to see you!"



Inquiries: "how are you" → e.g., "I'm doing great, thanks!"



Sentiments: "I'm happy" → e.g., "That's awesome to hear!"



Exit: "bye," "exit," or "quit" → e.g., "Goodbye! Take care!"



View conversation history in chat_log.txt after the session.

Example interaction:

Welcome to the Advanced Chatbot! Type 'bye', 'exit', or 'quit' to stop.
You: hello
Bot: Hi! Great to see you!
You: how are you
Bot: I'm doing great, thanks!
You: I'm happy
Bot: That's awesome to hear!
You: bye
Bot: Goodbye! Take care!
Chatbot shutting down. Check 'chat_log.txt' for conversation history.
