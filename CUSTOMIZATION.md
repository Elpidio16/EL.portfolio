# Guide de Personnalisation du Portfolio

Voici comment personnaliser votre portfolio avec vos informations.

## 📝 Étape 1: Informations de Base

### Ouvrez `app/templates/index.html`

1. **Ligne ~50-60 (Section Héros)**
   ```html
   <h1 class="hero-title">Élpidia Lissassi</h1>
   <p class="hero-subtitle">Cloud Architect & DevOps Engineer</p>
   <p class="hero-description">Spécialiste en infrastructure cloud, automatisation et solutions d'entreprise</p>
   ```

2. **Votre Photo**
   - Placez votre photo dans `app/static/images/profile.jpg`
   - Ou modifiez le chemin si votre image a un autre nom

## 📌 Étape 2: Section À Propos

### Lignes ~95-110
Modifiez le texte descriptif pour parler de vous:
```html
<p>Bienvenue! Je suis un professionnel passionné par...</p>
```

### Statistiques
Lignes ~115-125 - Mettez à jour:
- "5+" → Vos années d'expérience
- "30+" → Nombre de projets
- "4" → Nombre de certifications

## 💼 Étape 3: Expérience Professionnelle

### Section `#experience` (Lignes ~140-210)

Pour chaque poste, modifiez:

```html
<div class="timeline-item">
    <div class="timeline-date">2023 - Présent</div>
    <div class="timeline-content">
        <h3>Votre Titre</h3>
        <p class="company">Nom de l'Entreprise</p>
        <ul class="experience-list">
            <li>Accomplissement 1</li>
            <li>Accomplissement 2</li>
            <li>Accomplissement 3</li>
        </ul>
        <div class="tech-tags">
            <span class="tag">Technologie 1</span>
            <span class="tag">Technologie 2</span>
        </div>
    </div>
</div>
```

## 🎓 Étape 4: Parcours Académique

### Section `#education` (Lignes ~225-260)

Modifiez pour chaque formation:
```html
<div class="education-card">
    <h3>Votre Diplôme</h3>
    <p class="education-school">Nom de l'Université</p>
    <p class="education-date">2015 - 2017</p>
    <p class="education-description">Votre spécialisation</p>
</div>
```

## 🛠️ Étape 5: Compétences

### Section `#skills` (Lignes ~270-330)

Modifiez les catégories et compétences:
```html
<div class="skill-category">
    <h3>Votre Catégorie</h3>
    <div class="skill-tags">
        <span class="skill-tag">Compétence 1</span>
        <span class="skill-tag">Compétence 2</span>
    </div>
</div>
```

## 🏆 Étape 6: Certifications

### Section `#certifications` (Lignes ~345-400)

Modifiez vos certifications:
```html
<div class="certification-card">
    <div class="cert-icon">
        <i class="fab fa-microsoft"></i>  <!-- Modifiez l'icône -->
    </div>
    <h3>AZ-104: Azure Administrator</h3>
    <p class="cert-issuer">Microsoft</p>
    <p class="cert-description">Description de votre certification</p>
</div>
```

**Icônes disponibles:**
- `fab fa-microsoft` - Microsoft
- `fab fa-amazon` - AWS
- `fas fa-cloud` - Cloud générique
- `fab fa-linux` - Linux
- `fab fa-docker` - Docker

[Voir plus d'icônes Font Awesome](https://fontawesome.com/icons)

## 📧 Étape 7: Informations de Contact

### Section `#contact` (Lignes ~410-460)

Modifiez:
```html
<!-- Email -->
<a href="mailto:votre-email@example.com">votre-email@example.com</a>

<!-- Téléphone -->
<a href="tel:+33612345678">+33 6 12 34 56 78</a>

<!-- Localisation -->
<a href="#">Votre Ville, Pays</a>
```

### Réseaux Sociaux

Lignes ~470-485:
```html
<a href="https://linkedin.com/in/votre-profil" target="_blank">
    <i class="fab fa-linkedin"></i>
</a>
<a href="https://github.com/votre-profil" target="_blank">
    <i class="fab fa-github"></i>
</a>
<a href="https://twitter.com/votre-profil" target="_blank">
    <i class="fab fa-twitter"></i>
</a>
```

## 🎨 Étape 8: Personnalisation des Couleurs

### Ouvrez `app/static/css/style.css`

Lignes ~1-25 - Modifiez les couleurs:
```css
--primary-color: #6366f1;      /* Couleur principale (bleu indigo) */
--secondary-color: #ec4899;    /* Couleur secondaire (rose) */
--dark-bg: #0f172a;            /* Fond sombre */
--light-bg: #f8fafc;           /* Fond clair */
```

**Suggestions de couleurs:**
- Bleu: `#3b82f6`
- Violet: `#a855f7`
- Rose: `#ec4899`
- Vert: `#10b981`
- Orange: `#f97316`

## 📱 Étape 9: Ajouter votre Photo

1. Placez une image JPG ou PNG dans `app/static/images/`
   - Recommandé: `profile.jpg` (300x400px minimum)

2. Assurez-vous que l'image s'appelle `profile.jpg` ou modifiez:
   ```html
   <img src="{{ url_for('static', filename='images/ma-photo.jpg') }}" alt="Votre Nom">
   ```

## 🔗 Étape 10: Mises à Jour Supplémentaires

### Dans `base.html` (Lignes ~40-50)
- Titre du site: `<title>Élpidia Lissassi - Portfolio</title>`
- Meta description: `<meta name="description" content="..."`

### Dans `base.html` Footer
- Ajouter vos vrais liens de réseaux sociaux
- Mettre à jour l'année de copyright

## ✅ Checklist Avant Déploiement

- [ ] Votre nom et titre personnalisés
- [ ] Votre photo ajoutée
- [ ] À propos mis à jour
- [ ] Expériences professionnelles modifiées
- [ ] Formation académique complétée
- [ ] Compétences listées
- [ ] Certifications ajoutées
- [ ] Informations de contact configurées
- [ ] Liens réseaux sociaux mis à jour
- [ ] Couleurs personnalisées (optionnel)
- [ ] Testé localement: `python app/app.py`

## 🚀 Prêt pour Vercel?

Quand tout est personnalisé:

1. Testez localement: `python app/app.py`
2. Vérifiez l'apparence sur mobile et desktop
3. Cliquez sur "Deploy" sur Vercel
4. Configurez votre domaine personnalisé (optionnel)

## 💡 Conseils d'Amélioration

1. **Blog**: Ajoutez une section articles/blog
2. **Projets**: Créez une galerie de vos projets
3. **Téléchargement CV**: Implémentez un endpoint de téléchargement
4. **Analytics**: Ajoutez Google Analytics pour suivre les visiteurs
5. **Newsletter**: Proposez une inscription newsletter
6. **Chat**: Intégrez un chatbot pour répondre aux questions courantes

---

**Besoin d'aide? Consultez le README.md!**
