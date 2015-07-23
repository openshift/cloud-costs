# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_38588816 = {}
_static_35799696 = {}
_static_38462608 = {}
_static_38590736 = {}
_static_38589968 = {}
_static_35802320 = {}
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
    _backup_attrs_35342528 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24cd910> name=None at 24cd410> -> _value
    _value = _static_38590736
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35343752 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24cd610> name=None at 24cd8d0> -> _value
    _value = _static_38589968
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35343680 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24cd190> name=None at 24cdfd0> -> _value
    _value = _static_38588816
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35343392 = get('default', _marker)

    # <Marker name='default' at 24cd710> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'message' (3:27)> -> _cache_38588624
    try:
        _cache_38588624 = getitem('message')
    except:
        rcontext.setdefault('__error__', []).append((u'message', 3, 27, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'message' (3:27)> value=<Marker name='default' at 24cd590> at 24cd490> -> _condition
    _expression = _cache_38588624

    # <Marker name='default' at 24cd590> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_38588624
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
    if (_backup_default_35343392 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35343392
    append(u'</div>')
    if (_backup_attrs_35343680 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35343680
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35343176 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ae490> name=None at 24ae810> -> _value
    _value = _static_38462608
    econtext['attrs'] = _value

    # <div ... (4:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35344112 = get('default', _marker)

    # <Marker name='default' at 24aebd0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'message' (4:32)> -> _cache_38461520
    try:
        _cache_38461520 = getitem('message')
    except:
        rcontext.setdefault('__error__', []).append((u'message', 4, 32, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'message' (4:32)> value=<Marker name='default' at 24ae910> at 24ae210> -> _condition
    _expression = _cache_38461520

    # <Marker name='default' at 24ae910> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_38461520
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
    if (_backup_default_35344112 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35344112
    append(u'</div>')
    if (_backup_attrs_35343176 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35343176
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38452616 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224290> name=None at 2224050> -> _value
    _value = _static_35799696
    econtext['attrs'] = _value

    # <div ... (5:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35340656 = get('default', _marker)

    # <Marker name='default' at 24ae110> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'string:${message}' (5:27)> -> _cache_38464720
    try:
        _cache_38464720 = getitem('message')
        _cache_38464720 = _cache_38464720
    except:
        rcontext.setdefault('__error__', []).append((u'string:${message}', 5, 27, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'string:${message}' (5:27)> value=<Marker name='default' at 24ae690> at 24ae990> -> _condition
    _expression = _cache_38464720

    # <Marker name='default' at 24ae690> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_38464720
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
    if (_backup_default_35340656 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35340656
    append(u'</div>')
    if (_backup_attrs_38452616 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38452616
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_37030800 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224cd0> name=None at 22244d0> -> _value
    _value = _static_35802320
    econtext['attrs'] = _value

    # <div ... (6:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_35875584 = get('default', _marker)

    # <Marker name='default' at 2224d10> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'string:${message}' (6:32)> -> _cache_35802448
    try:
        _cache_35802448 = getitem('message')
        _cache_35802448 = _cache_35802448
    except:
        rcontext.setdefault('__error__', []).append((u'string:${message}', 6, 32, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'string:${message}' (6:32)> value=<Marker name='default' at 22243d0> at 2224090> -> _condition
    _expression = _cache_35802448

    # <Marker name='default' at 22243d0> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_35802448
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
    if (_backup_default_35875584 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35875584
    append(u'</div>')
    if (_backup_attrs_37030800 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37030800

    # <Expression u'message' (7:6)> -> _content_139955154988272
    try:
        _content_139955154988272 = getitem('message')
    except:
        rcontext.setdefault('__error__', []).append((u'message', 7, 6, '<string>', _sys.exc_info()[1], ))
        raise

    if (_content_139955154988272 is None):
        pass
    else:
        if (_content_139955154988272 is False):
            _content_139955154988272 = None
        else:
            _tt = type(_content_139955154988272)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _content_139955154988272 = unicode(_content_139955154988272)
            else:
                try:
                    if (_tt is str):
                        _content_139955154988272 = decode(_content_139955154988272)
                    else:
                        if (_tt is not unicode):
                            try:
                                _content_139955154988272 = _content_139955154988272.__html__
                            except:
                                _content_139955154988272 = convert(_content_139955154988272)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _content_139955154988272 = _content_139955154988272()
                else:
                    if ((_content_139955154988272 is not None) and (re_needs_escape(_content_139955154988272) is not None)):
                        if ('&' in _content_139955154988272):
                            if (';' in _content_139955154988272):
                                _content_139955154988272 = re_amp.sub('&amp;', _content_139955154988272)
                            else:
                                _content_139955154988272 = _content_139955154988272.replace('&', '&amp;')
                        if ('<' in _content_139955154988272):
                            _content_139955154988272 = _content_139955154988272.replace('<', '&lt;')
                        if ('>' in _content_139955154988272):
                            _content_139955154988272 = _content_139955154988272.replace('>', '&gt;')
                        if ('\x00' in _content_139955154988272):
                            _content_139955154988272 = _content_139955154988272.replace('\x00', '&#34;')
    _content_139955154988272 = ('%s%s%s' % ((u'\n    ' if (u'\n    ' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u'\n  ' if (u'\n  ' is not None) else ''), ))
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_35343752 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35343752
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_35342528 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35342528
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass