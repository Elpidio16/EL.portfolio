#!/usr/bin/env python
"""
Vercel Serverless Function Entry Point
"""
import os
import sys
from pathlib import Path

# Add parent directory to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import Flask app
from app.app import app

# Vercel expects the Flask app to be exposed as 'app'

