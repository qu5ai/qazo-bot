name: Qazo Cloud Automation

on:
  schedule:
    - cron: '0 18 * * 4,5'
  workflow_dispatch:

jobs:
  run-bot:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Verify files
        run: ls -la  # هذه الخطوة تطبع لك الملفات الموجودة عشان نتأكد إن qazo_bot.py موجود

      - name: Run Qazo Bot
        run: python qazo_bot.py
