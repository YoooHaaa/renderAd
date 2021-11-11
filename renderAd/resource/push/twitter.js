
// 1-监控中  2-正在加载  3-error
var JS_MONITOR = "监控中"
var JS_LOAD    = "加载中"
var JS_ERROR   = "Error"

var load_gdt = false;
var click_gdt = false;
var load_csj = false;
var click_csj = false
var load_ks = false;
var click_ks = false;

function log_print(info){
	var Log = Java.use("android.util.Log");
    Log.i("yooha-testjs", info);

}

function sendData(sdk, event, status, msg){
    send_info(sdk, event, msg, status)
}

function filter_repeat(classname, funcname, argslen){
    if (classname.indexOf('com.qq.e') != -1){
        if (funcname.indexOf("$init") != -1){
            if (argslen == 3){
                return true;
            }
        }
        else if(funcname.indexOf("bindAdToView") != -1){
            if (argslen == 4){
                return true;
            }
        }
    }
    else if(classname.indexOf('com.bytedance.sdk') != -1){
        if (funcname.indexOf("loadFeedAd") != -1){
            if (argslen == 2){
                return true;
            }
        }
        else if(funcname.indexOf("loadNativeAd") != -1){
            if (argslen == 2){
                return true;
            }
        }
        else if(funcname.indexOf("loadDrawFeedAd") != -1){
            if (argslen == 2){
                return true;
            }
        }
        else if(funcname.indexOf("registerViewForInteraction") != -1){
            if (argslen == 6){
                return true;
            }
        }
    }
    else if(classname.indexOf('com.kwad.sdk') != -1){
        if (funcname.indexOf("loadNativeAd") != -1){
            if (argslen == 2){
                return true;
            }
        }
        else if(funcname.indexOf("registerViewForInteraction") != -1){
            if (argslen == 3){
                return true;
            }
        }
    }
    return false;
}
function hook_func(classname, funcname, sdk, event){
    try{
        log_print("正在hook " + classname + " -> " + funcname);
        var Platform = Java.use(classname);
        var len = Platform[funcname].overloads.length;   
        for(var i = 0; i < len; ++i) {
            Platform[funcname].overloads[i].implementation = function () {    
                var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
                if (filter_repeat(classname, funcname, arguments.length)){
                    //console.log(stack);
                    sendData(sdk, event, JS_LOAD, stack);
                }
                this[funcname].apply(this, arguments);
            }
        }  
        sendData(sdk, event, JS_MONITOR, '');
    }catch(error){
        sendData(sdk, event, JS_ERROR, '');
    }
}
function discern_gdt(name){
    if (!load_gdt && name.indexOf("com.qq.e.ads.nativ.NativeUnifiedAD") != -1){
        //load广告的接口-广点通
        hook_func('com.qq.e.ads.nativ.NativeUnifiedAD', "$init", "广点通", "加载自渲染信息流广告");
        load_gdt = true;
    }
    if (!click_gdt && name.indexOf("com.qq.e.ads.nativ.NativeUnifiedADDataAdapter") != -1){
        //设置点击view的接口-广点通
        hook_func('com.qq.e.ads.nativ.NativeUnifiedADDataAdapter', "bindAdToView", "广点通", "设置点击事件");
        click_gdt = true;
    }
}
function discern_csj(name){
    if (!load_csj){
        var hookCls = Java.use(name);
        var interFaces = hookCls.class.getInterfaces();
        if(interFaces.length > 0){
            //load广告的接口-穿山甲
            if (interFaces[0].toString().indexOf("com.bytedance.sdk.openadsdk.TTAdNative") != -1){
                var srevar = interFaces[0].toString();
                if (srevar == "interface com.bytedance.sdk.openadsdk.TTAdNative"){
                    if (Java.use(name).class.isInterface() == false){
                        console.log("--> 实现类", name);
                        console.log("--> 接口类", interFaces[0].toString());
                        hook_func(name, "loadFeedAd",     "穿山甲", "加载自渲染信息流广告");
                        hook_func(name, "loadNativeAd",   "穿山甲", "加载自渲染插屏/Banner广告")
                        hook_func(name, "loadDrawFeedAd", "穿山甲", "加载自渲染Draw广告")
                        load_csj = true;
                        return;

                    }
                }
            }
        }
    }
    if (!click_csj){
        var hookCls = Java.use(name);
        var interFaces = hookCls.class.getInterfaces();
        if(interFaces.length > 0){
            //设置点击view的接口-穿山甲
            if (interFaces[0].toString().indexOf("com.bytedance.sdk.openadsdk.TTNativeAd") != -1){
                var srevar = interFaces[0].toString();
                if (srevar == "interface com.bytedance.sdk.openadsdk.TTNativeAd"){
                    if(Java.use(name).class.isInterface() == false){
                        console.log("--> 实现类", name);
                        console.log("--> 接口类", interFaces[0].toString());
                        hook_func(name, "registerViewForInteraction", "穿山甲", "设置点击事件");
                        click_csj = true;
                        return;
                    }
                }
            }
        }
    }
}

