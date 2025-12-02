#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Vercel Serverless Function - Flask App Entry Point
This file serves as the entry point for Vercel's Python runtime
"""

import sys
import os
from pathlib import Path

# Add the parent directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    # Import the Flask application
    from app.app import app
    
    # Vercel expects this variable to be named 'app'
    # It will automatically call app(environ, start_response) for WSGI
    
except ImportError as e:
    print(f"Error importing app: {e}", file=sys.stderr)
    # Create a minimal fallback app
    def app(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [b'Error: Could not import Flask application']


