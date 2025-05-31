# GenAILab: Generative AI Laboratory

This repository serves as a laboratory for experimenting with, deploying, and managing various Generative AI solutions in Kubernetes environments. GenAILab provides a comprehensive set of tools and configurations for AI engineering, model serving, and agent deployment.

## Overview

GenAILab is designed as a learning and experimentation platform for AI engineering with a focus on:

- **Agentic AI systems**
- **Model deployment and serving**
- **MLOps on Kubernetes**
- **AI agent orchestration**

## Repository Structure

- **`/kagent/`**: Kubernetes deployment for kagent, an AI agent framework
- **`/kserve/`**: Model serving using KServe for ML model deployment
- **`/openwebui/`**: Web interface for interacting with LLMs like Ollama
- **`/tailscale/`**: Network configurations for secure access
- **`/contents_crew/`**: Sample implementation of CrewAI for agent orchestration
- **`/prompts/`**: Collection of prompts for various AI use cases

## Key Components

### KAgent

KAgent is a Kubernetes-native agent framework for deploying and managing AI agents:

```bash
# Deploy KAgent
kubectl apply -k kagent
```

Configuration includes:
- Custom resource definitions for model deployment
- Integration with Ollama and other model providers
- Environment for agent execution

### Model Serving

Supports model deployment using KServe:

```bash
# Deploy KServe
kubectl apply -k kserve
```

### Open WebUI

Web interface for interacting with language models:

```bash
# Deploy Open WebUI
kubectl apply -k openwebui
```

### CrewAI Example

Multi-agent orchestration example using CrewAI:

```bash
# Run CrewAI example
cd contents_crew
crewai run
```

## Learning Objectives

This lab supports learning in:

1. **AI Agency**: Understanding and implementing agentic AI systems
2. **Agent Orchestration**: Coordinating multiple agents to accomplish complex tasks
3. **MCP Development**: Multi-provider systems development
4. **Agent Development**: Building intelligent AI agents

## MLOps on Kubernetes

GenAILab demonstrates Kubernetes-native MLOps practices:

1. Efficient deployment and scaling of ML workloads
2. Observability for AI/ML components
3. GitOps-friendly declarative configurations using CRDs
4. Integration of various AI frameworks

## Getting Started

1. Clone this repository
2. Set up a Kubernetes cluster (local or cloud-based)
3. Deploy components as needed for experimentation
4. Explore different AI use cases and configurations

## Requirements

- Kubernetes cluster (local or cloud-based)
- kubectl and kustomize installed
- Helm for chart management
- Python 3.10+ for CrewAI examples

## Contributing

This repository is designed as a lab for experimentation. Feel free to:

- Add new AI components
- Experiment with different model configurations
- Implement new agent patterns
- Share findings and improvements

---

This lab is a continuously evolving platform for AI engineering experimentation and learning.