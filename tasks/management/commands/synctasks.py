from django.core.management.base import BaseCommand
from tasks.models import DescriptionTask
from mtbolt.mturk import open_connection, get_open_assignments, code_for_assignment

def sync_turk_tasks():
    connection = open_connection()
    assignments = get_open_assignments(connection)
    approval_count = 0
    rejection_count = 0
    untouched_count = 0
    not_found_count = 0
    for a in assignments:
        code = code_for_assignment(a)
        matching_tasks = DescriptionTask.objects.filter(completion_code=code)
        if matching_tasks:
            if len(matching_tasks) > 1:
                print 'multiple tasks found for %s: %s' % (code, len(matching_tasks))
            description_task = matching_tasks[0]
            if description_task.approved == True:
                print 'approving %s, %s' % (a, code)
                connection.approve_assignment(a.AssignmentId)
                approval_count += 1
            elif description_task.approved == False:
                print 'rejecting %s, %s' % (a, code)
                connection.reject_assignment(a.assignmentId)
                rejection_count += 1
            else:
                untouched_count += 1
                # connection.approve_assignment(a)
        else:
            print 'no tasks found for %s' % code
            not_found_count += 1
    print 'approved: %s' % approval_count
    print 'rejected: %s' % rejection_count
    print 'untouched: %s' % untouched_count
    print 'not_found: %s' % not_found_count

class Command(BaseCommand):
    help = "Approves or rejects active Turk assignments that have been flagged in the database"

    def handle(self, *args, **options):
        sync_turk_tasks()
