# Text Mining in Python: Module 5 - Large Language Models

## Overview

This project demonstrates a text processing pipeline using Large Language Models (LLMs) for the Text Mining in Python class, Module 5. The focus is on showcasing how to integrate and use various LLMs for text analysis and generation tasks, particularly in the context of summarizing information about Missouri conservation areas.

## Project Structure

- `biagen/`: Main package directory
  - `io.py`: Utilities for handling JSONL files
  - `llm.py`: Interfaces for different LLM providers (Cohere, Groq, OpenAI, Google AI)
  - `scrape.py`: Web scraping utilities for data collection
- `notebooks/`:
  - `01-scrape.ipynb`: Demonstration of web scraping techniques
  - `02-preprocess.ipynb`: Text preprocessing and data preparation
  - `03-process_one.ipynb`: Example of processing a single document using LLMs
  - `04-process_many.ipynb`: Batch processing of multiple documents
  - `04a-process_many-localmodel.ipynb`: Using a local LLM for batch processing
- `assets/`: Data files and resources
- `pyproject.toml`: Project dependencies and configuration

## Key Concepts Demonstrated

1. **Web Scraping**: Collecting data about Missouri conservation areas
2. **Text Preprocessing**: Cleaning and preparing text data for analysis
3. **LLM Integration**: Using various LLM providers for text processing tasks
4. **Abstractive Summarization**: Implementing the Chain of Density prompting technique
5. **Batch Processing**: Applying LLM-based analysis to multiple documents
6. **Local LLM Usage**: Demonstrating how to use locally hosted language models

## Getting Started

1. Install dependencies:
   ```
   pip install poetry
   poetry install
   ```

2. Explore the notebooks in order:
   - Start with `01-scrape.ipynb` to understand data collection
   - Move through the preprocessing and processing notebooks to see the full pipeline

## Configuring Your .env File

To use the various LLM providers in this project, you'll need to set up API keys. Create a `.env` file in the root directory of the project and add one or more of your API keys as follows:

```
COHERE_API_KEY=your_cohere_api_key
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```

Replace `your_*_api_key` with the actual API keys you obtain from each provider.

### Signing Up for API Keys

#### Cohere

1. Visit [Cohere's website](https://cohere.ai/)
2. Click on "Sign Up" or "Get API Key"
3. Follow the registration process
4. Once registered, you can find your API key in your account dashboard

#### Groq

1. Go to [Groq's website](https://www.groq.com/)
2. Look for a "Sign Up" or "Get Started" option
3. Complete the registration process
4. Access your API key from your account settings

#### OpenAI

1. Visit [OpenAI's website](https://openai.com/)
2. Click on "Sign Up" in the top right corner
3. Follow the registration steps
4. Once logged in, go to the API section to find your API key

#### Google AI (for Gemini)

1. Go to the [Google AI Studio](https://ai.google.dev/aistudio)
2. Click on "Sign In To AI Studio"
3. Sign in with your Google account or create a new one
4. Set up a project and enable the necessary APIs
5. Create credentials to get your API key

Remember to keep your API keys confidential and never share them publicly or commit them to version control systems.

## Key Components

- `biagen.llm`: Provides a unified interface for different LLM providers
- `biagen.io`: Utilities for handling JSONL data storage and retrieval
- `biagen.scrape`: Web scraping functions for data collection

## Learning Objectives

- Understand how to integrate LLMs into a text mining pipeline
- Explore different LLM providers and their capabilities
- Learn about abstractive summarization techniques
- Gain experience in processing both individual and multiple documents using LLMs

## Note to Students

This project is a demonstration of concepts covered in Module 5 of the Text Mining in Python class. It showcases a practical application of LLMs in processing and summarizing real-world data. As you go through the notebooks, pay attention to:

- How different LLM providers are integrated and used
- The steps involved in preprocessing text data for LLM input
- The implementation of the Chain of Density prompting technique
- Considerations when processing multiple documents with LLMs

Feel free to experiment with the code, try different LLM providers, or apply these techniques to other datasets.

## Resources

- [Chain of Density Prompting Paper](https://arxiv.org/abs/2309.04269)
- Documentation for LLM providers used in this project:
  - [Cohere](https://docs.cohere.com/)
  - [Groq](https://www.groq.com/)
  - [OpenAI](https://platform.openai.com/docs/)
  - [Google AI](https://cloud.google.com/ai-platform/docs)
