# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_37141392 = {}
_static_37138960 = {}
_static_36743056 = {}
_marker_default = _Placeholder()
import re
import functools
_marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def render(stream, econtext, rcontext):
    append = stream.append
    getitem = econtext.__getitem__
    get = econtext.get
    _i18n_domain = None
    re_amp = g_re_amp
    re_needs_escape = g_re_needs_escape
    decode = getitem('decode')
    convert = getitem('convert')
    translate = getitem('translate')
    _backup_attrs_40147424 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x230a790> name=None at 230a490> -> _value
    _value = _static_36743056
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    __fallback_34354496 = len(stream)
    try:
        _backup_attrs_40147568 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x236b210> name=None at 236b490> -> _value
        _value = _static_37138960
        econtext['attrs'] = _value

        # <body ... (2:2)
        # --------------------------------------------------------
        append(u'<body>')
        _content_139955154988272 = u'\n    '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        _backup_attrs_40167832 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x236bb90> name=None at 236b3d0> -> _value
        _value = _static_37141392
        econtext['attrs'] = _value

        # <div ... (3:4)
        # --------------------------------------------------------
        append(u'<div>')
        _backup_default_40145120 = get('default', _marker)

        # <Marker name='default' at 236b690> -> _value
        _value = _marker_default
        econtext['default'] = _value

        # <Expression u'undefined' (3:22)> -> _cache_37138512
        try:
            _cache_37138512 = getitem('undefined')
        except:
            rcontext.setdefault('__error__', []).append((u'undefined', 3, 22, '<string>', _sys.exc_info()[1], ))
            raise


        # <Identity expression=<Expression u'undefined' (3:22)> value=<Marker name='default' at 236b7d0> at 236bfd0> -> _condition
        _expression = _cache_37138512

        # <Marker name='default' at 236b7d0> -> _value
        _value = _marker_default
        _condition = (_expression is _value)
        if _condition:
            pass
        else:
            _content = _cache_37138512
            if (_content is None):
                pass
            else:
                if (_content is False):
                    _content = None
                else:
                    _tt = type(_content)
                    if ((_tt is int) or (_tt is float) or (_tt is long)):
                        _content = unicode(_content)
                    else:
                        try:
                            if (_tt is str):
                                _content = decode(_content)
                            else:
                                if (_tt is not unicode):
                                    try:
                                        _content = _content.__html__
                                    except:
                                        _content = convert(_content)
                                    else:
                                        raise RuntimeError
                        except RuntimeError:
                            _content = _content()
                        else:
                            if ((_content is not None) and (re_needs_escape(_content) is not None)):
                                if ('&' in _content):
                                    if (';' in _content):
                                        _content = re_amp.sub('&amp;', _content)
                                    else:
                                        _content = _content.replace('&', '&amp;')
                                if ('<' in _content):
                                    _content = _content.replace('<', '&lt;')
                                if ('>' in _content):
                                    _content = _content.replace('>', '&gt;')
                                if ('\x00' in _content):
                                    _content = _content.replace('\x00', '&#34;')
            if (_content is not None):
                append(_content)
        if (_backup_default_40145120 is _marker):
            del econtext['default']
        else:
            econtext['default'] = _backup_default_40145120
        append(u'</div>')
        if (_backup_attrs_40167832 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_40167832
        _content_139955154988272 = u'\n  '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</body>')
        if (_backup_attrs_40147568 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_40147568
    except (NameError, ValueError, AttributeError, LookupError, TypeError, ):
        del stream[__fallback_34354496:]

        # <Expression u'string:error' (2:22)> -> _content
        try:
            _content = u'error'
        except:
            rcontext.setdefault('__error__', []).append((u'string:error', 2, 22, '<string>', _sys.exc_info()[1], ))
            raise

        if (_content is not None):
            _tt = type(_content)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _content = str(_content)
            else:
                if (_tt is str):
                    _content = decode(_content)
                else:
                    if (_tt is not unicode):
                        try:
                            _content = _content.__html__
                        except AttributeError:
                            _content = convert(_content)
                        else:
                            _content = _content()
        if (_content is not None):
            append(_content)

    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_40147424 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_40147424
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass