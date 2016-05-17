import json
import logging
import yaml

log = logging.getLogger(__name__)

def load_json(filename):
    log.debug(filename)
    fh = None
    try:
        with open(filename) as f:
            fh = json.load(f)
    except TypeError:
        fh = json.load(filename)
    except IOError:
        fh = json.loads('{}')
    except ValueError:
        log.error('Unable to read %s' % filename)
        sys.exit()
    return fh

def save_json(filename, data):
    log.debug(filename)
    try:
        json.dump(data, open(filename, 'w+'))
    except TypeError:
        json.dump(data, filename)
    except IOError:
        raise

def load_yaml(filename):
    log.debug(filename)
    try:
        yamlfile = yaml.load(open(filename, 'r+'))
    except TypeError:
        yamlfile = yaml.load(filename)
    except IOError:
        raise
    return yamlfile

def save_yaml(filename, data):
    log.debug(filename)
    try:
        yaml.dump(data, open(filename, 'w+'))
    except TypeError:
        yaml.dump(data, filename)
    except IOError:
        raise

