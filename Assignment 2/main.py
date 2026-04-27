from openai import OpenAI

# Set your OpenAI API key here
# Replace 'your-api-key-here' with your actual OpenAI API key
client = OpenAI(api_key='your Api Key Here')

def chat_with_ai():
    """
    Function to handle the chat interaction with the AI.
    This function runs a loop that prompts the user for input,
    sends it to the OpenAI API, and prints the AI's response.
    """
    # Print a welcome message
    print("Chat with AI! Type 'exit' to end the conversation.")

    # Start an infinite loop for continuous conversation
    while True:
        # Prompt the user for input
        user_input = input("You: ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            # Create a chat completion request to OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Using GPT-3.5-turbo model
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )

            # Extract the AI's response
            ai_response = response.choices[0].message.content

            # Print the AI's response
            print("AI:", ai_response)

        except Exception as e:
            # Handle any errors that occur during the API call
            print("Error:", str(e))

# Main entry point of the script
if __name__ == "__main__":
    chat_with_ai()