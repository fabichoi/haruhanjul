import json
import os

from django.conf import settings

from apps.quotes.models import Quote


def import_quotes():
    if Quote.objects.last():
        return

    file_path = os.path.join(settings.BASE_DIR.parent, "scripts/init_quote.json")

    with open(file_path, "r", encoding="utf-8") as file:
        quotes = json.load(file)

    for quote_data in quotes:
        Quote.objects.create(
            text=quote_data["text"],
            approved=True
        )


def run():
    import_quotes()
