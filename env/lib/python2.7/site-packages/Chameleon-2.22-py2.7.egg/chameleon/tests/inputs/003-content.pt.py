# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_35889296 = {}
_static_36669328 = {}
_static_35932752 = {}
_static_35780752 = {}
_static_35829264 = {}
_static_35830160 = {}
_static_36668752 = {}
_static_35800464 = {}
_static_35829776 = {}
_static_36669776 = {}
_static_35831056 = {}
_static_35932624 = {}
_static_35883024 = {}
_static_35889872 = {}
_static_35882896 = {}
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
    _backup_attrs_36729128 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2238790> name=None at 2238590> -> _value
    _value = _static_35882896
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36718280 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2244a50> name=None at 2244990> -> _value
    _value = _static_35932752
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36722808 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22449d0> name=None at 2244d50> -> _value
    _value = _static_35932624
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_36723816 = get('default', _marker)

    # <Marker name='default' at 2244b90> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (3:22)> -> _cache_35933712
    try:
        _cache_35933712 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 3, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (3:22)> value=<Marker name='default' at 2244e50> at 2244d10> -> _condition
    _expression = _cache_35933712

    # <Marker name='default' at 2244e50> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35933712
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
    if (_backup_default_36723816 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36723816
    append(u'</div>')
    if (_backup_attrs_36722808 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36722808
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36725608 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222b810> name=None at 222b050> -> _value
    _value = _static_35829776
    econtext['attrs'] = _value

    # <div ... (4:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_36723960 = get('default', _marker)

    # <Marker name='default' at 2244e90> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (4:22)> -> _cache_35932816
    try:
        _cache_35932816 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 4, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (4:22)> value=<Marker name='default' at 2244650> at 2244850> -> _condition
    _expression = _cache_35932816

    # <Marker name='default' at 2244650> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35932816
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
    if (_backup_default_36723960 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36723960
    append(u'</div>')
    if (_backup_attrs_36725608 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36725608
    _content_139955154988272 = u'1\n   2'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36728632 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222b610> name=None at 222b6d0> -> _value
    _value = _static_35829264
    econtext['attrs'] = _value

    # <div ... (5:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_36726760 = get('default', _marker)

    # <Marker name='default' at 222b510> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (5:22)> -> _cache_35828624
    try:
        _cache_35828624 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 5, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (5:22)> value=<Marker name='default' at 222b0d0> at 222b190> -> _condition
    _expression = _cache_35828624

    # <Marker name='default' at 222b0d0> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35828624
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
    if (_backup_default_36726760 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36726760
    append(u'</div>')
    if (_backup_attrs_36728632 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36728632
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35918048 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222b990> name=None at 222b110> -> _value
    _value = _static_35830160
    econtext['attrs'] = _value

    # <div ... (6:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35918624 = get('default', _marker)

    # <Marker name='default' at 222bfd0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (6:22)> -> _cache_35828432
    try:
        _cache_35828432 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 6, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (6:22)> value=<Marker name='default' at 222b090> at 222bad0> -> _condition
    _expression = _cache_35828432

    # <Marker name='default' at 222b090> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35828432
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
    if (_backup_default_35918624 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35918624
    append(u'</div>')
    if (_backup_attrs_35918048 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35918048
    _content_139955154988272 = u'3\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36622920 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222bd10> name=None at 222b750> -> _value
    _value = _static_35831056
    econtext['attrs'] = _value

    # <div ... (7:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35917904 = get('default', _marker)

    # <Marker name='default' at 222b890> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (7:22)> -> _cache_35830544
    try:
        _cache_35830544 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 7, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (7:22)> value=<Marker name='default' at 222b910> at 222ba10> -> _condition
    _expression = _cache_35830544

    # <Marker name='default' at 222b910> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _content_139955154988272 = u'4'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    else:
        _content = _cache_35830544
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
    if (_backup_default_35917904 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35917904
    append(u'</div>')
    if (_backup_attrs_36622920 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36622920
    _content_139955154988272 = u'5\n   6'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36625656 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224590> name=None at 22243d0> -> _value
    _value = _static_35800464
    econtext['attrs'] = _value

    # <div ... (8:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_36625512 = get('default', _marker)

    # <Marker name='default' at 22242d0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (8:22)> -> _cache_35799696
    try:
        _cache_35799696 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 8, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (8:22)> value=<Marker name='default' at 2224150> at 2224fd0> -> _condition
    _expression = _cache_35799696

    # <Marker name='default' at 2224150> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35799696
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
    if (_backup_default_36625512 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36625512
    append(u'</div>')
    if (_backup_attrs_36625656 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36625656
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36629968 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8550> name=None at 22f82d0> -> _value
    _value = _static_36668752
    econtext['attrs'] = _value

    # <div ... (9:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_36638016 = get('default', _marker)

    # <Marker name='default' at 2224dd0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'1' (9:22)> -> _cache_35801168
    try:
        _cache_35801168 = 1
    except:
        rcontext.setdefault('__error__', []).append((u'1', 9, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'1' (9:22)> value=<Marker name='default' at 22249d0> at 2224990> -> _condition
    _expression = _cache_35801168

    # <Marker name='default' at 22249d0> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35801168
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
    if (_backup_default_36638016 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36638016
    append(u'</div>')
    if (_backup_attrs_36629968 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36629968
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36645704 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8790> name=None at 22f8750> -> _value
    _value = _static_36669328
    econtext['attrs'] = _value

    # <div ... (10:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_36644696 = get('default', _marker)

    # <Marker name='default' at 22f8350> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'1.0' (10:22)> -> _cache_36667600
    try:
        _cache_36667600 = 1.0
    except:
        rcontext.setdefault('__error__', []).append((u'1.0', 10, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'1.0' (10:22)> value=<Marker name='default' at 22f8150> at 22f8490> -> _condition
    _expression = _cache_36667600

    # <Marker name='default' at 22f8150> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_36667600
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
    if (_backup_default_36644696 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36644696
    append(u'</div>')
    if (_backup_attrs_36645704 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36645704
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35900664 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8950> name=None at 22f8890> -> _value
    _value = _static_36669776
    econtext['attrs'] = _value

    # <div ... (11:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35898288 = get('default', _marker)

    # <Marker name='default' at 22f8bd0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'True' (11:22)> -> _cache_36671120
    try:
        _cache_36671120 = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 11, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'True' (11:22)> value=<Marker name='default' at 22f8f10> at 22f8f50> -> _condition
    _expression = _cache_36671120

    # <Marker name='default' at 22f8f10> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_36671120
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
    if (_backup_default_35898288 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35898288
    append(u'</div>')
    if (_backup_attrs_35900664 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35900664
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36634424 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2238810> name=None at 2238290> -> _value
    _value = _static_35883024
    econtext['attrs'] = _value

    # <div ... (12:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35900232 = get('default', _marker)

    # <Marker name='default' at 22f84d0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'False' (12:22)> -> _cache_36668816
    try:
        _cache_36668816 = False
    except:
        rcontext.setdefault('__error__', []).append((u'False', 12, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'False' (12:22)> value=<Marker name='default' at 22f8c90> at 22f8c50> -> _condition
    _expression = _cache_36668816

    # <Marker name='default' at 22f8c90> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_36668816
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
    if (_backup_default_35900232 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35900232
    append(u'</div>')
    if (_backup_attrs_36634424 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36634424
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35898792 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x221f890> name=None at 221ff90> -> _value
    _value = _static_35780752
    econtext['attrs'] = _value

    # <div ... (13:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_36721512 = get('default', _marker)

    # <Marker name='default' at 221fcd0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'0' (13:22)> -> _cache_35708496
    try:
        _cache_35708496 = 0
    except:
        rcontext.setdefault('__error__', []).append((u'0', 13, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'0' (13:22)> value=<Marker name='default' at 220ddd0> at 220dd50> -> _condition
    _expression = _cache_35708496

    # <Marker name='default' at 220ddd0> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35708496
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
    if (_backup_default_36721512 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36721512
    append(u'</div>')
    if (_backup_attrs_35898792 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35898792
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35898504 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x223a090> name=None at 223a050> -> _value
    _value = _static_35889296
    econtext['attrs'] = _value

    # <div ... (14:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35897784 = get('default', _marker)

    # <Marker name='default' at 221f610> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'None' (14:22)> -> _cache_35781136
    try:
        _cache_35781136 = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 14, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'None' (14:22)> value=<Marker name='default' at 221ff10> at 221f490> -> _condition
    _expression = _cache_35781136

    # <Marker name='default' at 221ff10> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35781136
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
    if (_backup_default_35897784 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35897784
    append(u'</div>')
    if (_backup_attrs_35898504 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35898504
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_35899440 = get('default', _marker)

    # <Marker name='default' at 223a590> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'content' (15:22)> -> _cache_35890192
    try:
        _cache_35890192 = getitem('content')
    except:
        rcontext.setdefault('__error__', []).append((u'content', 15, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'content' (15:22)> value=<Marker name='default' at 223a490> at 223a4d0> -> _condition
    _expression = _cache_35890192

    # <Marker name='default' at 223a490> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_35901024 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x223a2d0> name=None at 223a290> -> _value
        _value = _static_35889872
        econtext['attrs'] = _value

        # <div ... (15:4)
        # --------------------------------------------------------
        append(u'<div />')
        if (_backup_attrs_35901024 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35901024
    else:
        _content = _cache_35890192
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
    if (_backup_default_35899440 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35899440
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_36718280 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36718280
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_36729128 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36729128
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass