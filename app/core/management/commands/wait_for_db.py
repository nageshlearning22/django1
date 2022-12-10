from django.core.management.base import BaseCommand

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management.base import BaseCommand

from django.db.utils import OperationalError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for Database...')

        db_up =False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up= True
            except(Psycopg2OpError,OperationalError):
                self.stdout.write('Database Unavailable waiting 1s ')

        self.stdout.write(self.style.SUCCESS('Database Available'))
        pass
       
