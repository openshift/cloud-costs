# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_38403088 = {}
_static_36668752 = {}
_static_40208144 = {}
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
    _backup_attrs_35947656 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8550> name=None at 230a350> -> _value
    _value = _static_36668752
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35343464 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249fc10> name=None at 249fa90> -> _value
    _value = _static_38403088
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_i_35341160 = get('i', _marker)
    _backup_j_35341160 = get('j', _marker)

    # <Expression u'((1, 2), (3, 4))' (3:28)> -> _iterator
    try:
        _iterator = ((1, 2, ), (3, 4, ), )
    except:
        rcontext.setdefault('__error__', []).append((u'((1, 2), (3, 4))', 3, 28, '<string>', _sys.exc_info()[1], ))
        raise

    (_iterator, __index_40209040, ) = getitem('repeat')((u'i', u'j', ), _iterator)
    econtext['i'] = econtext['j'] = None
    for _item in _iterator:
        (econtext['i'], econtext['j'], ) = _item
        _backup_attrs_35343248 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2658710> name=None at 2658750> -> _value
        _value = _static_40208144
        econtext['attrs'] = _value

        # <div ... (3:4)
        # --------------------------------------------------------
        append(u'<div>')

        # <Expression u"repeat['i', 'j'].number" (4:8)> -> _content_139955154988272
        try:
            _content_139955154988272 = getitem('repeat')[('i', 'j', )].number
        except:
            rcontext.setdefault('__error__', []).append((u"repeat['i', 'j'].number", 4, 8, '<string>', _sys.exc_info()[1], ))
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

        # <Expression u'i' (4:36)> -> _content_139955154988272_97
        try:
            _content_139955154988272_97 = getitem('i')
        except:
            rcontext.setdefault('__error__', []).append((u'i', 4, 36, '<string>', _sys.exc_info()[1], ))
            raise

        if (_content_139955154988272_97 is None):
            pass
        else:
            if (_content_139955154988272_97 is False):
                _content_139955154988272_97 = None
            else:
                _tt = type(_content_139955154988272_97)
                if ((_tt is int) or (_tt is float) or (_tt is long)):
                    _content_139955154988272_97 = unicode(_content_139955154988272_97)
                else:
                    try:
                        if (_tt is str):
                            _content_139955154988272_97 = decode(_content_139955154988272_97)
                        else:
                            if (_tt is not unicode):
                                try:
                                    _content_139955154988272_97 = _content_139955154988272_97.__html__
                                except:
                                    _content_139955154988272_97 = convert(_content_139955154988272_97)
                                else:
                                    raise RuntimeError
                    except RuntimeError:
                        _content_139955154988272_97 = _content_139955154988272_97()
                    else:
                        if ((_content_139955154988272_97 is not None) and (re_needs_escape(_content_139955154988272_97) is not None)):
                            if ('&' in _content_139955154988272_97):
                                if (';' in _content_139955154988272_97):
                                    _content_139955154988272_97 = re_amp.sub('&amp;', _content_139955154988272_97)
                                else:
                                    _content_139955154988272_97 = _content_139955154988272_97.replace('&', '&amp;')
                            if ('<' in _content_139955154988272_97):
                                _content_139955154988272_97 = _content_139955154988272_97.replace('<', '&lt;')
                            if ('>' in _content_139955154988272_97):
                                _content_139955154988272_97 = _content_139955154988272_97.replace('>', '&gt;')
                            if ('\x00' in _content_139955154988272_97):
                                _content_139955154988272_97 = _content_139955154988272_97.replace('\x00', '&#34;')

        # <Expression u'j' (4:42)> -> _content_139955154988272_103
        try:
            _content_139955154988272_103 = getitem('j')
        except:
            rcontext.setdefault('__error__', []).append((u'j', 4, 42, '<string>', _sys.exc_info()[1], ))
            raise

        if (_content_139955154988272_103 is None):
            pass
        else:
            if (_content_139955154988272_103 is False):
                _content_139955154988272_103 = None
            else:
                _tt = type(_content_139955154988272_103)
                if ((_tt is int) or (_tt is float) or (_tt is long)):
                    _content_139955154988272_103 = unicode(_content_139955154988272_103)
                else:
                    try:
                        if (_tt is str):
                            _content_139955154988272_103 = decode(_content_139955154988272_103)
                        else:
                            if (_tt is not unicode):
                                try:
                                    _content_139955154988272_103 = _content_139955154988272_103.__html__
                                except:
                                    _content_139955154988272_103 = convert(_content_139955154988272_103)
                                else:
                                    raise RuntimeError
                    except RuntimeError:
                        _content_139955154988272_103 = _content_139955154988272_103()
                    else:
                        if ((_content_139955154988272_103 is not None) and (re_needs_escape(_content_139955154988272_103) is not None)):
                            if ('&' in _content_139955154988272_103):
                                if (';' in _content_139955154988272_103):
                                    _content_139955154988272_103 = re_amp.sub('&amp;', _content_139955154988272_103)
                                else:
                                    _content_139955154988272_103 = _content_139955154988272_103.replace('&', '&amp;')
                            if ('<' in _content_139955154988272_103):
                                _content_139955154988272_103 = _content_139955154988272_103.replace('<', '&lt;')
                            if ('>' in _content_139955154988272_103):
                                _content_139955154988272_103 = _content_139955154988272_103.replace('>', '&gt;')
                            if ('\x00' in _content_139955154988272_103):
                                _content_139955154988272_103 = _content_139955154988272_103.replace('\x00', '&#34;')
        _content_139955154988272 = ('%s%s%s%s%s%s%s' % ((u'\n      ' if (u'\n      ' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u', ' if (u', ' is not None) else ''), (_content_139955154988272_97 if (_content_139955154988272_97 is not None) else ''), (u', ' if (u', ' is not None) else ''), (_content_139955154988272_103 if (_content_139955154988272_103 is not None) else ''), (u'\n    ' if (u'\n    ' is not None) else ''), ))
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</div>')
        if (_backup_attrs_35343248 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_35343248
        __index_40209040 -= 1
        if (__index_40209040 > 0):
            append('\n    ')
    if (_backup_i_35341160 is _marker):
        del econtext['i']
    else:
        econtext['i'] = _backup_i_35341160
    if (_backup_j_35341160 is _marker):
        del econtext['j']
    else:
        econtext['j'] = _backup_j_35341160
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_35343464 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35343464
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_35947656 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35947656
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass