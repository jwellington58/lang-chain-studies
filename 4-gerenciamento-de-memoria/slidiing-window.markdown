## 🧠 Como Funciona o Gerenciamento de Memória no LangChain
O gerenciamento de memória no LangChain permite que um LLM (Large Language Model) tenha acesso a mensagens passadas em uma conversa. Sem isso, cada pergunta que você faz seria tratada de forma isolada, e o modelo não saberia o contexto anterior.

O processo funciona com dois componentes principais:

Armazenamento do Histórico (ChatMessageHistory): É o objeto que de fato guarda as mensagens. O LangChain oferece várias implementações:

InMemoryChatMessageHistory: Armazena as mensagens em uma variável na memória RAM do seu programa. É simples e rápido para testes, mas o histórico é perdido assim que o programa para de rodar. (É o que seu exemplo usa no session_store).

Armazenamento Persistente: Salva as mensagens em um banco de dados externo, como RedisChatMessageHistory, MongoDBChatMessageHistory, SQLChatMessageHistory, etc. Isso garante que o histórico de uma sessão sobreviva entre execuções do programa.

Estratégia de Gerenciamento (RunnableWithMessageHistory): É o "orquestrador" que integra o armazenamento ao seu chain. Ele intercepta as entradas e saídas, carrega o histórico relevante daquele session_id antes de chamar o LLM, e salva a nova interação (pergunta do usuário e resposta do modelo) de volta no armazenamento.

A "janela deslizante" (sliding window) que você mencionou é uma estratégia para controlar o tamanho do histórico enviado ao LLM, para evitar exceder o limite de tokens do modelo e controlar custos. Em vez de enviar o histórico completo, você envia apenas as N últimas mensagens. A função trim_messages é a ferramenta perfeita para isso.

## 🪟 Analisando os Parâmetros do trim_messages
A função trim_messages é a responsável por implementar a lógica da janela deslizante no seu exemplo. Vamos analisar os parâmetros que você usou:

raw_history: É a lista completa de mensagens da conversa que será "podada".

token_counter=len: Aqui você define como os tokens são contados. No seu exemplo, está usando a função len, que simplesmente conta o número de caracteres. Para um controle mais preciso, você poderia usar uma biblioteca de tokenização como a tiktoken.

max_tokens=2: Este é o tamanho da sua janela. Ele define o número máximo de "tokens" (no seu caso, caracteres, devido ao token_counter) que o histórico final pode ter. Você usou 2, que é um valor muito baixo e provavelmente apenas para fins de teste. Na prática, seria algo como 4000 ou 8000.

strategy="last": Define a estratégia de poda. "last" significa que a função manterá as mensagens mais recentes e descartará as mais antigas até que o histórico se encaixe no max_tokens.

start_on="human": Garante que o histórico podado não comece com uma mensagem do assistente. Se a primeira mensagem após a poda for do assistente, ela também será removida para garantir que o contexto comece com uma entrada do usuário.

include_system=True: Garante que a mensagem de sistema ("You're a helpful assistant...") seja sempre incluída no histórico final, mesmo que as outras mensagens sejam cortadas. Isso é fundamental para manter o comportamento do seu bot.

allow_partial=False: Se a última mensagem for muito longa e exceder o max_tokens por si só, essa opção define se ela deve ser cortada (True) ou descartada por completo (False).

Em resumo, sua função prepare_inputs pega o histórico bruto, aplica uma janela deslizante extremamente pequena (max_tokens=2) mantendo as últimas mensagens e a mensagem de sistema, e passa esse histórico "podado" para o prompt.