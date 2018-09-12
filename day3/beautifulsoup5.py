#find(name,attrs,recursive,text,**kwargs)
#find_all() 方法将返回文档总负荷条件的所有tag
#find_all() 方法只返回一个

html_doc="""
<html >
<head >

    <meta http-equiv = "content-type" content = "text/html;charset=utf-8" >
    <meta http-equiv = "X-UA-Compatible" content = "IE=Edge" >
	<meta content = "always" name = "referrer" >
    <meta name = "theme-color" content = "#2932e1" >
    <link rel = "shortcut icon" href = "/favicon.ico" type = "image/x-icon" / >
    <link rel = "search" type = "application/opensearchdescription+xml" href = "/content-search.xml" title = "百度搜索" / >
    <link rel = "icon" sizes = "any" mask href = "//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg" >

	<link rel = "dns-prefetch" href = "//s1.bdstatic.com"/>
	<link rel = "dns-prefetch" href = "//t1.baidu.com"/>
	<link rel = "dns-prefetch" href = "//t2.baidu.com"/>
	<link rel = "dns-prefetch" href = "//t3.baidu.com"/>
	<link rel = "dns-prefetch" href = "//t10.baidu.com"/>
	<link rel = "dns-prefetch" href = "//t11.baidu.com"/>
	<link rel = "dns-prefetch" href = "//t12.baidu.com"/>
	<link rel = "dns-prefetch" href = "//b1.bdstatic.com"/>

    <title > 百度一下，你就知道 < /title >

</head >

<body link = "#0000cc" >
	<script >
	if (/Chrome\/ 37.0.2062.94/i.test(navigator.userAgent) & & (/(windows 7) | (windows nt 6.1)/i.test(navigator.userAgent))) {
		var _chrome_37_fix = document.createElement("style");
		_chrome_37_fix.type = "text/css";
		_chrome_37_fix.setAttribute("data-for", "result");
		_chrome_37_fix.innerHTML = ".t,.f16,#kw,.s_ipt,.c-title,.c-title-size,.to_zhidao,.to_tieba,.to_zhidao_bottom{font-size:15px;} .ec-hospital-info-main h2,.ad-widget-gx_sck-ylzx-doctor-info h2,.ec-card-main h2,.ad-widget-h1 h2,.ad-widget-title h2,.ad-widget-small-head h2,.ad-widget-small-head h2 a,.ad-widget-header .ec-figcaption h2{font-size: 15px !important;}";
		document.getElementsByTagName("head")[0].appendChild(_chrome_37_fix); 	}
	</script >
    <div id="wrapper" style="display:none;">
        


        


<script>if(window.bds&&bds.util&&bds.util.setContainerWidth){bds.util.setContainerWidth();}</script><div id="head"><div class="head_wrapper"><div class="s_form"><div class="s_form_wrapper"><style>.index-logo-srcnew {display: none;}@media (-webkit-min-device-pixel-ratio: 2),(min--moz-device-pixel-ratio: 2),(-o-min-device-pixel-ratio: 2),(min-device-pixel-ratio: 2){.index-logo-src {display: none;}.index-logo-srcnew {display: inline;}}</style><div id="lg"><img hidefocus="true" class='index-logo-src' src="//www.baidu.com/img/bd_logo1.png" width="270" height="129" usemap="#mp"><img hidefocus="true" class='index-logo-srcnew' src="//www.baidu.com/img/bd_logo1.png?qua=high" width="270" height="129" usemap="#mp"><map name="mp"><area style="outline:none;" hidefocus="true" shape="rect" coords="0,0,270,129" href="//www.baidu.com/s?wd=%E4%BB%8A%E6%97%A5%E6%96%B0%E9%B2%9C%E4%BA%8B&tn=SE_PclogoS_8whnvm25&sa=ire_dl_gh_logo&rsv_dl=igh_logo_pcs" onmousedown="return ns_c({fm: 'tab', tab: 'felogo', rsv_platform: 'wwwhome' })" target="_blank" title="点击一下，了解更多"onmousedown="return ns_c({'fm':'behs','tab':'bdlogo'})"></map></div><a href="/" id="result_logo" onmousedown="return c({'fm':'tab','tab':'logo'})"><img class='index-logo-src' src="//www.baidu.com/img/baidu_jgylogo3.gif" alt="到百度首页" title="到百度首页"><img class='index-logo-srcnew' src="//www.baidu.com/img/baidu_jgylogo3.gif" alt="到百度首页" title="到百度首页"></a><form id="form" name="f" action="/s" class="fm"><input type="hidden" name="ie" value="utf-8"><input type="hidden" name="f" value="8"><input type="hidden" name="rsv_bp" value="1"><input type="hidden" name="rsv_idx" value="1"><input type=hidden name=ch value=""><input type=hidden name=tn value="baidu"><input type=hidden name=bar value=""><span class="bg s_ipt_wr"><input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off"></span><span class="bg s_btn_wr"><input type="submit" id="su" value="百度一下" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>输入法</span></div><ul id="mMenu"><li><a href="javascript:;" name="ime_hw">手写</a></li><li><a href="javascript:;" name="ime_py">拼音</a></li><li class="ln"></li><li><a href="javascript:;" name="ime_cl">关闭</a></li></ul></span></span><input type="hidden" name="rn" value=""><input type="hidden" name="oq" value=""><input type="hidden" name="rsv_pq" value="aca5b12e0001e443"><input type="hidden" name="rsv_t" value="e04dgGEOxcO6WGAxLnpgKrggBUyNIIuIx1sc64GXl74f7jkBotKftPeDaOA"><input type="hidden" name="rqlang" value="cn"></form><div id="m"></div></div></div><div id="u"><a class="toindex" href="/">百度首页</a><a href="javascript:;" name="tj_settingicon" class="pf">设置<i class="c-icon c-icon-triangle-down"></i></a><a href="https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5" name="tj_login" class="lb" onclick="return false;">登录</a></div><div id="u1"><a href="http://news.baidu.com" name="tj_trnews" class="mnav">新闻</a><a href="https://www.hao123.com" name="tj_trhao123" class="mnav">hao123</a><a href="http://map.baidu.com" name="tj_trmap" class="mnav">地图</a><a href="http://v.baidu.com" name="tj_trvideo" class="mnav">视频</a><a href="http://tieba.baidu.com" name="tj_trtieba" class="mnav">贴吧</a><a href="http://xueshu.baidu.com" name="tj_trxueshu" class="mnav">学术</a><a href="https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5" name="tj_login" class="lb" onclick="return false;">登录</a><a href="http://www.baidu.com/gaoji/preferences.html" name="tj_settingicon" class="pf">设置</a><a href="http://www.baidu.com/more/" name="tj_briicon" class="bri" style="display: block;">更多产品</a></div></div></div>



<div class="s_tab" id="s_tab">
<div class="s_tab_inner">
    <b>网页</b>
    <a href="//www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
    <a href="http://tieba.baidu.com/f?kw=&fr=wwwt" wdfield="kw"  onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
    <a href="http://zhidao.baidu.com/q?ct=17&pn=0&tn=ikaslist&rn=10&word=&fr=wwwt" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
    <a href="http://music.taihe.com/search?fr=ps&ie=utf-8&key=" wdfield="key"  onmousedown="return c({'fm':'tab','tab':'music'})">音乐</a>
    <a href="http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'pic'})">图片</a>
    <a href="http://v.baidu.com/v?ct=301989888&rn=20&pn=0&db=0&s=25&ie=utf-8&word=" wdfield="word"   onmousedown="return c({'fm':'tab','tab':'video'})">视频</a>
    <a href="http://map.baidu.com/m?word=&fr=ps01000" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'map'})">地图</a>
    <a href="http://wenku.baidu.com/search?word=&lm=0&od=0&ie=utf-8" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'wenku'})">文库</a>
    <a href="//www.baidu.com/more/"  onmousedown="return c({'fm':'tab','tab':'more'})">更多»</a>
</div>
</div>

        

<div class="qrcodeCon">
	<div id="qrcode">
		<div class="qrcode-item qrcode-item-1">
			<div class="qrcode-img"></div>
			<div class="qrcode-text">
					<p><b>百度</b></p>
			</div>
		</div>
	</div>
</div>
<div id="ftCon">

<div class="ftCon-Wrapper"><div id="ftConw"><p id="lh"><a id="setf" href="//www.baidu.com/cache/sethelp/help.html" onmousedown="return ns_c({'fm':'behs','tab':'favorites','pos':0})" target="_blank">把百度设为主页</a><a onmousedown="return ns_c({'fm':'behs','tab':'tj_about'})" href="http://home.baidu.com">关于百度</a><a onmousedown="return ns_c({'fm':'behs','tab':'tj_about_en'})" href="http://ir.baidu.com">About&nbsp;&nbsp;Baidu</a><a onmousedown="return ns_c({'fm':'behs','tab':'tj_tuiguang'})" href="http://e.baidu.com/?refer=888">百度推广</a></p><p id="cp">&copy;2018&nbsp;Baidu&nbsp;<a href="http://www.baidu.com/duty/" onmousedown="return ns_c({'fm':'behs','tab':'tj_duty'})">使用百度前必读</a>&nbsp;<a href="http://jianyi.baidu.com/" class="cp-feedback" onmousedown="return ns_c({'fm':'behs','tab':'tj_homefb'})">意见反馈</a>&nbsp;京ICP证030173号&nbsp;<i class="c-icon-icrlogo"></i>&nbsp;<a id="jgwab"  target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000001">京公网安备11000002000001号</a>&nbsp;<i class="c-icon-jgwablogo"></i></p></div></div></div>
        <div id="wrapper_wrapper">
        </div>
    </div>
    <div class="c-tips-container" id="c-tips-container"></div>

</body>
</html>
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,'lxml')
#1.find()
print(soup.find('title'))

#2.find_all() 和find()区别,返回元素列表/返回结果 返回空列表/返回None
print(soup.find('xxxx'))

#soup.head.title  是tag的名字 方法的简写多次调用find()
print(soup.find('head').find('title'))