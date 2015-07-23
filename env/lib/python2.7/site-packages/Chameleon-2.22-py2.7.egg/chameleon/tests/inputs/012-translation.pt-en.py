# -*- coding: utf-8 -*-
pass
import sys as _sys
from chameleon.utils import DebuggingOutputStream as _DebuggingOutputStream
pass
_static_38488016 = {}
_static_38579984 = {}
_static_38488272 = {}
_static_38487184 = {}
_static_38579536 = {}
_static_35831120 = {}
_static_38489936 = {}
_static_38487632 = {}
_static_35883600 = {}
_static_36668432 = {}
_static_38576848 = {}
_static_35331024 = {}
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
    _backup_attrs_38523248 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8410> name=None at 2372990> -> _value
    _value = _static_36668432
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38625792 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2238a50> name=None at 2238690> -> _value
    _value = _static_35883600
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38624936 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222bd50> name=None at 222be10> -> _value
    _value = _static_35831120
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_35884752 = _DebuggingOutputStream()
    _append_35884752 = _stream_35884752.append
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        _append_35884752(_content_139955154988272)
    _msgid_35884752 = re_whitespace(''.join(_stream_35884752)).strip()
    append(translate(_msgid_35884752, mapping=None, default=_msgid_35884752, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38624936 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38624936
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38619904 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x21b1bd0> name=None at 23171d0> -> _value
    _value = _static_35331024
    econtext['attrs'] = _value

    # <div ... (6:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_36796624 = _DebuggingOutputStream()
    _append_36796624 = _stream_36796624.append
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        _append_36796624(_content_139955154988272)
    _msgid_36796624 = re_whitespace(''.join(_stream_36796624)).strip()
    append(translate(u'hello_world', mapping=None, default=_msgid_36796624, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38619904 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38619904
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38620264 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b4f50> name=None at 24b4d10> -> _value
    _value = _static_38489936
    econtext['attrs'] = _value

    # <div ... (9:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_38487504 = _DebuggingOutputStream()
    _append_38487504 = _stream_38487504.append
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        _append_38487504(_content_139955154988272)
    _backup_attrs_38617888 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b48d0> name=None at 24b4e10> -> _value
    _value = _static_38488272
    econtext['attrs'] = _value

    # <sup ... (10:6)
    # --------------------------------------------------------
    _append_38487504(u'<sup>')
    _content_139955154988272 = u'Hello world!'
    if (_content_139955154988272 is not None):
        _append_38487504(_content_139955154988272)
    _append_38487504(u'</sup>')
    if (_backup_attrs_38617888 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38617888
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        _append_38487504(_content_139955154988272)
    _msgid_38487504 = re_whitespace(''.join(_stream_38487504)).strip()
    append(translate(_msgid_38487504, mapping=None, default=_msgid_38487504, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38620264 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38620264
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38616672 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b47d0> name=None at 24b4890> -> _value
    _value = _static_38488016
    econtext['attrs'] = _value

    # <div ... (12:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_35215016_first = ''
    _stream_35215016_second = ''
    _stream_38487888 = _DebuggingOutputStream()
    _append_38487888 = _stream_38487888.append
    _content_139955154988272 = u'\n      Hello '
    if (_content_139955154988272 is not None):
        _append_38487888(_content_139955154988272)
    _stream_35215016_first = _DebuggingOutputStream()
    _append_35215016_first = _stream_35215016_first.append
    _backup_attrs_39096120 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b4650> name=None at 24b42d0> -> _value
    _value = _static_38487632
    econtext['attrs'] = _value

    # <em ... (13:12)
    # --------------------------------------------------------
    _append_35215016_first(u'<em>')

    # <Expression u"'world'" (13:36)> -> _content_139955154988272
    try:
        _content_139955154988272 = 'world'
    except:
        rcontext.setdefault('__error__', []).append((u"'world'", 13, 36, '<string>', _sys.exc_info()[1], ))
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
        _append_35215016_first(_content_139955154988272)
    _append_35215016_first(u'</em>')
    if (_backup_attrs_39096120 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39096120
    _append_38487888(u'${first}')
    _stream_35215016_first = ''.join(_stream_35215016_first)
    _content_139955154988272 = u'!\n      Goodbye '
    if (_content_139955154988272 is not None):
        _append_38487888(_content_139955154988272)
    _stream_35215016_second = _DebuggingOutputStream()
    _append_35215016_second = _stream_35215016_second.append
    _backup_attrs_39090152 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b4490> name=None at 24b4150> -> _value
    _value = _static_38487184
    econtext['attrs'] = _value

    # <em ... (14:14)
    # --------------------------------------------------------
    _append_35215016_second(u'<em>')

    # <Expression u"'planet'" (14:39)> -> _content_139955154988272
    try:
        _content_139955154988272 = 'planet'
    except:
        rcontext.setdefault('__error__', []).append((u"'planet'", 14, 39, '<string>', _sys.exc_info()[1], ))
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
        _append_35215016_second(_content_139955154988272)
    _append_35215016_second(u'</em>')
    if (_backup_attrs_39090152 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39090152
    _append_38487888(u'${second}')
    _stream_35215016_second = ''.join(_stream_35215016_second)
    _content_139955154988272 = u'!\n    '
    if (_content_139955154988272 is not None):
        _append_38487888(_content_139955154988272)
    _msgid_38487888 = re_whitespace(''.join(_stream_38487888)).strip()
    append(translate(_msgid_38487888, mapping={u'second': _stream_35215016_second, u'first': _stream_35215016_first, }, default=_msgid_38487888, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38616672 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38616672
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39091376 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24caf10> name=None at 24ca850> -> _value
    _value = _static_38579984
    econtext['attrs'] = _value

    # <div ... (16:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_35215016_first = ''
    _stream_35215016_second = ''
    _stream_38486672 = _DebuggingOutputStream()
    _append_38486672 = _stream_38486672.append
    _content_139955154988272 = u'\n      Hello '
    if (_content_139955154988272 is not None):
        _append_38486672(_content_139955154988272)
    _stream_35215016_first = _DebuggingOutputStream()
    _append_35215016_first = _stream_35215016_first.append
    _backup_attrs_39080520 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ca2d0> name=None at 24cafd0> -> _value
    _value = _static_38576848
    econtext['attrs'] = _value

    # <em ... (17:12)
    # --------------------------------------------------------
    _append_35215016_first(u'<em>')

    # <Expression u"'world'" (17:36)> -> _content_139955154988272
    try:
        _content_139955154988272 = 'world'
    except:
        rcontext.setdefault('__error__', []).append((u"'world'", 17, 36, '<string>', _sys.exc_info()[1], ))
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
        _append_35215016_first(_content_139955154988272)
    _append_35215016_first(u'</em>')
    if (_backup_attrs_39080520 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39080520
    _append_38486672(u'${first}')
    _stream_35215016_first = ''.join(_stream_35215016_first)
    _content_139955154988272 = u'!\n      Goodbye '
    if (_content_139955154988272 is not None):
        _append_38486672(_content_139955154988272)
    _stream_35215016_second = _DebuggingOutputStream()
    _append_35215016_second = _stream_35215016_second.append
    _backup_attrs_39080592 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24cad50> name=None at 24ca110> -> _value
    _value = _static_38579536
    econtext['attrs'] = _value

    # <em ... (18:14)
    # --------------------------------------------------------
    _append_35215016_second(u'<em>')

    # <Expression u"'planet'" (18:39)> -> _content_139955154988272
    try:
        _content_139955154988272 = 'planet'
    except:
        rcontext.setdefault('__error__', []).append((u"'planet'", 18, 39, '<string>', _sys.exc_info()[1], ))
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
        _append_35215016_second(_content_139955154988272)
    _append_35215016_second(u'</em>')
    if (_backup_attrs_39080592 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39080592
    _append_38486672(u'${second}')
    _stream_35215016_second = ''.join(_stream_35215016_second)
    _content_139955154988272 = u'!\n    '
    if (_content_139955154988272 is not None):
        _append_38486672(_content_139955154988272)
    _msgid_38486672 = re_whitespace(''.join(_stream_38486672)).strip()
    append(translate(u'hello_goodbye', mapping={u'second': _stream_35215016_second, u'first': _stream_35215016_first, }, default=_msgid_38486672, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_39091376 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39091376
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_38625792 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38625792
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_38523248 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38523248
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass