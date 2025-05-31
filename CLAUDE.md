# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

GenAILab is a Generative AI Laboratory for experimenting with and deploying AI solutions in Kubernetes environments. The project focuses on agentic AI systems, model deployment, and MLOps practices.

## Commands

### Development Environment Setup
```bash
# Enter Nix development shell
nix-shell

# Install Python dependencies
poetry install

# Run Python scripts in the poetry environment
poetry run python <script.py>
```

### Kubernetes Operations
```bash
# Deploy components (when manifests are available)
kubectl apply -k kagent
kubectl apply -k kserve
kubectl apply -k openwebui

# Use kustomize for manifest management (available in nix-shell)
kustomize build <directory>
```

### CrewAI Development
```bash
# Run CrewAI examples (when available)
cd contents_crew
crewai run
```

## Architecture

The project is structured as a Kubernetes-native AI platform with the following planned components:

1. **kagent** - Kubernetes Agent component
2. **kserve** - Model serving infrastructure
3. **openwebui** - Web interface for AI interactions
4. **tailscale** - Secure networking layer
5. **contents_crew** - CrewAI multi-agent implementations

Current implementation includes:
- `/usecases/` - Practical AI implementations (e.g., langchain-agents)
- `/prompts/` - AI prompt templates
- Python 3.12 with Poetry for dependency management
- Nix shell providing kustomize_4

## Key Technologies

- **LangChain** - For building AI agents
- **Tavily API** - Web search capabilities (requires TAVILY_API_KEY)
- **Anthropic API** - Claude AI integration (requires ANTHROPIC_API_KEY)
- **Kubernetes** - Container orchestration
- **KServe** - Model serving
- **CrewAI** - Multi-agent orchestration

## Environment Variables

Required API keys:
- `TAVILY_API_KEY` - For web search functionality
- `ANTHROPIC_API_KEY` - For Claude AI integration

## Development Notes

- Python version: 3.12.10
- Use Poetry for all Python dependency management
- Nix shell provides kustomize_4 for Kubernetes manifest management
- Project follows MLOps best practices for Kubernetes deployments