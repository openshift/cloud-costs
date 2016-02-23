# -*- coding: utf-8 -*-
pass
from chameleon.utils import DebuggingOutputStream as _DebuggingOutputStream
pass
_static_37140048 = {}
_static_38400656 = {}
_static_36787600 = {u'class': u'test', }
_static_37140688 = {}
_static_38402256 = {u'class': u'test', }
_static_37142352 = {}
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
    _backup_attrs_39931128 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236bf50> name=None at 236be90> -> _value
    _value = _static_37142352
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _previous_i18n_domain_36787856 = _i18n_domain
    _i18n_domain = u'old'
    _backup_attrs_39848848 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236b8d0> name=None at 236b150> -> _value
    _value = _static_37140688
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _previous_i18n_domain_37142224 = _i18n_domain
    _i18n_domain = u'new'
    _backup_attrs_40301704 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236b650> name=None at 236b050> -> _value
    _value = _static_37140048
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_37142416 = _DebuggingOutputStream()
    _append_37142416 = _stream_37142416.append
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        _append_37142416(_content_139955154988272)
    _msgid_37142416 = re_whitespace(''.join(_stream_37142416)).strip()
    append(translate(_msgid_37142416, mapping=None, default=_msgid_37142416, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_40301704 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_40301704
    _i18n_domain = _previous_i18n_domain_37142224
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39862784 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249f290> name=None at 249f3d0> -> _value
    _value = _static_38400656
    econtext['attrs'] = _value

    # <div ... (6:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_38576208 = _DebuggingOutputStream()
    _append_38576208 = _stream_38576208.append
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        _append_38576208(_content_139955154988272)
    _msgid_38576208 = re_whitespace(''.join(_stream_38576208)).strip()
    append(translate(_msgid_38576208, mapping=None, default=_msgid_38576208, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_39862784 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39862784
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _previous_i18n_domain_36789456 = _i18n_domain
    _i18n_domain = u'new'
    _backup_attrs_38619904 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249f8d0> name=None at 249fe10> -> _value
    _value = _static_38402256
    econtext['attrs'] = _value

    # <div ... (9:4)
    # --------------------------------------------------------
    append(u'<div')
    _backup_default_38620624 = get('default', _marker)
    _value = u'test'
    econtext['default'] = _value

    # <Translate msgid=None node=<_ast.Str object at 0x249fc10> at 249f190> -> _attr_class
    _attr_class = u'test'
    _attr_class = translate(_attr_class, default=_attr_class, domain=_i18n_domain)
    if (_attr_class is None):
        pass
    else:
        if (_attr_class is False):
            _attr_class = None
        else:
            _tt = type(_attr_class)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_class = unicode(_attr_class)
            else:
                try:
                    if (_tt is str):
                        _attr_class = decode(_attr_class)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_class = _attr_class.__html__
                            except:
                                _attr_class = convert(_attr_class)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_class = _attr_class()
                else:
                    if ((_attr_class is not None) and (re_needs_escape(_attr_class) is not None)):
                        if ('&' in _attr_class):
                            if (';' in _attr_class):
                                _attr_class = re_amp.sub('&amp;', _attr_class)
                            else:
                                _attr_class = _attr_class.replace('&', '&amp;')
                        if ('<' in _attr_class):
                            _attr_class = _attr_class.replace('<', '&lt;')
                        if ('>' in _attr_class):
                            _attr_class = _attr_class.replace('>', '&gt;')
                        if (u'"' in _attr_class):
                            _attr_class = _attr_class.replace(u'"', '&#34;')
    if (_attr_class is not None):
        append((u' class="%s"' % _attr_class))
    if (_backup_default_38620624 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38620624
    append(u'>')
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_38619904 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38619904
    _i18n_domain = _previous_i18n_domain_36789456
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _previous_i18n_domain_36786320 = _i18n_domain
    _i18n_domain = u'new'
    _backup_attrs_38620120 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2315590> name=None at 23151d0> -> _value
    _value = _static_36787600
    econtext['attrs'] = _value

    # <div ... (12:4)
    # --------------------------------------------------------
    append(u'<div')
    _backup_default_38618464 = get('default', _marker)
    _value = u'test'
    econtext['default'] = _value

    # <Translate msgid=u'test_msgid' node=<_ast.Str object at 0x2315050> at 2315f10> -> _attr_class
    _attr_class = u'test'
    _attr_class = translate(u'test_msgid', default=_attr_class, domain=_i18n_domain)
    if (_attr_class is None):
        pass
    else:
        if (_attr_class is False):
            _attr_class = None
        else:
            _tt = type(_attr_class)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_class = unicode(_attr_class)
            else:
                try:
                    if (_tt is str):
                        _attr_class = decode(_attr_class)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_class = _attr_class.__html__
                            except:
                                _attr_class = convert(_attr_class)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_class = _attr_class()
                else:
                    if ((_attr_class is not None) and (re_needs_escape(_attr_class) is not None)):
                        if ('&' in _attr_class):
                            if (';' in _attr_class):
                                _attr_class = re_amp.sub('&amp;', _attr_class)
                            else:
                                _attr_class = _attr_class.replace('&', '&amp;')
                        if ('<' in _attr_class):
                            _attr_class = _attr_class.replace('<', '&lt;')
                        if ('>' in _attr_class):
                            _attr_class = _attr_class.replace('>', '&gt;')
                        if (u'"' in _attr_class):
                            _attr_class = _attr_class.replace(u'"', '&#34;')
    if (_attr_class is not None):
        append((u' class="%s"' % _attr_class))
    if (_backup_default_38618464 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38618464
    append(u'>')
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_38620120 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38620120
    _i18n_domain = _previous_i18n_domain_36786320
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_39848848 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39848848
    _i18n_domain = _previous_i18n_domain_36787856
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_39931128 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39931128
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass