# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_37142480 = {}
_static_38891664 = {}
_static_37142352 = {}
_static_38894800 = {}
_static_38893584 = {}
_static_36788624 = {}
_static_37141584 = {}
_static_36789456 = {}
_static_38400400 = {}
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
    _backup_attrs_39791864 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2315cd0> name=None at 2315090> -> _value
    _value = _static_36789456
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39094824 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2315990> name=None at 2315f90> -> _value
    _value = _static_36788624
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u'True' (3:21)> -> _cache_37139408
    try:
        _cache_37139408 = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 3, 21, '<string>', _sys.exc_info()[1], ))
        raise

    _backup_attrs_38450528 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236bc50> name=None at 236b150> -> _value
    _value = _static_37141584
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_35792944 = get('default', _marker)
    _value = _cache_37139408
    econtext['default'] = _value

    # <Equality expression=<Expression u'True' (3:21)> value=<Expression u'False' (4:22)> at 236bcd0> -> _condition
    _expression = _cache_37139408

    # <Expression u'False' (4:22)> -> _value
    try:
        _value = False
    except:
        rcontext.setdefault('__error__', []).append((u'False', 4, 22, '<string>', _sys.exc_info()[1], ))
        raise

    _condition = (_expression == _value)
    if _condition:
        _backup_attrs_35791864 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x236bf50> name=None at 236b210> -> _value
        _value = _static_37142352
        econtext['attrs'] = _value

        # <span ... (4:6)
        # --------------------------------------------------------
        append(u'<span>')
        _content_139955154988272 = u'bad'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</span>')
        if (_backup_attrs_35791864 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35791864
    if (_backup_default_35792944 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35792944
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_35794240 = get('default', _marker)
    _value = _cache_37139408
    econtext['default'] = _value

    # <Equality expression=<Expression u'True' (3:21)> value=<Expression u'True' (5:22)> at 249f050> -> _condition
    _expression = _cache_37139408

    # <Expression u'True' (5:22)> -> _value
    try:
        _value = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 5, 22, '<string>', _sys.exc_info()[1], ))
        raise

    _condition = (_expression == _value)
    if _condition:
        _backup_attrs_35794024 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x236bfd0> name=None at 236bb10> -> _value
        _value = _static_37142480
        econtext['attrs'] = _value

        # <span ... (5:6)
        # --------------------------------------------------------
        append(u'<span>')
        _content_139955154988272 = u'ok'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</span>')
        if (_backup_attrs_35794024 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35794024
    if (_backup_default_35794240 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35794240
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_35792224 = get('default', _marker)
    _value = _cache_37139408
    econtext['default'] = _value

    # <Equality expression=<Expression u'True' (3:21)> value=<Expression u'not not True' (6:22)> at 249fc50> -> _condition
    _expression = _cache_37139408

    # <Expression u'not not True' (6:22)> -> _value
    try:
        _value = not not True
    except:
        rcontext.setdefault('__error__', []).append((u'not not True', 6, 22, '<string>', _sys.exc_info()[1], ))
        raise

    _condition = (_expression == _value)
    if _condition:
        _backup_attrs_35794312 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x249f190> name=None at 249f950> -> _value
        _value = _static_38400400
        econtext['attrs'] = _value

        # <span ... (6:6)
        # --------------------------------------------------------
        append(u'<span>')
        _content_139955154988272 = u'ok'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</span>')
        if (_backup_attrs_35794312 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35794312
    if (_backup_default_35792224 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35792224
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_38450528 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38450528
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u'True' (8:21)> -> _cache_38892304
    try:
        _cache_38892304 = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 8, 21, '<string>', _sys.exc_info()[1], ))
        raise

    _backup_attrs_39792936 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2517090> name=None at 2517150> -> _value
    _value = _static_38891664
    econtext['attrs'] = _value

    # <div ... (8:4)
    # --------------------------------------------------------
    append(u'<div>')
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_39865448 = get('default', _marker)
    _value = _cache_38892304
    econtext['default'] = _value

    # <Equality expression=<Expression u'True' (8:21)> value=<Expression u'False' (9:22)> at 2517590> -> _condition
    _expression = _cache_38892304

    # <Expression u'False' (9:22)> -> _value
    try:
        _value = False
    except:
        rcontext.setdefault('__error__', []).append((u'False', 9, 22, '<string>', _sys.exc_info()[1], ))
        raise

    _condition = (_expression == _value)
    if _condition:
        _backup_attrs_39863216 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2517810> name=None at 2517690> -> _value
        _value = _static_38893584
        econtext['attrs'] = _value

        # <span ... (9:6)
        # --------------------------------------------------------
        append(u'<span>')
        _content_139955154988272 = u'bad'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</span>')
        if (_backup_attrs_39863216 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_39863216
    if (_backup_default_39865448 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39865448
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_39804224 = get('default', _marker)
    _value = _cache_38892304
    econtext['default'] = _value

    # <Equality expression=<Expression u'True' (8:21)> value=<Expression u'default' (10:22)> at 2517a50> -> _condition
    _expression = _cache_38892304

    # <Expression u'default' (10:22)> -> _value
    try:
        _value = getitem('default')
    except:
        rcontext.setdefault('__error__', []).append((u'default', 10, 22, '<string>', _sys.exc_info()[1], ))
        raise

    _condition = (_expression == _value)
    if _condition:
        _backup_attrs_39865808 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2517cd0> name=None at 2517b90> -> _value
        _value = _static_38894800
        econtext['attrs'] = _value

        # <span ... (10:6)
        # --------------------------------------------------------
        append(u'<span>')
        _content_139955154988272 = u'ok'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</span>')
        if (_backup_attrs_39865808 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_39865808
    if (_backup_default_39804224 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39804224
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_39792936 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39792936
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_39094824 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39094824
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_39791864 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39791864
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass