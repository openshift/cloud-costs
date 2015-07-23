# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
from chameleon.utils import DebuggingOutputStream as _DebuggingOutputStream
pass
_static_38577168 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_marker_default = _Placeholder()
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
    _backup_attrs_38450168 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x24ca410> name=None at 24ca490> -> _value
    _value = _static_38577168
    econtext['attrs'] = _value

    # <div ... (1:0)
    # --------------------------------------------------------
    append(u'<div')
    _attr_xmlns = u'http://www.w3.org/1999/xhtml'
    if (_attr_xmlns is not None):
        append((u' xmlns="%s"' % _attr_xmlns))
    append(u'>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _stream_35214320_year = ''
    _stream_35214320_monthname = ''
    _stream_38579664 = _DebuggingOutputStream()
    _append_38579664 = _stream_38579664.append
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        _append_38579664(_content_139955154988272)
    _stream_35214320_monthname = _DebuggingOutputStream()
    _append_35214320_monthname = _stream_35214320_monthname.append
    _backup_default_38618392 = get('default', _marker)

    # <Marker name='default' at 24ae690> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u"'october'" (6:25)> -> _cache_38463888
    try:
        _cache_38463888 = 'october'
    except:
        rcontext.setdefault('__error__', []).append((u"'october'", 6, 25, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u"'october'" (6:25)> value=<Marker name='default' at 24ae150> at 24ae890> -> _condition
    _expression = _cache_38463888

    # <Marker name='default' at 24ae150> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _content_139955154988272 = u'monthname'
        if (_content_139955154988272 is not None):
            _append_35214320_monthname(_content_139955154988272)
    else:
        _content = _cache_38463888
        _content = translate(_content, default=None, domain=_i18n_domain)
        if (_content is not None):
            _append_35214320_monthname(_content)
    if (_backup_default_38618392 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38618392
    _append_38579664(u'${monthname}')
    _stream_35214320_monthname = ''.join(_stream_35214320_monthname)
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        _append_38579664(_content_139955154988272)
    _stream_35214320_year = _DebuggingOutputStream()
    _append_35214320_year = _stream_35214320_year.append
    _backup_default_36748968 = get('default', _marker)

    # <Marker name='default' at 24a5dd0> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'1982' (10:25)> -> _cache_38427600
    try:
        _cache_38427600 = 1982
    except:
        rcontext.setdefault('__error__', []).append((u'1982', 10, 25, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'1982' (10:25)> value=<Marker name='default' at 24a5410> at 24a5f90> -> _condition
    _expression = _cache_38427600

    # <Marker name='default' at 24a5410> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _content_139955154988272 = u'year'
        if (_content_139955154988272 is not None):
            _append_35214320_year(_content_139955154988272)
    else:
        _content = _cache_38427600
        _content = translate(_content, default=None, domain=_i18n_domain)
        if (_content is not None):
            _append_35214320_year(_content)
    if (_backup_default_36748968 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36748968
    _append_38579664(u'${year}')
    _stream_35214320_year = ''.join(_stream_35214320_year)
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        _append_38579664(_content_139955154988272)
    _msgid_38579664 = re_whitespace(''.join(_stream_38579664)).strip()
    append(translate(_msgid_38579664, mapping={u'monthname': _stream_35214320_monthname, u'year': _stream_35214320_year, }, default=_msgid_38579664, domain=_i18n_domain))
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_38450168 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38450168
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass