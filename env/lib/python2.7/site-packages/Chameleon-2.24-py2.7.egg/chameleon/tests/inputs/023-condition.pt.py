# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_37141392 = {}
_static_38401104 = {}
_static_38400656 = {}
_static_37139024 = {}
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
    _backup_attrs_38619040 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249f290> name=None at 249fc10> -> _value
    _value = _static_38400656
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u'True' (2:23)> -> _condition
    try:
        _condition = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 2, 23, '<string>', _sys.exc_info()[1], ))
        raise

    if _condition:
        _backup_attrs_39065432 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x249f450> name=None at 249f850> -> _value
        _value = _static_38401104
        econtext['attrs'] = _value

        # <body ... (2:2)
        # --------------------------------------------------------
        append(u'<body>')
        _content_139955154988272 = u'\n    '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        _backup_selector_38402576 = get('selector', _marker)

        # <Expression u'False' (3:31)> -> _value
        try:
            _value = False
        except:
            rcontext.setdefault('__error__', []).append((u'False', 3, 31, '<string>', _sys.exc_info()[1], ))
            raise

        econtext['selector'] = _value

        # <Expression u'selector' (3:53)> -> _condition
        try:
            _condition = getitem('selector')
        except:
            rcontext.setdefault('__error__', []).append((u'selector', 3, 53, '<string>', _sys.exc_info()[1], ))
            raise

        if _condition:
            _backup_attrs_39065576 = get('attrs', _marker)

            # <Static value=<_ast.Dict object at 0x236b250> name=None at 236b450> -> _value
            _value = _static_37139024
            econtext['attrs'] = _value

            # <span ... (3:4)
            # --------------------------------------------------------
            append(u'<span>')
            _content_139955154988272 = u'bad'
            if (_content_139955154988272 is not None):
                append(_content_139955154988272)
            append(u'</span>')
            if (_backup_attrs_39065576 is _marker):
                del econtext['attrs']
            else:
                econtext['attrs'] = _backup_attrs_39065576
        if (_backup_selector_38402576 is _marker):
            del econtext['selector']
        else:
            econtext['selector'] = _backup_selector_38402576
        _content_139955154988272 = u'\n    '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)

        # <Expression u'True' (4:25)> -> _condition
        try:
            _condition = True
        except:
            rcontext.setdefault('__error__', []).append((u'True', 4, 25, '<string>', _sys.exc_info()[1], ))
            raise

        if _condition:
            _backup_attrs_39064784 = get('attrs', _marker)

            # <Static value=<_ast.Dict object at 0x236bb90> name=None at 236bbd0> -> _value
            _value = _static_37141392
            econtext['attrs'] = _value

            # <span ... (4:4)
            # --------------------------------------------------------
            append(u'<span>')
            _content_139955154988272 = u'ok'
            if (_content_139955154988272 is not None):
                append(_content_139955154988272)
            append(u'</span>')
            if (_backup_attrs_39064784 is _marker):
                del econtext['attrs']
            else:
                econtext['attrs'] = _backup_attrs_39064784
        _content_139955154988272 = u'\n  '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</body>')
        if (_backup_attrs_39065432 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_39065432
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_38619040 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38619040
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass