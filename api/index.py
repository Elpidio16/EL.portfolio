#!/usr/bin/env python
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.app import app

# Export the app as the handler for Vercel
handler = app
