# Building a Simple Retrieval-Augmented Generation System with LangChain


Naive RAG: A Simple Retrieval-Augmented Generation System

This project demonstrates the creation of a simple Retrieval-Augmented Generation (RAG) system using LangChain, HuggingFace, and Chroma. RAG is a technique that combines two powerful approaches in natural language processing: information retrieval and text generation. The system retrieves relevant documents from a document store (using embeddings and vector search with Chroma) and then uses a large language model (LLM) from HuggingFace to generate coherent and informative responses based on the retrieved information.

By integrating the power of language models with retrieval-based methods, the system ensures that the responses are more grounded and contextually relevant. This project focuses on combining document loading (with PyPDF), text splitting (with LangChain's text splitter), embeddings (using HuggingFaceEmbeddings), and vector storage (via Chroma) to create a streamlined process for text generation.

The goal is to demonstrate how a simple, yet effective, RAG system can be constructed to handle tasks such as question answering and information retrieval from documents.

Key Features:

Document Loading: PDF documents are parsed using PyPDFLoader.
Text Splitting: The text is divided into smaller, manageable chunks for easier processing.
Embeddings: HuggingFace embeddings are used to generate meaningful vector representations of the text.
Vector Search: Chroma vector store enables efficient similarity search to retrieve relevant documents.
Text Generation: A HuggingFace-based LLM is used to generate responses from the retrieved documents.
This project is designed for individuals looking to explore the potential of combining retrieval and generation techniques in NLP, and to understand how LangChain can streamline these processes.

## Installation

To get started, you need to install the following dependencies:

```bash
# Install LangChain Community edition
pip install -U langchain-community

# Install LangChain HuggingFace integration
pip install langchain_huggingface

# Install PyPDF for document loading
pip install pypdf

# Install Chroma for vector storage and similarity search
pip install chromadb
