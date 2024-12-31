import pyautogui
import time
import pyperclip
from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(api_key="<Your Key Here>")

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    # Check if the last message in the chat log is from the specified sender
    messages = chat_log.strip().split("/2024] ")[-1]
    return sender_name in messages

# Step 1: Open Chrome by clicking at specified coordinates
pyautogui.click(1639, 1412)
time.sleep(1)

while True:
    time.sleep(5)

    # Step 2: Drag the mouse to select chat text
    pyautogui.moveTo(972, 202)
    pyautogui.dragTo(2213, 1278, duration=2.0, button='left')

    # Step 3: Copy selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1994, 281)  # Refocus chat area if needed

    # Step 4: Retrieve chat history from clipboard
    chat_history = pyperclip.paste()
    print(chat_history)  # Verify copied text
    print(is_last_message_from_sender(chat_history))

    # Process response if the last message is from the sender
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Naruto who speaks Hindi and English, from India, and you're a coder. Analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)."},
                {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das:"},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Paste and send the response
        pyautogui.click(1808, 1328)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
