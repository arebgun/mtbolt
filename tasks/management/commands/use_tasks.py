from os.path import join
from django.core.management.base import BaseCommand
from mtbolt.settings import PROJECT_ROOT
from tasks.models import DescriptionQuestion

def use_tasks(num_to_use):
    with open(join(PROJECT_ROOT, 'passed_all_shuffled')) as f:
        shuffled = map(int, f.read().split())
    good = set(shuffled[:num_to_use])
    for dq in DescriptionQuestion.objects.all():
        dq.use_in_object_tasks = (dq.id in good)
        dq.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if len(args) == 1:
            use_tasks(int(args[0]))
