# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_38461520 = {u'alt': u"'Hello world!'", }
_static_38577424 = {}
_static_38427984 = {}
_static_38578896 = {u'alt': u"${'Hello world!'}", }
_static_38401104 = {u'alt': u"'Hello world!'", }
_static_38462480 = {u'alt': u"${'Hello world!'}", }
_static_38428112 = {}
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
    _backup_attrs_37150016 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24a5dd0> name=None at 24a59d0> -> _value
    _value = _static_38428112
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36785184 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24a5d50> name=None at 24a5a50> -> _value
    _value = _static_38427984
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38523176 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ca510> name=None at 24ca9d0> -> _value
    _value = _static_38577424
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _backup_default_36784176 = get('default', _marker)

    # <Marker name='default' at 24cae10> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'string:Hello world!' (3:40)> -> _cache_38578576
    try:
        _cache_38578576 = u'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u'string:Hello world!', 3, 40, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'string:Hello world!' (3:40)> value=<Marker name='default' at 24ca890> at 24ca110> -> _condition
    _expression = _cache_38578576

    # <Marker name='default' at 24ca890> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _content_139955154988272 = u'\n      Hello world!\n    '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    else:
        _content = _cache_38578576
        _content = translate(_content, default=None, domain=_i18n_domain)
        if (_content is not None):
            append(_content)
    if (_backup_default_36784176 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36784176
    append(u'</div>')
    if (_backup_attrs_38523176 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38523176
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36793448 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24caad0> name=None at 24cae90> -> _value
    _value = _static_38578896
    econtext['attrs'] = _value

    # <img ... (6:4)
    # --------------------------------------------------------
    append(u'<img')
    _backup_default_36792152 = get('default', _marker)
    _value = u"${'Hello world!'}"
    econtext['default'] = _value

    # <Translate msgid=None node=<Interpolation value=u"${'Hello world!'}" escape=True at 24ae090> at 24ae190> -> _attr_alt

    # <Interpolation value=u"${'Hello world!'}" escape=True at 24ae090> -> _attr_alt

    # <Expression u"'Hello world!'" (6:16)> -> _attr_alt
    try:
        _attr_alt = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 6, 16, '<string>', _sys.exc_info()[1], ))
        raise

    _attr_alt = _attr_alt
    _attr_alt = translate(_attr_alt, default=_attr_alt, domain=_i18n_domain)
    if (_attr_alt is None):
        pass
    else:
        if (_attr_alt is False):
            _attr_alt = None
        else:
            _tt = type(_attr_alt)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_alt = unicode(_attr_alt)
            else:
                try:
                    if (_tt is str):
                        _attr_alt = decode(_attr_alt)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_alt = _attr_alt.__html__
                            except:
                                _attr_alt = convert(_attr_alt)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_alt = _attr_alt()
                else:
                    if ((_attr_alt is not None) and (re_needs_escape(_attr_alt) is not None)):
                        if ('&' in _attr_alt):
                            if (';' in _attr_alt):
                                _attr_alt = re_amp.sub('&amp;', _attr_alt)
                            else:
                                _attr_alt = _attr_alt.replace('&', '&amp;')
                        if ('<' in _attr_alt):
                            _attr_alt = _attr_alt.replace('<', '&lt;')
                        if ('>' in _attr_alt):
                            _attr_alt = _attr_alt.replace('>', '&gt;')
                        if (u'"' in _attr_alt):
                            _attr_alt = _attr_alt.replace(u'"', '&#34;')
    if (_attr_alt is not None):
        append((u' alt="%s"' % _attr_alt))
    if (_backup_default_36792152 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36792152
    append(u' />')
    if (_backup_attrs_36793448 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36793448
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_37151448 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ae410> name=None at 24ae310> -> _value
    _value = _static_38462480
    econtext['attrs'] = _value

    # <img ... (7:4)
    # --------------------------------------------------------
    append(u'<img')
    _backup_default_37154184 = get('default', _marker)
    _value = u"${'Hello world!'}"
    econtext['default'] = _value

    # <Translate msgid=u'hello_world' node=<Interpolation value=u"${'Hello world!'}" escape=True at 24ae9d0> at 24aecd0> -> _attr_alt

    # <Interpolation value=u"${'Hello world!'}" escape=True at 24ae9d0> -> _attr_alt

    # <Expression u"'Hello world!'" (7:16)> -> _attr_alt
    try:
        _attr_alt = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 7, 16, '<string>', _sys.exc_info()[1], ))
        raise

    _attr_alt = _attr_alt
    _attr_alt = translate(u'hello_world', default=_attr_alt, domain=_i18n_domain)
    if (_attr_alt is None):
        pass
    else:
        if (_attr_alt is False):
            _attr_alt = None
        else:
            _tt = type(_attr_alt)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_alt = unicode(_attr_alt)
            else:
                try:
                    if (_tt is str):
                        _attr_alt = decode(_attr_alt)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_alt = _attr_alt.__html__
                            except:
                                _attr_alt = convert(_attr_alt)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_alt = _attr_alt()
                else:
                    if ((_attr_alt is not None) and (re_needs_escape(_attr_alt) is not None)):
                        if ('&' in _attr_alt):
                            if (';' in _attr_alt):
                                _attr_alt = re_amp.sub('&amp;', _attr_alt)
                            else:
                                _attr_alt = _attr_alt.replace('&', '&amp;')
                        if ('<' in _attr_alt):
                            _attr_alt = _attr_alt.replace('<', '&lt;')
                        if ('>' in _attr_alt):
                            _attr_alt = _attr_alt.replace('>', '&gt;')
                        if (u'"' in _attr_alt):
                            _attr_alt = _attr_alt.replace(u'"', '&#34;')
    if (_attr_alt is not None):
        append((u' alt="%s"' % _attr_alt))
    if (_backup_default_37154184 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_37154184
    append(u' />')
    if (_backup_attrs_37151448 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37151448
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_37152528 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ae050> name=None at 24ae210> -> _value
    _value = _static_38461520
    econtext['attrs'] = _value

    # <img ... (8:4)
    # --------------------------------------------------------
    append(u'<img')
    _backup_default_37151520 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Translate msgid=None node=<Expression u"'Hello world!'" (8:29)> at 24ae750> -> _attr_alt

    # <Expression u"'Hello world!'" (8:29)> -> _attr_alt
    try:
        _attr_alt = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 8, 29, '<string>', _sys.exc_info()[1], ))
        raise

    _attr_alt = translate(_attr_alt, default=_attr_alt, domain=_i18n_domain)
    if (_attr_alt is None):
        pass
    else:
        if (_attr_alt is False):
            _attr_alt = None
        else:
            _tt = type(_attr_alt)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_alt = unicode(_attr_alt)
            else:
                try:
                    if (_tt is str):
                        _attr_alt = decode(_attr_alt)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_alt = _attr_alt.__html__
                            except:
                                _attr_alt = convert(_attr_alt)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_alt = _attr_alt()
                else:
                    if ((_attr_alt is not None) and (re_needs_escape(_attr_alt) is not None)):
                        if ('&' in _attr_alt):
                            if (';' in _attr_alt):
                                _attr_alt = re_amp.sub('&amp;', _attr_alt)
                            else:
                                _attr_alt = _attr_alt.replace('&', '&amp;')
                        if ('<' in _attr_alt):
                            _attr_alt = _attr_alt.replace('<', '&lt;')
                        if ('>' in _attr_alt):
                            _attr_alt = _attr_alt.replace('>', '&gt;')
                        if ('"' in _attr_alt):
                            _attr_alt = _attr_alt.replace('"', '&#34;')
    if (_attr_alt is not None):
        append((u' alt="%s"' % _attr_alt))
    if (_backup_default_37151520 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_37151520
    append(u' />')
    if (_backup_attrs_37152528 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37152528
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_37151088 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249f450> name=None at 249fcd0> -> _value
    _value = _static_38401104
    econtext['attrs'] = _value

    # <img ... (9:4)
    # --------------------------------------------------------
    append(u'<img')
    _backup_default_37154472 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Translate msgid=u'hello_world' node=<Expression u"'Hello world!'" (9:29)> at 249fc50> -> _attr_alt

    # <Expression u"'Hello world!'" (9:29)> -> _attr_alt
    try:
        _attr_alt = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 9, 29, '<string>', _sys.exc_info()[1], ))
        raise

    _attr_alt = translate(u'hello_world', default=_attr_alt, domain=_i18n_domain)
    if (_attr_alt is None):
        pass
    else:
        if (_attr_alt is False):
            _attr_alt = None
        else:
            _tt = type(_attr_alt)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_alt = unicode(_attr_alt)
            else:
                try:
                    if (_tt is str):
                        _attr_alt = decode(_attr_alt)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_alt = _attr_alt.__html__
                            except:
                                _attr_alt = convert(_attr_alt)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_alt = _attr_alt()
                else:
                    if ((_attr_alt is not None) and (re_needs_escape(_attr_alt) is not None)):
                        if ('&' in _attr_alt):
                            if (';' in _attr_alt):
                                _attr_alt = re_amp.sub('&amp;', _attr_alt)
                            else:
                                _attr_alt = _attr_alt.replace('&', '&amp;')
                        if ('<' in _attr_alt):
                            _attr_alt = _attr_alt.replace('<', '&lt;')
                        if ('>' in _attr_alt):
                            _attr_alt = _attr_alt.replace('>', '&gt;')
                        if ('"' in _attr_alt):
                            _attr_alt = _attr_alt.replace('"', '&#34;')
    if (_attr_alt is not None):
        append((u' alt="%s"' % _attr_alt))
    if (_backup_default_37154472 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_37154472
    append(u' />')
    if (_backup_attrs_37151088 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37151088
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_36785184 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36785184
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_37150016 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37150016
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass