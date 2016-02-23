# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_38401872 = {}
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
    _backup_attrs_35793880 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249f750> name=None at 249f810> -> _value
    _value = _static_38401872
    econtext['attrs'] = _value

    # <div ... (1:0)
    # --------------------------------------------------------
    append(u'<div>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_40161008 = get('default', _marker)

    # <Marker name='default' at 2658ad0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello World!'" (2:24)> -> _cache_40208016
    try:
        _cache_40208016 = 'Hello World!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello World!'", 2, 24, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello World!'" (2:24)> value=<Marker name='default' at 2658710> at 2658990> -> _condition
    _expression = _cache_40208016

    # <Marker name='default' at 2658710> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_40208016
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
    if (_backup_default_40161008 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_40161008
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_35794744 = get('default', _marker)

    # <Marker name='default' at 2521610> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello World!'" (3:28)> -> _cache_36787408
    try:
        _cache_36787408 = 'Hello World!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello World!'", 3, 28, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello World!'" (3:28)> value=<Marker name='default' at 2521f90> at 2521cd0> -> _condition
    _expression = _cache_36787408

    # <Marker name='default' at 2521f90> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_36787408
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
    if (_backup_default_35794744 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35794744
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_35792944 = get('default', _marker)

    # <Marker name='default' at 25219d0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello World!'" (4:20)> -> _cache_40209232
    try:
        _cache_40209232 = 'Hello World!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello World!'", 4, 20, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello World!'" (4:20)> value=<Marker name='default' at 2521810> at 2521910> -> _condition
    _expression = _cache_40209232

    # <Marker name='default' at 2521810> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_40209232
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
    if (_backup_default_35792944 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35792944
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_i_40210256 = get('i', _marker)

    # <Expression u'range(3)' (5:26)> -> _iterator
    try:
        _iterator = get('range', range)(3)
    except:
        rcontext.setdefault('__error__', []).append((u'range(3)', 5, 26, '<string>', _sys.exc_info()[1], ))
        raise

    (_iterator, __index_38934736, ) = getitem('repeat')(u'i', _iterator)
    econtext['i'] = None
    for _item in _iterator:
        econtext['i'] = _item
        _backup_default_40162008 = get('default', _marker)

        # <Marker name='default' at 2521f50> -> _value
        _value = _marker_default
        econtext['default'] = _value

        # <Expression u'i' (5:45)> -> _cache_38932816
        try:
            _cache_38932816 = getitem('i')
        except:
            rcontext.setdefault('__error__', []).append((u'i', 5, 45, '<string>', _sys.exc_info()[1], ))
            raise


        # <Identity expression=<Expression u'i' (5:45)> value=<Marker name='default' at 2521050> at 25213d0> -> _condition
        _expression = _cache_38932816

        # <Marker name='default' at 2521050> -> _value
        _value = _marker_default
        _condition = (_expression is _value)
        if _condition:
            pass
        else:
            _content = _cache_38932816
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
        if (_backup_default_40162008 is _marker):
            del econtext['default']
        else:
            econtext['default'] = _backup_default_40162008
        __index_38934736 -= 1
        if (__index_38934736 > 0):
            append('\n  ')
    if (_backup_i_40210256 is _marker):
        del econtext['i']
    else:
        econtext['i'] = _backup_i_40210256
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u'True' (6:22)> -> _condition
    try:
        _condition = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 6, 22, '<string>', _sys.exc_info()[1], ))
        raise

    if _condition:
        _content_139955154988272 = u'True'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_35793880 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35793880
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass