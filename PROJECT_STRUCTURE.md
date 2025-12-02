# 📁 Structure du Projet

```
My_portfolio/
│
├── 📄 README.md                    # Guide principal du projet
├── 📄 DEPLOYMENT_GUIDE.md          # Guide complet de déploiement Vercel
├── 📄 CUSTOMIZATION.md             # Guide de personnalisation
├── 📄 EMAIL_SETUP.md               # Configuration du formulaire de contact
├── 📄 PROJECT_STRUCTURE.md         # Ce fichier
│
├── 📄 requirements.txt             # Dépendances Python (Flask, Gunicorn, etc.)
├── 📄 vercel.json                  # Configuration pour Vercel
├── 📄 package.json                 # Métadonnées du projet
├── 📄 Dockerfile                   # Configuration Docker (optionnel)
├── 📄 wsgi.py                      # Point d'entrée pour serveurs WSGI
│
├── 📄 .gitignore                   # Fichiers ignorés par Git
├── 📄 .env.example                 # Template pour variables d'environnement
│
├── 🚀 run.bat                      # Script de démarrage (Windows)
├── 🚀 run.sh                       # Script de démarrage (Mac/Linux)
│
└── 📁 app/                         # Application Flask principale
    │
    ├── 📄 app.py                   # Application Flask (routes, API)
    │
    ├── 📁 templates/               # Templates HTML (Jinja2)
    │   ├── 📄 base.html            # Template de base (layout)
    │   ├── 📄 index.html           # Page d'accueil (portfolio)
    │   ├── 📄 404.html             # Page d'erreur 404
    │   └── 📄 500.html             # Page d'erreur 500
    │
    └── 📁 static/                  # Fichiers statiques
        ├── 📁 css/
        │   └── 📄 style.css        # Styles CSS (couleurs, layout, animations)
        │
        ├── 📁 js/
        │   └── 📄 script.js        # JavaScript (navigation, formulaires, animations)
        │
        └── 📁 images/
            ├── 📄 profile.jpg      # Votre photo de profil
            └── 📄 favicon.ico      # Icône du site (à ajouter)
```

## 📋 Détails des Fichiers

### 📄 Racine du Projet

| Fichier | Description |
|---------|-------------|
| `README.md` | Guide principal avec features et installation |
| `DEPLOYMENT_GUIDE.md` | Étapes complètes pour déployer sur Vercel |
| `CUSTOMIZATION.md` | Comment personnaliser avec vos infos |
| `EMAIL_SETUP.md` | Configuration du formulaire de contact |
| `requirements.txt` | Liste des dépendances Python |
| `vercel.json` | Configuration pour le déploiement Vercel |
| `package.json` | Métadonnées du projet |
| `Dockerfile` | Configuration Docker (optionnel) |
| `wsgi.py` | Point d'entrée serveur WSGI |
| `.gitignore` | Fichiers à ne pas pusher sur Git |
| `.env.example` | Template des variables d'environnement |
| `run.bat` | Script pour lancer localement (Windows) |
| `run.sh` | Script pour lancer localement (Mac/Linux) |

### 🎯 Application Flask (`app/`)

#### `app.py` - Cœur de l'application
```
Routes principales:
- GET /                     → Page d'accueil (index.html)
- GET /api/contact          → Endpoint pour formulaire (POST)
- GET /api/download-cv      → Télécharger CV (à implémenter)
- 404                       → Page d'erreur 404
- 500                       → Page d'erreur 500

Configuration:
- Flask app initialization
- Error handlers
- API endpoints
- Static/Template directories
```

#### 📁 `templates/` - Pages HTML

| Fichier | Description |
|---------|-------------|
| `base.html` | Template parent avec navbar, footer, structure |
| `index.html` | Page principale avec toutes les sections |
| `404.html` | Page affichée si URL non trouvée |
| `500.html` | Page affichée en cas d'erreur serveur |

#### 📁 `static/css/` - Styles

| Fichier | Description |
|---------|-------------|
| `style.css` | Tous les styles du site (2000+ lignes) |
| | - Variables CSS (couleurs, fonts) |
| | - Responsive design (mobile, tablet, desktop) |
| | - Animations et transitions |
| | - Sections: hero, about, experience, etc. |

#### 📁 `static/js/` - JavaScript

| Fichier | Description |
|---------|-------------|
| `script.js` | Interactivité et logique côté client |
| | - Navigation et menu hamburger |
| | - Formulaire de contact |
| | - Animations au scroll |
| | - Dark mode |
| | - Compteur statistiques |

#### 📁 `static/images/` - Médias

