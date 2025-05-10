from django.contrib import admin
from vote_app.models import Category, Nominee, Vote
from django.db.models import Count

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_nominees', 'winner_and_votes')

    def show_nominees(self, obj):
        nominees = obj.nominees.all()[:4]
        return "\n".join([f"- {n.name}" for n in nominees]) or "Aucun nominé"
    show_nominees.short_description = 'Nominés (4 premiers)'

    def winner_and_votes(self, obj):
        # Compter les votes par nominé pour cette catégorie
        vote_counts = (
            Vote.objects.filter(nominee__category=obj)
            .values('nominee__name')
            .annotate(vote_count=Count('id'))
            .order_by('-vote_count')
        )
        if vote_counts:
            winner = vote_counts[0]
            return f"{winner['nominee__name']} (Gagnant) {winner['vote_count']} votes"
        return "Aucun vote"
    winner_and_votes.short_description = 'Gagnant et Votes'

admin.site.register(Category, CategoryAdmin)

class NomineeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
admin.site.register(Nominee, NomineeAdmin)
