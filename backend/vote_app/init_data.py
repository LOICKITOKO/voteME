from vote_app.models import Category, Nominee

def create_categories_and_nominees():
    data = {
        "Meilleur artiste": ["Ninho", "Aya Nakamura", "Tiakola"],
        "Rappeur": ["SDM", "Gazo", "Hamza"],
        "Chanteur": ["Tayc", "Dadju", "Franglish"],
        "DJ": ["DJ Snake", "DJ Kore", "DJ Myst"],
        "Révélation": ["Werenoi", "Ronisia", "Ziak"],
        "Groupe de danse": ["Les Twins", "Serial Stepperz", "Swaggers"],
        "Web media": ["Booska-P", "Rapunchline", "GQ France"],
        "Humoriste": ["Paul Mirabel", "Inès Reg", "Redouane Bougheraba"],
        "Influenceur": ["Léna Situations", "Michou", "Just Riadh"],
        "Ambassadeur": ["Kylian Mbappé", "Omar Sy", "Aya Nakamura"],
        "Collaboration": ["Hamza x Damso", "Tiakola x Gazo", "Ninho x Ayra Starr"],
        "Performance live": ["Damso à Bercy", "Niska au Zénith", "Aya à l'Accor Arena"],
        "Réalisateur": ["Ladj Ly", "Maïmouna Doucouré", "Romain Gavras"],
    }

    for name, nominees in data.items():
        slug = name.lower().replace(" ", "-").replace("é", "e").replace("à", "a")
        category, _ = Category.objects.get_or_create(name=name, slug=slug)
        for nominee_name in nominees:
            Nominee.objects.get_or_create(name=nominee_name, category=category)
