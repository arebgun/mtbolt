from django.core.management.base import BaseCommand, CommandError
from django.core.files.images import ImageFile
from scenes.models import Scene, Entity, GeneratedDescription
import json
from glob import glob
from os.path import basename, join, isdir

class Command(BaseCommand):
    args = "<base_dir>"
    help = "Loads all scenes contained in <base_dir>. <base_dir> should contain one directory for each scene, with a json file and an image"

    def load_single(self, scene_name, image_path, json_path, desc_path):
        self.stdout.write("Creating scene %s from image %s, json schematic %s and generated description file %s\n" % (scene_name, image_path, json_path, desc_path))

        scene = Scene(name=scene_name)

        with open(image_path) as f:
            scene.image.save(basename(image_path), ImageFile(f), save=True)

        scene.save()

        with open(json_path) as f:
            json_data = json.load(f)
            self.stdout.write("\tCreating entities:")

            for entity_desc in json_data['objects']:
                entity_name = entity_desc['name']
                self.stdout.write(" %s" % entity_name)
                entity = Entity(name=entity_name, scene=scene)
                entity.save()

            self.stdout.write("\n")

        with open(desc_path) as df:
            for dl in df:
                ent_name, text, corpus_size, representation_model = dl.split(';')
                entity = Entity.objects.get(scene__name=scene_name, name=ent_name)
                entity.generated_descriptions.create(text=text.strip(), corpus_size=corpus_size.strip(), representation_model=representation_model.strip())


    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError("Usage: %s" % args)

        basedir = args[0]

        for scene_path in sorted(glob(join(basedir, '*'))):
            if isdir(scene_path):
                self.stdout.write("Looking for scenes in %s\n" % scene_path)
                scene_name = basename(scene_path)
                image_path = min(glob(join(scene_path, '*.png')))
                json_path = min(glob(join(scene_path, '*.json')))
                desc_path = min(glob(join(scene_path, '*.txt')))
                self.load_single(scene_name, image_path, json_path, desc_path)
