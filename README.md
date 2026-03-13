CODSOFT AI Internship - Task 1: Rule-Based Chatbot
Overview

This project implements a Rule-Based Chatbot named GANI, developed as part of the CODSOFT AI Internship. The chatbot responds to user inputs using predefined patterns and provides relevant answers, including greetings, jokes, time/date, and AI-related information.

Features

Responds to greetings (hi, hello, etc.)

Answers questions about the bot (your name, who made you)

Shares current time and date

Tells jokes

Provides basic information about AI

Responds to user moods (good, sad, tired, etc.)

Handles unrecognized inputs with polite fallback responses

Requirements

Python 3.x

No additional external libraries required (uses built-in re, random, and datetime modules)

GitHub Repository

You can find the project on GitHub:
Project Repository

To clone the repository:

git clone https://github.com/ganesmpsmg/chat-app.git
cd chatbot-app
How to Run

Clone or download the repository (see above).

Open a terminal/command prompt in the project directory.

Run the chatbot:

python chatbot.py

Chat with the bot by typing your messages.

Type bye, goodbye, exit, or quit to end the conversation.

Example Conversation
You: hi
Bot: Hello! How can I help you?

You: what is ai
Bot: AI is machines simulating human intelligence.

You: tell me a joke
Bot: Why did the computer get cold? It forgot to close Windows!

You: bye
Bot: Goodbye! Have a great day!
Code Structure

chatbot.py: Main Python script containing the rule-based chatbot logic.

RULES: List of regex patterns and possible responses.

get_response(user_input): Function to match user input with patterns and return an appropriate response.

Main loop handles user interaction until exit.

Future Improvements

Integrate live weather API for weather updates.

Expand knowledge base for more questions.

Add machine learning-based responses for more dynamic conversations.

Author

GANI — CODSOFT AI Internship Task 1
github repolink: https://github.com/ganesmpsmg/chatbot-app
