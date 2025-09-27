from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
load_dotenv()


template = PromptTemplate(
    input_variables=["name"], 
    template="Hi!! I'm {name}, tell me a joke about my name"
)

text = template.format(name="Wellinton")


model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.5)
result = model.invoke(text)
print(result.content)