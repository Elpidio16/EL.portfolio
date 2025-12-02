# 🚀 Guide Complet de Déploiement sur Vercel

Ce guide vous accompagnera étape par étape pour déployer votre portfolio sur Vercel.

## ⚡ Avant de Commencer

Vous aurez besoin de:
- Un compte GitHub (gratuit)
- Un compte Vercel (gratuit)
- L'application Git installée sur votre ordinateur
- VS Code ou un éditeur de texte

## 🔧 Étape 1: Installer Git

### Windows
1. Téléchargez Git depuis [git-scm.com](https://git-scm.com)
2. Installez avec les paramètres par défaut
3. Redémarrez votre ordinateur
4. Ouvrez PowerShell et tapez: `git --version`

### Vérifier l'installation
```powershell
git --version
```

## 👤 Étape 2: Configurer Git

Ouvrez PowerShell et exécutez:

```powershell
git config --global user.name "Votre Nom"
git config --global user.email "votre-email@gmail.com"
```

## 📦 Étape 3: Initialiser le Repository Git

Dans le dossier de votre portfolio (PowerShell):

```powershell
cd C:\Users\ElpidioLissassi\Documents\My_portfolio
git init
git add .
git commit -m "Initial commit: portfolio website"
```

Vous devriez voir quelque chose comme:
```
[main (root-commit) abc1234] Initial commit: portfolio website
 15 files changed, 5000 insertions(+)
```

## 🐙 Étape 4: Créer un Repository GitHub

1. Allez sur [github.com](https://github.com)
2. Connectez-vous (ou créez un compte gratuit)
3. Cliquez sur le "+" en haut à droite → "New repository"
4. Nommez-le: `my-portfolio` ou similaire
5. **Important**: Laissez tous les champs vides (ne l'initialisez pas)
6. Cliquez sur "Create repository"

## 🔗 Étape 5: Connecter Git à GitHub

Copiez et exécutez les commandes que GitHub vous montre (dans PowerShell):

```powershell
git remote add origin https://github.com/VOTRE_USERNAME/my-portfolio.git
git branch -M main
git push -u origin main
```

**Entrez vos identifiants GitHub quand demandé.**

Après cela, votre code sera sur GitHub ✅

## 🎯 Étape 6: Créer un Compte Vercel

1. Allez sur [vercel.com](https://vercel.com)
2. Cliquez sur "Sign Up"
3. Choisissez "Continue with GitHub"
4. Autorisez Vercel à accéder à votre GitHub
5. Complétez votre profil

## 📤 Étape 7: Déployer sur Vercel

### Option A: Via l'interface web (Recommandée)

1. Connectez-vous sur [vercel.com](https://vercel.com/dashboard)
2. Cliquez sur "Add New" → "Project"
3. Cherchez votre repository `my-portfolio`
4. Cliquez sur "Import"
5. **Configuration du Projet**:
   - Framework: `Other`
   - Root Directory: `.`
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: Laisser vide
   - Install Command: Laisser vide

6. Cliquez sur "Deploy"

**Vercel va maintenant construire et déployer votre site!** ⏳

### Option B: Via Vercel CLI (Avancé)

```powershell
npm install -g vercel
vercel login
vercel --prod
```

## ✅ Étape 8: Vérifier le Déploiement

1. Attendez que Vercel termine la construction
2. Vous verrez une URL comme: `https://my-portfolio-abc123.vercel.app`
3. Cliquez sur le lien pour visiter votre site
4. Vérifiez que tout fonctionne correctement

## 🎁 Bonus: Configurer un Domaine Personnalisé

### Avec un domaine que vous possédez

1. Sur Vercel: Dashboard → Votre Projet → Settings
2. Allez à l'onglet "Domains"
3. Entrez votre domaine (ex: `monportfolio.com`)
4. Suivez les instructions DNS
5. Attendez que le DNS se propage (jusqu'à 48h)

### Acheter un domaine

**Fournisseurs recommandés:**
- [Namecheap.com](https://namecheap.com) - Bon marché
- [Google Domains](https://domains.google) - Simple
- [OVH](https://www.ovh.com) - Français
- [Gandi](https://www.gandi.net) - Français

**Prix:** À partir de 5-10€ par an

## 🔄 Étape 9: Mises à Jour Futures

Quand vous modifiez votre portfolio:

```powershell
git add .
git commit -m "Description de la modification"
git push
```

Vercel redéploiera automatiquement votre site! 🎉

## 🐛 Troubleshooting

### "Build failed" ou "Deployment error"

**Solution 1**: Vérifiez `requirements.txt`
```powershell
cat requirements.txt
```

Devrait contenir:
```
Flask==3.0.0
Werkzeug==3.0.1
Jinja2==3.1.2
MarkupSafe==2.1.3
click==8.1.7
itsdangerous==2.1.2
python-dotenv==1.0.0
gunicorn==21.2.0
```

**Solution 2**: Vérifiez les logs Vercel
- Allez sur votre Projet → Deployments
- Cliquez sur le déploiement échoué
- Consultez les "Build Logs"

### "Module not found" ou "ImportError"

Assurez-vous que `requirements.txt` contient toutes les dépendances:
```powershell
pip freeze > requirements.txt
```

### Le site affiche une page vide

1. Vérifiez les chemins des fichiers
2. Contrôlez les logs navigateur (F12)
3. Redéployez: `git push`

### Le formulaire de contact ne fonctionne pas

C'est normal pour une première configuration!

Pour l'activer:
1. Configurez les variables d'environnement Vercel
2. Mettez à jour `app.py` pour utiliser l'email
3. Utilisez un service comme SendGrid ou Mailgun

## 📊 Monitoring et Analytics

### Accéder aux analytics Vercel
1. Dashboard Vercel → Votre Projet
2. Onglet "Analytics"
3. Consultez les visites et performances

### Ajouter Google Analytics
1. Créez un compte [Google Analytics](https://analytics.google.com)
2. Récupérez votre ID de suivi (GA-XXXXX ou G-XXXXX)
3. Ajoutez dans `base.html` avant `</head>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXX');
</script>
```

## 🔐 Variables d'Environnement

Si vous utilisiez des variables `.env` localement:

1. Sur Vercel: Projet → Settings → Environment Variables
2. Ajoutez les mêmes variables
3. Redéployez

Exemple:
- `EMAIL_ADDRESS`: votre-email@gmail.com
- `EMAIL_PASSWORD`: votre-mot-de-passe
- `SECRET_KEY`: votre-cle-secrete

## 📱 Tester sur Mobile

1. Ouvrez votre URL Vercel sur votre téléphone
2. Vérifiez que le design responsive fonctionne
3. Testez les formulaires et les clics

Ou utilisez Chrome DevTools (F12) → Mode téléphone

## 🎉 Félicitations!

Votre portfolio est en ligne! 

### Prochaines étapes:
- [ ] Testez le site complet
- [ ] Partagez le lien sur vos réseaux sociaux
- [ ] Ajoutez votre URL Vercel à votre CV
- [ ] Mettez à jour vos infos LinkedIn
- [ ] Demandez des retours

## 📞 Besoin d'aide?

**Ressources:**
- [Documentation Vercel](https://vercel.com/docs)
- [Documentation Flask](https://flask.palletsprojects.com/)
- [GitHub Docs](https://docs.github.com)
- Stack Overflow pour les questions spécifiques

**Commandes utiles:**
```powershell
# Vérifier votre connexion Git
git status

# Voir l'historique des commits
git log --oneline

# Voir la configuration Git
git config --list

# Tester localement
python app/app.py

# Vérifier les dépendances
pip list
```

---

**Créé pour vous aider à mettre en ligne votre portfolio professionnel! 🚀**

Dernière mise à jour: Décembre 2025
