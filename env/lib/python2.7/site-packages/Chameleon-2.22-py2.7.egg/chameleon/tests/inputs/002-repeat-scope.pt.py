# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_35799760 = {}
_static_35781456 = {}
_static_35800848 = {}
_static_35801104 = {}
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
    _backup_attrs_35876448 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224710> name=None at 220dc10> -> _value
    _value = _static_35800848
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35899944 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22242d0> name=None at 2224190> -> _value
    _value = _static_35799760
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_text_35782352 = get('text', _marker)

    # <Expression u"('Hello', 'Goodbye')" (3:26)> -> _iterator
    try:
        _iterator = ('Hello', 'Goodbye', )
    except:
        rcontext.setdefault('__error__', []).append((u"('Hello', 'Goodbye')", 3, 26, '<string>', _sys.exc_info()[1], ))
        raise

    (_iterator, __index_35781840, ) = getitem('repeat')(u'text', _iterator)
    econtext['text'] = None
    for _item in _iterator:
        econtext['text'] = _item
        _backup_attrs_35900664 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2224810> name=None at 2224a10> -> _value
        _value = _static_35801104
        econtext['attrs'] = _value

        # <div ... (3:4)
        # --------------------------------------------------------
        append(u'<div>')
        _content_139955154988272 = u'\n      '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        _backup_char_35801040 = get('char', _marker)

        # <Expression u"('!', '.')" (4:29)> -> _iterator
        try:
            _iterator = ('!', '.', )
        except:
            rcontext.setdefault('__error__', []).append((u"('!', '.')", 4, 29, '<string>', _sys.exc_info()[1], ))
            raise

        (_iterator, __index_35780944, ) = getitem('repeat')(u'char', _iterator)
        econtext['char'] = None
        for _item in _iterator:
            econtext['char'] = _item
            _backup_attrs_35899800 = get('attrs', _marker)

            # <Static value=<_ast.Dict object at 0x221fb50> name=None at 221fbd0> -> _value
            _value = _static_35781456
            econtext['attrs'] = _value

            # <span ... (4:6)
            # --------------------------------------------------------
            append(u'<span>')

            # <Expression u'text' (4:43)> -> _content_139955154988272
            try:
                _content_139955154988272 = getitem('text')
            except:
                rcontext.setdefault('__error__', []).append((u'text', 4, 43, '<string>', _sys.exc_info()[1], ))
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

            # <Expression u'char' (4:50)> -> _content_139955154988272_113
            try:
                _content_139955154988272_113 = getitem('char')
            except:
                rcontext.setdefault('__error__', []).append((u'char', 4, 50, '<string>', _sys.exc_info()[1], ))
                raise

            if (_content_139955154988272_113 is None):
                pass
            else:
                if (_content_139955154988272_113 is False):
                    _content_139955154988272_113 = None
                else:
                    _tt = type(_content_139955154988272_113)
                    if ((_tt is int) or (_tt is float) or (_tt is long)):
                        _content_139955154988272_113 = unicode(_content_139955154988272_113)
                    else:
                        try:
                            if (_tt is str):
                                _content_139955154988272_113 = decode(_content_139955154988272_113)
                            else:
                                if (_tt is not unicode):
                                    try:
                                        _content_139955154988272_113 = _content_139955154988272_113.__html__
                                    except:
                                        _content_139955154988272_113 = convert(_content_139955154988272_113)
                                    else:
                                        raise RuntimeError
                        except RuntimeError:
                            _content_139955154988272_113 = _content_139955154988272_113()
                        else:
                            if ((_content_139955154988272_113 is not None) and (re_needs_escape(_content_139955154988272_113) is not None)):
                                if ('&' in _content_139955154988272_113):
                                    if (';' in _content_139955154988272_113):
                                        _content_139955154988272_113 = re_amp.sub('&amp;', _content_139955154988272_113)
                                    else:
                                        _content_139955154988272_113 = _content_139955154988272_113.replace('&', '&amp;')
                                if ('<' in _content_139955154988272_113):
                                    _content_139955154988272_113 = _content_139955154988272_113.replace('<', '&lt;')
                                if ('>' in _content_139955154988272_113):
                                    _content_139955154988272_113 = _content_139955154988272_113.replace('>', '&gt;')
                                if ('\x00' in _content_139955154988272_113):
                                    _content_139955154988272_113 = _content_139955154988272_113.replace('\x00', '&#34;')
            _content_139955154988272 = ('%s%s' % ((_content_139955154988272 if (_content_139955154988272 is not None) else ''), (_content_139955154988272_113 if (_content_139955154988272_113 is not None) else ''), ))
            if (_content_139955154988272 is not None):
                append(_content_139955154988272)
            append(u'</span>')
            if (_backup_attrs_35899800 is _marker):
                del econtext['attrs']
            else:
                econtext['attrs'] = _backup_attrs_35899800
            __index_35780944 -= 1
            if (__index_35780944 > 0):
                append('\n      ')
        if (_backup_char_35801040 is _marker):
            del econtext['char']
        else:
            econtext['char'] = _backup_char_35801040
        _content_139955154988272 = u'\n    '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</div>')
        if (_backup_attrs_35900664 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35900664
        __index_35781840 -= 1
        if (__index_35781840 > 0):
            append('\n    ')
    if (_backup_text_35782352 is _marker):
        del econtext['text']
    else:
        econtext['text'] = _backup_text_35782352
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)

    # <Expression u'not: exists: text' (6:26)> -> _condition
    try:
        try:
            _ignore = getitem('text')
        except (AttributeError, LookupError, TypeError, NameError, KeyError, ):
            _condition = 0
        else:
            _condition = 1
        _condition = not _condition
    except:
        rcontext.setdefault('__error__', []).append((u'not: exists: text', 6, 26, '<string>', _sys.exc_info()[1], ))
        raise

    if _condition:
        _content_139955154988272 = u'ok'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_35899944 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35899944
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_35876448 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35876448
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass