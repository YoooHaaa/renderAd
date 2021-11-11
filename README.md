# renderAd
自渲染监控2.0版

先安装Magisk插件  /resource/push 中的Riru.zip  和 FridatRiruMoudle.zip 重启手机，把 /resource/config.json 中的init改成false 就ok了

本工具在1.0 的基础上改进，无需再开启fridaserver， 插件会使目标应用主动加载gadget

hook 监控的脚本在 /resource/push/twitter.js 

twitter.js 脚本加载时会先加载 yooha.dex 我把socket通讯写在这个dex中，由dex中的socket与PC进行通讯

这个版本我测试过，比上个版本更加稳定，不得不说gadget比server更稳，比较适合用于持久化的生产环境中，最近在看雪看到有个fridaManager，听说是用的Riru，应用跟我这个原理差不多。

