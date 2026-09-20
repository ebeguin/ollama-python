# ollama-python

Petit client de chat Python pour Ollama.

## Prerequis

1. Installer Ollama depuis https://ollama.com/download.
2. Demarrer Ollama.
3. Telecharger un modele :

```powershell
ollama pull llama3.2
```

## Installation

Dans PowerShell :

```powershell
cd C:\Users\ebegu\Documents\ollama-python
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -e .
```

## Lancement

```powershell
python main.py
```

Le modele utilise par defaut est `llama3.2`. Pour en choisir un autre :

```powershell
$env:OLLAMA_MODEL = "mistral"
python main.py
```
