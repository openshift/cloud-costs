# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_39975056 = {}
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

    def _slot_title(stream, econtext, rcontext, _i18n_domain=_i18n_domain):
        getitem = econtext.__getitem__
        get = econtext.get
        _backup_kind_37140176 = get('kind', _marker)

        # <Expression u"'New'" (2:50)> -> _value
        try:
            _value = 'New'
        except:
            rcontext.setdefault('__error__', []).append((u"'New'", 2, 50, '<string>', _sys.exc_info()[1], ))
            raise

        econtext['kind'] = _value
        _backup_attrs_38600784 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x261f890> name=None at 261fc50> -> _value
        _value = _static_39975056
        econtext['attrs'] = _value

        # <title ... (2:2)
        # --------------------------------------------------------
        append(u'<title>')

        # <Expression u'kind' (3:6)> -> _content_139955154988272
        try:
            _content_139955154988272 = getitem('kind')
        except:
            rcontext.setdefault('__error__', []).append((u'kind', 3, 6, '<string>', _sys.exc_info()[1], ))
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
        _content_139955154988272 = ('%s%s%s' % ((u'\n    ' if (u'\n    ' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u' title\n  ' if (u' title\n  ' is not None) else ''), ))
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</title>')
        if (_backup_attrs_38600784 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_38600784
        if (_backup_kind_37140176 is _marker):
            del econtext['kind']
        else:
            econtext['kind'] = _backup_kind_37140176
    try:
        _slots = getitem(u'_slot_title')
    except:
        _slots = econtext[u'_slot_title'] = [_slot_title, ]
    else:
        _slots.append(_slot_title)

    # <Expression u"load('032-master-template.pt').macros['main']" (1:23)> -> _macro
    try:
        _macro = getitem('load')('032-master-template.pt').macros['main']
    except:
        rcontext.setdefault('__error__', []).append((u"load('032-master-template.pt').macros['main']", 1, 23, '<string>', _sys.exc_info()[1], ))
        raise

    _macro.include(stream, econtext.copy(), rcontext)
    econtext.update(rcontext)
pass