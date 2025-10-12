from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain


from dotenv import load_dotenv
load_dotenv()

long_text = """
🧠 1. ROLE PROMPTING (Definição de Papel)
👉 O que é:
Você orienta o modelo a “atuar” com uma identidade ou função específica, o que direciona o estilo, o vocabulário e o raciocínio da resposta.

🧩 Exemplo:
"Você é um professor de física experiente. Explique a teoria da relatividade para um aluno do ensino médio."

📘 Por que funciona:
O modelo ajusta o tom, nível técnico e formato da explicação conforme o papel definido.


⚙️ 2. ZERO-SHOT PROMPTING
👉 O que é:
Você não fornece exemplos — apenas descreve a tarefa de forma clara e direta. O modelo infere o padrão de resposta com base apenas na instrução.

🧩 Exemplo:
"Traduza a frase 'A inteligência artificial está mudando o mundo' para o inglês."

📘 Por que funciona:
Ideal para tarefas simples ou já conhecidas pelo modelo.


🎯 3. FEW-SHOT PROMPTING
👉 O que é:
Você fornece alguns exemplos (2–5) de entrada e saída para o modelo aprender o padrão desejado antes da tarefa final. Serve como “mini-treinamento” no próprio prompt.

🧩 Exemplo:
Traduza as frases para o inglês:
- "Bom dia" → "Good morning"
- "Como vai você?" → "How are you?"
- "Estou com fome" → ?

📘 Por que funciona:
O modelo aprende o formato e contexto a partir dos exemplos anteriores.


🪜 4. CHAIN OF THOUGHT (Cadeia de Pensamento)
👉 O que é:
Você incentiva o modelo a explicar o raciocínio passo a passo antes da resposta final. Isso melhora a precisão em tarefas complexas (como lógica, matemática ou planejamento).

🧩 Exemplo:
"Resolva passo a passo: Se João tem 3 maçãs e compra mais 4, quantas maçãs ele tem agora? Mostre o raciocínio."

📘 Por que funciona:
O modelo “pensa em voz alta” e evita erros por pular etapas.


🧩 5. SELF-CONSISTENCY (Consistência Própria)
👉 O que é:
Gera várias cadeias de raciocínio diferentes e escolhe a resposta mais frequente entre elas. É usada internamente em frameworks de IA ou com prompts que pedem “várias hipóteses antes da conclusão”.

🧩 Exemplo:
"Liste três maneiras possíveis de resolver este problema matemático e escolha a mais correta no final."

📘 Por que funciona:
Reduz respostas incoerentes e melhora a robustez lógica.


🔄 6. REACT (Reason + Act)
👉 O que é:
Combina raciocínio (“Reason”) e ação (“Act”), permitindo que o modelo pense, execute uma ação (como chamar uma API, pesquisar ou lembrar algo), e continue o raciocínio.

🧩 Exemplo:
"Pense sobre a capital da França. (Raciocine) Agora, diga qual é o país onde essa cidade está localizada. (Aja)"

📘 Por que funciona:
Simula o comportamento de agentes autônomos (muito usado em IA com ferramentas externas).


📋 7. INSTRUCTION PROMPTING (Instruções Claras)
👉 O que é:
Você fornece instruções explícitas sobre formato, estilo, tamanho e objetivo da resposta. Serve para alinhar o modelo ao resultado esperado.

🧩 Exemplo:
"Explique a Revolução Francesa em até 100 palavras, com linguagem simples e em tópicos."

📘 Por que funciona:
Define limites e estrutura de saída.


🔍 8. PROMPT CHAINING (Encadeamento de Prompts)
👉 O que é:
Divide uma tarefa complexa em várias etapas (prompts sequenciais). A saída de um prompt serve como entrada para o próximo.

🧩 Exemplo:
1️⃣ “Resuma este texto.”
2️⃣ “Agora, com base nesse resumo, gere 3 títulos possíveis.”

📘 Por que funciona:
Aumenta o controle e reduz erros em tarefas longas ou complexas.


💬 9. META PROMPTING
👉 O que é:
Você pede ao modelo para gerar o próprio prompt ideal para uma tarefa. Útil para otimizar a comunicação com o modelo.

🧩 Exemplo:
“Crie um prompt que ensine o modelo a escrever um roteiro de vídeo de 1 minuto sobre IA de forma divertida.”

📘 Por que funciona:
O modelo aprende a estruturar instruções eficazes para si mesmo.


🧮 10. GENERATED KNOWLEDGE PROMPTING
👉 O que é:
Antes de responder à pergunta principal, o modelo é instruído a gerar fatos ou contexto relevantes, e só então formular a resposta final.

🧩 Exemplo:
“Primeiro, liste fatos importantes sobre o aquecimento global. Em seguida, use essas informações para explicar suas causas.”

📘 Por que funciona:
Melhora respostas em temas complexos e reduz alucinações.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300, chunk_overlap = 70
)

chunks = splitter.create_documents([long_text])

for chunk in chunks:
    print(chunk.page_content)
    print("--"*10)



llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

chain_sumarize = load_summarize_chain(llm, chain_type="map_reduce", verbose=True)

result = chain_sumarize.invoke({"input_documents": chunks})

print(result["output_text"])