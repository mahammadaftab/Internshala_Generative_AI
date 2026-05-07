# HelloBot: Telegram AI Welcome Bot

## Objective

Create a Telegram chat bot in Python that sends a friendly greeting when a user starts a chat, then uses the OpenAI API to respond to messages.

## Files

- `main.py` — Telegram bot implementation
- `requirements.txt` — dependencies for the bot

## Setup Instructions

1. Create a new Telegram bot with BotFather and copy the bot token.
2. Set environment variables:
   - `TELEGRAM_BOT_TOKEN` — your Telegram bot token
   - `OPENROUTER_API_KEY` — your OpenRouter API key

   On Windows PowerShell:
   ```powershell
   $env:TELEGRAM_BOT_TOKEN="<your-telegram-token>"
   $env:OPENROUTER_API_KEY="<your-openrouter-key>"
   ```

3. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Run the bot:
   ```powershell
   python main.py
   ```

## How It Works

- The bot listens for `/start` and `/help` commands using `CommandStart()`.
- When a user starts a chat, it sends a welcome message:
  - `Hello! I am GPT Chat BOT. 😊 You can ask me anything, and I’ll do my best to help.`
- All other text messages are forwarded to OpenAI's Chat Completion API using the `gpt-3.5-turbo` model.

## Testing the Greeting

1. Open Telegram and search for your bot.
2. Send `/start`.
3. Confirm the bot replies with the greeting message.
4. Send a follow-up question like "What can you do?" to verify the OpenAI response.

## Validation and Screenshots

Capture screenshots of the following:

- Bot startup terminal showing `main.py` running
- Telegram chat with the bot returning the welcome message
- An example message and AI-generated reply

## Notes

- Keep your API keys private.
- If the bot fails, verify that both environment variables are set correctly.
- The bot uses the OpenAI API for conversational responses after the greeting.
