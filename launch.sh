#!/bin/bash

# Change to "my-app" then start npm in background
(cd my-app && npm start &)

# Wait for browser start-up 
sleep 1

# Start Back-End
python3 flask-server/server.py
