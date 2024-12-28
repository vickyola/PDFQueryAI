#Lösungsvorschlag: RAG mit PDF ohne Speichern

# TODO path des datasets 27
# TODO OPENAI_API_KEY als environmentvariable

# Für meinen Lösungsvorschlag habe ich das folgende Langchain Tutorial verwendet
#https://python.langchain.com/v0.2/docs/tutorials/pdf_qa/

from pathlib import Path
from langchain.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()
import sys
import os

# PDF ingestion and Question/Answering system

# Change path of dataset here:
pathstring =  os.getenv("DATASET_PATH")#str

path = Path(pathstring)

#  OPEN_AI_API key in Environmental Variable

# Check if OPENAI_API_KEY is set
if "OPENAI_API_KEY" not in os.environ:
    raise EnvironmentError("Please set the 'OPENAI_API_KEY' environment variable.")

# Load PDFs 
docs = []
for file_path in path.glob("*.pdf"):
    # Extract text data
    loader = PyPDFLoader(str(file_path))
    docs.extend(loader.load())

# Initialize language model
llm = ChatOpenAI(model="gpt-4o")

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large", #'text-embedding-ada-002' # old but default
)

# Split documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, #close to average length of doc (800)
    chunk_overlap=200,
    add_start_index=True,
    separators=["\n\n", "\n", " ", ""]
)

splits = text_splitter.split_documents(docs) #to fit in context window of llm

# Load splits into vector store
# embed the contents of each document split and insert these embeddings into a vector database 
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# Create retriever
retriever = vectorstore.as_retriever()

# Define prompt template
system_prompt = ("Du bist ein Assistent für die Beantwortung technischer Fragen. Verwende die folgenden bereitgestellten Informationen in den technischen Datenblättern, um die Frage zu beantworten. Wenn du die Antwort nicht weißt, gib an, dass du sie nicht weißt. Begrenze die Antwort auf maximal drei Sätze und halte sie prägnant."
"\n\n"
"{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Create RetrievalQA chain
question_answer_chain = create_stuff_documents_chain(llm, prompt) #Create a chain for passing a list of Documents to a model.

rag_chain = create_retrieval_chain(retriever, question_answer_chain) #Create retrieval chain that retrieves documents and then passes them on.

fragen = ["Wie viel wiegt XBO 4000 W/HS XL OFR?", "Welche Leuchte eignet sich am Besten für mein Heimkino?",
          "Gebe mir alle Leuchtmittel mit mindestens 1500W und einer Lebensdauer von mehr als 3000 Stunden",
          "Was ist die kleinste Einheit, die ich bestellen kann?" ]
 
for frage in fragen:
    result = rag_chain.invoke({"input": frage})        
    print(result["answer"])
    
#   for document in result["context"]:
#     print(document)
#     print()




