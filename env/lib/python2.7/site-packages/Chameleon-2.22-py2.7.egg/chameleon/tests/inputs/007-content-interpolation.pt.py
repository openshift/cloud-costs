# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_36670096 = {}
_static_35829392 = {}
_static_35708624 = {}
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
    _backup_attrs_37246736 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x220ded0> name=None at 221fb90> -> _value
    _value = _static_35708624
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38435512 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222b690> name=None at 222bb50> -> _value
    _value = _static_35829392
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')

    # <Expression u"'Hello world!'" (3:6)> -> _content_139955154988272
    try:
        _content_139955154988272 = 'Hello world!'
    except:
        rcontext.setdefault('__error__', []).append((u"'Hello world!'", 3, 6, '<string>', _sys.exc_info()[1], ))
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

    # <Expression u'literal' (4:6)> -> _content_139955154988272_42
    try:
        _content_139955154988272_42 = getitem('literal')
    except:
        rcontext.setdefault('__error__', []).append((u'literal', 4, 6, '<string>', _sys.exc_info()[1], ))
        raise

    if (_content_139955154988272_42 is None):
        pass
    else:
        if (_content_139955154988272_42 is False):
            _content_139955154988272_42 = None
        else:
            _tt = type(_content_139955154988272_42)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _content_139955154988272_42 = unicode(_content_139955154988272_42)
            else:
                try:
                    if (_tt is str):
                        _content_139955154988272_42 = decode(_content_139955154988272_42)
                    else:
                        if (_tt is not unicode):
                            try:
                                _content_139955154988272_42 = _content_139955154988272_42.__html__
                            except:
                                _content_139955154988272_42 = convert(_content_139955154988272_42)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _content_139955154988272_42 = _content_139955154988272_42()
                else:
                    if ((_content_139955154988272_42 is not None) and (re_needs_escape(_content_139955154988272_42) is not None)):
                        if ('&' in _content_139955154988272_42):
                            if (';' in _content_139955154988272_42):
                                _content_139955154988272_42 = re_amp.sub('&amp;', _content_139955154988272_42)
                            else:
                                _content_139955154988272_42 = _content_139955154988272_42.replace('&', '&amp;')
                        if ('<' in _content_139955154988272_42):
                            _content_139955154988272_42 = _content_139955154988272_42.replace('<', '&lt;')
                        if ('>' in _content_139955154988272_42):
                            _content_139955154988272_42 = _content_139955154988272_42.replace('>', '&gt;')
                        if ('\x00' in _content_139955154988272_42):
                            _content_139955154988272_42 = _content_139955154988272_42.replace('\x00', '&#34;')

    # <Expression u'None' (5:6)> -> _content_139955154988272_57
    try:
        _content_139955154988272_57 = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 5, 6, '<string>', _sys.exc_info()[1], ))
        raise

    if (_content_139955154988272_57 is None):
        pass
    else:
        if (_content_139955154988272_57 is False):
            _content_139955154988272_57 = None
        else:
            _tt = type(_content_139955154988272_57)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _content_139955154988272_57 = unicode(_content_139955154988272_57)
            else:
                try:
                    if (_tt is str):
                        _content_139955154988272_57 = decode(_content_139955154988272_57)
                    else:
                        if (_tt is not unicode):
                            try:
                                _content_139955154988272_57 = _content_139955154988272_57.__html__
                            except:
                                _content_139955154988272_57 = convert(_content_139955154988272_57)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _content_139955154988272_57 = _content_139955154988272_57()
                else:
                    if ((_content_139955154988272_57 is not None) and (re_needs_escape(_content_139955154988272_57) is not None)):
                        if ('&' in _content_139955154988272_57):
                            if (';' in _content_139955154988272_57):
                                _content_139955154988272_57 = re_amp.sub('&amp;', _content_139955154988272_57)
                            else:
                                _content_139955154988272_57 = _content_139955154988272_57.replace('&', '&amp;')
                        if ('<' in _content_139955154988272_57):
                            _content_139955154988272_57 = _content_139955154988272_57.replace('<', '&lt;')
                        if ('>' in _content_139955154988272_57):
                            _content_139955154988272_57 = _content_139955154988272_57.replace('>', '&gt;')
                        if ('\x00' in _content_139955154988272_57):
                            _content_139955154988272_57 = _content_139955154988272_57.replace('\x00', '&#34;')
    _content_139955154988272 = ('%s%s%s%s%s%s%s' % ((u'\n    ' if (u'\n    ' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u'\n    ' if (u'\n    ' is not None) else ''), (_content_139955154988272_42 if (_content_139955154988272_42 is not None) else ''), (u'\n    ' if (u'\n    ' is not None) else ''), (_content_139955154988272_57 if (_content_139955154988272_57 is not None) else ''), (u'\n    ' if (u'\n    ' is not None) else ''), ))
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38446936 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8a90> name=None at 22f8810> -> _value
    _value = _static_36670096
    econtext['attrs'] = _value

    # <div ... (6:4)
    # --------------------------------------------------------
    append(u'<div>')

    # <Expression u'None' (6:11)> -> _content_139955154988272
    try:
        _content_139955154988272 = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 6, 11, '<string>', _sys.exc_info()[1], ))
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
    _content_139955154988272 = _content_139955154988272
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_38446936 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38446936
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_38435512 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38435512
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_37246736 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37246736
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass