from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"], 
    template="Hi!! I'm {name}, tell me a joke about my name"
)

text = template.format(name="Wellinton")

print(text)
