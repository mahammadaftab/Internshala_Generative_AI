# Assignment 2: Python Meets AI: Your Custom Chat Assistant

This Python application demonstrates interaction with the OpenAI API to create a simple conversational AI agent.

## Problem Statement

Create an application that interacts with the OpenAI API to simulate a simple conversational agent, demonstrating understanding of AI code components.

## Features

- Interactive chat with AI using OpenAI's GPT-3.5-turbo model
- Continuous conversation loop
- Error handling for API interactions
- Easy exit command

## Requirements

- Python 3.14 or higher
- OpenAI API key (sign up at https://platform.openai.com/)
- `openai` Python package

## Installation

1. Ensure Python is installed and configured.
2. Install the required package:
   ```
   pip install openai
   ```

## Usage

1. Obtain an OpenAI API key from https://platform.openai.com/
2. Edit `main.py` and replace `'your-api-key-here'` with your actual API key.
3. Run the application:
   ```
   python main.py
   ```
4. Start chatting with the AI! Type your messages and press Enter.
5. Type 'exit' to end the conversation.

## Code Components

- **OpenAI Client Initialization**: Sets up the connection to OpenAI API
- **Chat Function**: Handles the conversation loop
- **API Request**: Sends user messages to OpenAI and receives responses
- **Error Handling**: Catches and displays API-related errors

## Troubleshooting

- **API Key Error**: Ensure your OpenAI API key is correctly set in the code.
- **Import Error**: Make sure the `openai` package is installed.
- **Network Issues**: Check your internet connection for API calls.

## Notes

- This is a basic implementation. For production use, consider adding conversation history, better error handling, and security measures.
- Be mindful of OpenAI's usage policies and costs.