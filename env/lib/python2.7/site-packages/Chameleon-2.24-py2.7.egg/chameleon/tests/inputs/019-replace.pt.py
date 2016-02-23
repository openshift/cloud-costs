# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_36788688 = {}
_static_36744848 = {}
_static_38465168 = {}
_static_38401424 = {}
_static_38427088 = {}
_static_38579856 = {}
_static_37141712 = {}
_static_37140688 = {}
_static_36790160 = {}
_static_36789584 = {}
_static_37141776 = {}
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
    _backup_attrs_39046608 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24aee90> name=None at 24ae750> -> _value
    _value = _static_38465168
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35794168 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24a59d0> name=None at 24a5690> -> _value
    _value = _static_38427088
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_38452904 = get('default', _marker)

    # <Marker name='default' at 236b550> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (3:22)> -> _cache_36742672
    try:
        _cache_36742672 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 3, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (3:22)> value=<Marker name='default' at 230a750> at 230ac90> -> _condition
    _expression = _cache_36742672

    # <Marker name='default' at 230a750> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_35754136 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x230ae90> name=None at 24a5e90> -> _value
        _value = _static_36744848
        econtext['attrs'] = _value

        # <div ... (3:4)
        # --------------------------------------------------------
        append(u'<div />')
        if (_backup_attrs_35754136 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35754136
    else:
        _content = _cache_36742672
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
    if (_backup_default_38452904 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38452904
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_39065936 = get('default', _marker)

    # <Marker name='default' at 236b910> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (4:22)> -> _cache_37138960
    try:
        _cache_37138960 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 4, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (4:22)> value=<Marker name='default' at 236bf10> at 236b250> -> _condition
    _expression = _cache_37138960

    # <Marker name='default' at 236bf10> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_39064568 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x236bcd0> name=None at 236b5d0> -> _value
        _value = _static_37141712
        econtext['attrs'] = _value

        # <div ... (4:4)
        # --------------------------------------------------------
        append(u'<div />')
        if (_backup_attrs_39064568 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_39064568
    else:
        _content = _cache_37138960
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
    if (_backup_default_39065936 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39065936
    _content_139955154988272 = u'1\n   2'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_39065000 = get('default', _marker)

    # <Marker name='default' at 236b650> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (5:22)> -> _cache_37140112
    try:
        _cache_37140112 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 5, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (5:22)> value=<Marker name='default' at 236bb90> at 236b3d0> -> _condition
    _expression = _cache_37140112

    # <Marker name='default' at 236bb90> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_39067304 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x236b8d0> name=None at 236bbd0> -> _value
        _value = _static_37140688
        econtext['attrs'] = _value

        # <div ... (5:4)
        # --------------------------------------------------------
        append(u'<div />')
        if (_backup_attrs_39067304 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_39067304
    else:
        _content = _cache_37140112
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
    if (_backup_default_39065000 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39065000
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_39095472 = get('default', _marker)

    # <Marker name='default' at 249f290> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (6:22)> -> _cache_38401040
    try:
        _cache_38401040 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 6, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (6:22)> value=<Marker name='default' at 249f750> at 249f210> -> _condition
    _expression = _cache_38401040

    # <Marker name='default' at 249f750> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_39095400 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x236bd10> name=None at 236b590> -> _value
        _value = _static_37141776
        econtext['attrs'] = _value

        # <div ... (6:4)
        # --------------------------------------------------------
        append(u'<div />')
        if (_backup_attrs_39095400 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_39095400
    else:
        _content = _cache_38401040
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
    if (_backup_default_39095472 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39095472
    _content_139955154988272 = u'3\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_35897496 = get('default', _marker)

    # <Marker name='default' at 24caa90> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (7:22)> -> _cache_38403600
    try:
        _cache_38403600 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 7, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (7:22)> value=<Marker name='default' at 249fc50> at 249f950> -> _condition
    _expression = _cache_38403600

    # <Marker name='default' at 249fc50> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_35900880 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x249f590> name=None at 249f450> -> _value
        _value = _static_38401424
        econtext['attrs'] = _value

        # <div ... (7:4)
        # --------------------------------------------------------
        append(u'<div>')
        _content_139955154988272 = u'4'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</div>')
        if (_backup_attrs_35900880 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35900880
    else:
        _content = _cache_38403600
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
    if (_backup_default_35897496 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35897496
    _content_139955154988272 = u'5\n   6'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_38618392 = get('default', _marker)

    # <Marker name='default' at 24ca150> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello world!'" (8:22)> -> _cache_38578576
    try:
        _cache_38578576 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 8, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello world!'" (8:22)> value=<Marker name='default' at 24cadd0> at 24caa10> -> _condition
    _expression = _cache_38578576

    # <Marker name='default' at 24cadd0> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_35899152 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x24cae90> name=None at 24ca510> -> _value
        _value = _static_38579856
        econtext['attrs'] = _value

        # <div ... (8:4)
        # --------------------------------------------------------
        append(u'<div>')
        append(u'</div>')
        if (_backup_attrs_35899152 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35899152
    else:
        _content = _cache_38578576
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
    if (_backup_default_38618392 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38618392
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_38617960 = get('default', _marker)

    # <Marker name='default' at 2315510> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'1' (9:22)> -> _cache_36790096
    try:
        _cache_36790096 = 1
    except:
        rcontext.setdefault('__error__', []).append((u'1', 9, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'1' (9:22)> value=<Marker name='default' at 2315690> at 23155d0> -> _condition
    _expression = _cache_36790096

    # <Marker name='default' at 2315690> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_38618320 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2315f90> name=None at 23154d0> -> _value
        _value = _static_36790160
        econtext['attrs'] = _value

        # <div ... (9:4)
        # --------------------------------------------------------
        append(u'<div />')
        if (_backup_attrs_38618320 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_38618320
    else:
        _content = _cache_36790096
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
    if (_backup_default_38617960 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38617960
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_38631256 = get('default', _marker)

    # <Marker name='default' at 2315dd0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'1.0' (10:22)> -> _cache_36789200
    try:
        _cache_36789200 = 1.0
    except:
        rcontext.setdefault('__error__', []).append((u'1.0', 10, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'1.0' (10:22)> value=<Marker name='default' at 2315c10> at 2315a10> -> _condition
    _expression = _cache_36789200

    # <Marker name='default' at 2315c10> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_38619832 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2315d50> name=None at 2315190> -> _value
        _value = _static_36789584
        econtext['attrs'] = _value

        # <div ... (10:4)
        # --------------------------------------------------------
        append(u'<div />')
        if (_backup_attrs_38619832 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_38619832
    else:
        _content = _cache_36789200
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
    if (_backup_default_38631256 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38631256
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_38647928 = get('default', _marker)

    # <Marker name='default' at 2315290> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'True' (11:22)> -> _cache_36789072
    try:
        _cache_36789072 = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 11, 22, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'True' (11:22)> value=<Marker name='default' at 23157d0> at 2315b90> -> _condition
    _expression = _cache_36789072

    # <Marker name='default' at 23157d0> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_39044664 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x23159d0> name=None at 2315110> -> _value
        _value = _static_36788688
        econtext['attrs'] = _value

        # <div ... (11:4)
        # --------------------------------------------------------
        append(u'<div />')
        if (_backup_attrs_39044664 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_39044664
    else:
        _content = _cache_36789072
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
    if (_backup_default_38647928 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38647928
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_35794168 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35794168
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_39046608 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39046608
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass