# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_35706576 = {}
_static_35782288 = {}
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
    _backup_attrs_35341232 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x221fe90> name=None at 221fb50> -> _value
    _value = _static_35782288
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_text_35704976 = get('text', _marker)

    # <Expression u"'Hello world!'" (2:25)> -> _value
    try:
        _value = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 2, 25, '<string>', _sys.exc_info()[1], ))
        raise

    econtext['text'] = _value
    _backup_attrs_35343320 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x220d6d0> name=None at 221f410> -> _value
    _value = _static_35706576
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')

    # <Expression u'text' (3:6)> -> _content_139955154988272
    try:
        _content_139955154988272 = getitem('text')
    except:
        rcontext.setdefault('__error__', []).append((u'text', 3, 6, '<string>', _sys.exc_info()[1], ))
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

    # <Expression u'text' (4:5)> -> _content_139955154988272_65
    try:
        _content_139955154988272_65 = getitem('text')
    except:
        rcontext.setdefault('__error__', []).append((u'text', 4, 5, '<string>', _sys.exc_info()[1], ))
        raise

    if (_content_139955154988272_65 is None):
        pass
    else:
        if (_content_139955154988272_65 is False):
            _content_139955154988272_65 = None
        else:
            _tt = type(_content_139955154988272_65)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _content_139955154988272_65 = unicode(_content_139955154988272_65)
            else:
                try:
                    if (_tt is str):
                        _content_139955154988272_65 = decode(_content_139955154988272_65)
                    else:
                        if (_tt is not unicode):
                            try:
                                _content_139955154988272_65 = _content_139955154988272_65.__html__
                            except:
                                _content_139955154988272_65 = convert(_content_139955154988272_65)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _content_139955154988272_65 = _content_139955154988272_65()
                else:
                    if ((_content_139955154988272_65 is not None) and (re_needs_escape(_content_139955154988272_65) is not None)):
                        if ('&' in _content_139955154988272_65):
                            if (';' in _content_139955154988272_65):
                                _content_139955154988272_65 = re_amp.sub('&amp;', _content_139955154988272_65)
                            else:
                                _content_139955154988272_65 = _content_139955154988272_65.replace('&', '&amp;')
                        if ('<' in _content_139955154988272_65):
                            _content_139955154988272_65 = _content_139955154988272_65.replace('<', '&lt;')
                        if ('>' in _content_139955154988272_65):
                            _content_139955154988272_65 = _content_139955154988272_65.replace('>', '&gt;')
                        if ('\x00' in _content_139955154988272_65):
                            _content_139955154988272_65 = _content_139955154988272_65.replace('\x00', '&#34;')
    _content_139955154988272 = ('%s%s%s%s%s' % ((u'\n    ' if (u'\n    ' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u'\n    ' if (u'\n    ' is not None) else ''), (_content_139955154988272_65 if (_content_139955154988272_65 is not None) else ''), (u'\n  ' if (u'\n  ' is not None) else ''), ))
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_35343320 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35343320
    if (_backup_text_35704976 is _marker):
        del econtext['text']
    else:
        econtext['text'] = _backup_text_35704976
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u'exists: text' (6:24)> -> _condition
    try:
        try:
            _ignore = getitem('text')
        except (AttributeError, LookupError, TypeError, NameError, KeyError, ):
            _condition = 0
        else:
            _condition = 1
    except:
        rcontext.setdefault('__error__', []).append((u'exists: text', 6, 24, '<string>', _sys.exc_info()[1], ))
        raise

    if _condition:
        _content_139955154988272 = u'\n    bad\n  '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u'not: exists: text' (9:24)> -> _condition
    try:
        try:
            _ignore = getitem('text')
        except (AttributeError, LookupError, TypeError, NameError, KeyError, ):
            _condition = 0
        else:
            _condition = 1
        _condition = not _condition
    except:
        rcontext.setdefault('__error__', []).append((u'not: exists: text', 9, 24, '<string>', _sys.exc_info()[1], ))
        raise

    if _condition:
        _content_139955154988272 = u'\n    ok\n  '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_35341232 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35341232
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass