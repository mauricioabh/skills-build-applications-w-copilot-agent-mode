OctoFit Tracker backend

Setup (from repository root):

1. Create the venv (already done in this branch):

```bash
python3 -m venv octofit-tracker/backend/venv
```

2. Activate the venv:

```bash
source octofit-tracker/backend/venv/bin/activate
```

3. Install requirements:

```bash
pip install -r octofit-tracker/backend/requirements.txt
```

4. Run Django checks and the dev server:

```bash
python octofit-tracker/backend/manage.py check
python octofit-tracker/backend/manage.py runserver 8000
```

Notes:
- The project uses `djongo` in `settings.py` as a development convenience; configure your MongoDB client settings as needed.
- Don't forget to set a secure `SECRET_KEY` and `DEBUG = False` in production.