| Fichier | Description |
|---------|-------------|
| `profile.jpg` | Votre photo de profil (300x400px min) |
| `favicon.ico` | Icône du site (à créer) |

## 🔄 Flux de Requête

```
Visiteur accède à votre domaine
    ↓
Vercel route vers Flask
    ↓
Flask exécute app.py
    ↓
Route "/" est appelée
    ↓
render_template('index.html')
    ↓
base.html chargé + index.html
    ↓
CSS appliqué (style.css)
    ↓
JS exécuté (script.js)
    ↓
Page affichée dans le navigateur
    ↓
Utilisateur voit votre portfolio! 🎉
```

## 📦 Dépendances Python

```
Flask==3.0.0              # Framework web
Werkzeug==3.0.1          # Utilities pour Flask
Jinja2==3.1.2            # Template engine
MarkupSafe==2.1.3        # Sécurité templates
click==8.1.7             # CLI toolkit
itsdangerous==2.1.2      # Signing/verification
python-dotenv==1.0.0     # Variables d'environnement
gunicorn==21.2.0         # Production WSGI server
```

## 🎨 Sections du Portfolio (index.html)

| Section | Contenu |
|---------|---------|
| Hero | Titre, subtitle, photo, CTA |
| About | Texte, stats, image |
| Experience | Timeline des expériences pro |
| Education | Cartes formations académiques |
| Skills | Catégories de compétences |
| Certifications | Cartes des certifications |
| Contact | Formulaire + infos contact |

## 🔐 Variables d'Environnement

```
FLASK_ENV=production          # Mode production sur Vercel
FLASK_DEBUG=False            # Pas de debug mode
EMAIL_ADDRESS                # Votre email (optionnel)
EMAIL_PASSWORD               # Mot de passe app (optionnel)
SENDGRID_API_KEY             # Clé SendGrid (optionnel)
SECRET_KEY                   # Clé secrète Flask
```

## 🚀 Points d'Entrée

### Développement Local
```
python app/app.py
```
ou
```
run.bat  (Windows)
run.sh   (Mac/Linux)
```

### Production Vercel
```
wsgi.py → gunicorn
```

Vercel lit `vercel.json` et exécute:
```
Build: pip install -r requirements.txt
Serve: gunicorn --bind 0.0.0.0:5000 app:app
```

## 📊 Taille du Projet

```
Total: ~500KB
├── HTML Templates: ~50KB
├── CSS: ~100KB
├── JavaScript: ~30KB
├── Python Code: ~10KB
└── Configuration: ~10KB
```

## 🔄 Cycle de Développement

1. **Local**: Modifier fichiers → `python app/app.py` → Tester
2. **Git**: `git add .` → `git commit` → `git push`
3. **Vercel**: Auto-détecte le push → Build → Deploy
4. **Production**: Accessible via votre URL

## 📱 Responsive Breakpoints

```css
Desktop:  1024px+
Tablet:   768px - 1023px
Mobile:   480px - 767px
Petit:    < 480px
```

## 🎯 Pour Aller Plus Loin

### Ajouter Blog
- Créer `blog/` avec posts Markdown
- Route `/blog` dans app.py
- Template `blog.html`

### Ajouter Projets
- Créer `projects/` avec galerie
- Images + descriptions
- Filtrage par technologie

### Analytics
- Google Analytics
- Vercel Analytics (gratuit)

### Email
- SendGrid (gratuit)
- Mailgun (gratuit)
- Gmail SMTP

### Domaine Personnalisé
- Acheter sur Namecheap, Gandi, OVH
- Configurer DNS
- HTTPS automatique

## ✅ Checklist de Déploiement

- [ ] Code personnalisé
- [ ] Photo de profil ajoutée
- [ ] `.env` configuré (optionnel)
- [ ] Testé localement
- [ ] Push sur GitHub
- [ ] Import sur Vercel
- [ ] Domaine configuré (optionnel)
- [ ] Email configuré (optionnel)

## 🆘 Où Trouver Quoi

**Veux personnaliser...**
- ...ton nom? `index.html` ligne ~50
- ...ta photo? `static/images/profile.jpg`
- ...tes couleurs? `style.css` lignes ~1-20
- ...tes experiences? `index.html` ligne ~140-210
- ...tes certifications? `index.html` ligne ~345-400
- ...tes réseaux? `base.html` lignes ~40-50

**Veux améliorer...**
- ...la navigation? `script.js` lignes ~1-50
- ...le formulaire? `script.js` lignes ~70-150
- ...les animations? `style.css` lignes ~1800-1900
- ...la responsive? `style.css` lignes ~2000+

---

**Créé pour vous guider à travers la structure! 🗂️**

Dernière mise à jour: Décembre 2025