function discern_ks(name){
    if (!load_ks){
        var hookCls = Java.use(name);
        var interFaces = hookCls.class.getInterfaces();
        if(interFaces.length > 0){
            //load广告的接口-快手
            if (interFaces[0].toString().indexOf("com.kwad.sdk.api.KsLoadManager") != -1){
                var srevar = interFaces[0].toString();
                if (srevar == "interface com.kwad.sdk.api.KsLoadManager"){
                    if (Java.use(name).class.isInterface() == false){
                        console.log("--> 实现类", name);
                        console.log("--> 接口类", interFaces[0].toString());
                        hook_func(name, "loadNativeAd", "快手", "加载自渲染广告");
                        load_ks = true;
                        return;
                    }
                }
            }
        }
    }
    if (!click_ks){
        var hookCls = Java.use(name);
        var interFaces = hookCls.class.getInterfaces();
        if(interFaces.length > 0){
            //设置点击view的接口-快手
            if (interFaces[0].toString().indexOf("com.kwad.sdk.api.core.AbstractKsNativeAd") != -1){
                var srevar = interFaces[0].toString();
                if (srevar == "interface com.kwad.sdk.api.core.AbstractKsNativeAd"){
                    if(Java.use(name).class.isInterface() == false){
                        console.log("--> 实现类", name);
                        console.log("--> 接口类", interFaces[0].toString());
                        log_print(name + ' --> registerViewForInteraction')
                        hook_func(name, "registerViewForInteraction", "快手", "设置点击事件");
                        click_ks = true;
                        return;
                    }
                }
            }
        }
    }
}
function enumerateClass(){
    Java.enumerateLoadedClasses({
        onMatch: function (name, handle){
            if (name.indexOf("com.qq.e") != -1){
                discern_gdt(name);
            }
            else if(name.indexOf("com.bytedance.sdk") != -1){
                discern_csj(name);
            }
            else if(name.indexOf("com.kwad.sdk") != -1){
                discern_ks(name);
            }
        },
        onComplete: function () {
        }
    })
}
function monitor(){
    Java.perform(function(){
        enumerateClass();
    });
}


function load_dex(){
    var dexPath = "/data/local/tmp/yooha.dex";
    Java.openClassFile(dexPath).load();
    log_print("inject " + dexPath + " successfully!")
}

function init_dex(){
    log_print("init_dex");
    Java.use("com.yooha.linkpc.MyServer").linkSocket();
}

function send_info(type, event, msg, status){ 
    try{
        Java.use("com.yooha.linkpc.MyServer").sendMsg(type, event, msg, status);
    }catch(e){
        log_print("send_info error:" + String(e));
    }
}

function main(){
    Java.perform(function(){
        load_dex();
        init_dex();

        setInterval(() => {monitor()}, 10000);
    });
}
setImmediate(main)