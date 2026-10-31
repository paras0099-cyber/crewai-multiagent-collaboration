# CrewAI Multi-Agent Collaboration

> **Today I learned how to build multi-agent AI workflows using CrewAI, orchestrating a researcher and technical writer agent with Google Gemini.**

## 📌 Overview
This repository demonstrates how to build an autonomous multi-agent pipeline using [CrewAI](https://github.com/crewAIInc/crewAI):
- **Researcher Agent:** Conducts technical research and identifies verified facts on a given topic.
- **Writer Agent:** Transforms research insights into a clean, engaging 2-paragraph summary suitable for social media.
- **Crew Orchestration:** Coordinates sequential task execution with input interpolation and shared context.
- **LLM Backbone:** Powered by Google Gemini through CrewAI's `LLM` interface.

## 🛠️ Requirements
- Python `>=3.10, <3.14` (recommended: Python 3.11 or 3.12)
- Dependencies: `crewai`, `python-dotenv`

## 🚀 Setup & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/paras0099-cyber/crewai-multiagent-collaboration.git
   cd crewai-multiagent-collaboration
   ```

2. Create a virtual environment and install packages:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install crewai python-dotenv
   ```

3. Add your Gemini API key in a `.env` file:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. Run the crew:
   ```bash
   python crew_ai.py
   ```
