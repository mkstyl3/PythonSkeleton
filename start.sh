#!/bin/bash
source .pyvenv/bin/activate
exec .pyvenv/bin/gunicorn -w 3 -b '0.0.0.0:8082' bootstrap:app

