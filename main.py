import openai

openai.api_key = "sk-proj-Nfdt6kffakpRr9Eq1MW9T3BlbkFJ5CTstDyR8QboaCsiLnpd"

def gpt_chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__=="__main__":
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response=gpt_chat(user_input)
        print("Chatbot: ", response)
