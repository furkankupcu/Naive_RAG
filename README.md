# Naive RAG: A Simple Retrieval-Augmented Generation System

## Overview

This project demonstrates the creation of a simple **Retrieval-Augmented Generation (RAG)** system using **LangChain**, **HuggingFace**, and **Chroma**. RAG is a technique that integrates two powerful methods in Natural Language Processing (NLP): **information retrieval** and **text generation**. The system retrieves relevant documents from a document store (using embeddings and vector search with Chroma) and then leverages a large language model (LLM) from HuggingFace to generate coherent and informative responses based on the retrieved documents.

By combining the power of language models with retrieval-based methods, this project ensures that the generated responses are contextually relevant and grounded in the retrieved data. The main goal of this project is to show how a simple, yet effective, RAG system can handle tasks such as **question answering** and **information retrieval** from documents.

## Key Features

- **Document Loading**: Parse PDF documents using `PyPDFLoader`.
- **Text Splitting**: Divide the text into smaller, manageable chunks for easier processing with `RecursiveCharacterTextSplitter`.
- **Embeddings**: Generate meaningful vector representations of the text using **HuggingFaceEmbeddings**.
- **Vector Search**: Use **Chroma** vector store to perform efficient similarity search for retrieving relevant documents.
- **Text Generation**: Utilize a **HuggingFace-based LLM** to generate responses from the retrieved documents.

## Installation

To get started with this project, you'll need to install the following dependencies:

```bash
# Install LangChain Community edition
pip install -U langchain-community

# Install LangChain HuggingFace integration
pip install langchain_huggingface

# Install PyPDF for document loading
pip install pypdf

# Install Chroma for vector storage and similarity search
pip install chromadb
