import json
import logging
import yaml

def load_json(filename):
    fh = None
    try:
        with open(filename) as f:
            fh = json.load(f)
    except TypeError:
        fh = json.load(filename)
    except IOError:
        fh = json.loads('{}')
    except ValueError:
        log = logging.getLogger(__name__)
        log.error('Unable to read %s' % filename)
    return fh

def save_json(filename, data):
    try:
        json.dump(data, open(filename, 'w+'))
    except TypeError:
        json.dump(data, filename)
    except IOError:
        raise

def load_yaml(filename):
    try:
        yamlfile = yaml.load(open(filename, 'r+'))
    except TypeError:
        yamlfile = yaml.load(filename)
    except IOError:
        raise
    return yamlfile

def save_yaml(filename, data):
    try:
        yaml.dump(data, open(filename, 'w+'))
    except TypeError:
        yaml.dump(data, filename)
    except IOError:
        raise

