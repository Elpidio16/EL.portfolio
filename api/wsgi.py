#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Vercel Serverless Handler - WSGI Entry Point
This file handles all incoming requests for Vercel
"""
import sys
import os
import logging
from pathlib import Path

# Configure logging first
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)

# Add the project root to the path
# api/wsgi.py -> api -> project_root
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logger.info(f"Project root: {project_root}")
logger.info(f"Python path: {sys.path[0]}")

try:
    # Import the Flask app
    logger.info("Importing Flask app...")
    from app.app import app
    logger.info("✓ Flask app imported successfully")
    logger.info(f"  Static folder: {app.static_folder}")
    logger.info(f"  Template folder: {app.template_folder}")
    
except Exception as e:
    logger.error(f"✗ Failed to import Flask app: {e}", exc_info=True)
    
    # Create a fallback WSGI app
    def app(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        
        error_msg = f"Error loading Flask app: {str(e)}\n"
        error_msg += f"Project root: {project_root}\n"
        error_msg += f"App folder exists: {(project_root / 'app').exists()}\n"
        error_msg += f"App.py exists: {(project_root / 'app' / 'app.py').exists()}\n"
        
        return [error_msg.encode('utf-8')]

# This is what Vercel calls
# The WSGI interface
if __name__ == '__main__':
    import asyncio
    app.run(debug=False, host='0.0.0.0', port=5000)

