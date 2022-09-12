__all__ = ['md5']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['md5_ff', 'safe_add', 'core_hmac_md5', 'binl2b64', 'b64pad', 'md5_gg', 'b64_md5', 'core_md5', 'b64_hmac_md5', 'hex_hmac_md5', 'md5_hh', 'md5_vm_test', 'bit_rol', 'binl2hex', 'str2binl', 'chrsz', 'str_hmac_md5', 'str_md5', 'hex_md5', 'hexcase', 'binl2str', 'md5_cmn', 'md5_ii'])
@Js
def PyJsHoisted_hex_md5_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['s'])
    return var.get('binl2hex')(var.get('core_md5')(var.get('str2binl')(var.get('s')), (var.get('s').get('length')*var.get('chrsz'))))
PyJsHoisted_hex_md5_.func_name = 'hex_md5'
var.put('hex_md5', PyJsHoisted_hex_md5_)
@Js
def PyJsHoisted_b64_md5_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['s'])
    return var.get('binl2b64')(var.get('core_md5')(var.get('str2binl')(var.get('s')), (var.get('s').get('length')*var.get('chrsz'))))
PyJsHoisted_b64_md5_.func_name = 'b64_md5'
var.put('b64_md5', PyJsHoisted_b64_md5_)
@Js
def PyJsHoisted_str_md5_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['s'])
    return var.get('binl2str')(var.get('core_md5')(var.get('str2binl')(var.get('s')), (var.get('s').get('length')*var.get('chrsz'))))
PyJsHoisted_str_md5_.func_name = 'str_md5'
var.put('str_md5', PyJsHoisted_str_md5_)
@Js
def PyJsHoisted_hex_hmac_md5_(key, data, this, arguments, var=var):
    var = Scope({'key':key, 'data':data, 'this':this, 'arguments':arguments}, var)
    var.registers(['key', 'data'])
    return var.get('binl2hex')(var.get('core_hmac_md5')(var.get('key'), var.get('data')))
PyJsHoisted_hex_hmac_md5_.func_name = 'hex_hmac_md5'
var.put('hex_hmac_md5', PyJsHoisted_hex_hmac_md5_)
@Js
def PyJsHoisted_b64_hmac_md5_(key, data, this, arguments, var=var):
    var = Scope({'key':key, 'data':data, 'this':this, 'arguments':arguments}, var)
    var.registers(['key', 'data'])
    return var.get('binl2b64')(var.get('core_hmac_md5')(var.get('key'), var.get('data')))
PyJsHoisted_b64_hmac_md5_.func_name = 'b64_hmac_md5'
var.put('b64_hmac_md5', PyJsHoisted_b64_hmac_md5_)
@Js
def PyJsHoisted_str_hmac_md5_(key, data, this, arguments, var=var):
    var = Scope({'key':key, 'data':data, 'this':this, 'arguments':arguments}, var)
    var.registers(['key', 'data'])
    return var.get('binl2str')(var.get('core_hmac_md5')(var.get('key'), var.get('data')))
