#!/usr/bin/env bash
# Robust entrypoint: start uvicorn and streamlit, forward signals and wait
set -euo pipefail

# If a virtual env is present and activate script exists, source it (useful in some dev setups)
if [ -f "/app/.venv/bin/activate" ]; then
	# shellcheck disable=SC1091
	source /app/.venv/bin/activate
fi

UVICORN_MODULE=${UVICORN_MODULE:-backend.api:app}
UVICORN_HOST=${UVICORN_HOST:-0.0.0.0}
UVICORN_PORT=${UVICORN_PORT:-8000}
STREAMLIT_SCRIPT=${STREAMLIT_SCRIPT:-frontend/app.py}
STREAMLIT_PORT=${STREAMLIT_PORT:-8501}
STREAMLIT_ADDR=${STREAMLIT_ADDR:-0.0.0.0}

PIDS=""

start_uvicorn() {
	echo "[entrypoint] Starting uvicorn ($UVICORN_MODULE) on $UVICORN_HOST:$UVICORN_PORT"
	uvicorn "$UVICORN_MODULE" --host "$UVICORN_HOST" --port "$UVICORN_PORT" &
	PIDS="$PIDS $!"
}

start_streamlit() {
	echo "[entrypoint] Starting streamlit ($STREAMLIT_SCRIPT) on $STREAMLIT_ADDR:$STREAMLIT_PORT"
	streamlit run "$STREAMLIT_SCRIPT" --server.port "$STREAMLIT_PORT" --server.address "$STREAMLIT_ADDR" &
	PIDS="$PIDS $!"
}

term_handler() {
	echo "[entrypoint] Caught termination signal, forwarding to children..."
	for pid in $PIDS; do
		if kill -0 "$pid" 2>/dev/null; then
			kill -TERM "$pid" || true
		fi
	done
	wait
	exit 0
}

trap term_handler SIGTERM SIGINT

# Start services
start_uvicorn
start_streamlit

# Wait for children
for pid in $PIDS; do
	wait "$pid" || true
done