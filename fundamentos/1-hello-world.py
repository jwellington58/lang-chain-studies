from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# model = ChatOpenAI(model_name="gpt-5-nano", temperature=0.5)
# message = model.invoke("Hello World")
# print(message)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

response = llm.invoke("Poderia me ajudar a entender como funciona o langchain?")
print(response.content)