# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_36670736 = {u'src': u"${'#'}", u'alt': u'copyright (c) ${2010}', }
_static_36669072 = {u'class': u'ltr', }
_static_36669648 = {u'src': u'${None}', }
_static_36667984 = {}
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
    _backup_attrs_36723672 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8250> name=None at 22f8550> -> _value
    _value = _static_36667984
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36648360 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8690> name=None at 22f80d0> -> _value
    _value = _static_36669072
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body')
    _attr_class = u'ltr'
    if (_attr_class is not None):
        append((u' class="%s"' % _attr_class))
    append(u'>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36648216 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8d10> name=None at 22f8d90> -> _value
    _value = _static_36670736
    econtext['attrs'] = _value

    # <img ... (3:4)
    # --------------------------------------------------------
    append(u'<img')
    _backup_default_36648432 = get('default', _marker)
    _value = u"${'#'}"
    econtext['default'] = _value

    # <Interpolation value=u"${'#'}" escape=True at 22f8a50> -> _attr_src

    # <Expression u"'#'" (3:16)> -> _attr_src
    try:
        _attr_src = '#'
    except:
        rcontext.setdefault('__error__', []).append((u"'#'", 3, 16, '<string>', _sys.exc_info()[1], ))
        raise

    _attr_src = _attr_src
    if (_attr_src is None):
        pass
    else:
        if (_attr_src is False):
            _attr_src = None
        else:
            _tt = type(_attr_src)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_src = unicode(_attr_src)
            else:
                try:
                    if (_tt is str):
                        _attr_src = decode(_attr_src)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_src = _attr_src.__html__
                            except:
                                _attr_src = convert(_attr_src)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_src = _attr_src()
                else:
                    if ((_attr_src is not None) and (re_needs_escape(_attr_src) is not None)):
                        if ('&' in _attr_src):
                            if (';' in _attr_src):
                                _attr_src = re_amp.sub('&amp;', _attr_src)
                            else:
                                _attr_src = _attr_src.replace('&', '&amp;')
                        if ('<' in _attr_src):
                            _attr_src = _attr_src.replace('<', '&lt;')
                        if ('>' in _attr_src):
                            _attr_src = _attr_src.replace('>', '&gt;')
                        if (u'"' in _attr_src):
                            _attr_src = _attr_src.replace(u'"', '&#34;')
    if (_attr_src is not None):
        append((u' src="%s"' % _attr_src))
    if (_backup_default_36648432 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36648432
    _backup_default_39035896 = get('default', _marker)
    _value = u'copyright (c) ${2010}'
    econtext['default'] = _value

    # <Interpolation value=u'copyright (c) ${2010}' escape=True at 22f8090> -> _attr_alt

    # <Expression u'2010' (3:43)> -> _attr_alt
    try:
        _attr_alt = 2010
    except:
        rcontext.setdefault('__error__', []).append((u'2010', 3, 43, '<string>', _sys.exc_info()[1], ))
        raise

    _attr_alt = ('%s%s' % ((u'copyright (c) ' if (u'copyright (c) ' is not None) else ''), (_attr_alt if (_attr_alt is not None) else ''), ))
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
    if (_backup_default_39035896 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39035896
    append(u' />')
    if (_backup_attrs_36648216 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36648216
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36650448 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f88d0> name=None at 22f8590> -> _value
    _value = _static_36669648
    econtext['attrs'] = _value

    # <img ... (4:4)
    # --------------------------------------------------------
    append(u'<img')
    _backup_default_36650232 = get('default', _marker)
    _value = u'${None}'
    econtext['default'] = _value

    # <Interpolation value=u'${None}' escape=True at 221fb90> -> _attr_src

    # <Expression u'None' (4:16)> -> _attr_src
    try:
        _attr_src = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 4, 16, '<string>', _sys.exc_info()[1], ))
        raise

    _attr_src = _attr_src
    if (_attr_src is None):
        pass
    else:
        if (_attr_src is False):
            _attr_src = None
        else:
            _tt = type(_attr_src)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_src = unicode(_attr_src)
            else:
                try:
                    if (_tt is str):
                        _attr_src = decode(_attr_src)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_src = _attr_src.__html__
                            except:
                                _attr_src = convert(_attr_src)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_src = _attr_src()
                else:
                    if ((_attr_src is not None) and (re_needs_escape(_attr_src) is not None)):
                        if ('&' in _attr_src):
                            if (';' in _attr_src):
                                _attr_src = re_amp.sub('&amp;', _attr_src)
                            else:
                                _attr_src = _attr_src.replace('&', '&amp;')
                        if ('<' in _attr_src):
                            _attr_src = _attr_src.replace('<', '&lt;')
                        if ('>' in _attr_src):
                            _attr_src = _attr_src.replace('>', '&gt;')
                        if (u'"' in _attr_src):
                            _attr_src = _attr_src.replace(u'"', '&#34;')
    if (_attr_src is not None):
        append((u' src="%s"' % _attr_src))
    if (_backup_default_36650232 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36650232
    append(u' />')
    if (_backup_attrs_36650448 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36650448
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_36648360 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36648360
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_36723672 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36723672
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass