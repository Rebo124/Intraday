# Zerodha NIFTY Auto Trader

## Run locally
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
cp .env.template .env  # fill with your credentials
python main.py
```

## Run with Docker
```bash
docker build -t zerodha-nifty-bot .
docker run --env-file .env zerodha-nifty-bot
```

## Run with GitHub Actions
- Go to GitHub repo → Settings → Secrets → Actions
- Add `API_KEY`, `API_SECRET`, `ACCESS_TOKEN`
- Workflow file is in `.github/workflows/run.yml`
