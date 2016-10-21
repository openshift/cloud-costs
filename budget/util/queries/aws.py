from datetime import datetime, timedelta
from budget.models import *

last_year = datetime.now() - timedelta(days=365)

def get_metadata(account_id):
    ''' collected metadata tags about our AWS accounts.
    '''
    try:
        results = DBSession.query(
                        AwsAccountMetadata.tags
                    ).filter(
                        AwsAccountMetadata.account_id == account_id
                    ).all();
        # generate a flattened list of individual tags
        # if there are comma-separated values in the results
        metadata = [r for tup in results for result in tup for r in result.split(',')]
    except NoResultFound:
        metadata = []
    return metadata

def get_dates(params):
    ''' Fetch dates we have invoices for within the last year.
        Return a tuple with:
            - list of datetimes for future use in UI
            - a datetime representing the selected date. defaults to latest date,
                if no date was selected
    '''
    dates = DBSession.query(
                AwsCostAllocation.billing_period_start_date.distinct()
            ).filter(
                AwsCostAllocation.billing_period_start_date >= last_year,
            ).all()
    dates = sorted(set([ item[0].strftime("%Y-%m-%d") for item in dates ]))

    if 'date' in params:
        selected_date = datetime.strptime(params['date'], "%Y-%m-%d")
    else:
        selected_date = max(dates)

#    # munge selected_date to avoid presenting "dd/mm/yyyy 00:00:00" in the UI
#    if not isinstance(selected_date, str):
#        selected_date = selected_date.strftime("%Y-%m-%d")

    return (dates, selected_date)

