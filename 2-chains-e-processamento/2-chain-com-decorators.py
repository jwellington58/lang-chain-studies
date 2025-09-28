from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.runnables import chain
load_dotenv()

@chain
def square(x:int) -> int:
    return {"square_result": x**2}



template = PromptTemplate(
    input_variables=["name"], 
    template="Hi!! I'm {name}, tell me a joke about my name"
)

template2 = PromptTemplate(
    input_variables=["square_result"],
    template="Tell me about the number {square_result}"
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.5)
chain = template | model


#result = chain.invoke({"name": "Wellinton"})

chain2 = square | template2 | model
result = chain2.invoke(100)

print(result.content)