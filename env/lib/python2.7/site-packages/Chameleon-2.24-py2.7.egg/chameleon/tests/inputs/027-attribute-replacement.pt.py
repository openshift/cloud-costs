# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_38936400 = {}
_static_38932624 = {}
_static_39101904 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_39103376 = {u'style': u"'hij'", u'id': u'test', u'onClick': u'', u'class': u'dummy', }
_static_38935952 = {}
_static_38934352 = {}
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
    _backup_attrs_39046104 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x254a5d0> name=None at 249f050> -> _value
    _value = _static_39101904
    econtext['attrs'] = _value

    # <div ... (1:0)
    # --------------------------------------------------------
    append(u'<div')
    _attr_xmlns = u'http://www.w3.org/1999/xhtml'
    if (_attr_xmlns is not None):
        append((u' xmlns="%s"' % _attr_xmlns))
    append(u'>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_a_35883472 = get('a', _marker)

    # <Expression u"'abc'" (6:22)> -> _value
    try:
        _value = 'abc'
    except:
        rcontext.setdefault('__error__', []).append((u"'abc'", 6, 22, '<string>', _sys.exc_info()[1], ))
        raise

    econtext['a'] = _value
    _backup_attrs_38523464 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x254ab90> name=None at 254aa50> -> _value
    _value = _static_39103376
    econtext['attrs'] = _value

    # <span ... (3:2)
    # --------------------------------------------------------
    append(u'<span')
    _attr_id = u'test'
    if (_attr_id is not None):
        append((u' id="%s"' % _attr_id))
    _backup_default_39046968 = get('default', _marker)
    _value = u'dummy'
    econtext['default'] = _value

    # <Expression u"'def' + a + default" (7:30)> -> _attr_class
    try:
        _attr_class = (('def' + getitem('a')) + getitem('default'))
    except:
        rcontext.setdefault('__error__', []).append((u"'def' + a + default", 7, 30, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_class is None):
        pass
    else:
        if (_attr_class is False):
            _attr_class = None
        else:
            _tt = type(_attr_class)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_class = unicode(_attr_class)
            else:
                try:
                    if (_tt is str):
                        _attr_class = decode(_attr_class)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_class = _attr_class.__html__
                            except:
                                _attr_class = convert(_attr_class)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_class = _attr_class()
                else:
                    if ((_attr_class is not None) and (re_needs_escape(_attr_class) is not None)):
                        if ('&' in _attr_class):
                            if (';' in _attr_class):
                                _attr_class = re_amp.sub('&amp;', _attr_class)
                            else:
                                _attr_class = _attr_class.replace('&', '&amp;')
                        if ('<' in _attr_class):
                            _attr_class = _attr_class.replace('<', '&lt;')
                        if ('>' in _attr_class):
                            _attr_class = _attr_class.replace('>', '&gt;')
                        if (u'"' in _attr_class):
                            _attr_class = _attr_class.replace(u'"', '&#34;')
    if (_attr_class is not None):
        append((u'\n        class="%s"' % _attr_class))
    if (_backup_default_39046968 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39046968
    _backup_default_38526416 = get('default', _marker)
    _value = u''
    econtext['default'] = _value

    # <Expression u"'alert();'" (7:70)> -> _attr_onClick
    try:
        _attr_onClick = 'alert();'
    except:
        rcontext.setdefault('__error__', []).append((u"'alert();'", 7, 70, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_onClick is None):
        pass
    else:
        if (_attr_onClick is False):
            _attr_onClick = None
        else:
            _tt = type(_attr_onClick)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_onClick = unicode(_attr_onClick)
            else:
                try:
                    if (_tt is str):
                        _attr_onClick = decode(_attr_onClick)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_onClick = _attr_onClick.__html__
                            except:
                                _attr_onClick = convert(_attr_onClick)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_onClick = _attr_onClick()
                else:
                    if ((_attr_onClick is not None) and (re_needs_escape(_attr_onClick) is not None)):
                        if ('&' in _attr_onClick):
                            if (';' in _attr_onClick):
                                _attr_onClick = re_amp.sub('&amp;', _attr_onClick)
                            else:
                                _attr_onClick = _attr_onClick.replace('&', '&amp;')
                        if ('<' in _attr_onClick):
                            _attr_onClick = _attr_onClick.replace('<', '&lt;')
                        if ('>' in _attr_onClick):
                            _attr_onClick = _attr_onClick.replace('>', '&gt;')
                        if (u'"' in _attr_onClick):
                            _attr_onClick = _attr_onClick.replace(u'"', '&#34;')
    if (_attr_onClick is not None):
        append((u'\n        onClick="%s"' % _attr_onClick))
    if (_backup_default_38526416 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38526416
    _backup_default_38524760 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Expression u"'hij'" (7:56)> -> _attr_style
    try:
        _attr_style = 'hij'
    except:
        rcontext.setdefault('__error__', []).append((u"'hij'", 7, 56, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_style is None):
        pass
    else:
        if (_attr_style is False):
            _attr_style = None
        else:
            _tt = type(_attr_style)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_style = unicode(_attr_style)
            else:
                try:
                    if (_tt is str):
                        _attr_style = decode(_attr_style)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_style = _attr_style.__html__
                            except:
                                _attr_style = convert(_attr_style)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_style = _attr_style()
                else:
                    if ((_attr_style is not None) and (re_needs_escape(_attr_style) is not None)):
                        if ('&' in _attr_style):
                            if (';' in _attr_style):
                                _attr_style = re_amp.sub('&amp;', _attr_style)
                            else:
                                _attr_style = _attr_style.replace('&', '&amp;')
                        if ('<' in _attr_style):
                            _attr_style = _attr_style.replace('<', '&lt;')
                        if ('>' in _attr_style):
                            _attr_style = _attr_style.replace('>', '&gt;')
                        if ('"' in _attr_style):
                            _attr_style = _attr_style.replace('"', '&#34;')
    if (_attr_style is not None):
        append((u' style="%s"' % _attr_style))
    if (_backup_default_38524760 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38524760
    append('>')
    _backup_default_38525480 = get('default', _marker)

    # <Marker name='default' at 254a9d0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"a + 'ghi'" (8:21)> -> _cache_39100816
    try:
        _cache_39100816 = (getitem('a') + 'ghi')
    except:
        rcontext.setdefault('__error__', []).append((u"a + 'ghi'", 8, 21, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"a + 'ghi'" (8:21)> value=<Marker name='default' at 254a890> at 254a090> -> _condition
    _expression = _cache_39100816

    # <Marker name='default' at 254a890> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        pass
    else:
        _content = _cache_39100816
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
    if (_backup_default_38525480 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38525480
    append(u'</span>')
    if (_backup_attrs_38523464 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38523464
    if (_backup_a_35883472 is _marker):
        del econtext['a']
    else:
        econtext['a'] = _backup_a_35883472
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_39596544 = get('default', _marker)

    # <Marker name='default' at 2521f90> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello World!'" (9:21)> -> _cache_38934928
    try:
        _cache_38934928 = 'Hello World!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello World!'", 9, 21, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello World!'" (9:21)> value=<Marker name='default' at 2521c50> at 2521b50> -> _condition
    _expression = _cache_38934928

    # <Marker name='default' at 2521c50> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_38526488 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2521d90> name=None at 2521e10> -> _value
        _value = _static_38935952
        econtext['attrs'] = _value

        # <span ... (9:2)
        # --------------------------------------------------------
        append(u'<span>')
        _content_139955154988272 = u'Hello '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        _backup_attrs_36682352 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2521750> name=None at 2521ed0> -> _value
        _value = _static_38934352
        econtext['attrs'] = _value

        # <b ... (9:43)
        # --------------------------------------------------------
        append(u'<b>')
        _content_139955154988272 = u'Universe'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</b>')
        if (_backup_attrs_36682352 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_36682352
        _content_139955154988272 = u'!'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</span>')
        if (_backup_attrs_38526488 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_38526488
    else:
        _content = _cache_38934928
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
    if (_backup_default_39596544 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39596544
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_default_36682856 = get('default', _marker)

    # <Marker name='default' at 2521710> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'Hello World!'" (10:21)> -> _cache_38932752
    try:
        _cache_38932752 = 'Hello World!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello World!'", 10, 21, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'Hello World!'" (10:21)> value=<Marker name='default' at 2521410> at 25214d0> -> _condition
    _expression = _cache_38932752

    # <Marker name='default' at 2521410> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _backup_attrs_36682928 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2521090> name=None at 25215d0> -> _value
        _value = _static_38932624
        econtext['attrs'] = _value

        # <span ... (10:2)
        # --------------------------------------------------------
        append(u'<span>')
        _backup_attrs_35804656 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2521f50> name=None at 2521490> -> _value
        _value = _static_38936400
        econtext['attrs'] = _value

        # <b ... (10:37)
        # --------------------------------------------------------
        append(u'<b>')
        _content_139955154988272 = u'Hello Universe!'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</b>')
        if (_backup_attrs_35804656 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35804656
        append(u'</span>')
        if (_backup_attrs_36682928 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_36682928
    else:
        _content = _cache_38932752
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
    if (_backup_default_36682856 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36682856
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_39046104 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39046104
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass