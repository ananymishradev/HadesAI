# Hades AI 

A Bare metal agent to learn AI Engineering from scratch. It does not uses frameworks or any plugins. 
It will have an opionionated Eval system and RL environment to evaluate the agent's performance and improve it.

---

### Overview

A user will ask Agent a simple question. 
The agent usesd a tool, effectively pulling in context from the environment. 
The context is present to agent, which decides that it has enough information to answer the user query. 
The agent prints out its answer to the user. 

**LLM** is the brain of the agent. and i am going to use qwen3:0.6b model, locallly deployed on my workstation. 

Although I will still use Deepseek-V4 to evaluate my agent and will create an RL environment for it. 

---

### OpenAI API

We use OpenAI API to run the model remotely.

`base_url` is the URL of the API. Default is `https://api.openai.com/v1`.

`api_key` is the authentication key for the API. 

`model` the name of the model. Default is `qwen-3.0-0.6b`.

`messages` is a list of messages to send to the API. A message is a python dictionary with key-value pairs. 

### Ollama 

We will use Ollama API to run the model locally.

`base_url` is the URL of the API. Default is `http://localhost:11434/v1`.

```bash
ollama pull qwen-3.0-0.6b
ollama run qwen-3.0-0.6b
```

