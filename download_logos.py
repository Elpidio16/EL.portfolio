#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script pour télécharger les logos des entreprises
"""
import urllib.request
import os
from pathlib import Path

logos_dir = Path('app/static/images/company-logos')
logos_dir.mkdir(parents=True, exist_ok=True)

# URLs des logos (transparents si possible)
logos = {
    'cellenza.png': 'https://www.cellenza.com/wp-content/uploads/2023/02/Logo-Cellenza-bleu-horizontal.png',
    'devoteam.png': 'https://www.devoteam.com/cdn-cgi/image/width=450,height=200,fit=contain,format=auto/https://www.devoteam.com/themes/custom/devoteam/logo.svg',
    'chanel.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Chanel_logo.svg/1024px-Chanel_logo.svg.png',
    'universite-lome.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Universit%C3%A9_de_Lom%C3%A9_logo.png/220px-Universit%C3%A9_de_Lom%C3%A9_logo.png'
}

for filename, url in logos.items():
    try:
        filepath = logos_dir / filename
        if not filepath.exists():
            print(f"Téléchargement {filename}...")
            urllib.request.urlretrieve(url, filepath)
            print(f"✓ {filename} téléchargé")
        else:
            print(f"✓ {filename} existe déjà")
    except Exception as e:
        print(f"✗ Erreur pour {filename}: {e}")

print("Done!")
