# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_39102032 = {}
_static_39102544 = {}
_static_37140880 = {}
_static_39103376 = {}
_static_37139664 = {}
_static_37139600 = {}
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
    _backup_attrs_39095400 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236b4d0> name=None at 236b310> -> _value
    _value = _static_37139664
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39815792 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236b990> name=None at 236b890> -> _value
    _value = _static_37140880
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39828080 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236b490> name=None at 236b390> -> _value
    _value = _static_37139600
    econtext['attrs'] = _value

    # <ul ... (3:4)
    # --------------------------------------------------------
    append(u'<ul>')
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_i_35883472 = get('i', _marker)

    # <Expression u'(1, 2, 3)' (4:26)> -> _iterator
    try:
        _iterator = (1, 2, 3, )
    except:
        rcontext.setdefault('__error__', []).append((u'(1, 2, 3)', 4, 26, '<string>', _sys.exc_info()[1], ))
        raise

    (_iterator, __index_39101968, ) = getitem('repeat')(u'i', _iterator)
    econtext['i'] = None
    for _item in _iterator:
        econtext['i'] = _item
        _backup_attrs_40288912 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x254a650> name=None at 254a190> -> _value
        _value = _static_39102032
        econtext['attrs'] = _value

        # <li ... (4:37)
        # --------------------------------------------------------
        append(u'<li>')
        _backup_default_39802640 = get('default', _marker)

        # <Marker name='default' at 254a510> -> _value
        _value = _marker_default
        econtext['default'] = _value

        # <Expression u'i' (4:54)> -> _cache_39101904
        try:
            _cache_39101904 = getitem('i')
        except:
            rcontext.setdefault('__error__', []).append((u'i', 4, 54, '<string>', _sys.exc_info()[1], ))
            raise


        # <Identity expression=<Expression u'i' (4:54)> value=<Marker name='default' at 254a110> at 254a2d0> -> _condition
        _expression = _cache_39101904

        # <Marker name='default' at 254a110> -> _value
        _value = _marker_default
        _condition = (_expression is _value)
        if _condition:
            pass
        else:
            _content = _cache_39101904
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
        if (_backup_default_39802640 is _marker):
            del econtext['default']
        else:
            econtext['default'] = _backup_default_39802640
        append(u'</li>')
        if (_backup_attrs_40288912 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_40288912
        __index_39101968 -= 1
        if (__index_39101968 > 0):
            append('\n      ')
    if (_backup_i_35883472 is _marker):
        del econtext['i']
    else:
        econtext['i'] = _backup_i_35883472
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_j_37194704 = get('j', _marker)

    # <Expression u'(1, 2, 3)' (5:42)> -> _iterator
    try:
        _iterator = (1, 2, 3, )
    except:
        rcontext.setdefault('__error__', []).append((u'(1, 2, 3)', 5, 42, '<string>', _sys.exc_info()[1], ))
        raise

    (_iterator, __index_39100944, ) = getitem('repeat')(u'j', _iterator)
    econtext['j'] = None
    for _item in _iterator:
        econtext['j'] = _item
        _backup_attrs_40302712 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x254ab90> name=None at 254af90> -> _value
        _value = _static_39103376
        econtext['attrs'] = _value

        # <li ... (5:53)
        # --------------------------------------------------------
        append(u'<li>')
        _backup_default_40289920 = get('default', _marker)

        # <Marker name='default' at 254a890> -> _value
        _value = _marker_default
        econtext['default'] = _value

        # <Expression u'j' (5:70)> -> _cache_39103632
        try:
            _cache_39103632 = getitem('j')
        except:
            rcontext.setdefault('__error__', []).append((u'j', 5, 70, '<string>', _sys.exc_info()[1], ))
            raise


        # <Identity expression=<Expression u'j' (5:70)> value=<Marker name='default' at 254aa90> at 254a390> -> _condition
        _expression = _cache_39103632

        # <Marker name='default' at 254aa90> -> _value
        _value = _marker_default
        _condition = (_expression is _value)
        if _condition:
            pass
        else:
            _content = _cache_39103632
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
        if (_backup_default_40289920 is _marker):
            del econtext['default']
        else:
            econtext['default'] = _backup_default_40289920
        append(u'</li>')
        if (_backup_attrs_40302712 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_40302712
        __index_39100944 -= 1
        if (__index_39100944 > 0):
            append('\n      ')
    if (_backup_j_37194704 is _marker):
        del econtext['j']
    else:
        econtext['j'] = _backup_j_37194704
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _content_139955154988272 = u'\n        '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_count_37019152 = get('count', _marker)

    # <Expression u'(1, 2, 3)' (7:38)> -> _iterator
    try:
        _iterator = (1, 2, 3, )
    except:
        rcontext.setdefault('__error__', []).append((u'(1, 2, 3)', 7, 38, '<string>', _sys.exc_info()[1], ))
        raise

    (_iterator, __index_39104016, ) = getitem('repeat')(u'count', _iterator)
    econtext['count'] = None
    for _item in _iterator:
        econtext['count'] = _item
        _content_139955154988272 = u'\n          '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        _backup_default_39927960 = get('default', _marker)

        # <Marker name='default' at 251bf10> -> _value
        _value = _marker_default
        econtext['default'] = _value

        # <Expression u'count' (8:29)> -> _cache_38911312
        try:
            _cache_38911312 = getitem('count')
        except:
            rcontext.setdefault('__error__', []).append((u'count', 8, 29, '<string>', _sys.exc_info()[1], ))
            raise


        # <Identity expression=<Expression u'count' (8:29)> value=<Marker name='default' at 251bc10> at 251bc90> -> _condition
        _expression = _cache_38911312

        # <Marker name='default' at 251bc10> -> _value
        _value = _marker_default
        _condition = (_expression is _value)
        if _condition:
            _backup_attrs_39930912 = get('attrs', _marker)

            # <Static value=<_ast.Dict object at 0x254a850> name=None at 254ae90> -> _value
            _value = _static_39102544
            econtext['attrs'] = _value

            # <span ... (8:10)
            # --------------------------------------------------------
            append(u'<span\n                />')
            if (_backup_attrs_39930912 is _marker):
                del econtext['attrs']
            else:
                econtext['attrs'] = _backup_attrs_39930912
        else:
            _content = _cache_38911312
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
        if (_backup_default_39927960 is _marker):
            del econtext['default']
        else:
            econtext['default'] = _backup_default_39927960

        # <Expression u"not repeat['count'].end" (9:40)> -> _condition
        try:
            _condition = not getitem('repeat')['count'].end
        except:
            rcontext.setdefault('__error__', []).append((u"not repeat['count'].end", 9, 40, '<string>', _sys.exc_info()[1], ))
            raise

        if _condition:
            _content_139955154988272 = u','
            if (_content_139955154988272 is not None):
                append(_content_139955154988272)
        _content_139955154988272 = u'\n       '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        __index_39104016 -= 1
        if (__index_39104016 > 0):
            append('\n        ')
    if (_backup_count_37019152 is _marker):
        del econtext['count']
    else:
        econtext['count'] = _backup_count_37019152
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _content_139955154988272 = u'.\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</ul>')
    if (_backup_attrs_39828080 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39828080
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_39815792 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39815792
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_39095400 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39095400
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass