from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Configuration email - Utilisez des variables d'environnement en production
EMAIL_ADDRESS = 'elpidiolissassi2@gmail.com'
RECIPIENT_EMAIL = 'elpidiolissassi2@gmail.com'
# Pour Gmail, créez un mot de passe d'application (App Password) à https://myaccount.google.com/apppasswords
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')

def send_email(sender_name, sender_email, subject, message):
    """Envoie un email via SMTP Gmail"""
    try:
        if not EMAIL_PASSWORD:
            print("⚠️ EMAIL_PASSWORD non configuré. Email non envoyé.")
            return False
            
        # Créer le message email
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Portfolio: {subject}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Reply-To'] = sender_email
        
        # Créer le corps du message en HTML
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #6366f1;">Nouveau Message du Portfolio</h2>
                    <hr style="border: 1px solid #e2e8f0;">
                    
                    <p><strong>Nom:</strong> {sender_name}</p>
                    <p><strong>Email:</strong> {sender_email}</p>
                    <p><strong>Sujet:</strong> {subject}</p>
                    
                    <hr style="border: 1px solid #e2e8f0;">
                    <h3>Message:</h3>
                    <p>{message.replace(chr(10), '<br>')}</p>
                    
                    <hr style="border: 1px solid #e2e8f0;">
                    <p style="font-size: 12px; color: #999;">
                        Message envoyé depuis votre portfolio personnel
                    </p>
                </div>
            </body>
        </html>
        """
        
        # Texte alternatif
        text_body = f"""
        NOUVEAU MESSAGE DU PORTFOLIO
        
        Nom: {sender_name}
        Email: {sender_email}
        Sujet: {subject}
        
        Message:
        {message}
        """
        
        part1 = MIMEText(text_body, 'plain')
        part2 = MIMEText(html_body, 'html')
        msg.attach(part1)
        msg.attach(part2)
        
        # Envoyer via SMTP Gmail
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Email envoyé avec succès de {sender_email}")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("❌ Erreur d'authentification Gmail. Vérifiez le mot de passe d'application.")
        return False
    except smtplib.SMTPException as e:
        print(f"❌ Erreur SMTP: {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi d'email: {e}")
        return False

@app.route('/')
def index():
    """Page d'accueil du portfolio"""
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    """Endpoint pour le formulaire de contact"""
    try:
        data = request.json
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # Validation des champs
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'error': 'Tous les champs sont requis'}), 400
        
        if len(name) < 2 or len(name) > 100:
            return jsonify({'success': False, 'error': 'Le nom doit contenir entre 2 et 100 caractères'}), 400
        
        # Validation email simple
        if '@' not in email or '.' not in email:
            return jsonify({'success': False, 'error': 'Email invalide'}), 400
        
        if len(subject) < 3 or len(subject) > 200:
            return jsonify({'success': False, 'error': 'Le sujet doit contenir entre 3 et 200 caractères'}), 400
        
        if len(message) < 10 or len(message) > 5000:
            return jsonify({'success': False, 'error': 'Le message doit contenir entre 10 et 5000 caractères'}), 400
        
        # Envoyer l'email
        email_sent = send_email(name, email, subject, message)
        
        if email_sent:
            return jsonify({
                'success': True,
                'message': 'Message envoyé avec succès! Je vous répondrai très bientôt.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Le message a été reçu mais l\'envoi d\'email n\'est pas configuré.'
            }), 500
            
    except Exception as e:
        print(f"Erreur dans /api/contact: {e}")
        return jsonify({'success': False, 'error': f'Erreur serveur: {str(e)}'}), 500

@app.route('/api/download-cv', methods=['GET'])
def download_cv():
    """Endpoint pour télécharger le CV (à implémenter)"""
    return jsonify({'message': 'CV téléchargement non configuré'})

@app.errorhandler(404)
def not_found(error):
    """Gestion des pages non trouvées"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """Gestion des erreurs serveur"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
