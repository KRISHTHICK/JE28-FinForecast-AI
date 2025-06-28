import subprocess

def ask_investment_agent(prompt):
    command = f"User wants investment advice: {prompt}"
    result = subprocess.run(["ollama", "run", "tinyllama", command], capture_output=True, text=True)
    return result.stdout.strip()
