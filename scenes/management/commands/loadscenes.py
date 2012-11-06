from django.core.management.base import BaseCommand, CommandError
from django.core.files.images import ImageFile
from scenes.models import Scene, Entity
import json
from os.path import basename

class Command(BaseCommand):
    args = "stuff"
    help = "help!"

    def handle(self, *args, **options):
        scene_name, image_path, json_path = args
        self.stdout.write("Creating scene %s from image %s and json schematic %s" % (scene_name, image_path, json_path))

        scene = Scene(name=scene_name)
        with open(image_path) as f:
            scene.image.save(basename(image_path), ImageFile(f), save=True)
        scene.save()

        with open(json_path) as f:
            json_data = json.load(f)
            for entity_desc in json_data:
                entity_name = entity_desc['name']
                self.stdout.write("\tCreating entity %s" % entity_name)
                entity = Entity(name=entity_name, scene=scene)
                entity.save()
