from vote_app.models import Category, Nominee

def create_categories_and_nominees():
    categories = [
        "Meilleur artiste",
        "Rappeur",
        "Chanteur",
        "DJ",
        "Révélation",
        "Groupe de danse",
        "Web media",
        "Humoriste",
        "Influenceur",
        "Ambassadeur",
        "Collaboration",
        "Performance live",
        "Réalisateur",
    ]

    for name in categories:
        slug = name.lower().replace(" ", "-").replace("é", "e").replace("à", "a")
        category, _ = Category.objects.get_or_create(name=name, slug=slug)
        for i in range(1, 5):
            Nominee.objects.get_or_create(
                name=f"Nominee {i}",
                category=category,
                defaults={"image_url": "https://via.placeholder.com/150"}
            )
