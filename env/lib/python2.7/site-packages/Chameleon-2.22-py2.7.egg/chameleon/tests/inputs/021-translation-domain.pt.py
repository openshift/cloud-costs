# -*- coding: utf-8 -*-
pass
from chameleon.utils import DebuggingOutputStream as _DebuggingOutputStream
pass
_static_37141584 = {u'class': u'test', }
_static_38400080 = {}
_static_36787472 = {}
_static_36787536 = {}
_static_37142224 = {u'class': u'test', }
_static_38401744 = {}
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
    _backup_attrs_35899728 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249f050> name=None at 249fdd0> -> _value
    _value = _static_38400080
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _previous_i18n_domain_37140368 = _i18n_domain
    _i18n_domain = u'old'
    _backup_attrs_35899296 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249f6d0> name=None at 249f850> -> _value
    _value = _static_38401744
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _previous_i18n_domain_36787664 = _i18n_domain
    _i18n_domain = u'new'
    _backup_attrs_35899656 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2315550> name=None at 2315d90> -> _value
    _value = _static_36787536
    econtext['attrs'] = _value

    # <div ... (3:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_36789456 = _DebuggingOutputStream()
    _append_36789456 = _stream_36789456.append
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        _append_36789456(_content_139955154988272)
    _msgid_36789456 = re_whitespace(''.join(_stream_36789456)).strip()
    append(translate(_msgid_36789456, mapping=None, default=_msgid_36789456, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_35899656 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35899656
    _i18n_domain = _previous_i18n_domain_36787664
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38614584 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2315510> name=None at 23153d0> -> _value
    _value = _static_36787472
    econtext['attrs'] = _value

    # <div ... (6:4)
    # --------------------------------------------------------
    append(u'<div>')
    _stream_36787280 = _DebuggingOutputStream()
    _append_36787280 = _stream_36787280.append
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        _append_36787280(_content_139955154988272)
    _msgid_36787280 = re_whitespace(''.join(_stream_36787280)).strip()
    append(translate(_msgid_36787280, mapping=None, default=_msgid_36787280, domain=_i18n_domain))
    append(u'</div>')
    if (_backup_attrs_38614584 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38614584
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _previous_i18n_domain_37139408 = _i18n_domain
    _i18n_domain = u'new'
    _backup_attrs_36648648 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236bc50> name=None at 24ae750> -> _value
    _value = _static_37141584
    econtext['attrs'] = _value

    # <div ... (9:4)
    # --------------------------------------------------------
    append(u'<div')
    _backup_default_36650880 = get('default', _marker)
    _value = u'test'
    econtext['default'] = _value

    # <Translate msgid=None node=<_ast.Str object at 0x236bf50> at 236b210> -> _attr_class
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
    if (_backup_default_36650880 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36650880
    append(u'>')
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_36648648 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36648648
    _i18n_domain = _previous_i18n_domain_37139408
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _previous_i18n_domain_37139344 = _i18n_domain
    _i18n_domain = u'new'
    _backup_attrs_39044808 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x236bed0> name=None at 236b4d0> -> _value
    _value = _static_37142224
    econtext['attrs'] = _value

    # <div ... (12:4)
    # --------------------------------------------------------
    append(u'<div')
    _backup_default_39044664 = get('default', _marker)
    _value = u'test'
    econtext['default'] = _value

    # <Translate msgid=u'test_msgid' node=<_ast.Str object at 0x236b650> at 236b7d0> -> _attr_class
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
    if (_backup_default_39044664 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39044664
    append(u'>')
    _content_139955154988272 = u'\n      Hello world!\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_39044808 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39044808
    _i18n_domain = _previous_i18n_domain_37139344
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_35899296 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35899296
    _i18n_domain = _previous_i18n_domain_37140368
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_35899728 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35899728
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass