# BuildXvibe

Vibe create your own Web app

run the code using UV

```bash
rm -rf .venv
uv venv
source .venv/bin/activate
uv sync
# or if you use a requirements.txt file:
# uv pip install -r requirements.txt
uv run main.py
# The UserWarning should no longer appear.
```

```bash
uv run core/build.py     
uv run -m core.e2b_runner
```
