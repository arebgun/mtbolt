from django.core.management.base import BaseCommand
import object_tasks.models
import tasks.models
from mtbolt.settings import PROJECT_ROOT
from os.path import join

def num_correct(task):
        return sum(map(lambda eb: eb.binding == int(eb.description.entity.name), task.entity_bindings.all()))

def descriptions_passing_extra_validation():
    with open(join(PROJECT_ROOT, 'passed_in_all.txt')) as f:
        return set([int(s) for s in f.read().split()])

def print_stats(extra_validation=False):
    if extra_validation:
        validated_set = descriptions_passing_extra_validation()
    obj_desc_tasks = object_tasks.models.ObjectDescriptionTask.objects.all()

    print 'number of HITs completed: %d' % len(obj_desc_tasks)

    correct_per = map(num_correct, obj_desc_tasks)
    print correct_per[:30]
    print sum(correct_per)
    print 'average bindings correct per HIT: %f' % (float(sum(correct_per)) / (5 * len(correct_per)))

    sentences = tasks.models.DescriptionQuestion.objects.filter(use_in_object_tasks=True).all()
    if extra_validation:
        sentences = [s for s in sentences if s.id in validated_set]
    bindings_per_sent = map(lambda sent: sent.entity_bindings.count(), sentences)
    num_proofed = len([n for n in bindings_per_sent if n > 0])
    print 'number of sentences proofed: %d' % num_proofed
    num_bindings = sum(bindings_per_sent)
    print 'number of bindings: %d' % num_bindings
    print 'average bindings per proofed sentence: %f' % (float(num_bindings) / num_proofed)
    num_bindings_freq = {}
    for n in bindings_per_sent:
        num_bindings_freq[n] = num_bindings_freq.get(n, 0) + 1
    print 'bindings per sentence'
    for (n, count) in num_bindings_freq.items():
        print '\t%d sentences have %d bindings' % (count, n)

class Command(BaseCommand):
    help = "Prints completion stats for object_tasks"

    def handle(self, *args, **options):
        print 'stats for all sentences'
        print_stats(extra_validation=False)
        print '\nstats for extra validated sentences'
        print_stats(extra_validation=True)
