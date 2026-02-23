#!/bin/bash
cd code
gunicorn app:app --bind 0.0.0.0:$PORT
