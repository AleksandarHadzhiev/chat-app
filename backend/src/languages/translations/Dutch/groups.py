from src.languages.translations.base import Base


class GroupsDutchTranlsations(Base):
    def __init__(self):
        self.translations = {
            "join": "Meedoen",
            "leave": "Vertrekken",
            "cancel": "Annuleren",
            "submit": "Indienen",
            "search": "Zoekopdracht",
            "edit": "Bewerking",
            "delete": "Verwijderen",
            "kick": "Lid eruit schoppen",
            "name": "Naam",
            "current name": "Huidige naam",
            "new name": "Nieuwe naam",
            "loading": "Bezig met laden...",
            "role": "Rol",
            "actions": "Acties",
            "members": "Leden:",
            "created group": "Je hebt een groep aangemaakt. Maak hem populair.",
            "edited": "Je hebt de naam van de groep gewijzigd.",
            "deleted": "Je hebt de groep verwijderd.",
            "left": "Je hebt de groep verlaten",
            "kicked": "Je hebt het lid uit de groep gezet."     
        }

    def get_translations(self) -> dict:
        return self.translations
