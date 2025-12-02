#!/usr/bin/env python3
"""
Script pour créer un favicon personnalisé à partir du logo lesageconsulting
"""

from PIL import Image, ImageDraw
import os

def create_favicon():
    """Crée un favicon rond et joli à partir du logo"""
    
    # Paths
    input_path = os.path.join(os.path.dirname(__file__), 'lesageconsulting.png')
    output_path = os.path.join(os.path.dirname(__file__), 'app', 'static', 'images', 'favicon.png')
    
    # Vérifier que l'image source existe
    if not os.path.exists(input_path):
        print(f"❌ Erreur: {input_path} non trouvé")
        return False
    
    try:
        # Ouvrir l'image
        img = Image.open(input_path).convert('RGBA')
        
        # Créer un canvas carré (pour favicon)
        size = 512  # Haute résolution
        canvas = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        
        # Redimensionner l'image pour qu'elle s'adapte
        # En laissant de la place pour le padding
        img_size = int(size * 0.85)
        img_resized = img.resize((img_size, img_size), Image.Resampling.LANCZOS)
        
        # Centrer l'image sur le canvas
        offset = (size - img_size) // 2
        canvas.paste(img_resized, (offset, offset), img_resized)
        
        # Créer un masque circulaire
        mask = Image.new('L', (size, size), 0)
        mask_draw = ImageDraw.Draw(mask)
        # Dessiner un cercle blanc sur le masque noir
        mask_draw.ellipse([0, 0, size-1, size-1], fill=255)
        
        # Appliquer le masque circulaire
        # Créer une nouvelle image avec fond blanc
        final = Image.new('RGBA', (size, size), (255, 255, 255, 255))
        final.paste(canvas, (0, 0), mask)
        
        # Ajouter une bordure subtile (optionnel)
        # On peut ajouter une bordure pour plus de style
        border_draw = ImageDraw.Draw(final)
        border_color = (99, 102, 241, 200)  # Couleur primaire du portfolio
        border_draw.ellipse([2, 2, size-3, size-3], outline=border_color, width=3)
        
        # Créer le répertoire s'il n'existe pas
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Sauvegarder
        final.save(output_path, 'PNG', quality=95)
        print(f"✅ Favicon créé avec succès: {output_path}")
        
        # Aussi créer des tailles supplémentaires pour différentes utilisations
        sizes = [
            (32, 'favicon-32.png'),
            (64, 'favicon-64.png'),
            (128, 'favicon-128.png'),
            (256, 'favicon-256.png'),
        ]
        
        for favicon_size, filename in sizes:
            favicon = final.resize((favicon_size, favicon_size), Image.Resampling.LANCZOS)
            favicon_path = os.path.join(os.path.dirname(output_path), filename)
            favicon.save(favicon_path, 'PNG', quality=95)
            print(f"✅ {filename} créé ({favicon_size}x{favicon_size})")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la création du favicon: {e}")
        return False

if __name__ == '__main__':
    success = create_favicon()
    exit(0 if success else 1)
