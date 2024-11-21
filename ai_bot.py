from openai import OpenAI

client = OpenAI(
    base_url= "http://localhost:11434/v1",
    api_key= "ollama"
)
#Test
# response = client.chat.completions.create (
#     model= "llama3.2",
#     messages=[{"role": "user","content": "Hello, bot!"}]
# )

# reply = response.choices[0].message.content
# print(reply)
messages = []
while True:
    user_input = input(f"\nYou: ")
    if user_input == "exit":
        break
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="llama3.2",
        stream=True,
        messages = messages
    )
    bot_reply = ""
    for chunk in response:
        bot_reply += chunk.choices[0].delta.content or ""
        print(chunk.choices[0].delta.content or "",end="",flush=True)
    messages.append({"role": "user", "content": bot_reply})