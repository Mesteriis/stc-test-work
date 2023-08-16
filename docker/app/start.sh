#!/bin/bash
uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port "$APP_PORT"
