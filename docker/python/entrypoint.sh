#!/usr/bin/env bash
gunicorn --reload delegadomotos.wsgi -c /usr/src/delegadomotos/gunicorn.py -b 0.0.0.0:8888