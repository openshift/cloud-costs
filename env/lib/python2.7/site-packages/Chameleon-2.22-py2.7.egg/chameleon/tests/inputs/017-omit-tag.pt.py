# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_38461840 = {}
_static_38461520 = {}
_static_38576336 = {u'class': u"${'omitted'}", }
_static_38578640 = {u'class': u'omitted', }
_static_38464592 = {}
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
    _backup_attrs_38457568 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ae190> name=None at 24aebd0> -> _value
    _value = _static_38461840
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36649800 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24aec50> name=None at 24ae510> -> _value
    _value = _static_38464592
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _content_139955154988272 = u'Hello world!'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _content_139955154988272 = u'1\n      Hello world!\n   2'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _content_139955154988272 = u'3\n   4'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Negate value=<Expression u'True' (7:23)> at 249f690> -> _cache_38401680

    # <Expression u'True' (7:23)> -> _cache_38401680
    try:
        _cache_38401680 = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 7, 23, '<string>', _sys.exc_info()[1], ))
        raise

    _cache_38401680 = not _cache_38401680
    _backup_attrs_38602080 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ae050> name=None at 24ae210> -> _value
    _value = _static_38461520
    econtext['attrs'] = _value
    _condition = _cache_38401680
    if _condition:

        # <div ... (7:4)
        # --------------------------------------------------------
        append(u'<div>')
    _content_139955154988272 = u'Hello world!'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _condition = _cache_38401680
    if _condition:
        append(u'</div>')
    if (_backup_attrs_38602080 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38602080
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Negate value=<Expression u'False' (8:23)> at 249f750> -> _cache_38401872

    # <Expression u'False' (8:23)> -> _cache_38401872
    try:
        _cache_38401872 = False
    except:
        rcontext.setdefault('__error__', []).append((u'False', 8, 23, '<string>', _sys.exc_info()[1], ))
        raise

    _cache_38401872 = not _cache_38401872
    _backup_attrs_37106464 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249f190> name=None at 249f950> -> _value
    _value = _static_38400400
    econtext['attrs'] = _value
    _condition = _cache_38401872
    if _condition:

        # <div ... (8:4)
        # --------------------------------------------------------
        append(u'<div>')
    _content_139955154988272 = u'Hello world!'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _condition = _cache_38401872
    if _condition:
        append(u'</div>')
    if (_backup_attrs_37106464 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37106464
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Negate value=<Expression u'True' (9:39)> at 24cae10> -> _cache_38579728

    # <Expression u'True' (9:39)> -> _cache_38579728
    try:
        _cache_38579728 = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 9, 39, '<string>', _sys.exc_info()[1], ))
        raise

    _cache_38579728 = not _cache_38579728
    _backup_attrs_37107904 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ca9d0> name=None at 24ca490> -> _value
    _value = _static_38578640
    econtext['attrs'] = _value
    _condition = _cache_38579728
    if _condition:

        # <div ... (9:4)
        # --------------------------------------------------------
        append(u'<div')
        _attr_class = u'omitted'
        if (_attr_class is not None):
            append((u' class="%s"' % _attr_class))
        append(u'>')
    _content_139955154988272 = u'Hello world!'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _condition = _cache_38579728
    if _condition:
        append(u'</div>')
    if (_backup_attrs_37107904 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37107904
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Negate value=<Expression u'True' (10:44)> at 24a5f90> -> _cache_38428560

    # <Expression u'True' (10:44)> -> _cache_38428560
    try:
        _cache_38428560 = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 10, 44, '<string>', _sys.exc_info()[1], ))
        raise

    _cache_38428560 = not _cache_38428560
    _backup_attrs_37108768 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ca0d0> name=None at 24caad0> -> _value
    _value = _static_38576336
    econtext['attrs'] = _value
    _condition = _cache_38428560
    if _condition:

        # <div ... (10:4)
        # --------------------------------------------------------
        append(u'<div')
        _backup_default_36682712 = get('default', _marker)
        _value = u"${'omitted'}"
        econtext['default'] = _value

        # <Interpolation value=u"${'omitted'}" escape=True at 24ca050> -> _attr_class

        # <Expression u"'omitted'" (10:18)> -> _attr_class
        try:
            _attr_class = 'omitted'
        except:
            rcontext.setdefault('__error__', []).append((u"'omitted'", 10, 18, '<string>', _sys.exc_info()[1], ))
            raise

        _attr_class = _attr_class
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
            append((u' class="%s"' % _attr_class))
        if (_backup_default_36682712 is _marker):
            del econtext['default']
        else:
            econtext['default'] = _backup_default_36682712
        append(u'>')
    _content_139955154988272 = u'Hello world!'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _condition = _cache_38428560
    if _condition:
        append(u'</div>')
    if (_backup_attrs_37108768 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37108768
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_36649800 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36649800
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_38457568 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38457568
pass