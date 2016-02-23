# -*- coding: utf-8 -*-
pass
import sys as _sys
from chameleon.utils import DebuggingOutputStream as _DebuggingOutputStream
pass
_static_36670928 = {}
_static_38428304 = {}
_static_38579280 = {}
_static_38488592 = {}
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
    _backup_attrs_38960088 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8dd0> name=None at 22f8610> -> _value
    _value = _static_36670928
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38430264 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24cac50> name=None at 24ca050> -> _value
    _value = _static_38579280
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39079448 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ca910> name=None at 24cad10> -> _value
    _value = _static_38578448
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_35215016_price = ''
    _stream_38577872 = _DebuggingOutputStream()
    _append_38577872 = _stream_38577872.append
    _content_139955154988272 = u'\n      Price:\n      '
    if (_content_139955154988272 is not None):
        _append_38577872(_content_139955154988272)
    _stream_35215016_price = _DebuggingOutputStream()
    _append_35215016_price = _stream_35215016_price.append
    _backup_attrs_39124432 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24b4a10> name=None at 24b4d50> -> _value
    _value = _static_38488592
    econtext['attrs'] = _value

    # <span ... (5:6)
    # --------------------------------------------------------
    _append_35215016_price(u'<span>')
    _stream_35215248_amount = ''
    _stream_38576464 = _DebuggingOutputStream()
    _append_38576464 = _stream_38576464.append
    _content_139955154988272 = u'\n        Per kilo '
    if (_content_139955154988272 is not None):
        _append_38576464(_content_139955154988272)
    _stream_35215248_amount = _DebuggingOutputStream()
    _append_35215248_amount = _stream_35215248_amount.append
    _backup_attrs_38958432 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24a5e90> name=None at 24a5bd0> -> _value
    _value = _static_38428304
    econtext['attrs'] = _value

    # <em ... (6:17)
    # --------------------------------------------------------
    _append_35215248_amount(u'<em>')

    # <Expression u'12.5' (6:42)> -> _content_139955154988272
    try:
        _content_139955154988272 = 12.5
    except:
        rcontext.setdefault('__error__', []).append((u'12.5', 6, 42, '<string>', _sys.exc_info()[1], ))
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
        _append_35215248_amount(_content_139955154988272)
    _append_35215248_amount(u'</em>')
    if (_backup_attrs_38958432 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38958432
    _append_38576464(u'${amount}')
    _stream_35215248_amount = ''.join(_stream_35215248_amount)
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        _append_38576464(_content_139955154988272)
    _msgid_38576464 = re_whitespace(''.join(_stream_38576464)).strip()
    _append_35215016_price(translate(_msgid_38576464, mapping={u'amount': _stream_35215248_amount, }, default=_msgid_38576464, domain=_i18n_domain))
    _append_35215016_price(u'</span>')
    if (_backup_attrs_39124432 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39124432
    _append_38577872(u'${price}')
    _stream_35215016_price = ''.join(_stream_35215016_price)
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        _append_38577872(_content_139955154988272)
    _msgid_38577872 = re_whitespace(''.join(_stream_38577872)).strip()
    append(translate(_msgid_38577872, mapping={u'price': _stream_35215016_price, }, default=_msgid_38577872, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_39079448 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39079448
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_38430264 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38430264
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_38960088 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38960088
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass