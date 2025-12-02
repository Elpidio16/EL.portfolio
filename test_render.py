#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.app import app

with app.app_context():
    try:
        from flask import render_template
        html = render_template('index.html')
        print("SUCCESS: Template rendered successfully")
        print(f"HTML length: {len(html)} characters")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
