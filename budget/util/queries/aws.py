from datetime import datetime, timedelta
from budget.models import *

last_year = datetime.now() - timedelta(days=365)

def get_metadata(account_id):
    try:
        results = DBSession.query(
                        AwsAccountMetadata.tags
                    ).filter(
                        AwsAccountMetadata.account_id == account_id
                    ).all();
        # generate a single, flattened list
        metadata = [r for tup in results for result in tup for r in result.split(',')]
    except NoResultFound:
        metadata = []
    return metadata

def get_dates(params):
    ''' Fetch dates we have invoices for within the last year.
        Return date list for future use -selections and a selected date the UI
        should display data from.
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

    # munge selected_date to avoid presenting "dd/mm/yy 00:00:00" in the UI
    if not isinstance(selected_date, str):
        selected_date = selected_date.strftime("%Y-%m-%d")

    return (dates, selected_date)

