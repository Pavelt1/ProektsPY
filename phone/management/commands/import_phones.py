import csv
from django.core.management.base import BaseCommand
from phone.models import Document
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Import phones from CSV file to database'

    def add_arguments(self, parser):
        parser.add_argument('project3\phones.csv', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['project3\phones.csv']
        phones_to_create = []

        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                phones_to_create.append(
                    Document(
                        id=int(phone["id"]),
                        name=phone["name"],
                        image=phone["image"],
                        price=float(phone["price"]),
                        release_date=phone["release_date"],
                        lte_exists=phone["lte_exists"].lower() == 'true',
                        slug=slugify(phone["name"])
                    )
                )

            Document.objects.bulk_create(phones_to_create)
            self.stdout.write(self.style.SUCCESS(f'Сохранено {len(phones_to_create)} тел.'))