PyJsHoisted_str_hmac_md5_.func_name = 'str_hmac_md5'
var.put('str_hmac_md5', PyJsHoisted_str_hmac_md5_)
@Js
def PyJsHoisted_md5_vm_test_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return (var.get('hex_md5')(Js('abc'))==Js('900150983cd24fb0d6963f7d28e17f72'))
PyJsHoisted_md5_vm_test_.func_name = 'md5_vm_test'
var.put('md5_vm_test', PyJsHoisted_md5_vm_test_)
@Js
def PyJsHoisted_core_md5_(x, len, this, arguments, var=var):
    var = Scope({'x':x, 'len':len, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'c', 'len', 'i', 'a', 'oldd', 'olda', 'd', 'oldb', 'oldc', 'b'])
    var.get('x').put((var.get('len')>>Js(5.0)), (Js(128)<<(var.get('len')%Js(32.0))), '|')
    var.get('x').put(((PyJsBshift((var.get('len')+Js(64.0)),Js(9.0))<<Js(4.0))+Js(14.0)), var.get('len'))
    var.put('a', Js(1732584193.0))
    var.put('b', (-Js(271733879.0)))
    var.put('c', (-Js(1732584194.0)))
    var.put('d', Js(271733878.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('x').get('length')):
        try:
            var.put('olda', var.get('a'))
            var.put('oldb', var.get('b'))
            var.put('oldc', var.get('c'))
            var.put('oldd', var.get('d'))
            var.put('a', var.get('md5_ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(0.0))), Js(7.0), (-Js(680876936.0))))
            var.put('d', var.get('md5_ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(1.0))), Js(12.0), (-Js(389564586.0))))
            var.put('c', var.get('md5_ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(2.0))), Js(17.0), Js(606105819.0)))
            var.put('b', var.get('md5_ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(3.0))), Js(22.0), (-Js(1044525330.0))))
            var.put('a', var.get('md5_ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(4.0))), Js(7.0), (-Js(176418897.0))))
            var.put('d', var.get('md5_ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(5.0))), Js(12.0), Js(1200080426.0)))
            var.put('c', var.get('md5_ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(6.0))), Js(17.0), (-Js(1473231341.0))))
            var.put('b', var.get('md5_ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(7.0))), Js(22.0), (-Js(45705983.0))))
            var.put('a', var.get('md5_ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(8.0))), Js(7.0), Js(1770035416.0)))
            var.put('d', var.get('md5_ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(9.0))), Js(12.0), (-Js(1958414417.0))))
            var.put('c', var.get('md5_ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(10.0))), Js(17.0), (-Js(42063.0))))
            var.put('b', var.get('md5_ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(11.0))), Js(22.0), (-Js(1990404162.0))))
            var.put('a', var.get('md5_ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(12.0))), Js(7.0), Js(1804603682.0)))
            var.put('d', var.get('md5_ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(13.0))), Js(12.0), (-Js(40341101.0))))
            var.put('c', var.get('md5_ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(14.0))), Js(17.0), (-Js(1502002290.0))))
            var.put('b', var.get('md5_ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(15.0))), Js(22.0), Js(1236535329.0)))
            var.put('a', var.get('md5_gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(1.0))), Js(5.0), (-Js(165796510.0))))
            var.put('d', var.get('md5_gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(6.0))), Js(9.0), (-Js(1069501632.0))))
            var.put('c', var.get('md5_gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(11.0))), Js(14.0), Js(643717713.0)))
            var.put('b', var.get('md5_gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(0.0))), Js(20.0), (-Js(373897302.0))))
            var.put('a', var.get('md5_gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(5.0))), Js(5.0), (-Js(701558691.0))))
            var.put('d', var.get('md5_gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(10.0))), Js(9.0), Js(38016083.0)))
            var.put('c', var.get('md5_gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(15.0))), Js(14.0), (-Js(660478335.0))))
            var.put('b', var.get('md5_gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(4.0))), Js(20.0), (-Js(405537848.0))))
            var.put('a', var.get('md5_gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(9.0))), Js(5.0), Js(568446438.0)))
            var.put('d', var.get('md5_gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(14.0))), Js(9.0), (-Js(1019803690.0))))
            var.put('c', var.get('md5_gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(3.0))), Js(14.0), (-Js(187363961.0))))
            var.put('b', var.get('md5_gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(8.0))), Js(20.0), Js(1163531501.0)))
            var.put('a', var.get('md5_gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(13.0))), Js(5.0), (-Js(1444681467.0))))
            var.put('d', var.get('md5_gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(2.0))), Js(9.0), (-Js(51403784.0))))
            var.put('c', var.get('md5_gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(7.0))), Js(14.0), Js(1735328473.0)))
            var.put('b', var.get('md5_gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(12.0))), Js(20.0), (-Js(1926607734.0))))
            var.put('a', var.get('md5_hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(5.0))), Js(4.0), (-Js(378558.0))))
            var.put('d', var.get('md5_hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(8.0))), Js(11.0), (-Js(2022574463.0))))
            var.put('c', var.get('md5_hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(11.0))), Js(16.0), Js(1839030562.0)))
            var.put('b', var.get('md5_hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(14.0))), Js(23.0), (-Js(35309556.0))))
            var.put('a', var.get('md5_hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(1.0))), Js(4.0), (-Js(1530992060.0))))
            var.put('d', var.get('md5_hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(4.0))), Js(11.0), Js(1272893353.0)))
            var.put('c', var.get('md5_hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(7.0))), Js(16.0), (-Js(155497632.0))))
            var.put('b', var.get('md5_hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(10.0))), Js(23.0), (-Js(1094730640.0))))
            var.put('a', var.get('md5_hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(13.0))), Js(4.0), Js(681279174.0)))
            var.put('d', var.get('md5_hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(0.0))), Js(11.0), (-Js(358537222.0))))
            var.put('c', var.get('md5_hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(3.0))), Js(16.0), (-Js(722521979.0))))
            var.put('b', var.get('md5_hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(6.0))), Js(23.0), Js(76029189.0)))
            var.put('a', var.get('md5_hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(9.0))), Js(4.0), (-Js(640364487.0))))
            var.put('d', var.get('md5_hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(12.0))), Js(11.0), (-Js(421815835.0))))
            var.put('c', var.get('md5_hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(15.0))), Js(16.0), Js(530742520.0)))
            var.put('b', var.get('md5_hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(2.0))), Js(23.0), (-Js(995338651.0))))
            var.put('a', var.get('md5_ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(0.0))), Js(6.0), (-Js(198630844.0))))
            var.put('d', var.get('md5_ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(7.0))), Js(10.0), Js(1126891415.0)))
            var.put('c', var.get('md5_ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(14.0))), Js(15.0), (-Js(1416354905.0))))
            var.put('b', var.get('md5_ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(5.0))), Js(21.0), (-Js(57434055.0))))
            var.put('a', var.get('md5_ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(12.0))), Js(6.0), Js(1700485571.0)))
            var.put('d', var.get('md5_ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(3.0))), Js(10.0), (-Js(1894986606.0))))
            var.put('c', var.get('md5_ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(10.0))), Js(15.0), (-Js(1051523.0))))
            var.put('b', var.get('md5_ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(1.0))), Js(21.0), (-Js(2054922799.0))))
            var.put('a', var.get('md5_ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(8.0))), Js(6.0), Js(1873313359.0)))
            var.put('d', var.get('md5_ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(15.0))), Js(10.0), (-Js(30611744.0))))
            var.put('c', var.get('md5_ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(6.0))), Js(15.0), (-Js(1560198380.0))))
            var.put('b', var.get('md5_ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(13.0))), Js(21.0), Js(1309151649.0)))
            var.put('a', var.get('md5_ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(4.0))), Js(6.0), (-Js(145523070.0))))
            var.put('d', var.get('md5_ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(11.0))), Js(10.0), (-Js(1120210379.0))))
            var.put('c', var.get('md5_ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(2.0))), Js(15.0), Js(718787259.0)))
            var.put('b', var.get('md5_ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(9.0))), Js(21.0), (-Js(343485551.0))))
            var.put('a', var.get('safe_add')(var.get('a'), var.get('olda')))
            var.put('b', var.get('safe_add')(var.get('b'), var.get('oldb')))
            var.put('c', var.get('safe_add')(var.get('c'), var.get('oldc')))
            var.put('d', var.get('safe_add')(var.get('d'), var.get('oldd')))
        finally:
                var.put('i', Js(16.0), '+')
    return var.get('Array')(var.get('a'), var.get('b'), var.get('c'), var.get('d'))
PyJsHoisted_core_md5_.func_name = 'core_md5'
var.put('core_md5', PyJsHoisted_core_md5_)
@Js
def PyJsHoisted_md5_cmn_(q, a, b, x, s, t, this, arguments, var=var):
    var = Scope({'q':q, 'a':a, 'b':b, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'q', 'a', 't', 'b', 's'])
    return var.get('safe_add')(var.get('bit_rol')(var.get('safe_add')(var.get('safe_add')(var.get('a'), var.get('q')), var.get('safe_add')(var.get('x'), var.get('t'))), var.get('s')), var.get('b'))
PyJsHoisted_md5_cmn_.func_name = 'md5_cmn'
var.put('md5_cmn', PyJsHoisted_md5_cmn_)
@Js
def PyJsHoisted_md5_ff_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'c', 'a', 'd', 't', 'b', 's'])
    return var.get('md5_cmn')(((var.get('b')&var.get('c'))|((~var.get('b'))&var.get('d'))), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_md5_ff_.func_name = 'md5_ff'
var.put('md5_ff', PyJsHoisted_md5_ff_)
@Js
def PyJsHoisted_md5_gg_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'c', 'a', 'd', 't', 'b', 's'])
    return var.get('md5_cmn')(((var.get('b')&var.get('d'))|(var.get('c')&(~var.get('d')))), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_md5_gg_.func_name = 'md5_gg'
var.put('md5_gg', PyJsHoisted_md5_gg_)
@Js
def PyJsHoisted_md5_hh_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'c', 'a', 'd', 't', 'b', 's'])
    return var.get('md5_cmn')(((var.get('b')^var.get('c'))^var.get('d')), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_md5_hh_.func_name = 'md5_hh'
var.put('md5_hh', PyJsHoisted_md5_hh_)
@Js
def PyJsHoisted_md5_ii_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'c', 'a', 'd', 't', 'b', 's'])
    return var.get('md5_cmn')((var.get('c')^(var.get('b')|(~var.get('d')))), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_md5_ii_.func_name = 'md5_ii'
var.put('md5_ii', PyJsHoisted_md5_ii_)
@Js
def PyJsHoisted_core_hmac_md5_(key, data, this, arguments, var=var):
    var = Scope({'key':key, 'data':data, 'this':this, 'arguments':arguments}, var)
    var.registers(['bkey', 'i', 'opad', 'key', 'ipad', 'data', 'hash'])
    var.put('bkey', var.get('str2binl')(var.get('key')))
    if (var.get('bkey').get('length')>Js(16.0)):
        var.put('bkey', var.get('core_md5')(var.get('bkey'), (var.get('key').get('length')*var.get('chrsz'))))
    var.put('ipad', var.get('Array')(Js(16.0)))
    var.put('opad', var.get('Array')(Js(16.0)))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(16.0)):
        try:
            var.get('ipad').put(var.get('i'), (var.get('bkey').get(var.get('i'))^Js(909522486)))
            var.get('opad').put(var.get('i'), (var.get('bkey').get(var.get('i'))^Js(1549556828)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('hash', var.get('core_md5')(var.get('ipad').callprop('concat', var.get('str2binl')(var.get('data'))), (Js(512.0)+(var.get('data').get('length')*var.get('chrsz')))))
    return var.get('core_md5')(var.get('opad').callprop('concat', var.get('hash')), (Js(512.0)+Js(128.0)))
PyJsHoisted_core_hmac_md5_.func_name = 'core_hmac_md5'
var.put('core_hmac_md5', PyJsHoisted_core_hmac_md5_)
@Js
def PyJsHoisted_safe_add_(x, y, this, arguments, var=var):
    var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'y', 'msw', 'lsw'])
    var.put('lsw', ((var.get('x')&Js(65535))+(var.get('y')&Js(65535))))
    var.put('msw', (((var.get('x')>>Js(16.0))+(var.get('y')>>Js(16.0)))+(var.get('lsw')>>Js(16.0))))
    return ((var.get('msw')<<Js(16.0))|(var.get('lsw')&Js(65535)))
PyJsHoisted_safe_add_.func_name = 'safe_add'
var.put('safe_add', PyJsHoisted_safe_add_)
@Js
def PyJsHoisted_bit_rol_(num, cnt, this, arguments, var=var):
    var = Scope({'num':num, 'cnt':cnt, 'this':this, 'arguments':arguments}, var)
    var.registers(['num', 'cnt'])
    return ((var.get('num')<<var.get('cnt'))|PyJsBshift(var.get('num'),(Js(32.0)-var.get('cnt'))))
PyJsHoisted_bit_rol_.func_name = 'bit_rol'
var.put('bit_rol', PyJsHoisted_bit_rol_)
@Js
def PyJsHoisted_str2binl_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['mask', 'bin', 'i', 'str'])
    var.put('bin', var.get('Array')())
    var.put('mask', ((Js(1.0)<<var.get('chrsz'))-Js(1.0)))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('str').get('length')*var.get('chrsz'))):
        try:
            var.get('bin').put((var.get('i')>>Js(5.0)), ((var.get('str').callprop('charCodeAt', (var.get('i')/var.get('chrsz')))&var.get('mask'))<<(var.get('i')%Js(32.0))), '|')
        finally:
                var.put('i', var.get('chrsz'), '+')
    return var.get('bin')
PyJsHoisted_str2binl_.func_name = 'str2binl'
var.put('str2binl', PyJsHoisted_str2binl_)
@Js
def PyJsHoisted_binl2str_(bin, this, arguments, var=var):
    var = Scope({'bin':bin, 'this':this, 'arguments':arguments}, var)
    var.registers(['mask', 'bin', 'i', 'str'])
    var.put('str', Js(''))
    var.put('mask', ((Js(1.0)<<var.get('chrsz'))-Js(1.0)))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('bin').get('length')*Js(32.0))):
        try:
            var.put('str', var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('bin').get((var.get('i')>>Js(5.0))),(var.get('i')%Js(32.0)))&var.get('mask'))), '+')
        finally:
                var.put('i', var.get('chrsz'), '+')
    return var.get('str')
PyJsHoisted_binl2str_.func_name = 'binl2str'
var.put('binl2str', PyJsHoisted_binl2str_)
@Js
def PyJsHoisted_binl2hex_(binarray, this, arguments, var=var):
    var = Scope({'binarray':binarray, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'hex_tab', 'binarray', 'str'])
    var.put('hex_tab', (Js('0123456789ABCDEF') if var.get('hexcase') else Js('0123456789abcdef')))
    var.put('str', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('binarray').get('length')*Js(4.0))):
        try:
            var.put('str', (var.get('hex_tab').callprop('charAt', ((var.get('binarray').get((var.get('i')>>Js(2.0)))>>(((var.get('i')%Js(4.0))*Js(8.0))+Js(4.0)))&Js(15)))+var.get('hex_tab').callprop('charAt', ((var.get('binarray').get((var.get('i')>>Js(2.0)))>>((var.get('i')%Js(4.0))*Js(8.0)))&Js(15)))), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('str')
PyJsHoisted_binl2hex_.func_name = 'binl2hex'
var.put('binl2hex', PyJsHoisted_binl2hex_)
@Js
def PyJsHoisted_binl2b64_(binarray, this, arguments, var=var):
    var = Scope({'binarray':binarray, 'this':this, 'arguments':arguments}, var)
    var.registers(['str', 'i', 'j', 'binarray', 'triplet', 'tab'])
    var.put('tab', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))
    var.put('str', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('binarray').get('length')*Js(4.0))):
        try:
            var.put('triplet', (((((var.get('binarray').get((var.get('i')>>Js(2.0)))>>(Js(8.0)*(var.get('i')%Js(4.0))))&Js(255))<<Js(16.0))|(((var.get('binarray').get(((var.get('i')+Js(1.0))>>Js(2.0)))>>(Js(8.0)*((var.get('i')+Js(1.0))%Js(4.0))))&Js(255))<<Js(8.0)))|((var.get('binarray').get(((var.get('i')+Js(2.0))>>Js(2.0)))>>(Js(8.0)*((var.get('i')+Js(2.0))%Js(4.0))))&Js(255))))
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<Js(4.0)):
                try:
                    if (((var.get('i')*Js(8.0))+(var.get('j')*Js(6.0)))>(var.get('binarray').get('length')*Js(32.0))):
                        var.put('str', var.get('b64pad'), '+')
                    else:
                        var.put('str', var.get('tab').callprop('charAt', ((var.get('triplet')>>(Js(6.0)*(Js(3.0)-var.get('j'))))&Js(63))), '+')
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        finally:
                var.put('i', Js(3.0), '+')
    return var.get('str')
PyJsHoisted_binl2b64_.func_name = 'binl2b64'
var.put('binl2b64', PyJsHoisted_binl2b64_)
var.put('hexcase', Js(0.0))
var.put('b64pad', Js(''))
var.put('chrsz', Js(8.0))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
md5 = var.to_python()