from django.core.management.base import BaseCommand
from tasks.models import DescriptionTask
from mtbolt.mturk import open_connection, get_open_assignments, code_for_assignment

def sync_turk_tasks():
    connection = open_connection()
    assignments = get_open_assignments(connection)
    for a in assignments:
        code = code_for_assignment(a)
        matching_tasks = DescriptionTask.objects.filter(completion_code=code)
        if matching_tasks:
            if len(matching_tasks) > 1:
                print 'multiple tasks found for %s: %s' % (code, len(matching_tasks))
            description_task = matching_tasks[0]
            if description_task.approved == True:
                print 'approving %s, %s' % (a, code)
            elif description_task.approved == False:
                print 'would reject %s, %s' % (a, code)
            else:
                print 'val for %s, %s = %s' % (a, code, description_task.approved)
                # connection.approve_assignment(a)
        else:
            print 'no tasks found for %s' % code

class Command(BaseCommand):
    help = "Approves or rejects active Turk assignments that have been flagged in the database"


    def handle(self, *args, **options):
        sync_turk_tasks()
