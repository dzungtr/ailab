# GenAILab: Generative AI Laboratory

This repository serves as a laboratory for experimenting with, deploying, and managing various Generative AI solutions. GenAILab provides a comprehensive set of tools and configurations for AI engineering, model serving, and agent development.

## Overview

GenAILab is designed as a learning and experimentation platform for AI engineering with a focus on:

- **Agentic AI systems**
- **LangChain agent development**
- **RAG (Retrieval-Augmented Generation) implementations**
- **AI agent orchestration**

## Repository Structure

- **`/usecases/`**: Practical AI implementations
  - **`/langchain-agents/simple/`**: LangChain agent examples including:
    - Basic agent with Tavily search integration
    - RAG implementations using Ollama embeddings
    - Structured output examples
    - Prompt template demonstrations
- **`/prompts/`**: Collection of prompts for various AI use cases
- **`/goals.md`**: Project goals and objectives
- **`/learning-plan.md`**: Structured learning path for AI development
- **`/CLAUDE.md`**: Guidelines for Claude AI assistance in this repository

## Key Components

### LangChain Agents

The repository includes several LangChain agent implementations:

#### Basic Agent with Web Search
```python
# Run the main agent with Tavily search
cd usecases/langchain-agents/simple
poetry run python main.py
```

#### RAG Implementations
- **rag1.py**: Basic RAG setup with document loading and retrieval
- **rag2.py**: Advanced RAG with LangGraph state management and tool integration

#### Prompt Templates
Demonstrates handling of structured LLM responses with reasoning:
```python
poetry run python prompts_template.py
```

### Technologies Used

- **LangChain**: Framework for building language model applications
- **LangGraph**: For building stateful, multi-step agent workflows
- **Ollama**: Local LLM inference (llama3.1:8b, qwen3:latest)
- **Tavily API**: Web search integration for agents
- **Anthropic Claude**: AI model integration
- **Poetry**: Python dependency management
- **Nix**: Development environment management

## Learning Objectives

This lab supports learning in:

1. **AI Agency**: Understanding and implementing agentic AI systems
2. **Agent Development**: Building intelligent AI agents with LangChain
3. **RAG Systems**: Implementing retrieval-augmented generation
4. **Multi-Agent Orchestration**: Coordinating agents for complex tasks
5. **Local LLM Integration**: Working with Ollama for local inference

## Getting Started

1. Clone this repository
2. Set up development environment:
   ```bash
   # Enter Nix shell for development tools
   nix-shell
   
   # Install Python dependencies
   poetry install
   ```
3. Configure environment variables:
   - `TAVILY_API_KEY`: For web search functionality
   - `ANTHROPIC_API_KEY`: For Claude AI integration
   - `LANGSMITH_API_KEY`: For LangSmith tracing (optional)
4. Run Ollama locally for LLM inference:
   ```bash
   ollama pull llama3.1:8b
   ollama pull qwen3:latest
   ollama pull nomic-embed-text
   ```
5. Explore the use cases in `/usecases/langchain-agents/simple/`

## Requirements

- Python 3.12+
- Poetry for dependency management
- Nix (optional, for development environment)
- Ollama for local LLM inference
- API keys for Tavily and Anthropic services

## Future Components (Planned)

The following components are planned for future implementation:

- **`/kagent/`**: Kubernetes-native agent framework
- **`/kserve/`**: Model serving using KServe
- **`/openwebui/`**: Web interface for LLM interaction
- **`/contents_crew/`**: CrewAI multi-agent orchestration examples

## Contributing

This repository is designed as a lab for experimentation. Feel free to:

- Add new AI agent implementations
- Experiment with different LLM models and configurations
- Implement new RAG patterns
- Share findings and improvements

---

This lab is a continuously evolving platform for AI engineering experimentation and learning.