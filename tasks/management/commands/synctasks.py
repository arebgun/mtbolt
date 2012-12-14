from django.core.management.base import BaseCommand
from tasks.models import DescriptionTask
from mtbolt.mturk import open_connection, get_open_assignments, code_for_assignment

class Command(BaseCommand):
    help = "Approves or rejects active Turk assignments that have been flagged in the database"

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
                if description_task == True:
                    print 'approving %s, %s' % (a, code)
                    # connection.approve_assignment(a)

    def handle(self, *args, **options):
        self.sync_turk_tasks()
