import os
from pathlib import Path

import ollama


def load_properties(file_path: Path) -> dict[str, str]:
    values: dict[str, str] = {}

    if not file_path.exists():
        return values

    for line in file_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip()

    return values


PROPERTIES = load_properties(Path(__file__).with_name("config.properties"))
MODEL = os.getenv("OLLAMA_MODEL", PROPERTIES.get("OLLAMA_MODEL", "llama3.2"))
OLLAMA_HOST = os.getenv("OLLAMA_HOST", PROPERTIES.get("OLLAMA_HOST", "http://127.0.0.1:11434"))
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
