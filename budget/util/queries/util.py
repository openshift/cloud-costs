'''' misc. utility functions for sqlalchemy '''
from sqlalchemy.sql.expression import ClauseElement

# https://stackoverflow.com/questions/6611563/sqlalchemy-on-duplicate-key-update
def insert_or_update(session, model, defaults=None, **kwargs):
    ''' checks for an existing DB object. if present, existing object is
        updated with supplied args. if absent, a new DB object is inserted.
    '''
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        for k, v in defaults.iteritems():
            setattr(instance, k, v)
        return instance
    else:
        params = dict((k, v) for k, v in kwargs.iteritems() \
                             if not isinstance(v, ClauseElement))
        if defaults:
            params.update(defaults)
        instance = model(**params)
        return instance

