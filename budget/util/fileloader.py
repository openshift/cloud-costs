import json
import yaml

def load_json(filename):
    fh = None
    try:
        with open(filename) as f:
            fh = json.load(f)
    except IOError:
        fh = json.loads('{}')
    except ValueError:
        log.error('Unable to read %s' % filename)
        sys.exit()
    return fh

def save_json(filename, data):
    try:
        json.dump(data, open(filename, 'w+'))
    except IOError:
        raise

def load_yaml(filename):
    try:
        yamlfile = yaml.load(open(filename, 'r+'))
    except IOError:
        raise
    return yamlfile

def save_yaml(filename, data):
    try:
        yaml.dump(data, open(filename, 'w+'))
    except IOError:
        raise

