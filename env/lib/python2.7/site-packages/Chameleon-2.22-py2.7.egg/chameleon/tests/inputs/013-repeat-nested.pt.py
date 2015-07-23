# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_36668880 = {}
_static_38578832 = {}
_static_38579728 = {}
_static_38579280 = {}
_static_35883664 = {}
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
    _backup_attrs_35898288 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24cac50> name=None at 24ca050> -> _value
    _value = _static_38579280
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38449232 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24cae10> name=None at 24cadd0> -> _value
    _value = _static_38579728
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38451104 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24caa90> name=None at 24ca6d0> -> _value
    _value = _static_38578832
    econtext['attrs'] = _value

    # <table ... (3:4)
    # --------------------------------------------------------
    append(u'<table>')
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_i_38402704 = get('i', _marker)

    # <Expression u'(1,2)' (4:24)> -> _iterator
    try:
        _iterator = (1, 2, )
    except:
        rcontext.setdefault('__error__', []).append((u'(1,2)', 4, 24, '<string>', _sys.exc_info()[1], ))
        raise

    (_iterator, __index_35889808, ) = getitem('repeat')(u'i', _iterator)
    econtext['i'] = None
    for _item in _iterator:
        econtext['i'] = _item
        _backup_attrs_38450384 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x22f85d0> name=None at 2372f50> -> _value
        _value = _static_36668880
        econtext['attrs'] = _value

        # <tr ... (4:6)
        # --------------------------------------------------------
        append(u'<tr>')
        _content_139955154988272 = u'\n        '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        _backup_j_34805456 = get('j', _marker)

        # <Expression u'(1,2)' (5:26)> -> _iterator
        try:
            _iterator = (1, 2, )
        except:
            rcontext.setdefault('__error__', []).append((u'(1,2)', 5, 26, '<string>', _sys.exc_info()[1], ))
            raise

        (_iterator, __index_35883600, ) = getitem('repeat')(u'j', _iterator)
        econtext['j'] = None
        for _item in _iterator:
            econtext['j'] = _item
            _backup_attrs_38450744 = get('attrs', _marker)

            # <Static value=<_ast.Dict object at 0x2238a90> name=None at 2238a10> -> _value
            _value = _static_35883664
            econtext['attrs'] = _value

            # <td ... (5:8)
            # --------------------------------------------------------
            append(u'<td>')

            # <Expression u'i' (6:13)> -> _content_139955154988272
            try:
                _content_139955154988272 = getitem('i')
            except:
                rcontext.setdefault('__error__', []).append((u'i', 6, 13, '<string>', _sys.exc_info()[1], ))
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

            # <Expression u'j' (6:18)> -> _content_139955154988272_110
            try:
                _content_139955154988272_110 = getitem('j')
            except:
                rcontext.setdefault('__error__', []).append((u'j', 6, 18, '<string>', _sys.exc_info()[1], ))
                raise

            if (_content_139955154988272_110 is None):
                pass
            else:
                if (_content_139955154988272_110 is False):
                    _content_139955154988272_110 = None
                else:
                    _tt = type(_content_139955154988272_110)
                    if ((_tt is int) or (_tt is float) or (_tt is long)):
                        _content_139955154988272_110 = unicode(_content_139955154988272_110)
                    else:
                        try:
                            if (_tt is str):
                                _content_139955154988272_110 = decode(_content_139955154988272_110)
                            else:
                                if (_tt is not unicode):
                                    try:
                                        _content_139955154988272_110 = _content_139955154988272_110.__html__
                                    except:
                                        _content_139955154988272_110 = convert(_content_139955154988272_110)
                                    else:
                                        raise RuntimeError
                        except RuntimeError:
                            _content_139955154988272_110 = _content_139955154988272_110()
                        else:
                            if ((_content_139955154988272_110 is not None) and (re_needs_escape(_content_139955154988272_110) is not None)):
                                if ('&' in _content_139955154988272_110):
                                    if (';' in _content_139955154988272_110):
                                        _content_139955154988272_110 = re_amp.sub('&amp;', _content_139955154988272_110)
                                    else:
                                        _content_139955154988272_110 = _content_139955154988272_110.replace('&', '&amp;')
                                if ('<' in _content_139955154988272_110):
                                    _content_139955154988272_110 = _content_139955154988272_110.replace('<', '&lt;')
                                if ('>' in _content_139955154988272_110):
                                    _content_139955154988272_110 = _content_139955154988272_110.replace('>', '&gt;')
                                if ('\x00' in _content_139955154988272_110):
                                    _content_139955154988272_110 = _content_139955154988272_110.replace('\x00', '&#34;')
            _content_139955154988272 = ('%s%s%s%s%s' % ((u'\n          [' if (u'\n          [' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u',' if (u',' is not None) else ''), (_content_139955154988272_110 if (_content_139955154988272_110 is not None) else ''), (u']\n        ' if (u']\n        ' is not None) else ''), ))
            if (_content_139955154988272 is not None):
                append(_content_139955154988272)
            append(u'</td>')
            if (_backup_attrs_38450744 is _marker):
                del econtext['attrs']
            else:
                econtext['attrs'] = _backup_attrs_38450744
            __index_35883600 -= 1
            if (__index_35883600 > 0):
                append('\n        ')
        if (_backup_j_34805456 is _marker):
            del econtext['j']
        else:
            econtext['j'] = _backup_j_34805456
        _content_139955154988272 = u'\n      '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</tr>')
        if (_backup_attrs_38450384 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_38450384
        __index_35889808 -= 1
        if (__index_35889808 > 0):
            append('\n      ')
    if (_backup_i_38402704 is _marker):
        del econtext['i']
    else:
        econtext['i'] = _backup_i_38402704
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</table>')
    if (_backup_attrs_38451104 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38451104
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_38449232 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38449232
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_35898288 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35898288
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass