# Portfolio Professionnel - Élpidia Lissassi

Un portfolio web moderne et professionnel créé avec Flask, HTML5, CSS3 et JavaScript.

## 🎯 Fonctionnalités

- ✅ Design responsive et moderne
- ✅ Sections: Accueil, À propos, Expérience, Parcours académique, Compétences, Certifications, Contact
- ✅ Formulaire de contact fonctionnel
- ✅ Animations fluides et transitions
- ✅ Navigation fluide (smooth scroll)
- ✅ Dark mode (optionnel)
- ✅ Performance optimisée
- ✅ SEO friendly

## 📋 Prérequis

- Python 3.8+
- pip (gestionnaire de paquets Python)
- Git (pour le déploiement sur Vercel)

## 🚀 Installation locale

1. **Cloner le repository ou télécharger les fichiers**

```bash
cd My_portfolio
```

2. **Créer un environnement virtuel**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Lancer le serveur de développement**

```bash
python app/app.py
```

Le site sera disponible sur `http://localhost:5000`

## 🎨 Personnalisation

Avant de déployer, mettez à jour les informations suivantes dans `app/templates/index.html`:

### Informations personnelles

- **Nom et titre**: Modifiez les sections `.hero-title` et `.hero-subtitle`
- **À propos**: Section `#about`
- **Expérience professionnelle**: Section `#experience`
- **Parcours académique**: Section `#education`
- **Compétences**: Section `#skills`
- **Certifications**: Section `#certifications`
- **Contact**: Section `#contact`

### Ajouter votre photo

1. Placez votre photo de profil dans `app/static/images/`
2. Mettez à jour le chemin dans `index.html`:
```html
<img src="{{ url_for('static', filename='images/votre-photo.jpg') }}" alt="Votre Nom">
```

### Configurer l'email de contact

Mettez à jour `app/app.py`:
```python
EMAIL_ADDRESS = 'votre-email@gmail.com'
EMAIL_PASSWORD = 'votre-mot-de-passe'
```

### Réseaux sociaux

Mettez à jour les liens dans les sections:
- Footer `.social-links`
- Section contact `.social-icons`

## 📦 Structure du projet

```
My_portfolio/
├── app/
│   ├── app.py                 # Application Flask principale
│   ├── templates/
│   │   ├── base.html          # Template de base
│   │   ├── index.html         # Page d'accueil
│   │   ├── 404.html           # Page d'erreur 404
│   │   └── 500.html           # Page d'erreur 500
│   └── static/
│       ├── css/
│       │   └── style.css      # Styles CSS
│       ├── js/
│       │   └── script.js      # Scripts JavaScript
│       └── images/            # Images et photos
├── requirements.txt           # Dépendances Python
├── vercel.json               # Configuration Vercel
├── wsgi.py                   # Point d'entrée WSGI
├── Dockerfile                # Configuration Docker
├── .gitignore                # Fichiers ignorés par Git
└── README.md                 # Ce fichier
```

## 🌐 Déploiement sur Vercel

### Étape 1: Préparer le repository Git

```bash
git init
git add .
git commit -m "Initial commit: portfolio website"
```

### Étape 2: Créer un compte Vercel

Allez sur [vercel.com](https://vercel.com) et créez un compte gratuit.

### Étape 3: Connecter votre repository

1. Poussez votre code sur GitHub:
```bash
git remote add origin https://github.com/votre-username/My_portfolio.git
git branch -M main
git push -u origin main
```

2. Sur Vercel:
   - Cliquez sur "New Project"
   - Connectez votre compte GitHub
   - Sélectionnez votre repository `My_portfolio`
   - Cliquez sur "Import"

### Étape 4: Configurer le déploiement

1. **Framework Preset**: Choisissez "Other"
2. **Build Command**: `pip install -r requirements.txt`
3. **Output Directory**: Laisser vide
4. **Environment Variables** (optionnel):
   - `EMAIL_ADDRESS`: votre-email@gmail.com
   - `EMAIL_PASSWORD`: votre-mot-de-passe

### Étape 5: Déployer

Cliquez sur "Deploy" et attendez que le déploiement soit terminé. Votre site sera disponible sur une URL Vercel.

## 🔧 Configuration Vercel avancée

Si vous avez besoin de configurations spécifiques, modifiez `vercel.json`:

```json
{
    "buildCommand": "pip install -r requirements.txt",
    "env": {
        "FLASK_ENV": "production"
    }
}
```

## 📧 Formulaire de contact

Le formulaire utilise l'endpoint `/api/contact`. Pour le rendre fonctionnel:

1. Configurez vos identifiants email dans `app.py`
2. Modifiez la fonction `contact()` pour envoyer de vrais emails
3. Vous pouvez utiliser `SendGrid`, `Mailgun` ou `SMTP`

## 📱 Responsive Design

Le site est optimisé pour tous les appareils:
- 📱 Mobile (480px+)
- 📱 Tablet (768px+)
- 💻 Desktop (1024px+)

## 🚀 Optimisations de performance

- Minification CSS/JS
- Lazy loading des images
- Compression des assets
- Caching intelligent
- CDN Vercel intégré

## 🔐 Sécurité

- Protection CSRF
- Validation des formulaires
- Headers de sécurité
- HTTPS automatique sur Vercel

## 📚 Technologies utilisées

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Hosting**: Vercel
- **Fonts**: Google Fonts (Poppins, JetBrains Mono)
- **Icons**: Font Awesome 6

## 📝 License

Ce projet est libre d'utilisation pour vos besoins personnels.

## 💡 Conseils supplémentaires

1. **Testez localement** avant de déployer
2. **Utilisez un domaine personnalisé** sur Vercel
3. **Mettez à jour régulièrement** vos expériences et compétences
4. **Demandez des retours** sur votre design
5. **Suivez les tendances** en matière de design web

## 🆘 Troubleshooting

### Le site ne se déploie pas
- Vérifiez que `requirements.txt` est correct
- Assurez-vous que `app.py` est dans le bon dossier
- Consultez les logs de Vercel

### Le formulaire ne fonctionne pas
- Vérifiez les erreurs dans la console du navigateur
- Assurez-vous que l'endpoint `/api/contact` est accessible
- Testez localement avec `python app/app.py`

### Les images ne s'affichent pas
- Vérifiez que les images sont dans `app/static/images/`
- Vérifiez les chemins dans `index.html`
- Utilisez `{{ url_for() }}` pour les URLs

## 📞 Support

Pour plus d'aide:
- Consultez la [documentation Flask](https://flask.palletsprojects.com/)
- Consultez la [documentation Vercel](https://vercel.com/docs)
- Visitez les [tutoriels Python](https://www.python.org/about/gettingstarted/)

---

**Créé avec ❤️ pour votre succès professionnel!**
