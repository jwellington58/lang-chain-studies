from langchain_core.runnables import RunnableLambda

def invert(text: str) -> str:
    return text[::-1]

runnable = RunnableLambda(invert)

result = runnable.invoke("Hello World")
print(result)