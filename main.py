import os

import ollama


MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
CLIENT = ollama.Client(host=OLLAMA_HOST)


def main() -> None:
    print(f"Chat Ollama avec {MODEL}. Tapez 'quit' pour sortir.")
    messages: list[dict[str, str]] = []

    while True:
        try:
            prompt = input("Vous : ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if prompt.lower() in {"quit", "exit"}:
            break
        if not prompt:
            continue

        messages.append({"role": "user", "content": prompt})
        response = CLIENT.chat(model=MODEL, messages=messages)
        answer = response["message"]["content"]
        messages.append({"role": "assistant", "content": answer})
        print(f"Ollama : {answer}\n")


if __name__ == "__main__":
    main()
