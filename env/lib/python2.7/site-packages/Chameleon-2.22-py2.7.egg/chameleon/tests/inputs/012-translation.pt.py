# -*- coding: utf-8 -*-
pass
import sys as _sys
from chameleon.utils import DebuggingOutputStream as _DebuggingOutputStream
pass
_static_38489680 = {}
_static_38487248 = {}
_static_38578448 = {}
_static_38486544 = {}
_static_35828816 = {}
_static_38488720 = {}
_static_36670992 = {}
_static_38579280 = {}
_static_35884240 = {}
_static_38486480 = {}
_static_38578832 = {}
_static_38486800 = {}
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
    _backup_attrs_38432352 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222b450> name=None at 222bfd0> -> _value
    _value = _static_35828816
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38429976 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b4310> name=None at 24b4a50> -> _value
    _value = _static_38486800
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38429832 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b44d0> name=None at 24b45d0> -> _value
    _value = _static_38487248
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_38489104 = _DebuggingOutputStream()
    _append_38489104 = _stream_38489104.append
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        _append_38489104(_content_139955154988272)
    _msgid_38489104 = re_whitespace(''.join(_stream_38489104)).strip()
    append(translate(_msgid_38489104, mapping=None, default=_msgid_38489104, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38429832 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38429832
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38412088 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b4210> name=None at 24b4510> -> _value
    _value = _static_38486544
    econtext['attrs'] = _value

    # <div ... (6:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_38487760 = _DebuggingOutputStream()
    _append_38487760 = _stream_38487760.append
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        _append_38487760(_content_139955154988272)
    _msgid_38487760 = re_whitespace(''.join(_stream_38487760)).strip()
    append(translate(u'hello_world', mapping=None, default=_msgid_38487760, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38412088 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38412088
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38411152 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b4e50> name=None at 24b4950> -> _value
    _value = _static_38489680
    econtext['attrs'] = _value

    # <div ... (9:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_38487888 = _DebuggingOutputStream()
    _append_38487888 = _stream_38487888.append
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        _append_38487888(_content_139955154988272)
    _backup_attrs_38409280 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b4a90> name=None at 24b4f10> -> _value
    _value = _static_38488720
    econtext['attrs'] = _value

    # <sup ... (10:6)
    # --------------------------------------------------------
    _append_38487888(u'<sup>')
    _content_139955154988272 = u'Hello world!'
    if (_content_139955154988272 is not None):
        _append_38487888(_content_139955154988272)
    _append_38487888(u'</sup>')
    if (_backup_attrs_38409280 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38409280
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        _append_38487888(_content_139955154988272)
    _msgid_38487888 = re_whitespace(''.join(_stream_38487888)).strip()
    append(translate(_msgid_38487888, mapping=None, default=_msgid_38487888, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38411152 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38411152
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38408848 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b41d0> name=None at 24b4350> -> _value
    _value = _static_38486480
    econtext['attrs'] = _value

    # <div ... (12:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_35215016_first = ''
    _stream_35215016_second = ''
    _stream_38489040 = _DebuggingOutputStream()
    _append_38489040 = _stream_38489040.append
    _content_139955154988272 = u'\n      Hello '
    if (_content_139955154988272 is not None):
        _append_38489040(_content_139955154988272)
    _stream_35215016_first = _DebuggingOutputStream()
    _append_35215016_first = _stream_35215016_first.append
    _backup_attrs_38460520 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24cac50> name=None at 24ca050> -> _value
    _value = _static_38579280
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
    if (_backup_attrs_38460520 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38460520
    _append_38489040(u'${first}')
    _stream_35215016_first = ''.join(_stream_35215016_first)
    _content_139955154988272 = u'!\n      Goodbye '
    if (_content_139955154988272 is not None):
        _append_38489040(_content_139955154988272)
    _stream_35215016_second = _DebuggingOutputStream()
    _append_35215016_second = _stream_35215016_second.append
    _backup_attrs_38461384 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ca910> name=None at 24cae10> -> _value
    _value = _static_38578448
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
    if (_backup_attrs_38461384 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38461384
    _append_38489040(u'${second}')
    _stream_35215016_second = ''.join(_stream_35215016_second)
    _content_139955154988272 = u'!\n    '
    if (_content_139955154988272 is not None):
        _append_38489040(_content_139955154988272)
    _msgid_38489040 = re_whitespace(''.join(_stream_38489040)).strip()
    append(translate(_msgid_38489040, mapping={u'second': _stream_35215016_second, u'first': _stream_35215016_first, }, default=_msgid_38489040, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38408848 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38408848
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38459368 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24caa90> name=None at 24ca6d0> -> _value
    _value = _static_38578832
    econtext['attrs'] = _value

    # <div ... (16:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_35215016_first = ''
    _stream_35215016_second = ''
    _stream_38578576 = _DebuggingOutputStream()
    _append_38578576 = _stream_38578576.append
    _content_139955154988272 = u'\n      Hello '
    if (_content_139955154988272 is not None):
        _append_38578576(_content_139955154988272)
    _stream_35215016_first = _DebuggingOutputStream()
    _append_35215016_first = _stream_35215016_first.append
    _backup_attrs_37105888 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2238cd0> name=None at 2238f90> -> _value
    _value = _static_35884240
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
    if (_backup_attrs_37105888 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37105888
    _append_38578576(u'${first}')
    _stream_35215016_first = ''.join(_stream_35215016_first)
    _content_139955154988272 = u'!\n      Goodbye '
    if (_content_139955154988272 is not None):
        _append_38578576(_content_139955154988272)
    _stream_35215016_second = _DebuggingOutputStream()
    _append_35215016_second = _stream_35215016_second.append
    _backup_attrs_37108840 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8e10> name=None at 22f8510> -> _value
    _value = _static_36670992
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
    if (_backup_attrs_37108840 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37108840
    _append_38578576(u'${second}')
    _stream_35215016_second = ''.join(_stream_35215016_second)
    _content_139955154988272 = u'!\n    '
    if (_content_139955154988272 is not None):
        _append_38578576(_content_139955154988272)
    _msgid_38578576 = re_whitespace(''.join(_stream_38578576)).strip()
    append(translate(u'hello_goodbye', mapping={u'second': _stream_35215016_second, u'first': _stream_35215016_first, }, default=_msgid_38578576, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38459368 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38459368
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_38429976 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38429976
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_38432352 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38432352
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass