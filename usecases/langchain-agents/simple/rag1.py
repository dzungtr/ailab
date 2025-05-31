import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from langchain_ollama import ChatOllama

# Load and chunk contents of the blog
loader = WebBaseLoader(
    # web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    web_paths=("https://www.growthunhinged.com/p/gtm-vibecoding-ideas?utm_source=tldrproduct",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

# Index chunks
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector_store = InMemoryVectorStore(embeddings)

_ = vector_store.add_documents(documents=all_splits)

# Define prompt for question-answering
# N.B. for non-US LangSmith endpoints, you may need to specify
# api_url="https://api.smith.langchain.com" in hub.pull.
prompt = hub.pull("rlm/rag-prompt")

llm = ChatOllama(
    # model="qwen3:latest",
    # model="llama3.1:8b",
    model="gemma3:12b-it-q8_0",
    base_url="http://localhost:11434"
)


# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


# Define application steps
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}


# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()
# run sample
response = graph.invoke({"question": "What is Vibecoding?"})
print(response["answer"])
