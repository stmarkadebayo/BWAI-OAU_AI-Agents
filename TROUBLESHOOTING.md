# 🛠️ Troubleshooting Guide

Running into issues? Don't panic — most problems at a workshop are one of these. Work through them in order.

---

## 🐍 Python Issues

### `python: command not found` or wrong version
ADK requires **Python 3.10 or higher**. Check your version:
```bash
python3 --version
```
If you see anything below 3.10, ask the workshop facilitator for help or use [Google Cloud Shell](https://shell.cloud.google.com) in your browser — it comes with Python 3.10+ pre-installed.

### `ModuleNotFoundError: No module named 'google.adk'`
Your virtual environment is not activated. Run:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```
Then re-run your command. You should see `(.venv)` at the start of your terminal prompt.

### `pip install` fails
Try upgrading pip first:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ☁️ Google Cloud / Vertex AI Issues

### `gcloud: command not found`
You need to install the Google Cloud CLI first:
```bash
# macOS (with Homebrew)
brew install google-cloud-sdk

# Linux / WSL
curl https://sdk.cloud.google.com | bash
exec -l $SHELL   # Restart your shell
```
For Windows, download the installer from [cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install).

**Alternative:** Use [Google Cloud Shell](https://shell.cloud.google.com) — it has `gcloud` pre-installed.

### `PERMISSION_DENIED` or `Vertex AI API has not been enabled`
1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Make sure you've selected the correct project (check the dropdown at the top)
3. Search for **"Vertex AI API"** and click **Enable**
4. If you see billing errors, make sure your credits are linked to this project

### `gcloud auth` token issues / `Request had invalid authentication credentials`
Your authentication token may have expired. Re-authenticate:
```bash
gcloud auth application-default login
```
Follow the browser prompt to re-authorize.

### `RESOURCE_EXHAUSTED` / Rate limit errors
This happens when too many people hit Vertex AI at the same time. Solutions:
1. **Wait 30 seconds** and try again
2. Switch your model to `gemini-2.0-flash` (faster, lower limits) in `agent.py`
3. Ask the facilitator if there are multiple project IDs to distribute load

---

## 🌐 ADK Web UI Issues

### `Address already in use` (port 8000)
Another process is using port 8000. Either kill it or use a different port:
```bash
adk web --port 8001 01_beginner/01_foundation_agent
```
Then open `http://localhost:8001` instead.

### Web UI shows but agent doesn't respond
1. Check your terminal for error messages — they appear in the terminal where `adk web` is running
2. Verify your `.env` file has the correct `GOOGLE_CLOUD_PROJECT` value
3. Make sure `GOOGLE_GENAI_USE_VERTEXAI=1` is set in `.env`

### `ConnectionRefusedError` when opening localhost
Make sure you're in the `labs/` directory when running `adk web`:
```bash
cd Building-AI-Agents/labs
adk web 01_beginner/01_foundation_agent
```

---

## 💻 Windows-Specific Issues

### PowerShell: `running scripts is disabled on this system`
Run this once in PowerShell (as Administrator):
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
Then try activating the venv again.

### Path separator issues
On Windows, use backslashes in file paths but forward slashes still work with `adk web`:
```bash
adk web 01_beginner/01_foundation_agent
```

---

## 🆘 Still Stuck?

1. **Google Cloud Shell** ([shell.cloud.google.com](https://shell.cloud.google.com)) — Everything is pre-installed. Clone the repo there and run the labs.
2. **Ask the facilitator** — That's what they're here for!
3. **Check the ADK docs** — [google.github.io/adk-docs](https://google.github.io/adk-docs/)
