# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_37140624 = {}
_static_37139664 = {}
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
    _backup_attrs_37108192 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236b4d0> name=None at 236b510> -> _value
    _value = _static_37139664
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38451104 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236b890> name=None at 236b8d0> -> _value
    _value = _static_37140624
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u"'first'" (5:10)> -> _content_139955154988272
    try:
        _content_139955154988272 = 'first'
    except:
        rcontext.setdefault('__error__', []).append((u"'first'", 5, 10, '<string>', _sys.exc_info()[1], ))
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
    _content_139955154988272 = ('%s%s%s' % ((u'\n        ' if (u'\n        ' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u'\n      ' if (u'\n      ' is not None) else ''), ))
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _content_139955154988272 = u'\n      second\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u'True' (9:26)> -> _condition
    try:
        _condition = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 9, 26, '<string>', _sys.exc_info()[1], ))
        raise

    if _condition:
        _content_139955154988272 = u'\n      ok\n    '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u'False' (12:26)> -> _condition
    try:
        _condition = False
    except:
        rcontext.setdefault('__error__', []).append((u'False', 12, 26, '<string>', _sys.exc_info()[1], ))
        raise

    if _condition:
        _content_139955154988272 = u'\n      bad\n    '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_38451104 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38451104
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_37108192 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37108192
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass