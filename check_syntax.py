from html.parser import HTMLParser
import os

# Vérifier le HTML
html_file = 'app/templates/index.html'
try:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parser = HTMLParser()
    parser.feed(content)
    print('✅ HTML - Syntaxe OK')
except Exception as e:
    print(f'❌ HTML - Erreur: {e}')

# Vérifier le CSS basique
css_file = 'app/static/css/style.css'
try:
    with open(css_file, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # Vérifier les accolades
    open_braces = css.count('{')
    close_braces = css.count('}')
    
    if open_braces == close_braces:
        print('✅ CSS - Syntaxe OK')
    else:
        print(f'❌ CSS - Accolades non équilibrées: {{ = {open_braces}, }} = {close_braces}')
except Exception as e:
    print(f'❌ CSS - Erreur: {e}')

# Vérifier les fichiers Python
import ast

files_to_check = ['app/app.py', 'api/wsgi.py']
for file in files_to_check:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            code = f.read()
            ast.parse(code)
        print(f'✅ {os.path.basename(file)} - Syntaxe OK')
    except SyntaxError as e:
        print(f'❌ {os.path.basename(file)} - Erreur: {e}')
    except FileNotFoundError:
        print(f'⚠️ {os.path.basename(file)} - Fichier non trouvé')
