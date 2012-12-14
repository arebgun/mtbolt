import os
from boto.mturk.connection import MTurkConnection

MTURK_ACCESS_KEY_ID = os.environ.get('MTURK_ACCESS_KEY_ID')
MTURK_SECRET_ACCESS_KEY = os.environ.get('MTURK_SECRET_ACCESS_KEY')
HOST='mechanicalturk.amazonaws.com'
SANDBOX_HOST='mechanicalturk.sandbox.amazonaws.com'

def open_connection(access_id=MTURK_ACCESS_KEY_ID, secret_key=MTURK_SECRET_ACCESS_KEY, sandbox=False):
    if sandbox:
        host = SANDBOX_HOST
    else:
        host = HOST
    return MTurkConnection(aws_access_key_id=access_id,
                           aws_secret_access_key=secret_key,
                           host=host)

def paginate_all(connection_fn, *args, **params):
    """ call like this: paginate_all(mtc.get_reviewable_hits) """
    page_size=50
    results = connection_fn(*args, page_size=page_size, **params)
    total_pages = float(results.TotalNumResults)/page_size
    int_total = int(total_pages)
    if(total_pages - int_total>0):
        total_pages = int_total+1
    else:
        total_pages = int_total
    pn = 1
    while pn < total_pages:
        pn += 1
        temp_results = connection_fn(*args, page_size=page_size, page_number=pn, **params)
        results.extend(temp_results)
    return results

def get_open_assignments(connection):
    hits = paginate_all(connection.get_reviewable_hits)
    assignments = []
    for hit in hits:
        hit_assignments = paginate_all(connection.get_assignments, hit.HITId, status='Submitted')
        assignments.extend(hit_assignments)
    return assignments

def code_for_assignment(assignment):
    return assignment.answers[0][0].fields[0].strip()

def approve_code(connection, code, open_assignments=None, feedback=None):
    if not open_assignments:
        open_assignments = get_open_assignments(connection)
    for a in open_assignments:
        if code_for_assignment(a) == code:
            connection.approve_assignment(a.AssignmentId, feedback)

def reject_code(connection, code, open_assignments=None, feedback=None):
    if not open_assignments:
        open_assignments = get_open_assignments(connection)
    for a in open_assignments:
        if code_for_assignment(a) == code:
            connection.reject_assignment(a.AssignmentId, feedback)
