# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_38579792 = {}
_static_38552272 = {}
_static_35801168 = {}
_static_38555600 = {}
_static_35799376 = {}
_static_38553168 = {}
_static_38553552 = {}
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
    _backup_attrs_39070032 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24c4650> name=None at 223a290> -> _value
    _value = _static_38553168
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39067944 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24c4fd0> name=None at 24c4f90> -> _value
    _value = _static_38555600
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39069312 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24c47d0> name=None at 24c4b90> -> _value
    _value = _static_38553552
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_39069744 = get('default', _marker)

    # <Marker name='default' at 24c4610> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'string:1 < 2' (3:27)> -> _cache_38555024
    try:
        _cache_38555024 = u'1 < 2'
    except:
        rcontext.setdefault('__error__', []).append((u'string:1 < 2', 3, 27, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'string:1 < 2' (3:27)> value=<Marker name='default' at 24c4e10> at 24c4950> -> _condition
    _expression = _cache_38555024

    # <Marker name='default' at 24c4e10> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_38555024
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
    if (_backup_default_39069744 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39069744
    append(u'</div>')
    if (_backup_attrs_39069312 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39069312
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39070608 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24c42d0> name=None at 24c4290> -> _value
    _value = _static_38552272
    econtext['attrs'] = _value

    # <div ... (4:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_39044592 = get('default', _marker)

    # <Marker name='default' at 24c49d0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'string:2 < 3' (4:32)> -> _cache_38552400
    try:
        _cache_38552400 = u'2 < 3'
    except:
        rcontext.setdefault('__error__', []).append((u'string:2 < 3', 4, 32, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'string:2 < 3' (4:32)> value=<Marker name='default' at 24c4890> at 24c4250> -> _condition
    _expression = _cache_38552400

    # <Marker name='default' at 24c4890> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_38552400
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
    if (_backup_default_39044592 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39044592
    append(u'</div>')
    if (_backup_attrs_39070608 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39070608
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_37107256 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224850> name=None at 22241d0> -> _value
    _value = _static_35801168
    econtext['attrs'] = _value

    # <div ... (5:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35897424 = get('default', _marker)

    # <Marker name='default' at 2224250> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"string:3 ${'<'} 4" (5:32)> -> _cache_38551888
    try:
        _cache_38551888 = '<'
        _cache_38551888 = ('%s%s%s' % ((u'3 ' if (u'3 ' is not None) else ''), (_cache_38551888 if (_cache_38551888 is not None) else ''), (u' 4' if (u' 4' is not None) else ''), ))
    except:
        rcontext.setdefault('__error__', []).append((u"string:3 ${'<'} 4", 5, 32, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"string:3 ${'<'} 4" (5:32)> value=<Marker name='default' at 24c4110> at 24c40d0> -> _condition
    _expression = _cache_38551888

    # <Marker name='default' at 24c4110> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_38551888
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
    if (_backup_default_35897424 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35897424
    append(u'</div>')
    if (_backup_attrs_37107256 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37107256
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39055304 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224150> name=None at 2224dd0> -> _value
    _value = _static_35799376
    econtext['attrs'] = _value

    # <div ... (6:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_39086560 = get('default', _marker)

    # <Marker name='default' at 2224a10> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'%d < %d' % (4, 5)" (6:32)> -> _cache_35801680
    try:
        _cache_35801680 = ('%d < %d' % (4, 5, ))
    except:
        rcontext.setdefault('__error__', []).append((u"'%d < %d' % (4, 5)", 6, 32, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'%d < %d' % (4, 5)" (6:32)> value=<Marker name='default' at 2224cd0> at 2224ed0> -> _condition
    _expression = _cache_35801680

    # <Marker name='default' at 2224cd0> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35801680
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
    if (_backup_default_39086560 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39086560
    append(u'</div>')
    if (_backup_attrs_39055304 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39055304
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_39076928 = get('default', _marker)

    # <Marker name='default' at 24ca810> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'content' (7:32)> -> _cache_38578128
    try:
        _cache_38578128 = getitem('content')
    except:
        rcontext.setdefault('__error__', []).append((u'content', 7, 32, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'content' (7:32)> value=<Marker name='default' at 24cab50> at 24ca610> -> _condition
    _expression = _cache_38578128

    # <Marker name='default' at 24cab50> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_39051992 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x24cae50> name=None at 24cac10> -> _value
        _value = _static_38579792
        econtext['attrs'] = _value

        # <div ... (7:4)
        # --------------------------------------------------------
        append(u'<div />')
        if (_backup_attrs_39051992 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_39051992
    else:
        _content = _cache_38578128
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
    if (_backup_default_39076928 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39076928
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_39067944 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39067944
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_39070032 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39070032
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass