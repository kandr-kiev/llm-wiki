---
source_url: https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_01958255553.html
ingested: 2026-07-17
sha256: d0092e54cddfd23fcdd68795359b7d7e4c608e93fbb59211f5f3e9424f253d01
blog_source: Oracle DBA Soyma
---
<!DOCTYPE html>
<html class='v2' dir='ltr' lang='en' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
<link href='https://www.blogger.com/static/v1/widgets/2872013778-css_bundle_v2.css' rel='stylesheet' type='text/css'/>
<meta content='width=1100' name='viewport'/>
<meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
<meta content='blogger' name='generator'/>
<link href='https://dbasoumya.blogspot.com/favicon.ico' rel='icon' type='image/x-icon'/>
<link href='https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_01958255553.html' rel='canonical'/>
<link rel="alternate" type="application/atom+xml" title="Soumya&#39;s Database Blog  - Atom" href="https://dbasoumya.blogspot.com/feeds/posts/default" />
<link rel="alternate" type="application/rss+xml" title="Soumya&#39;s Database Blog  - RSS" href="https://dbasoumya.blogspot.com/feeds/posts/default?alt=rss" />
<link rel="service.post" type="application/atom+xml" title="Soumya&#39;s Database Blog  - Atom" href="https://draft.blogger.com/feeds/8734340484599901680/posts/default" />

<link rel="alternate" type="application/atom+xml" title="Soumya&#39;s Database Blog  - Atom" href="https://dbasoumya.blogspot.com/feeds/2970540619944016535/comments/default" />
<!--Can't find substitution for tag [blog.ieCssRetrofitLinks]-->
<link href='https://blogger.googleusercontent.com/img/a/AVvXsEhxf3yyl-KFU9kXj_p62ZBwHtUFyeTEj_EaRNUIQZKbVSJvo1Dp_PPpvztGPCyE8q0b5WfFdknBqBsQ0BPp2c05ig_ENeCTit8HCaj8Koj5hnQ2hyLW5b3hGdw2L0PSncHtsomE9neSCnoqVK0AYO8P8ZBlFT6J9gEYsHmy0qzY2qHg_nowUvP01NBSpD0=w640-h474' rel='image_src'/>
<meta content='https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_01958255553.html' property='og:url'/>
<meta content='Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part IV' property='og:title'/>
<meta content='Find a solution for different databases such as Oracle, MSSQL,Mysql techniques and stay updated with new technologies related to them' property='og:description'/>
<meta content='https://blogger.googleusercontent.com/img/a/AVvXsEhxf3yyl-KFU9kXj_p62ZBwHtUFyeTEj_EaRNUIQZKbVSJvo1Dp_PPpvztGPCyE8q0b5WfFdknBqBsQ0BPp2c05ig_ENeCTit8HCaj8Koj5hnQ2hyLW5b3hGdw2L0PSncHtsomE9neSCnoqVK0AYO8P8ZBlFT6J9gEYsHmy0qzY2qHg_nowUvP01NBSpD0=w1200-h630-p-k-no-nu' property='og:image'/>
<title>Soumya's Database Blog : Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part IV</title>
<style id='page-skin-1' type='text/css'><!--
/*
-----------------------------------------------
Blogger Template Style
Name:     Simple
Designer: Blogger
URL:      www.blogger.com
----------------------------------------------- */
<script async="async" custom-element="amp-auto-ads" src="https://cdn.ampproject.org/v0/amp-auto-ads-0.1.js">
</script>
/* Variable definitions
====================
<Variable name="keycolor" description="Main Color" type="color" default="#66bbdd"/>
<Group description="Page Text" selector="body">
<Variable name="body.font" description="Font" type="font"
default="normal normal 12px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
<Variable name="body.text.color" description="Text Color" type="color" default="#222222"/>
</Group>
<Group description="Backgrounds" selector=".body-fauxcolumns-outer">
<Variable name="body.background.color" description="Outer Background" type="color" default="#66bbdd"/>
<Variable name="content.background.color" description="Main Background" type="color" default="#ffffff"/>
<Variable name="header.background.color" description="Header Background" type="color" default="transparent"/>
</Group>
<Group description="Links" selector=".main-outer">
<Variable name="link.color" description="Link Color" type="color" default="#2288bb"/>
<Variable name="link.visited.color" description="Visited Color" type="color" default="#888888"/>
<Variable name="link.hover.color" description="Hover Color" type="color" default="#33aaff"/>
</Group>
<Group description="Blog Title" selector=".header h1">
<Variable name="header.font" description="Font" type="font"
default="normal normal 60px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
<Variable name="header.text.color" description="Title Color" type="color" default="#3399bb" />
</Group>
<Group description="Blog Description" selector=".header .description">
<Variable name="description.text.color" description="Description Color" type="color"
default="#777777" />
</Group>
<Group description="Tabs Text" selector=".tabs-inner .widget li a">
<Variable name="tabs.font" description="Font" type="font"
default="normal normal 14px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
<Variable name="tabs.text.color" description="Text Color" type="color" default="#999999"/>
<Variable name="tabs.selected.text.color" description="Selected Color" type="color" default="#000000"/>
</Group>
<Group description="Tabs Background" selector=".tabs-outer .PageList">
<Variable name="tabs.background.color" description="Background Color" type="color" default="#f5f5f5"/>
<Variable name="tabs.selected.background.color" description="Selected Color" type="color" default="#eeeeee"/>
</Group>
<Group description="Post Title" selector="h3.post-title, .comments h4">
<Variable name="post.title.font" description="Font" type="font"
default="normal normal 22px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
</Group>
<Group description="Date Header" selector=".date-header">
<Variable name="date.header.color" description="Text Color" type="color"
default="#222222"/>
<Variable name="date.header.background.color" description="Background Color" type="color"
default="transparent"/>
<Variable name="date.header.font" description="Text Font" type="font"
default="normal bold 11px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
<Variable name="date.header.padding" description="Date Header Padding" type="string" default="inherit"/>
<Variable name="date.header.letterspacing" description="Date Header Letter Spacing" type="string" default="inherit"/>
<Variable name="date.header.margin" description="Date Header Margin" type="string" default="inherit"/>
</Group>
<Group description="Post Footer" selector=".post-footer">
<Variable name="post.footer.text.color" description="Text Color" type="color" default="#666666"/>
<Variable name="post.footer.background.color" description="Background Color" type="color"
default="#f9f9f9"/>
<Variable name="post.footer.border.color" description="Shadow Color" type="color" default="#eeeeee"/>
</Group>
<Group description="Gadgets" selector="h2">
<Variable name="widget.title.font" description="Title Font" type="font"
default="normal bold 11px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
<Variable name="widget.title.text.color" description="Title Color" type="color" default="#000000"/>
<Variable name="widget.alternate.text.color" description="Alternate Color" type="color" default="#999999"/>
</Group>
<Group description="Images" selector=".main-inner">
<Variable name="image.background.color" description="Background Color" type="color" default="#ffffff"/>
<Variable name="image.border.color" description="Border Color" type="color" default="#eeeeee"/>
<Variable name="image.text.color" description="Caption Text Color" type="color" default="#222222"/>
</Group>
<Group description="Accents" selector=".content-inner">
<Variable name="body.rule.color" description="Separator Line Color" type="color" default="#eeeeee"/>
<Variable name="tabs.border.color" description="Tabs Border Color" type="color" default="#eeeeee"/>
</Group>
<Variable name="body.background" description="Body Background" type="background"
color="#66bbdd" default="$(color) none repeat scroll top left"/>
<Variable name="body.background.override" description="Body Background Override" type="string" default=""/>
<Variable name="body.background.gradient.cap" description="Body Gradient Cap" type="url"
default="url(https://resources.blogblog.com/blogblog/data/1kt/simple/gradients_light.png)"/>
<Variable name="body.background.gradient.tile" description="Body Gradient Tile" type="url"
default="url(https://resources.blogblog.com/blogblog/data/1kt/simple/body_gradient_tile_light.png)"/>
<Variable name="content.background.color.selector" description="Content Background Color Selector" type="string" default=".content-inner"/>
<Variable name="content.padding" description="Content Padding" type="length" default="10px" min="0" max="100px"/>
<Variable name="content.padding.horizontal" description="Content Horizontal Padding" type="length" default="10px" min="0" max="100px"/>
<Variable name="content.shadow.spread" description="Content Shadow Spread" type="length" default="40px" min="0" max="100px"/>
<Variable name="content.shadow.spread.webkit" description="Content Shadow Spread (WebKit)" type="length" default="5px" min="0" max="100px"/>
<Variable name="content.shadow.spread.ie" description="Content Shadow Spread (IE)" type="length" default="10px" min="0" max="100px"/>
<Variable name="main.border.width" description="Main Border Width" type="length" default="0" min="0" max="10px"/>
<Variable name="header.background.gradient" description="Header Gradient" type="url" default="none"/>
<Variable name="header.shadow.offset.left" description="Header Shadow Offset Left" type="length" default="-1px" min="-50px" max="50px"/>
<Variable name="header.shadow.offset.top" description="Header Shadow Offset Top" type="length" default="-1px" min="-50px" max="50px"/>
<Variable name="header.shadow.spread" description="Header Shadow Spread" type="length" default="1px" min="0" max="100px"/>
<Variable name="header.padding" description="Header Padding" type="length" default="30px" min="0" max="100px"/>
<Variable name="header.border.size" description="Header Border Size" type="length" default="1px" min="0" max="10px"/>
<Variable name="header.bottom.border.size" description="Header Bottom Border Size" type="length" default="1px" min="0" max="10px"/>
<Variable name="header.border.horizontalsize" description="Header Horizontal Border Size" type="length" default="0" min="0" max="10px"/>
<Variable name="description.text.size" description="Description Text Size" type="string" default="140%"/>
<Variable name="tabs.margin.top" description="Tabs Margin Top" type="length" default="0" min="0" max="100px"/>
<Variable name="tabs.margin.side" description="Tabs Side Margin" type="length" default="30px" min="0" max="100px"/>
<Variable name="tabs.background.gradient" description="Tabs Background Gradient" type="url"
default="url(https://resources.blogblog.com/blogblog/data/1kt/simple/gradients_light.png)"/>
<Variable name="tabs.border.width" description="Tabs Border Width" type="length" default="1px" min="0" max="10px"/>
<Variable name="tabs.bevel.border.width" description="Tabs Bevel Border Width" type="length" default="1px" min="0" max="10px"/>
<Variable name="post.margin.bottom" description="Post Bottom Margin" type="length" default="25px" min="0" max="100px"/>
<Variable name="image.border.small.size" description="Image Border Small Size" type="length" default="2px" min="0" max="10px"/>
<Variable name="image.border.large.size" description="Image Border Large Size" type="length" default="5px" min="0" max="10px"/>
<Variable name="page.width.selector" description="Page Width Selector" type="string" default=".region-inner"/>
<Variable name="page.width" description="Page Width" type="string" default="auto"/>
<Variable name="main.section.margin" description="Main Section Margin" type="length" default="15px" min="0" max="100px"/>
<Variable name="main.padding" description="Main Padding" type="length" default="15px" min="0" max="100px"/>
<Variable name="main.padding.top" description="Main Padding Top" type="length" default="30px" min="0" max="100px"/>
<Variable name="main.padding.bottom" description="Main Padding Bottom" type="length" default="30px" min="0" max="100px"/>
<Variable name="paging.background"
color="#ffffff"
description="Background of blog paging area" type="background"
default="transparent none no-repeat scroll top center"/>
<Variable name="footer.bevel" description="Bevel border length of footer" type="length" default="0" min="0" max="10px"/>
<Variable name="mobile.background.overlay" description="Mobile Background Overlay" type="string"
default="transparent none repeat scroll top left"/>
<Variable name="mobile.background.size" description="Mobile Background Size" type="string" default="auto"/>
<Variable name="mobile.button.color" description="Mobile Button Color" type="color" default="#ffffff" />
<Variable name="startSide" description="Side where text starts in blog language" type="automatic" default="left"/>
<Variable name="endSide" description="Side where text ends in blog language" type="automatic" default="right"/>
*/
/* Content
----------------------------------------------- */
body {
font: normal normal 12px 'Trebuchet MS', Trebuchet, Verdana, sans-serif;
color: #222222;
background: #66bbdd none repeat scroll top left;
padding: 0 0 0 0;
}
html body .region-inner {
min-width: 0;
max-width: 100%;
width: auto;
}
h2 {
font-size: 22px;
}
a:link {
text-decoration:none;
color: #2288bb;
}
a:visited {
text-decoration:none;
color: #888888;
}
a:hover {
text-decoration:underline;
color: #33aaff;
}
.body-fauxcolumn-outer .fauxcolumn-inner {
background: transparent none repeat scroll top left;
_background-image: none;
}
.body-fauxcolumn-outer .cap-top {
position: absolute;
z-index: 1;
height: 400px;
width: 100%;
}
.body-fauxcolumn-outer .cap-top .cap-left {
width: 100%;
background: transparent none repeat-x scroll top left;
_background-image: none;
}
.content-outer {
-moz-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
-webkit-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
-goog-ms-box-shadow: 0 0 0 #333333;
box-shadow: 0 0 0 rgba(0, 0, 0, .15);
margin-bottom: 1px;
}
.content-inner {
padding: 10px 40px;
}
.content-inner {
background-color: #ffffff;
}
/* Header
----------------------------------------------- */
.header-outer {
background: rgba(0,0,0,0) none repeat-x scroll 0 -400px;
_background-image: none;
}
.Header h1 {
font: normal normal 40px 'Trebuchet MS',Trebuchet,Verdana,sans-serif;
color: #3399bb;
text-shadow: 0 0 0 rgba(0, 0, 0, .2);
}
.Header h1 a {
color: #3399bb;
}
.Header .description {
font-size: 18px;
color: #777777;
}
.header-inner .Header .titlewrapper {
padding: 22px 0;
}
.header-inner .Header .descriptionwrapper {
padding: 0 0;
}
/* Tabs
----------------------------------------------- */
.tabs-inner .section:first-child {
border-top: 0 solid #dddddd;
}
.tabs-inner .section:first-child ul {
margin-top: -1px;
border-top: 1px solid #dddddd;
border-left: 1px solid #dddddd;
border-right: 1px solid #dddddd;
}
.tabs-inner .widget ul {
background: #f5f5f5 none repeat-x scroll 0 -800px;
_background-image: none;
border-bottom: 1px solid #dddddd;
margin-top: 0;
margin-left: -30px;
margin-right: -30px;
}
.tabs-inner .widget li a {
display: inline-block;
padding: .6em 1em;
font: normal normal 12px 'Trebuchet MS', Trebuchet, Verdana, sans-serif;
color: #999999;
border-left: 1px solid #ffffff;
border-right: 1px solid #dddddd;
}
.tabs-inner .widget li:first-child a {
border-left: none;
}
.tabs-inner .widget li.selected a, .tabs-inner .widget li a:hover {
color: #000000;
background-color: #eeeeee;
text-decoration: none;
}
/* Columns
----------------------------------------------- */
.main-outer {
border-top: 0 solid #eeeeee;
}
.fauxcolumn-left-outer .fauxcolumn-inner {
border-right: 1px solid #eeeeee;
}
.fauxcolumn-right-outer .fauxcolumn-inner {
border-left: 1px solid #eeeeee;
}
/* Headings
----------------------------------------------- */
div.widget > h2,
div.widget h2.title {
margin: 0 0 1em 0;
font: normal bold 11px 'Trebuchet MS',Trebuchet,Verdana,sans-serif;
color: #000000;
}
/* Widgets
----------------------------------------------- */
.widget .zippy {
color: #999999;
text-shadow: 2px 2px 1px rgba(0, 0, 0, .1);
}
.widget .popular-posts ul {
list-style: none;
}
/* Posts
----------------------------------------------- */
h2.date-header {
font: normal bold 11px Arial, Tahoma, Helvetica, FreeSans, sans-serif;
}
.date-header span {
background-color: rgba(0,0,0,0);
color: #ffffff;
padding: 0.4em;
letter-spacing: 3px;
margin: inherit;
}
.main-inner {
padding-top: 35px;
padding-bottom: 65px;
}
.main-inner .column-center-inner {
padding: 0 0;
}
.main-inner .column-center-inner .section {
margin: 0 1em;
}
.post {
margin: 0 0 45px 0;
}
h3.post-title, .comments h4 {
font: normal normal 22px 'Trebuchet MS',Trebuchet,Verdana,sans-serif;
margin: .75em 0 0;
}
.post-body {
font-size: 110%;
line-height: 1.4;
position: relative;
}
.post-body img, .post-body .tr-caption-container, .Profile img, .Image img,
.BlogList .item-thumbnail img {
padding: 2px;
background: #ffffff;
border: 1px solid #eeeeee;
-moz-box-shadow: 1px 1px 5px rgba(0, 0, 0, .1);
-webkit-box-shadow: 1px 1px 5px rgba(0, 0, 0, .1);
box-shadow: 1px 1px 5px rgba(0, 0, 0, .1);
}
.post-body img, .post-body .tr-caption-container {
padding: 5px;
}
.post-body .tr-caption-container {
color: #666666;
}
.post-body .tr-caption-container img {
padding: 0;
background: transparent;
border: none;
-moz-box-shadow: 0 0 0 rgba(0, 0, 0, .1);
-webkit-box-shadow: 0 0 0 rgba(0, 0, 0, .1);
box-shadow: 0 0 0 rgba(0, 0, 0, .1);
}
.post-header {
margin: 0 0 1.5em;
line-height: 1.6;
font-size: 90%;
}
.post-footer {
margin: 20px -2px 0;
padding: 5px 10px;
color: #666666;
background-color: #f9f9f9;
border-bottom: 1px solid #eeeeee;
line-height: 1.6;
font-size: 90%;
}
#comments .comment-author {
padding-top: 1.5em;
border-top: 1px solid #eeeeee;
background-position: 0 1.5em;
}
#comments .comment-author:first-child {
padding-top: 0;
border-top: none;
}
.avatar-image-container {
margin: .2em 0 0;
}
#comments .avatar-image-container img {
border: 1px solid #eeeeee;
}
/* Comments
----------------------------------------------- */
.comments .comments-content .icon.blog-author {
background-repeat: no-repeat;
background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEgAACxIB0t1+/AAAAAd0SU1FB9sLFwMeCjjhcOMAAAD+SURBVDjLtZSvTgNBEIe/WRRnm3U8RC1neQdsm1zSBIU9VVF1FkUguQQsD9ITmD7ECZIJSE4OZo9stoVjC/zc7ky+zH9hXwVwDpTAWWLrgS3QAe8AZgaAJI5zYAmc8r0G4AHYHQKVwII8PZrZFsBFkeRCABYiMh9BRUhnSkPTNCtVXYXURi1FpBDgArj8QU1eVXUzfnjv7yP7kwu1mYrkWlU33vs1QNu2qU8pwN0UpKoqokjWwCztrMuBhEhmh8bD5UDqur75asbcX0BGUB9/HAMB+r32hznJgXy2v0sGLBcyAJ1EK3LFcbo1s91JeLwAbwGYu7TP/3ZGfnXYPgAVNngtqatUNgAAAABJRU5ErkJggg==);
}
.comments .comments-content .loadmore a {
border-top: 1px solid #999999;
border-bottom: 1px solid #999999;
}
.comments .comment-thread.inline-thread {
background-color: #f9f9f9;
}
.comments .continue {
border-top: 2px solid #999999;
}
/* Accents
---------------------------------------------- */
.section-columns td.columns-cell {
border-left: 1px solid #eeeeee;
}
.blog-pager {
background: transparent url(https://resources.blogblog.com/blogblog/data/1kt/simple/paging_dot.png) repeat-x scroll top center;
}
.blog-pager-older-link, .home-link,
.blog-pager-newer-link {
background-color: #ffffff;
padding: 5px;
}
.footer-outer {
border-top: 1px dashed #bbbbbb;
}
/* Mobile
----------------------------------------------- */
body.mobile  {
background-size: auto;
}
.mobile .body-fauxcolumn-outer {
background: transparent none repeat scroll top left;
}
.mobile .body-fauxcolumn-outer .cap-top {
background-size: 100% auto;
}
.mobile .content-outer {
-webkit-box-shadow: 0 0 3px rgba(0, 0, 0, .15);
box-shadow: 0 0 3px rgba(0, 0, 0, .15);
}
.mobile .tabs-inner .widget ul {
margin-left: 0;
margin-right: 0;
}
.mobile .post {
margin: 0;
}
.mobile .main-inner .column-center-inner .section {
margin: 0;
}
.mobile .date-header span {
padding: 0.1em 10px;
margin: 0 -10px;
}
.mobile h3.post-title {
margin: 0;
}
.mobile .blog-pager {
background: transparent none no-repeat scroll top center;
}
.mobile .footer-outer {
border-top: none;
}
.mobile .main-inner, .mobile .footer-inner {
background-color: #ffffff;
}
.mobile-index-contents {
color: #222222;
}
.mobile-link-button {
background-color: #2288bb;
}
.mobile-link-button a:link, .mobile-link-button a:visited {
color: #ffffff;
}
.mobile .tabs-inner .section:first-child {
border-top: none;
}
.mobile .tabs-inner .PageList .widget-content {
background-color: #eeeeee;
color: #000000;
border-top: 1px solid #dddddd;
border-bottom: 1px solid #dddddd;
}
.mobile .tabs-inner .PageList .widget-content .pagelist-arrow {
border-left: 1px solid #dddddd;
}

--></style>
<style id='template-skin-1' type='text/css'><!--
body {
min-width: 1250px;
}
.content-outer, .content-fauxcolumn-outer, .region-inner {
min-width: 1250px;
max-width: 1250px;
_width: 1250px;
}
.main-inner .columns {
padding-left: 0px;
padding-right: 270px;
}
.main-inner .fauxcolumn-center-outer {
left: 0px;
right: 270px;
/* IE6 does not respect left and right together */
_width: expression(this.parentNode.offsetWidth -
parseInt("0px") -
parseInt("270px") + 'px');
}
.main-inner .fauxcolumn-left-outer {
width: 0px;
}
.main-inner .fauxcolumn-right-outer {
width: 270px;
}
.main-inner .column-left-outer {
width: 0px;
right: 100%;
margin-left: -0px;
}
.main-inner .column-right-outer {
width: 270px;
margin-right: -270px;
}
#layout {
min-width: 0;
}
#layout .content-outer {
min-width: 0;
width: 800px;
}
#layout .region-inner {
min-width: 0;
width: auto;
}
body#layout div.add_widget {
padding: 8px;
}
body#layout div.add_widget a {
margin-left: 32px;
}
--></style>
<script type='text/javascript'>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
        ga('create', 'UA-65120560-1', 'auto', 'blogger');
        ga('blogger.send', 'pageview');
      </script>
<link href='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css' rel='stylesheet'/>
<script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js'></script>
<link href='https://draft.blogger.com/dyn-css/authorization.css?targetBlogID=8734340484599901680&amp;zx=41d1aced-0356-45f3-adfb-d6fbd4dc2cb7' media='none' onload='if(media!=&#39;all&#39;)media=&#39;all&#39;' rel='stylesheet'/><noscript><link href='https://draft.blogger.com/dyn-css/authorization.css?targetBlogID=8734340484599901680&amp;zx=41d1aced-0356-45f3-adfb-d6fbd4dc2cb7' rel='stylesheet'/></noscript>
<meta name='google-adsense-platform-account' content='ca-host-pub-1556223355139109'/>
<meta name='google-adsense-platform-domain' content='blogspot.com'/>

<!-- data-ad-client=ca-pub-1226247788850965 -->

</head>
<body class='loading'>
<div class='navbar section' id='navbar' name='Navbar'><div class='widget Navbar' data-version='1' id='Navbar1'><script type="text/javascript">
    function setAttributeOnload(object, attribute, val) {
      if(window.addEventListener) {
        window.addEventListener('load',
          function(){ object[attribute] = val; }, false);
      } else {
        window.attachEvent('onload', function(){ object[attribute] = val; });
      }
    }
  </script>
<div id="navbar-iframe-container"></div>
<script type="text/javascript" src="https://apis.google.com/js/platform.js"></script>
<script type="text/javascript">
      gapi.load("gapi.iframes:gapi.iframes.style.bubble", function() {
        if (gapi.iframes && gapi.iframes.getContext) {
          gapi.iframes.getContext().openChild({
              url: 'https://draft.blogger.com/navbar/8734340484599901680?po\x3d2970540619944016535\x26origin\x3dhttps://dbasoumya.blogspot.com',
              where: document.getElementById("navbar-iframe-container"),
              id: "navbar-iframe"
          });
        }
      });
    </script><script type="text/javascript">
(function() {
var script = document.createElement('script');
script.type = 'text/javascript';
script.src = '//pagead2.googlesyndication.com/pagead/js/google_top_exp.js';
var head = document.getElementsByTagName('head')[0];
if (head) {
head.appendChild(script);
}})();
</script>
</div></div>
<div class='body-fauxcolumns'>
<div class='fauxcolumn-outer body-fauxcolumn-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
</div>
<div class='content'>
<div class='content-fauxcolumns'>
<div class='fauxcolumn-outer content-fauxcolumn-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
</div>
<div class='content-outer'>
<div class='content-cap-top cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left content-fauxborder-left'>
<div class='fauxborder-right content-fauxborder-right'></div>
<div class='content-inner'>
<header>
<div class='header-outer'>
<div class='header-cap-top cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left header-fauxborder-left'>
<div class='fauxborder-right header-fauxborder-right'></div>
<div class='region-inner header-inner'>
<div class='header section' id='header' name='Header'><div class='widget Header' data-version='1' id='Header1'>
<div id='header-inner'>
<div class='titlewrapper'>
<h1 class='title'>
<a href='https://dbasoumya.blogspot.com/'>
Soumya's Database Blog 
</a>
</h1>
</div>
<div class='descriptionwrapper'>
<p class='description'><span>Dive into our comprehensive blog, your go-to resource for all things related to Oracle Database, Middleware, MSSQL, MySQL, and beyond. Whether you're a seasoned database administrator, an IT professional, or a tech enthusiast, you'll find valuable insights, expert tips, and the latest updates to help you master these powerful technologies and elevate your skills.</span></p>
</div>
</div>
</div></div>
</div>
</div>
<div class='header-cap-bottom cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
</header>
<div class='tabs-outer'>
<div class='tabs-cap-top cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left tabs-fauxborder-left'>
<div class='fauxborder-right tabs-fauxborder-right'></div>
<div class='region-inner tabs-inner'>
<div class='tabs no-items section' id='crosscol' name='Cross-Column'></div>
<div class='tabs no-items section' id='crosscol-overflow' name='Cross-Column 2'></div>
</div>
</div>
<div class='tabs-cap-bottom cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
<div class='main-outer'>
<div class='main-cap-top cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left main-fauxborder-left'>
<div class='fauxborder-right main-fauxborder-right'></div>
<div class='region-inner main-inner'>
<div class='columns fauxcolumns'>
<div class='fauxcolumn-outer fauxcolumn-center-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
<div class='fauxcolumn-outer fauxcolumn-left-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
<div class='fauxcolumn-outer fauxcolumn-right-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
<!-- corrects IE6 width calculation -->
<div class='columns-inner'>
<div class='column-center-outer'>
<div class='column-center-inner'>
<div class='main section' id='main' name='Main'><div class='widget Blog' data-version='1' id='Blog1'>
<div class='blog-posts hfeed'>

          <div class="date-outer">
        
<h2 class='date-header'><span>May 25, 2026</span></h2>

          <div class="date-posts">
        
<div class='post-outer'>
<div class='post hentry uncustomized-post-template' itemprop='blogPost' itemscope='itemscope' itemtype='http://schema.org/BlogPosting'>
<meta content='https://blogger.googleusercontent.com/img/a/AVvXsEhxf3yyl-KFU9kXj_p62ZBwHtUFyeTEj_EaRNUIQZKbVSJvo1Dp_PPpvztGPCyE8q0b5WfFdknBqBsQ0BPp2c05ig_ENeCTit8HCaj8Koj5hnQ2hyLW5b3hGdw2L0PSncHtsomE9neSCnoqVK0AYO8P8ZBlFT6J9gEYsHmy0qzY2qHg_nowUvP01NBSpD0=w640-h474' itemprop='image_url'/>
<meta content='8734340484599901680' itemprop='blogId'/>
<meta content='2970540619944016535' itemprop='postId'/>
<a name='2970540619944016535'></a>
<h3 class='post-title entry-title' itemprop='name'>
Upgrading Oracle E-Business Suite R12.2 Database from 12.1.0.2 to 19c - Part IV
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-2970540619944016535' itemprop='description articleBody'>
<p><span style="background-color: white; font-size: 17.6px;">This post is continuation of the third part of the post :&nbsp;</span><span style="font-size: 17.6px;"><a href="https://dbasoumya.blogspot.com/2026/05/upgrading-oracle-e-business-suite-r122_0156654061.html">Part III</a></span></p><p><br /></p><h1><span face="Tahoma, sans-serif" style="background-color: white; font-size: 16px; font-weight: 400;">Create the CDB:</span></h1>

<p class="MsoNormal" style="background: white; line-height: normal; mso-margin-bottom-alt: auto; mso-margin-top-alt: auto;"><span face="&quot;Tahoma&quot;,sans-serif" style="color: black; font-size: 12pt; mso-fareast-font-family: &quot;Times New Roman&quot;; mso-fareast-language: EN-IN;">On the database server node:<o:p></o:p></span></p>

<ol start="1" style="margin-top: 0cm;" type="a">
 <li class="MsoNormal" style="mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;">Run
     the Database Configuration Assistant (DBCA) to create the container
     database (CDB).<o:p></o:p></li>
 <li class="MsoNormal" style="mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;">When
     prompted, click on the "Create Database", "Advanced
     Configuration", and "General Purpose or Transaction
     Processing" options.<o:p></o:p></li>
 <li class="MsoNormal" style="mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;">In
     the Specify Database Identification screen, check to create an empty
     container database (CDB) without a PDB.<o:p></o:p></li>
 <li class="MsoNormal" style="mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;">Set
     the Global Database Name, the SID to the new CDB SID (maximum of 8
     characters), and check the "Use Local Undo tablespace for PDBs"
     checkbox. The CDB SID has to be different from the current ORACLE_SID,
     which will be the PDB SID.<o:p></o:p></li>
 <li class="MsoNormal" style="mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;">In
     the "Network Configuration" section, do not create a listener.
     In the "Specify Configuration Options" section, set the SGA and
     PGA sizes to 2G and 1G respectively.<o:p></o:p></li>
 <li class="MsoNormal" style="mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;">Click
     on the Character Sets tab and choose the Character Set and National
     Character Set to be the same as in the source database. If the appropriate
     Character Set does not show up, uncheck the "Show recommended
     character sets only" box.<o:p></o:p></li>
 <li class="MsoNormal" style="mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;">In
     the "Select Database Creation Option" section, click on the
     "Customize Storage Locations" button. Set the size of the redo
     log files to be the same as in the source database. Other options can be
     configured as appropriate.<o:p></o:p></li>
 <li class="MsoNormal" style="mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;">During
     the CDB creation, ignore ORA-00313 and ORA-27037 error messages about redo
     logs in the&nbsp;alert.log&nbsp;file. These messages are informational.</li>
</ol><div><br /></div><div><br /></div><div><p class="MsoNormal">[oraprod@non-prod-db ~]$ 19cdb_env</p><p class="MsoNormal">[oraprod@non-prod-db ~]$ dbca</p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEhxf3yyl-KFU9kXj_p62ZBwHtUFyeTEj_EaRNUIQZKbVSJvo1Dp_PPpvztGPCyE8q0b5WfFdknBqBsQ0BPp2c05ig_ENeCTit8HCaj8Koj5hnQ2hyLW5b3hGdw2L0PSncHtsomE9neSCnoqVK0AYO8P8ZBlFT6J9gEYsHmy0qzY2qHg_nowUvP01NBSpD0" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="741" data-original-width="999" height="474" src="https://blogger.googleusercontent.com/img/a/AVvXsEhxf3yyl-KFU9kXj_p62ZBwHtUFyeTEj_EaRNUIQZKbVSJvo1Dp_PPpvztGPCyE8q0b5WfFdknBqBsQ0BPp2c05ig_ENeCTit8HCaj8Koj5hnQ2hyLW5b3hGdw2L0PSncHtsomE9neSCnoqVK0AYO8P8ZBlFT6J9gEYsHmy0qzY2qHg_nowUvP01NBSpD0=w640-h474" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjEGGa85_iZm_ZauR_ob6j0CeBpJcjBjWEQGtVV54NkhhdujZbKPy8Kt0wFoLyEw9QYyiPE4L348dk5XEMFvqRIasZsf-v-cPssyPEo05bGKLUfIwo2i4tWgZO9Rew0ReXJbFk64GmToX8HEHK9yB1KU9QF7TrUaXywDT3lYg7YBXRIYgdVrNFuERLNcY4" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="725" data-original-width="1074" height="432" src="https://blogger.googleusercontent.com/img/a/AVvXsEjEGGa85_iZm_ZauR_ob6j0CeBpJcjBjWEQGtVV54NkhhdujZbKPy8Kt0wFoLyEw9QYyiPE4L348dk5XEMFvqRIasZsf-v-cPssyPEo05bGKLUfIwo2i4tWgZO9Rew0ReXJbFk64GmToX8HEHK9yB1KU9QF7TrUaXywDT3lYg7YBXRIYgdVrNFuERLNcY4=w640-h432" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEgsgfkLyl4pPwC0Wxx092yc3uz8PAUK8xFywcCzqWYpz2-pdXYlAwjxdPc2Zn2bL763k5U_mZKMdy2_mpnxbxBs_R6JeI5HEayQ3TywTwVn_02kZySJQjgsbM56wSzdnkaKKdqe_Zy0sL0yg998kLUDyxuTZBd_GfNfgocR69hA_bOXW0o7V39-RlgcHXM" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="752" data-original-width="1037" height="464" src="https://blogger.googleusercontent.com/img/a/AVvXsEgsgfkLyl4pPwC0Wxx092yc3uz8PAUK8xFywcCzqWYpz2-pdXYlAwjxdPc2Zn2bL763k5U_mZKMdy2_mpnxbxBs_R6JeI5HEayQ3TywTwVn_02kZySJQjgsbM56wSzdnkaKKdqe_Zy0sL0yg998kLUDyxuTZBd_GfNfgocR69hA_bOXW0o7V39-RlgcHXM=w640-h464" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjahQiyGKcAmRRB5_cx9KGJXL4OzuhZn0d1aAd1cOFiKGoosHmim1XG1Tgx1Qaeg1cmlpHszQwayQesEzkx6MV019yVSpKsx-noCgV1xcYYOhLM0gnuNQOcrRELp5n_YKbgYdUAIsxGpdhXMrV60cuZ_j8_sTZA5kBM2THrb6b2xuM7798hQ2naJhqwaYc" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="719" data-original-width="1027" height="448" src="https://blogger.googleusercontent.com/img/a/AVvXsEjahQiyGKcAmRRB5_cx9KGJXL4OzuhZn0d1aAd1cOFiKGoosHmim1XG1Tgx1Qaeg1cmlpHszQwayQesEzkx6MV019yVSpKsx-noCgV1xcYYOhLM0gnuNQOcrRELp5n_YKbgYdUAIsxGpdhXMrV60cuZ_j8_sTZA5kBM2THrb6b2xuM7798hQ2naJhqwaYc=w640-h448" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjos_X6m0Yz4k0lCfFca6ZUFscNgJtpFWrjuU_XIk55KrOsVNsVjRcGz8rKs1yOLQ7Loo0E0L5xwZUAk8R4-EGft_VUnOd0z1aYSVSS_zVd2kdhO-NJauadPUhcct2_ANIXBQToomQkRis3wg-fm2VRNBHyxy0vY3Ph6CW-Mkhzqe7Wso3-ikppTB2PX4c" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="772" data-original-width="1024" height="483" src="https://blogger.googleusercontent.com/img/a/AVvXsEjos_X6m0Yz4k0lCfFca6ZUFscNgJtpFWrjuU_XIk55KrOsVNsVjRcGz8rKs1yOLQ7Loo0E0L5xwZUAk8R4-EGft_VUnOd0z1aYSVSS_zVd2kdhO-NJauadPUhcct2_ANIXBQToomQkRis3wg-fm2VRNBHyxy0vY3Ph6CW-Mkhzqe7Wso3-ikppTB2PX4c=w640-h483" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEiUXwFrNbrAhMGqwyN0TsGXwtsGyU4ip-C045CBxPqJiDfuj3bJh87Yos37sI8WnFsE6A1t8IC-FWwJUWVHTyxI51x_p_rlU0_rFx0n5KffCZyl_p2rrCoSd6caIbHvVaWdsQ1mrvnZVoRJjLEVUCeXE9cYj3xw_KMoKCKYN3iHj1FpKppfDkFvILpUzbM" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="764" data-original-width="1004" height="488" src="https://blogger.googleusercontent.com/img/a/AVvXsEiUXwFrNbrAhMGqwyN0TsGXwtsGyU4ip-C045CBxPqJiDfuj3bJh87Yos37sI8WnFsE6A1t8IC-FWwJUWVHTyxI51x_p_rlU0_rFx0n5KffCZyl_p2rrCoSd6caIbHvVaWdsQ1mrvnZVoRJjLEVUCeXE9cYj3xw_KMoKCKYN3iHj1FpKppfDkFvILpUzbM=w640-h488" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEiQh0De5p8iAi3F--hXQo7fZUGBoujguqxV3n6absCqk6frqMLfNqRQ0VLae--c33nr8FtQRQRbC8gCCHxFKQBgugcpBIXR25BzeAzeGzTG3aKr0jSU7nlCNeO4J2K4oDBsyTb9cyQCWqTeomMkm6FYkp1BOmTUJEEgt4IXv27TIdbihpL8G2Gu3neZ05Y" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="759" data-original-width="997" height="488" src="https://blogger.googleusercontent.com/img/a/AVvXsEiQh0De5p8iAi3F--hXQo7fZUGBoujguqxV3n6absCqk6frqMLfNqRQ0VLae--c33nr8FtQRQRbC8gCCHxFKQBgugcpBIXR25BzeAzeGzTG3aKr0jSU7nlCNeO4J2K4oDBsyTb9cyQCWqTeomMkm6FYkp1BOmTUJEEgt4IXv27TIdbihpL8G2Gu3neZ05Y=w640-h488" width="640" /></a></div><br /><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEi7CdviEFs0cq9pWTue_u5720N_49DJg3INiXT2t_5DG9ZUktQNH9mgrvg8RIXh7Kx8hljZ_7qhlWO8yQQbHxcnkEu1gkrvBZ1lTgQMri5DYcoCRAU2ExXdhCM2yV6di5H-9k_DiNC34eDB-_HW9diSQyEUj4jmSX2Pu8q4RoyLby_ZyUFydOtV81xqt64" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="777" data-original-width="1030" height="483" src="https://blogger.googleusercontent.com/img/a/AVvXsEi7CdviEFs0cq9pWTue_u5720N_49DJg3INiXT2t_5DG9ZUktQNH9mgrvg8RIXh7Kx8hljZ_7qhlWO8yQQbHxcnkEu1gkrvBZ1lTgQMri5DYcoCRAU2ExXdhCM2yV6di5H-9k_DiNC34eDB-_HW9diSQyEUj4jmSX2Pu8q4RoyLby_ZyUFydOtV81xqt64=w640-h483" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEh6ARPEVuCrTxOwWkA8IsMZSWsU7m39EOWgv9qSyxyY1lovmm7AaZudXpfndBVr2X8HMX3jXLkUtRywRRDHe4UtzYLAUjOJ_UdtkCnurRwccoQLV2_v3mppWYTXW78iM8bGRKWv7EUKecMsha1KFTWgNCSBVjQHZB3sa4lLSIbUaeWeLXaRRGBmgPa2BlU" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="770" data-original-width="1012" height="488" src="https://blogger.googleusercontent.com/img/a/AVvXsEh6ARPEVuCrTxOwWkA8IsMZSWsU7m39EOWgv9qSyxyY1lovmm7AaZudXpfndBVr2X8HMX3jXLkUtRywRRDHe4UtzYLAUjOJ_UdtkCnurRwccoQLV2_v3mppWYTXW78iM8bGRKWv7EUKecMsha1KFTWgNCSBVjQHZB3sa4lLSIbUaeWeLXaRRGBmgPa2BlU=w640-h488" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEiE53Xdigyssz39PbrbN21hfjgwVL0mqI4vHzOgdshYedkrcuqRZ6osiJXvOvMTkxdbS7ykG0BWXJm9RuqXpXFukXUXcDwRmvPUYsklgm_G80B_f_xQfeeqgIM3YG55lXf-ipmLFSQfvOb0bM9Y97YRi_PWlombvDMthF0MQGTqvG6PD8IkW1xzddRSZGo" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="758" data-original-width="964" height="504" src="https://blogger.googleusercontent.com/img/a/AVvXsEiE53Xdigyssz39PbrbN21hfjgwVL0mqI4vHzOgdshYedkrcuqRZ6osiJXvOvMTkxdbS7ykG0BWXJm9RuqXpXFukXUXcDwRmvPUYsklgm_G80B_f_xQfeeqgIM3YG55lXf-ipmLFSQfvOb0bM9Y97YRi_PWlombvDMthF0MQGTqvG6PD8IkW1xzddRSZGo=w640-h504" width="640" /></a></div><div class="separator" style="clear: both; text-align: left;"><p class="MsoNormal">Note:- Select Database character set and national character
set same as source database.<o:p></o:p></p>

<p class="MsoNormal">NLS_CHARACTERSET&nbsp; :
UTF8<o:p></o:p></p>

<p class="MsoNormal">NLS_NCHAR_CHARACTERSET : AL16UTF16<o:p></o:p></p></div><br /></div><div class="separator" style="clear: both; text-align: left;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEgP5o2dvlTPgxzpSB11cudKl9TJvMMm8xhULkcWgs-whqLh8dC7U6BdJ2MJZaV0EVifTl1vd25DSEwTo7moqQ6cq_vhkg_wN5XCFomK9-NbsSr5oBf9vy6LyXstn29SwvOeSkX70FttXv_GC7Uimf1OmH4gLfY68wws-UHA5BJantXxqO3Fb2RhJTl2Ij8" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="708" data-original-width="933" height="486" src="https://blogger.googleusercontent.com/img/a/AVvXsEgP5o2dvlTPgxzpSB11cudKl9TJvMMm8xhULkcWgs-whqLh8dC7U6BdJ2MJZaV0EVifTl1vd25DSEwTo7moqQ6cq_vhkg_wN5XCFomK9-NbsSr5oBf9vy6LyXstn29SwvOeSkX70FttXv_GC7Uimf1OmH4gLfY68wws-UHA5BJantXxqO3Fb2RhJTl2Ij8=w640-h486" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEgrQS3yuwJJvSvO8AHR4DYUsmnuET5L9FyiERNHDaJeBV1UHjjnfM6g_6Pv1gQ8qsm4Rndos1pxsgflLOVdURYDxVK422SoEZrvvTXnvnzP4iRIg3Fd3ofYw7jA10L70LtKGxeP78vUgcuF0BdzYnEplfAZBBuYitIGhzXd1IrhdO2VcjfWNkC50CEpLcE" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="647" data-original-width="967" height="428" src="https://blogger.googleusercontent.com/img/a/AVvXsEgrQS3yuwJJvSvO8AHR4DYUsmnuET5L9FyiERNHDaJeBV1UHjjnfM6g_6Pv1gQ8qsm4Rndos1pxsgflLOVdURYDxVK422SoEZrvvTXnvnzP4iRIg3Fd3ofYw7jA10L70LtKGxeP78vUgcuF0BdzYnEplfAZBBuYitIGhzXd1IrhdO2VcjfWNkC50CEpLcE=w640-h428" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjSau8nQ4597owvWt6k_Vtzok-MmFdX9T_s8B9VbdBfv0yAmW7gubtWDHuXXXSnXJeFgwrLo4-sUmSi6Da09OrWO0dAnLJnPUpvO6gEE2lLPyhQU6ehkIN4JPFO8iJIgq3N3JV1Xg-ULvzOy2KvfIdLv_8uIQiRuJV0ykN5CNZoyOEGEv3fKGwrD-2_Y4s" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="712" data-original-width="966" height="472" src="https://blogger.googleusercontent.com/img/a/AVvXsEjSau8nQ4597owvWt6k_Vtzok-MmFdX9T_s8B9VbdBfv0yAmW7gubtWDHuXXXSnXJeFgwrLo4-sUmSi6Da09OrWO0dAnLJnPUpvO6gEE2lLPyhQU6ehkIN4JPFO8iJIgq3N3JV1Xg-ULvzOy2KvfIdLv_8uIQiRuJV0ykN5CNZoyOEGEv3fKGwrD-2_Y4s=w640-h472" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><p class="MsoNormal" style="text-align: left;">Here we added 1 more redolog group and 1 member for each
group and redolog size should be same source database.<o:p></o:p></p><p class="MsoNormal" style="text-align: left;"></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEj0EhFoiNHehEecN1WtdUpoqk-y7VLuGl9BpeCMTNlgo_WTyEKF-TpVlLVPAomQBP1wA5-1JT0uUABmpCXTX0TaIj6VSe0D8oy16VPx9HXVyvqdjZOZFvOjWjafd70V10Aq4Dd6LP_8a1UcZDgzrAjB1IeK1CZj-WxHCxlvCdAZ_7DZP1m8jWXKFzaplXg" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="745" data-original-width="971" height="491" src="https://blogger.googleusercontent.com/img/a/AVvXsEj0EhFoiNHehEecN1WtdUpoqk-y7VLuGl9BpeCMTNlgo_WTyEKF-TpVlLVPAomQBP1wA5-1JT0uUABmpCXTX0TaIj6VSe0D8oy16VPx9HXVyvqdjZOZFvOjWjafd70V10Aq4Dd6LP_8a1UcZDgzrAjB1IeK1CZj-WxHCxlvCdAZ_7DZP1m8jWXKFzaplXg=w640-h491" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjUcj9vRze853Ra_uxOXumPo4A6uwCWimoZqKbSHHK8po1dlEo4H2zVloSL-de02oGH2O4TtnGILAnBg1heDiamWp63amvub8X65LwiC1yrWDGNHan5SS70fo2EuaqrORL5e6sQo7lPIXtin_UASrcM3JqrdPRq_eiWEdu8N7uy8R2OyYDtD54DWj-ntO0" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="735" data-original-width="972" height="485" src="https://blogger.googleusercontent.com/img/a/AVvXsEjUcj9vRze853Ra_uxOXumPo4A6uwCWimoZqKbSHHK8po1dlEo4H2zVloSL-de02oGH2O4TtnGILAnBg1heDiamWp63amvub8X65LwiC1yrWDGNHan5SS70fo2EuaqrORL5e6sQo7lPIXtin_UASrcM3JqrdPRq_eiWEdu8N7uy8R2OyYDtD54DWj-ntO0=w640-h485" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjX6H2P712MFxanwCmwcrvUMY8EmlSthwPBKgaIQZVsiyzqf3tkDuRsrk19CldXU3vKb7DWMpMqFoJxvajMrSGOWJr11lXCYWyiIus5t5RH7rBNl6NYknDDNmJIT-EpVudU6rUaX5Xc7yz8VetcOqj5Uzojg48qVdoeQMv9GINQwNFncgV-VRgTa9QaqJ4" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="679" data-original-width="912" height="476" src="https://blogger.googleusercontent.com/img/a/AVvXsEjX6H2P712MFxanwCmwcrvUMY8EmlSthwPBKgaIQZVsiyzqf3tkDuRsrk19CldXU3vKb7DWMpMqFoJxvajMrSGOWJr11lXCYWyiIus5t5RH7rBNl6NYknDDNmJIT-EpVudU6rUaX5Xc7yz8VetcOqj5Uzojg48qVdoeQMv9GINQwNFncgV-VRgTa9QaqJ4=w640-h476" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEgiKjvm35vNED6i0ZHisxxMgnjP1HwW6sPwII7ONKNvyX20jf5MzRQ8H5IyoemEdvh2F2cMxekpad-Nrm2RLu-NI6AlB6d2bC15j5zGNg-JDZLxKzPGs3OjHguGLLMHhrsA8gLCCUWARdg3Z-e_aqcwxXXIn7KFZqUZuYfHMMwe8xLMYrPYhaaaHKY7lgo" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="613" data-original-width="825" height="476" src="https://blogger.googleusercontent.com/img/a/AVvXsEgiKjvm35vNED6i0ZHisxxMgnjP1HwW6sPwII7ONKNvyX20jf5MzRQ8H5IyoemEdvh2F2cMxekpad-Nrm2RLu-NI6AlB6d2bC15j5zGNg-JDZLxKzPGs3OjHguGLLMHhrsA8gLCCUWARdg3Z-e_aqcwxXXIn7KFZqUZuYfHMMwe8xLMYrPYhaaaHKY7lgo=w640-h476" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: left;"><span style="background-color: white; font-size: large;">Run
datapatch on CDB</span></div></div></div></div><p></p><div class="separator" style="clear: both;"><div class="separator" style="clear: both;"><div class="separator" style="clear: both;"><div class="separator" style="clear: both; text-align: left;">

<p class="MsoNormal" style="background: white;