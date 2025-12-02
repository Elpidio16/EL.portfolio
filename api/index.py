#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Vercel Serverless Function - Flask App Entry Point
This file serves as the entry point for Vercel's Python runtime
"""

import sys
import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

# Add the parent directory to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
logger.info(f"Project root: {project_root}")
logger.info(f"Python path: {sys.path[:2]}")

try:
    # Import the Flask application
    logger.info("Attempting to import Flask app...")
    from app.app import app
    logger.info("Successfully imported Flask app")
    
    # Vercel expects this variable to be named 'app'
    # It will automatically call app(environ, start_response) for WSGI
    
except Exception as e:
    logger.error(f"Error importing app: {e}", exc_info=True)
    import traceback
    traceback.print_exc(file=sys.stderr)
    # Create a minimal fallback app
    def app(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        error_msg = f'Error: Could not import Flask application: {str(e)}'
        return [error_msg.encode('utf-8')]


