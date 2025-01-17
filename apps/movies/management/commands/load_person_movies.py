import gzip
import json
import os
import sys
from json import JSONDecodeError

from django.core.management import BaseCommand
from apps.movies.models import *


class Command(BaseCommand):
    help = "Use this command to upload data to your database"

    def add_arguments(self, parser):
        parser.add_argument("--file", '-f', required=True)
        parser.add_argument('--delimeter', '-d', default='\t')

    def handle(self, *args, **options):
        filepath = options['file']
        delimeter = options['delimeter']

        if not os.path.exists(filepath):
            print(f'No file {filepath} found.')
            sys.exit(1)

        our_movies = Movie.objects.all()
        our_movies_dict = {}
        for m in our_movies:
            our_movies_dict[m.imdb_id] = m.id

        with gzip.open(filepath, 'rb') as person_and_movies_data_file:
            for line in person_and_movies_data_file.readlines():
                person_movie_data = line.decode('utf8').strip('\n').split(delimeter)
                if not person_movie_data[0].startswith('tt'):
                    continue
                print(person_movie_data)
                try:
                    movie_id = our_movies_dict[person_movie_data[0]]
                except KeyError:
                    continue

                print(person_movie_data)

                try:
                    characters = json.loads(person_movie_data[5])
                except JSONDecodeError:
                    characters = []

                if person_movie_data[3] == '\\N':
                    person_movie_data[3] = ''

                person_movie_dict = dict(
                    order=person_movie_data[1],
                    category=person_movie_data[3],
                    job=person_movie_data[4],
                    characters=characters
                )

                person, created = Person.objects.get_or_create(imdb_id=person_movie_data[2])

                person_movie, created = PersonMovie.objects.get_or_create(movie_id=movie_id, person=person,
                                                                          defaults=person_movie_dict)
                PersonMovie.objects.filter(id=person_movie.id).update(**person_movie_dict)
                person_movie.save()
            person_and_movies_data_file.close()
