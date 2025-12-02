# -*- coding: utf-8 -*-
"""
EL.portfolio - Cloud & DevOps Engineer Portfolio
Flask Application
"""
import sys
import logging
from flask import Flask, render_template, request, jsonify
import os
from pathlib import Path
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

# Try to load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    logger.warning("python-dotenv not available, skipping .env file loading")

# Get absolute paths based on this file's location
app_dir = Path(__file__).parent
static_dir = app_dir / 'static'
templates_dir = app_dir / 'templates'

logger.info(f"App directory: {app_dir}")
logger.info(f"Static directory: {static_dir} (exists: {static_dir.exists()})")
logger.info(f"Templates directory: {templates_dir} (exists: {templates_dir.exists()})")

# Create Flask app with absolute paths
app = Flask(__name__, 
            static_folder=str(static_dir),
            static_url_path='/static',
            template_folder=str(templates_dir))
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Email configuration - Use environment variables in production
EMAIL_ADDRESS = 'elpidiolissassi2@gmail.com'
RECIPIENT_EMAIL = 'elpidiolissassi2@gmail.com'
# For Gmail, create an application password at https://myaccount.google.com/apppasswords
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')

def send_email(sender_name, sender_email, subject, message):
    """Send email via SMTP Gmail"""
    try:
        if not EMAIL_PASSWORD:
            print("WARNING: EMAIL_PASSWORD not configured. Email not sent.")
            return False
            
        # Create email message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Portfolio: {subject}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Reply-To'] = sender_email
        
        # Create HTML message body
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #6366f1;">New Portfolio Message</h2>
                    <hr style="border: 1px solid #e2e8f0;">
                    
                    <p><strong>Name:</strong> {sender_name}</p>
                    <p><strong>Email:</strong> {sender_email}</p>
                    <p><strong>Subject:</strong> {subject}</p>
                    
                    <hr style="border: 1px solid #e2e8f0;">
                    <h3>Message:</h3>
                    <p>{message.replace(chr(10), '<br>')}</p>
                    
                    <hr style="border: 1px solid #e2e8f0;">
                    <p style="font-size: 12px; color: #999;">
                        Message sent from your personal portfolio
                    </p>
                </div>
            </body>
        </html>
        """
        
        # Plain text alternative
        text_body = f"""
        NEW PORTFOLIO MESSAGE
        
        Name: {sender_name}
        Email: {sender_email}
        Subject: {subject}
        
        Message:
        {message}
        """
        
        part1 = MIMEText(text_body, 'plain')
        part2 = MIMEText(html_body, 'html')
        msg.attach(part1)
        msg.attach(part2)
        
        # Send via SMTP Gmail
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"Email sent successfully from {sender_email}")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("Gmail authentication error. Check application password.")
        return False
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
        return False
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/')
def index():
    """Home page of the portfolio"""
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    """Endpoint for contact form"""
    try:
        data = request.json
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # Validate fields
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'error': 'All fields are required'}), 400
        
        if len(name) < 2 or len(name) > 100:
            return jsonify({'success': False, 'error': 'Name must be between 2 and 100 characters'}), 400
        
        # Simple email validation
        if '@' not in email or '.' not in email:
            return jsonify({'success': False, 'error': 'Invalid email'}), 400
        
        if len(subject) < 3 or len(subject) > 200:
            return jsonify({'success': False, 'error': 'Subject must be between 3 and 200 characters'}), 400
        
        if len(message) < 10 or len(message) > 5000:
            return jsonify({'success': False, 'error': 'Message must be between 10 and 5000 characters'}), 400
        
        # Send email
        email_sent = send_email(name, email, subject, message)
        
        if email_sent:
            return jsonify({
                'success': True,
                'message': 'Message sent successfully! I will reply very soon.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Message received but email sending is not configured.'
            }), 500
            
    except Exception as e:
        print(f"Error in /api/contact: {e}")
        return jsonify({'success': False, 'error': f'Server error: {str(e)}'}), 500

@app.route('/api/download-cv', methods=['GET'])
def download_cv():
    """Endpoint to download CV (to implement)"""
    return jsonify({'message': 'CV download not configured'})

@app.errorhandler(404)
def not_found(error):
    """Handle page not found"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """Handle server errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
