# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_36670928 = {}
_static_35883856 = {}
_static_38579280 = {}
_static_38578448 = {}
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
    _backup_attrs_38460808 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2238b50> name=None at 2238f90> -> _value
    _value = _static_35883856
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38457496 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8dd0> name=None at 22f8610> -> _value
    _value = _static_36670928
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_i_38402704 = get('i', _marker)

    # <Expression u'(3,4)' (3:24)> -> _iterator
    try:
        _iterator = (3, 4, )
    except:
        rcontext.setdefault('__error__', []).append((u'(3,4)', 3, 24, '<string>', _sys.exc_info()[1], ))
        raise

    (_iterator, __index_38579664, ) = getitem('repeat')(u'i', _iterator)
    econtext['i'] = None
    for _item in _iterator:
        econtext['i'] = _item
        _backup_attrs_38524328 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x24cac50> name=None at 24ca050> -> _value
        _value = _static_38579280
        econtext['attrs'] = _value

        # <span ... (3:4)
        # --------------------------------------------------------
        append(u'<span>')
        _content_139955154988272 = u'\n      '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        _backup_j_35779152 = get('j', _marker)

        # <Expression u'(3,4)' (4:26)> -> _iterator
        try:
            _iterator = (3, 4, )
        except:
            rcontext.setdefault('__error__', []).append((u'(3,4)', 4, 26, '<string>', _sys.exc_info()[1], ))
            raise

        (_iterator, __index_38578064, ) = getitem('repeat')(u'j', _iterator)
        econtext['j'] = None
        for _item in _iterator:
            econtext['j'] = _item
            _backup_attrs_38460304 = get('attrs', _marker)

            # <Static value=<_ast.Dict object at 0x24ca910> name=None at 24cad10> -> _value
            _value = _static_38578448
            econtext['attrs'] = _value

            # <span ... (4:6)
            # --------------------------------------------------------
            append(u'<span>')

            # <Expression u'i' (4:36)> -> _content_139955154988272
            try:
                _content_139955154988272 = getitem('i')
            except:
                rcontext.setdefault('__error__', []).append((u'i', 4, 36, '<string>', _sys.exc_info()[1], ))
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

            # <Expression u'j' (4:41)> -> _content_139955154988272_87
            try:
                _content_139955154988272_87 = getitem('j')
            except:
                rcontext.setdefault('__error__', []).append((u'j', 4, 41, '<string>', _sys.exc_info()[1], ))
                raise

            if (_content_139955154988272_87 is None):
                pass
            else:
                if (_content_139955154988272_87 is False):
                    _content_139955154988272_87 = None
                else:
                    _tt = type(_content_139955154988272_87)
                    if ((_tt is int) or (_tt is float) or (_tt is long)):
                        _content_139955154988272_87 = unicode(_content_139955154988272_87)
                    else:
                        try:
                            if (_tt is str):
                                _content_139955154988272_87 = decode(_content_139955154988272_87)
                            else:
                                if (_tt is not unicode):
                                    try:
                                        _content_139955154988272_87 = _content_139955154988272_87.__html__
                                    except:
                                        _content_139955154988272_87 = convert(_content_139955154988272_87)
                                    else:
                                        raise RuntimeError
                        except RuntimeError:
                            _content_139955154988272_87 = _content_139955154988272_87()
                        else:
                            if ((_content_139955154988272_87 is not None) and (re_needs_escape(_content_139955154988272_87) is not None)):
                                if ('&' in _content_139955154988272_87):
                                    if (';' in _content_139955154988272_87):
                                        _content_139955154988272_87 = re_amp.sub('&amp;', _content_139955154988272_87)
                                    else:
                                        _content_139955154988272_87 = _content_139955154988272_87.replace('&', '&amp;')
                                if ('<' in _content_139955154988272_87):
                                    _content_139955154988272_87 = _content_139955154988272_87.replace('<', '&lt;')
                                if ('>' in _content_139955154988272_87):
                                    _content_139955154988272_87 = _content_139955154988272_87.replace('>', '&gt;')
                                if ('\x00' in _content_139955154988272_87):
                                    _content_139955154988272_87 = _content_139955154988272_87.replace('\x00', '&#34;')
            _content_139955154988272 = ('%s%s%s%s%s' % ((u'[' if (u'[' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u',' if (u',' is not None) else ''), (_content_139955154988272_87 if (_content_139955154988272_87 is not None) else ''), (u']' if (u']' is not None) else ''), ))
            if (_content_139955154988272 is not None):
                append(_content_139955154988272)
            append(u'</span>')
            if (_backup_attrs_38460304 is _marker):
                del econtext['attrs']
            else:
                econtext['attrs'] = _backup_attrs_38460304
            __index_38578064 -= 1
            if (__index_38578064 > 0):
                append('\n      ')
        if (_backup_j_35779152 is _marker):
            del econtext['j']
        else:
            econtext['j'] = _backup_j_35779152
        _content_139955154988272 = u'\n    '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</span>')
        if (_backup_attrs_38524328 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_38524328
        __index_38579664 -= 1
        if (__index_38579664 > 0):
            append('\n    ')
    if (_backup_i_38402704 is _marker):
        del econtext['i']
    else:
        econtext['i'] = _backup_i_38402704
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_38457496 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38457496
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_38460808 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38460808
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass