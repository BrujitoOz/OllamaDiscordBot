# OllamaDiscordBot

Flexible Discord bot powered by the Ollama LLM platform, designed to interact with users using any Ollama model specified via environment variables. Ideal for engaging community conversations and providing dynamic, model-driven responses.

## Features

- **Customizable Models**: Use any model available in your Ollama instance by specifying the model name via environment variables.
- **Interactive Responses**: The bot responds to messages, mentions, and replies in Discord channels and DMs.
- **Docker Support**: Easily deploy the bot using Docker with configurable options for different environments.

## Prerequisites

- **Python 3.10+**
- **Discord Developer Account**: To create a bot and obtain a token.
- **Ollama Installed Locally**: Ensure that Ollama is running and accessible from your bot.

## Installation

### Clone the Repository
```bash
git clone https://github.com/tu_usuario/OllamaDiscordBot.git
cd OllamaDiscordBot
```
### Create a Virtual Environment (Optional)
#### Option 1: Using `venv`

##### On Windows (CMD or PowerShell)
1. **Create the virtual environment:**
    ```cmd
    python -m venv venv
    ```
2. **Activate the virtual environment:**
    - **Command Prompt:**
      ```cmd
      venv\Scripts\activate
      ```
    - **PowerShell:**
      ```powershell
      .\venv\Scripts\Activate.ps1
      ```

##### On macOS/Linux (Bash)
1. **Create the virtual environment:**
    ```bash
    python3 -m venv venv
    ```
2. **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```

#### Option 2: Using `conda`

1. **Create the conda environment:**
    ```bash
    conda create --name myenv python=3.10
    ```
2. **Activate the conda environment:**
    ```bash
    conda activate myenv
    ```

#### Deactivating the Environment
- **For `venv`:** Run `deactivate`.
- **For `conda`:** Run `conda deactivate`.

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration
### Environment Variables
Create a .env file in the root directory of your project with the following content:
#### On Windows (CMD):
```bash
set DISCORD_BOT_TOKEN=your_discord_bot_token
set OLLAMA_MODEL_NAME=your_model_name
set OLLAMA_PORT=11434 # Change if your Ollama instance is using a different port
```
#### On Windows (PowerShell):
```bash
$env:DISCORD_BOT_TOKEN="your_discord_bot_token"
$env:OLLAMA_MODEL_NAME="your_model_name"
$env:OLLAMA_PORT="11434"
```
#### On Linux/MacOS (Bash):
```bash
export DISCORD_BOT_TOKEN="your_discord_bot_token"
export OLLAMA_MODEL_NAME="your_model_name"
export OLLAMA_PORT="11434"
```

- **DISCORD_BOT_TOKEN**: The token for your Discord bot.
- **OLLAMA_MODEL_NAME**: The name of the model you want to use from your Ollama instance.
- **OLLAMA_PORT**: The port where Ollama is running (default is 11434).

### Running Locally
After configuring your .env file, you can run the bot locally:
```bash
python app.py
```

## Docker Deployment
### Build the Docker Image
```bash
docker build -t ollama-discord-bot .
```
### Run the Docker Container
```bash
docker run -d --name ollama-bot \
  -e DISCORD_BOT_TOKEN='your_discord_bot_token' \
  -e OLLAMA_MODEL_NAME='your_model_name' \
  -e OLLAMA_PORT='11434' \
  ollama-discord-bot
```

This command runs the bot in a Docker container with the specified environment variables.

## Stopping the Container
To stop the running container:
```bash
docker stop ollama-bot
```
## Usage
Once the bot is running, it will respond to the following interactions:
- **Mentions**: Mention the bot with @BotName and it will reply to your message.
- **Replies**: Reply to one of the bot's messages, and it will continue the conversation.
- **Direct Messages**: Send the bot a private message, and it will respond directly.

The bot can be configured to use any model available in your Ollama instance, making it versatile for different use cases.

## Troubleshooting
- **Bot not responding**: Ensure that the bot is online in Discord and that the token and model name are correctly set in the environment variables.
- **Docker networking issues**: If using Docker, make sure that the Docker container can access the Ollama instance on your host machine.

