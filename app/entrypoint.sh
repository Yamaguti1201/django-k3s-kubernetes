#!/usr/bin/env bash
set -e

echo "[entrypoint] Aguardando MySQL em ${DB_HOST:-mysql-service}:${DB_PORT:-3306}..."

python - <<'PY'
import os
import sys
import time
import pymysql

host = os.environ.get("DB_HOST", "mysql-service")
port = int(os.environ.get("DB_PORT", "3306"))
user = os.environ.get("DB_USER", "django_user")
password = os.environ.get("DB_PASSWORD", "django_pass")
database = os.environ.get("DB_NAME", "django_db")

for attempt in range(1, 61):
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            connect_timeout=3,
        )
        conn.close()
        print(f"[entrypoint] MySQL disponível na tentativa {attempt}!")
        sys.exit(0)
    except Exception as exc:
        print(f"[entrypoint] Tentativa {attempt}/60 falhou: {exc}")
        time.sleep(2)

print("[entrypoint] Tempo esgotado aguardando MySQL.", file=sys.stderr)
sys.exit(1)
PY

echo "[entrypoint] Aplicando migrations do Django..."
python manage.py migrate --noinput

echo "[entrypoint] Iniciando Gunicorn na porta 8000..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --keep-alive 0 \
    --access-logfile - \
    --error-logfile -
