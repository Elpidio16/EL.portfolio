# 📧 Configuration Email pour le Formulaire de Contact

## ⚡ Instructions Rapides

Pour activer l'envoi d'emails automatiques quand quelqu'un remplit le formulaire de contact:

### Étape 1: Créer un Mot de Passe d'Application Gmail

1. Allez à **https://myaccount.google.com/apppasswords**
2. Si vous n'avez pas la vérification en deux étapes:
   - Cliquez sur **Sécurité** dans le menu de gauche
   - Cherchez **Vérification en deux étapes** et activez-la
   - Puis revenez à https://myaccount.google.com/apppasswords

3. Sélectionnez:
   - **Mail**
   - **Windows Computer** (ou votre appareil)

4. Google génère un mot de passe de 16 caractères (ex: `abcd efgh ijkl mnop`)

### Étape 2: Configurer le Fichier .env

1. Ouvrez le fichier `.env` à la racine du projet
2. Remplacez `votre_mot_de_passe_application_ici` par le mot de passe généré:

```env
EMAIL_PASSWORD=abcdefghijklmnop
```

3. **Important:** Ne partagez JAMAIS ce fichier `.env` sur GitHub!

### Étape 3: Redémarrer le Serveur

```bash
# Arrêtez le serveur Flask (Ctrl+C dans le terminal)
# Redémarrez-le:
python app/app.py
```

## ✅ Vérifier que ça Marche

1. Allez sur votre portfolio: `http://localhost:5000`
2. Remplissez le formulaire "Parlons Ensemble"
3. Cliquez sur "Envoyer le Message"
4. Vérifiez votre boîte mail `elpidiolissassi2@gmail.com`
5. Le message devrait arriver dans 30 secondes

## 🔒 Sécurité en Production (Vercel)

Quand vous déployez sur Vercel:

1. **NE METTEZ PAS** le fichier `.env` sur GitHub
2. Dans Vercel:
   - Allez dans **Settings** → **Environment Variables**
   - Ajoutez: `EMAIL_PASSWORD` = `votre_mot_de_passe_application`
3. Vercel va automatiquement charger cette variable

## 📋 Structure Email Reçu

L'email que vous recevrez ressemblera à:

```
Nouveau Message du Portfolio

Nom: Jean Dupont
Email: jean@example.com
Sujet: Opportunité DevOps

Message:
Bonjour Elpidio, je suis intéressé par...
```

## ❌ Dépannage

| Problème | Solution |
|----------|----------|
| "Identifiant ou mot de passe incorrect" | Vérifiez le mot de passe d'application (16 caractères, pas votre mot de passe Gmail) |
| Aucun email reçu | Vérifiez la console (terminal) pour les erreurs |
| Spam/Dossier junk | Les emails pourraient être dans les spams, ajoutez `elpidiolissassi2@gmail.com` en contact de confiance |
| Erreur lors du test | Vérifiez que le serveur Flask est en cours d'exécution |

## 💡 Notes

- Les emails sont envoyés depuis votre adresse Gmail
- La personne peut répondre directement à son email depuis le formulaire
- Chaque message est enregistré dans les logs du serveur
- En développement, vous verrez les messages dans le terminal si l'email échoue

---

