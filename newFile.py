

a=2
b=3
print(a**b)


import openai
def openaiDoc(changes_in_file):
    openai.api_key = ""
    prompt = ""
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        )
    generated_documentation = response.choices[0].text.strip()

    print("generated openai Document - {}".format(generated_documentation))
    return generated_documentation


#addition of 2 value
a=2
b=3
print(a**b)



