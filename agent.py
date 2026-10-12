import subprocess
from tools import calculator, weather_api, joke
from prompts import AGENT_PROMPT

OLLAMA_PATH = "ollama"  # or full path to ollama.exe if needed

def call_ollama(prompt, model="llama2"):
    try:
        result = subprocess.run(
            [OLLAMA_PATH, "run", model, prompt, "--format", "json"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error calling Ollama: {e}\nstdout: {e.stdout}\nstderr: {e.stderr}"

def llm_decision(prompt: str) -> str:
    """
    Ask Ollama which tool to use
    """
    full_prompt = AGENT_PROMPT + "\n" + prompt
    response = call_ollama(full_prompt)
    return response

def agent(prompt: str) -> str:
    decision = llm_decision(prompt)
    print("LLM decision:", decision)

    if decision.startswith("calculator:"):
        arg = decision.split(":", 1)[1].strip()
        return calculator(arg)
    elif decision.startswith("weather_api:"):
        arg = decision.split(":", 1)[1].strip()
        return weather_api(arg)
    elif decision.startswith("joke:"):
        return joke(prompt)
    else:
        # fallback: just return the raw LLM response
        return decision

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        output = agent(user_input)
        print("Agent:", output)