**Besoin d'aide?** Consultez:
- [Configuration Gmail 2FA](https://support.google.com/accounts/answer/185833)
- [Mots de passe d'application Gmail](https://support.google.com/accounts/answer/185833)
        if '@' not in email:
            return jsonify({'success': False, 'error': 'Email invalide'}), 400
        
        # Envoyer l'email
        send_email(name, email, subject, message)
        
        return jsonify({
            'success': True,
            'message': 'Message envoyé avec succès! Je vous répondrai très bientôt.'
        })
    except Exception as e:
        print(f"Erreur: {e}")
        return jsonify({'success': False, 'error': 'Erreur lors de l\'envoi'}), 500

def send_email(name, sender_email, subject, message):
    """Envoyer un email via Gmail SMTP"""
    try:
        # Créer le message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = SENDER_EMAIL  # Envoyer à vous-même
        msg['Subject'] = f"Nouveau Message: {subject}"
        
        # Corps du message
        body = f"""
        Nouveau message de votre portfolio:
        
        Nom: {name}
        Email: {sender_email}
        Sujet: {subject}
        
        Message:
        {message}
        
        ---
        Répondre à: {sender_email}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Envoyer l'email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"Email envoyé avec succès de {sender_email}")
        return True
        
    except Exception as e:
        print(f"Erreur lors de l'envoi: {e}")
        raise

if __name__ == '__main__':
    app.run(debug=True)
```

3. **Sur Vercel**: 
   - Settings → Environment Variables
   - Ajouter: `EMAIL_PASSWORD` = votre mot de passe d'application
   - Redéployer

---

### Option 2: SendGrid (Recommandé pour Vercel)

SendGrid offre 100 emails gratuits par jour.

#### Installation

1. **Créer un compte SendGrid**:
   - Allez sur [sendgrid.com](https://sendgrid.com)
   - Inscrivez-vous gratuitement
   - Vérifiez votre email

2. **Obtenir la clé API**:
   - Allez dans Settings → API Keys
   - Créez une nouvelle clé (Full Access recommandé)
   - Copiez la clé

3. **Installer sendgrid Python**:

```powershell
pip install sendgrid
pip freeze > requirements.txt
```

4. **Modifier `app/app.py`**:

```python
from flask import Flask, render_template, request, jsonify
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
import os

app = Flask(__name__)

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
FROM_EMAIL = "noreply@votredomaine.com"  # Ou votre email vérifié SendGrid
TO_EMAIL = "votre-email@gmail.com"

@app.route('/api/contact', methods=['POST'])
def contact():
    """Endpoint pour le formulaire de contact"""
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'error': 'Tous les champs sont requis'}), 400
        
        if '@' not in email:
            return jsonify({'success': False, 'error': 'Email invalide'}), 400
        
        # Envoyer l'email via SendGrid
        send_email_sendgrid(name, email, subject, message)
        
        return jsonify({
            'success': True,
            'message': 'Message envoyé avec succès!'
        })
    except Exception as e:
        print(f"Erreur: {e}")
        return jsonify({'success': False, 'error': 'Erreur lors de l\'envoi'}), 500

def send_email_sendgrid(name, sender_email, subject, message_text):
    """Envoyer un email via SendGrid"""
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        
        # Message de bienvenue au visiteur
        welcome_msg = Mail(
            from_email=FROM_EMAIL,
            to_emails=sender_email,
            subject=f"Merci pour votre message: {subject}",
            plain_text_content=f"""Bonjour {name},

Merci d'avoir contacté mon portfolio. J'ai bien reçu votre message et vous répondrai très bientôt.

Cordialement,
Élpidia Lissassi"""
        )
        
        # Notification au propriétaire
        notify_msg = Mail(
            from_email=FROM_EMAIL,
            to_emails=TO_EMAIL,
            subject=f"Nouveau message: {subject}",
            plain_text_content=f"""Nouveau message de votre portfolio:

Nom: {name}
Email: {sender_email}
Sujet: {subject}

Message:
{message_text}

---
Répondre à: {sender_email}"""
        )
        
        # Envoyer les deux emails
        sg.send(welcome_msg)
        sg.send(notify_msg)
        
        print(f"Emails envoyés avec succès pour {sender_email}")
        return True
        
    except Exception as e:
        print(f"Erreur SendGrid: {e}")
        raise

if __name__ == '__main__':
    app.run(debug=True)
```

5. **Sur Vercel**:
   - Settings → Environment Variables
   - Ajouter: `SENDGRID_API_KEY` = votre clé API
   - Redéployer

---

### Option 3: Mailgun (Gratuit aussi)

Mailgun offre aussi des emails gratuits.

```python
import requests

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
MAILGUN_DOMAIN = "sandboxxxxx.mailgun.org"

def send_email_mailgun(name, sender_email, subject, message):
    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"{name} <{sender_email}>",
            "to": ["votre-email@gmail.com"],
            "subject": subject,
            "text": message
        }
    )
```

---

## 🧪 Tester Localement

```powershell
# Créer un fichier .env
$env:EMAIL_PASSWORD = "votre-mot-passe"
$env:SENDGRID_API_KEY = "votre-clé"

# Lancer Flask
python app/app.py

# Aller sur http://localhost:5000
# Testez le formulaire de contact
```

---

## ✅ Vérifier Que Ça Marche

1. Remplissez le formulaire de contact
2. Cliquez sur "Envoyer le Message"
3. Vous devriez voir: "Message envoyé avec succès!"
4. Vérifiez votre email (inbox ou spam)

---

## 📞 Dépannage

### Les emails n'arrivent pas

**Si vous utilisez Gmail:**
- Vérifiez le mot de passe d'application
- Activez "Applications moins sécurisées" (ancienne méthode)
- Vérifiez les spams

**Si vous utilisez SendGrid:**
- Vérifiez la clé API
- Vérifiez le domaine vérifié
- Consultez les logs SendGrid

### Erreur "Authentication failed"

- Vérifiez les variables d'environnement
- Assurez-vous qu'il n'y a pas d'espaces
- Redéployez sur Vercel

### L'API ne répond pas

- Vérifiez la connexion internet
- Attendez quelques secondes
- Consultez les logs Vercel (Deployments → Logs)

---

## 🎨 Améliorer les Emails

### Template HTML pour les emails

```python
html_content = f"""
<html>
<body style="font-family: Arial, sans-serif;">
    <h2>Merci pour votre message!</h2>
    <p>Bonjour {name},</p>
    <p>J'ai bien reçu votre message et vous répondrai très bientôt.</p>
    <p>Cordialement,<br>Élpidia Lissassi</p>
</body>
</html>
"""
```

---

## 💾 Sauvegarder les Messages en Base de Données

Si vous voulez garder l'historique:

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(200))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/api/contact', methods=['POST'])
def contact():
    # ... validation ...
    
    # Sauvegarder le message
    msg = ContactMessage(
        name=name,
        email=email,
        subject=subject,
        message=message
    )
    db.session.add(msg)
    db.session.commit()
    
    # ... envoyer l'email ...
```

---

**Choisissez l'option qui vous convient et testez bien! 📧**
