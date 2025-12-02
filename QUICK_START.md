# ⚡ Quick Start Guide

Commencez en 5 minutes!

## 🚀 Démarrage Rapide (Local)

### Windows
1. Double-cliquez sur `run.bat`
2. Attendez que ça compile
3. Ouvrez [http://localhost:5000](http://localhost:5000)
4. Voilà! 🎉

### Mac/Linux
```bash
chmod +x run.sh
./run.sh
```
Puis ouvrez [http://localhost:5000](http://localhost:5000)

## 📝 Personnaliser en 5 Minutes

Ouvrez `app/templates/index.html` et changez:

**Ligne ~50** (Votre nom):
```html
<h1 class="hero-title">Votre Nom Ici</h1>
<p class="hero-subtitle">Votre Titre</p>
```

**Ligne ~98** (À propos):
```html
<p>Écrivez votre description...</p>
```

**Ligne ~140** (Vos expériences) - Dupliquée et adaptez:
```html
<div class="timeline-item">
    <div class="timeline-date">Années</div>
    <div class="timeline-content">
        <h3>Votre Poste</h3>
        ...
    </div>
</div>
```

## 🖼️ Ajouter votre Photo

1. Mettez votre photo JPG dans `app/static/images/`
2. Nommez-la `profile.jpg`
3. Rafraîchissez le navigateur (Ctrl+F5)

## 🌐 Déployer sur Vercel

### 1. Git Push (5 min)
```powershell
cd My_portfolio
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/VOTREUSERNAME/my-portfolio.git
git push -u origin main
```

### 2. Vercel Deploy (2 min)
- Allez sur [vercel.com](https://vercel.com)
- Cliquez "Add New" → "Project"
- Sélectionnez `my-portfolio`
- Cliquez "Deploy"

**Prêt!** Votre site est en ligne! 🎊

## 📋 Fichiers Importants

| Fichier | Ce qu'il fait |
|---------|--------------|
| `index.html` | Contenu de votre portfolio |
| `style.css` | Couleurs, layout, design |
| `script.js` | Animations, formulaire |
| `app.py` | Serveur Flask |

## 🎨 Changer les Couleurs

Ouvrez `app/static/css/style.css` ligne ~10:

```css
--primary-color: #6366f1;      /* Bleu indigo - changer ici */
--secondary-color: #ec4899;    /* Rose - et ici */
```

Essayez:
- `#3b82f6` (bleu)
- `#a855f7` (violet)
- `#10b981` (vert)
- `#f97316` (orange)

## 📧 Formulaire de Contact

Le formulaire affiche actuellement un message de succès.

Pour recevoir les vrais emails, consultez `EMAIL_SETUP.md`

## ✅ Checklist

- [ ] Portfolio lancé localement
- [ ] Photo ajoutée
- [ ] Nom et titre personnalisés
- [ ] Expériences modifiées
- [ ] Certifications ajoutées
- [ ] Testé sur mobile (F12)
- [ ] Pushé sur GitHub
- [ ] Déployé sur Vercel
- [ ] URL partagée sur LinkedIn/Twitter

## 🆘 Problèmes?

### "Address already in use"
Le port 5000 est utilisé. Allez sur `app/app.py` et changez:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # 5001 au lieu de 5000
```

### La page est vide
Appuyez sur **Ctrl+Shift+Delete** pour nettoyer le cache
Puis rafraîchissez

### Photo ne s'affiche pas
1. Vérifiez que le fichier existe: `app/static/images/profile.jpg`
2. Vérifiez dans `index.html` ligne ~60 que le chemin est correct

### Vercel dit "Build failed"
Consultez les logs:
1. Dashboard Vercel → Votre Projet
2. Cliquez sur le déploiement échoué
3. Lire les "Build Logs"

## 📚 Docs Complètes

- **Détails complets**: `README.md`
- **Déploiement pas à pas**: `DEPLOYMENT_GUIDE.md`
- **Personnalisation avancée**: `CUSTOMIZATION.md`
- **Email setup**: `EMAIL_SETUP.md`
- **Structure du projet**: `PROJECT_STRUCTURE.md`

## 💡 Prochaines Étapes

1. ✅ Faire fonctionner localement
2. ✅ Personnaliser avec vos infos
3. ✅ Ajouter votre photo
4. ✅ Déployer sur Vercel
5. 🔜 Ajouter domaine personnalisé
6. 🔜 Configurer formulaire email
7. 🔜 Ajouter Google Analytics

## 🎯 Commandes Utiles

```powershell
# Tester localement
python app/app.py

# Vérifier la structure
dir app

# Voir les changements Git
git status

# Pousser sur GitHub
git push

# Arrêter le serveur
Ctrl+C
```

## 📞 Support Rapide

**Question**: Comment changer le titre?
**Réponse**: `index.html` ligne ~51 - `<h1 class="hero-title">`

**Question**: Comment ajouter plus d'expériences?
**Réponse**: Dupliciquez un `<div class="timeline-item">` et adaptez

**Question**: Où est la "barre de navigation"?
**Réponse**: En haut! Elle vient de `base.html` lignes ~20-35

**Question**: Comment qu'ça marche l'email?
**Réponse**: Voir `EMAIL_SETUP.md` pour 3 options

## 🚀 Résumé Ultra-Rapide

```bash
# Étape 1: Lancez localement
run.bat  # ou run.sh

# Étape 2: Personnalisez
Ouvrez index.html et changez le contenu

# Étape 3: Pushé sur GitHub
git add . && git commit -m "My portfolio" && git push

# Étape 4: Déployez sur Vercel
Dashboard Vercel → Import → Deploy

# Prêt! 🎉
```

---

**Bonne chance avec votre portfolio! 🚀**

Des questions? Consultez les autres guides!

Dernière mise à jour: Décembre 2025
