# -*- coding: utf-8 -*-
"""Naive_RAG.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zLgw7Jc6IFxCdjlEQtWqD5rMJKpOx6Ia
"""

import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain.vectorstores import Chroma
from langchain.llms import HuggingFaceEndpoint
from langchain.prompts import FewShotPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate

from google.colab import userdata
API_KEY = userdata.get('HUGGINGFACE_API')

from huggingface_hub import login

login(API_KEY)

pdf_path = "/content/lbdl.pdf"

chunk_size = 1000
chunk_overlap = 200

loader = PyPDFLoader(pdf_path)
data = loader.load()
print(data[0])

text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
docs = text_splitter.split_documents(data)

model_name="sentence-transformers/all-MiniLM-L6-v2"
embedding_model = HuggingFaceEmbeddings(model_name=model_name)

vectorstore = Chroma.from_documents(
    docs,
    embedding=embedding_model,
    persist_directory=os.getcwd()
)

retriever = vectorstore.as_retriever()

llm = HuggingFaceEndpoint(
            repo_id = 'meta-llama/Llama-3.2-1B-Instruct',
            task = 'text-generation',
            temperature=0.1,
            huggingfacehub_api_token=API_KEY
        )

examples = examples = [
    {"question": "What is deep learning and how is it different from traditional machine learning?",
     "answer": "Deep learning is a subset of machine learning that uses neural networks with many layers to automatically extract features from raw data. Unlike traditional machine learning, which often relies on hand-crafted features, deep learning can automatically learn hierarchical representations from data, making it particularly powerful for tasks like image recognition and natural language processing."},

    {"question": "What are the different types of neural networks used in deep learning?",
     "answer": "There are several types of neural networks in deep learning, including: \n1. **Feedforward Neural Networks (FNN)**: Basic neural networks where information moves in one direction from input to output. \n2. **Convolutional Neural Networks (CNNs)**: Specialized for image processing, using convolution layers to detect spatial hierarchies. \n3. **Recurrent Neural Networks (RNNs)**: Designed for sequential data, with feedback loops allowing information to persist over time. \n4. **Generative Adversarial Networks (GANs)**: Composed of two networks (generator and discriminator) that compete to improve each other's performance. \n5. **Transformer Networks**: Known for their use in natural language processing tasks, such as BERT and GPT."},

    {"question": "What is backpropagation and how does it work in training neural networks?",
     "answer": "Backpropagation is an optimization technique used to minimize the error in a neural network by adjusting the weights of the network. It works by calculating the gradient of the loss function with respect to each weight in the network using the chain rule of calculus. These gradients are then used to update the weights via an optimization algorithm like gradient descent."},

    {"question": "What is the vanishing gradient problem in deep learning?",
     "answer": "The vanishing gradient problem occurs when gradients become very small as they are backpropagated through many layers in a deep neural network. This results in the weights of the earlier layers receiving little to no updates, making it difficult for the network to learn effectively. This problem is often encountered in deep networks that use activation functions like the sigmoid or tanh."},

    {"question": "What are activation functions, and why are they important in neural networks?",
     "answer": "Activation functions introduce non-linearity into neural networks, allowing them to learn complex patterns. Without activation functions, a neural network would simply be a linear model, regardless of its depth. Some common activation functions include: \n1. **ReLU (Rectified Linear Unit)**: The most widely used, which outputs zero for negative values and the input itself for positive values. \n2. **Sigmoid**: Outputs a value between 0 and 1, often used in binary classification problems. \n3. **Tanh**: Similar to sigmoid but outputs values between -1 and 1. \n4. **Softmax**: Used in multi-class classification problems, it converts raw scores into probabilities."},

    {"question": "What is the difference between a convolutional neural network (CNN) and a recurrent neural network (RNN)?",
     "answer": "CNNs are designed to handle grid-like data such as images. They use convolutional layers to detect spatial hierarchies and are particularly effective in tasks like image classification. RNNs, on the other hand, are designed for sequential data, such as time series or text. They have feedback connections that allow information to persist, making them suitable for tasks like language modeling and speech recognition."},

    {"question": "What is overfitting in deep learning, and how can it be prevented?",
     "answer": "Overfitting occurs when a model learns the training data too well, including the noise and outliers, causing it to perform poorly on unseen data (test set). This typically happens in deep learning when a model has too many parameters or is trained for too many epochs. To prevent overfitting, techniques such as **regularization** (e.g., L2 regularization), **dropout**, **early stopping**, and **data augmentation** can be applied."},

    {"question": "What is transfer learning, and how is it used in deep learning?",
     "answer": "Transfer learning is the process of using a pre-trained model on one task and fine-tuning it for a new, but related task. This is particularly useful when there is limited data for the new task. By leveraging the knowledge the model has learned from large datasets (e.g., ImageNet for image tasks), transfer learning allows the model to generalize better and require less training time."},

    {"question": "What are Generative Adversarial Networks (GANs) and how do they work?",
     "answer": "GANs consist of two neural networks: a **generator** and a **discriminator**. The generator creates synthetic data (e.g., images), while the discriminator tries to distinguish between real and fake data. The two networks are trained together in a competitive process, with the generator improving its ability to produce realistic data, and the discriminator improving its ability to identify fake data. GANs are used in applications like image generation, video creation, and data augmentation."},

    {"question": "What are some common deep learning optimization algorithms?",
     "answer": "Some common optimization algorithms used in deep learning include: \n1. **Gradient Descent**: The most basic optimization method, which updates weights by taking steps in the direction of the negative gradient of the loss function. \n2. **Stochastic Gradient Descent (SGD)**: A variant that updates the weights after each mini-batch rather than the entire dataset, making it more efficient for large datasets. \n3. **Adam (Adaptive Moment Estimation)**: An adaptive optimizer that adjusts learning rates based on the average of past gradients and squared gradients, widely used in deep learning tasks."}
]

example_prompt = PromptTemplate(input_variables=["question"], template="{question}\n\n{answer}")

template = FewShotPromptTemplate(
            examples=examples,
            example_prompt=example_prompt,
            suffix="\n\n{question}",
            input_variables=["question"]
        )

chain = (
            {"context": retriever.get_relevant_documents, "question": RunnablePassthrough()}
            | template
            | llm
        )

query = "What is the main purpose of Computer Vision"
messages = chain.invoke(query)

messages

