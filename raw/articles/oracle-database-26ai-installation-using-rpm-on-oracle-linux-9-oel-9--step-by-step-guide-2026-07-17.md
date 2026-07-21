---
source_url: https://dbasoumya.blogspot.com/2026/06/oracle-database-26ai-installation-using.html
ingested: 2026-07-17
sha256: 819a5e46832819544cfcb21939caf34b5a75ea6dc8c88dd894f9e5b80952c97f
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
<link href='https://dbasoumya.blogspot.com/2026/06/oracle-database-26ai-installation-using.html' rel='canonical'/>
<link rel="alternate" type="application/atom+xml" title="Soumya&#39;s Database Blog  - Atom" href="https://dbasoumya.blogspot.com/feeds/posts/default" />
<link rel="alternate" type="application/rss+xml" title="Soumya&#39;s Database Blog  - RSS" href="https://dbasoumya.blogspot.com/feeds/posts/default?alt=rss" />
<link rel="service.post" type="application/atom+xml" title="Soumya&#39;s Database Blog  - Atom" href="https://draft.blogger.com/feeds/8734340484599901680/posts/default" />

<link rel="alternate" type="application/atom+xml" title="Soumya&#39;s Database Blog  - Atom" href="https://dbasoumya.blogspot.com/feeds/647880263112608079/comments/default" />
<!--Can't find substitution for tag [blog.ieCssRetrofitLinks]-->
<link href='https://blogger.googleusercontent.com/img/a/AVvXsEigkYam4dHomeAB5rM_HPX0zT9Ccpdst1eLhE3J_VV8Qjip_3dJTpct3uNApzRjJD3GP-dOaYAiu_xRLUuPi8I_Bt5hezEs_GDxKax0aTMOkKuIswZcaciY9tzHsBml2GzafhM1ijKP5wvH01WdSjhoHLQVpzjtgEv9QyE4IW9kqfYDhfIFfVSuLkXJMsc=w640-h430' rel='image_src'/>
<meta content='https://dbasoumya.blogspot.com/2026/06/oracle-database-26ai-installation-using.html' property='og:url'/>
<meta content='Oracle Database 26ai Installation Using RPM on Oracle Linux 9 (OEL 9) – Step-by-Step Guide' property='og:title'/>
<meta content='Find a solution for different databases such as Oracle, MSSQL,Mysql techniques and stay updated with new technologies related to them' property='og:description'/>
<meta content='https://blogger.googleusercontent.com/img/a/AVvXsEigkYam4dHomeAB5rM_HPX0zT9Ccpdst1eLhE3J_VV8Qjip_3dJTpct3uNApzRjJD3GP-dOaYAiu_xRLUuPi8I_Bt5hezEs_GDxKax0aTMOkKuIswZcaciY9tzHsBml2GzafhM1ijKP5wvH01WdSjhoHLQVpzjtgEv9QyE4IW9kqfYDhfIFfVSuLkXJMsc=w1200-h630-p-k-no-nu' property='og:image'/>
<title>Soumya's Database Blog : Oracle Database 26ai Installation Using RPM on Oracle Linux 9 (OEL 9) &#8211; Step-by-Step Guide</title>
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
              url: 'https://draft.blogger.com/navbar/8734340484599901680?po\x3d647880263112608079\x26origin\x3dhttps://dbasoumya.blogspot.com',
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
        
<h2 class='date-header'><span>June 6, 2026</span></h2>

          <div class="date-posts">
        
<div class='post-outer'>
<div class='post hentry uncustomized-post-template' itemprop='blogPost' itemscope='itemscope' itemtype='http://schema.org/BlogPosting'>
<meta content='https://blogger.googleusercontent.com/img/a/AVvXsEigkYam4dHomeAB5rM_HPX0zT9Ccpdst1eLhE3J_VV8Qjip_3dJTpct3uNApzRjJD3GP-dOaYAiu_xRLUuPi8I_Bt5hezEs_GDxKax0aTMOkKuIswZcaciY9tzHsBml2GzafhM1ijKP5wvH01WdSjhoHLQVpzjtgEv9QyE4IW9kqfYDhfIFfVSuLkXJMsc=w640-h430' itemprop='image_url'/>
<meta content='8734340484599901680' itemprop='blogId'/>
<meta content='647880263112608079' itemprop='postId'/>
<a name='647880263112608079'></a>
<h3 class='post-title entry-title' itemprop='name'>
Oracle Database 26ai Installation Using RPM on Oracle Linux 9 (OEL 9) &#8211; Step-by-Step Guide
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-647880263112608079' itemprop='description articleBody'>
<p>&nbsp;</p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEigkYam4dHomeAB5rM_HPX0zT9Ccpdst1eLhE3J_VV8Qjip_3dJTpct3uNApzRjJD3GP-dOaYAiu_xRLUuPi8I_Bt5hezEs_GDxKax0aTMOkKuIswZcaciY9tzHsBml2GzafhM1ijKP5wvH01WdSjhoHLQVpzjtgEv9QyE4IW9kqfYDhfIFfVSuLkXJMsc" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="746" data-original-width="1112" height="430" src="https://blogger.googleusercontent.com/img/a/AVvXsEigkYam4dHomeAB5rM_HPX0zT9Ccpdst1eLhE3J_VV8Qjip_3dJTpct3uNApzRjJD3GP-dOaYAiu_xRLUuPi8I_Bt5hezEs_GDxKax0aTMOkKuIswZcaciY9tzHsBml2GzafhM1ijKP5wvH01WdSjhoHLQVpzjtgEv9QyE4IW9kqfYDhfIFfVSuLkXJMsc=w640-h430" width="640" /></a></div><br /><p></p><p class="MsoNormal">In this post I will describe the installation of Oracle
Database 26ai 64-bit on Oracle Linux 9 (OL8) 64-bit. The installation requires
a minimum of 2g swap memory and secure Linux set to permissive or disabled.<o:p></o:p></p><p class="MsoNormal"></p><p class="MsoNormal">Add hosts entry in hosts file<o:p></o:p></p><br /><p></p><p class="MsoNormal"></p><div style="border: 1pt solid windowtext; mso-border-alt: solid windowtext .5pt; mso-element: para-border-div; padding: 1pt 4pt;">

<p class="MsoNormal" style="border-color: currentcolor; border-image: initial; border-style: none; border-width: medium; border: none; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 1.0pt 4.0pt 1.0pt 4.0pt; padding: 0cm;">[root@dbvm-1 opc]# cat
/etc/hosts<o:p></o:p></p>

<p class="MsoNormal" style="border-color: currentcolor; border-image: initial; border-style: none; border-width: medium; border: none; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 1.0pt 4.0pt 1.0pt 4.0pt; padding: 0cm;">127.0.0.1<span style="mso-spacerun: yes;">&nbsp;&nbsp; </span>localhost localhost.localdomain localhost4
localhost4.localdomain4<o:p></o:p></p>

<p class="MsoNormal" style="border-color: currentcolor; border-image: initial; border-style: none; border-width: medium; border: none; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 1.0pt 4.0pt 1.0pt 4.0pt; padding: 0cm;">::1<span style="mso-spacerun: yes;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>localhost localhost.localdomain
localhost6 localhost6.localdomain6<o:p></o:p></p>

<p class="MsoNormal" style="border-color: currentcolor; border-image: initial; border-style: none; border-width: medium; border: none; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 1.0pt 4.0pt 1.0pt 4.0pt; padding: 0cm;">10.0.0.45
dbvm-1.subnet09221504.vcn09221504.oraclevcn.com dbvm-1<o:p></o:p></p>

</div><br /><p></p><p class="MsoNormal"></p><p class="MsoNormal"><span lang="EN-US" style="mso-ansi-language: EN-US;">Download
the RPM for oracle installation:-<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="mso-ansi-language: EN-US;">The
required rpm can be downloaded directly from oracle website <o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="mso-ansi-language: EN-US;"><a href="https://www.oracle.com/database/free/get-started/">https://www.oracle.com/database/free/get-started/</a><o:p></o:p></span></p><br /><p></p><p class="MsoNormal"></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEim3jWAnPEZPILB5IVGTgd73dhwXODRUGM1Jgde3VawGCZb7PT8TWBCs-Iur5xdJ9FRqNseY12Adzbd6T7V_MVNYlG2nipcWtDEY4Ry3dp5WwxJNllbZSvnZeCDyLQjUWQI-U6vjiZQCsGemodL3So2mOqZsVMKq-_l4UaG2B8FTEEyuWgrWQQh89IUZl8" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="399" data-original-width="965" height="264" src="https://blogger.googleusercontent.com/img/a/AVvXsEim3jWAnPEZPILB5IVGTgd73dhwXODRUGM1Jgde3VawGCZb7PT8TWBCs-Iur5xdJ9FRqNseY12Adzbd6T7V_MVNYlG2nipcWtDEY4Ry3dp5WwxJNllbZSvnZeCDyLQjUWQI-U6vjiZQCsGemodL3So2mOqZsVMKq-_l4UaG2B8FTEEyuWgrWQQh89IUZl8=w640-h264" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><p></p><p class="MsoNormal">Rpm url : <a href="https://yum.oracle.com/repo/OracleLinux/OL9/appstream/aarch64/getPackage/oracle-ai-database-preinstall-26ai-1.0-2.el9.aarch64.rpm">oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64.rpm</a><span lang="EN-US"><o:p></o:p></span></p><div class="separator" style="clear: both; text-align: center;">

<p class="MsoNormal" style="text-align: left;"><span lang="EN-US">Download
the rpm as root user<o:p></o:p></span></p>

<table border="1" cellpadding="0" cellspacing="0" class="MsoTableGrid" style="border-collapse: collapse; border-color: currentcolor; border-image: initial; border-style: none; border-width: medium; border: none; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-yfti-tbllook: 1184;">
 <tbody><tr>
  <td style="border: 1pt solid windowtext; mso-border-alt: solid windowtext .5pt; padding: 0cm 5.4pt; width: 450.8pt;" valign="top" width="601">
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">[root@dbvm-1 opc]# wget </span>https://yum.oracle.com/repo/OracleLinux/OL9/appstream/x86_64/getPackage/oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64.rpm<span lang="EN-US"><o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;</span></p>
  </td>
 </tr>
</tbody></table></div><p class="MsoNormal"><br /></p><table border="1" cellpadding="0" cellspacing="0" class="MsoTableGrid" style="border-collapse: collapse; border-color: currentcolor; border-image: initial; border-style: none; border-width: medium; border: none; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-yfti-tbllook: 1184;">
 <tbody><tr>
  <td style="border: 1pt solid windowtext; mso-border-alt: solid windowtext .5pt; padding: 0cm 5.4pt; width: 450.8pt;" valign="top" width="601">
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">[root@dbvm-1 opc]# <b>dnf install
  -y oracle-ai-database-preinstall-26ai</b><o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;</span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Last metadata expiration check:
  0:04:32 ago on Sat 06 Jun 2026 06:11:34 AM GMT.<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Dependencies resolved.<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">==============================================================================================================================================================================================<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;Package&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Architecture&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Version&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Repository&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Size<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">==============================================================================================================================================================================================<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Installing:<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;oracle-ai-database-preinstall-26ai&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x86_64&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.0-1.el9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  ol9_appstream&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 34 k<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;</span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Transaction Summary<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">==============================================================================================================================================================================================<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Install&nbsp; 1 Package<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;</span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Total download size: 34 k<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Installed size: 81 k<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Downloading Packages:<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64.rpm&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  416 kB/s |&nbsp; 34 kB&nbsp;&nbsp;&nbsp;&nbsp; 00:00<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Total&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  407 kB/s |&nbsp; 34 kB&nbsp;&nbsp;&nbsp;&nbsp; 00:00<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Running transaction check<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Transaction check succeeded.<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Running transaction test<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Transaction test succeeded.<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Running transaction<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;
  Preparing&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  1/1<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;
  Installing&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :
  oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  1/1<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;
  Running scriptlet:
  oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  1/1<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;
  Verifying&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :
  oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  1/1<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;</span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Installed:<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;
  oracle-ai-database-preinstall-26ai-1.0-1.el9.x86_64<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;</span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Complete! [root@dbvm-1 opc]# <b>dnf
  install -y oracle-ai-database-preinstall-26ai</b><o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;</span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Last metadata expiration check:
  0:04:32 ago on Sat 06 Jun 2026 06:11:34 AM GMT.<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">Dependencies resolved.<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">==============================================================================================================================================================================================<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">&nbsp;Package&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Architecture&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Version&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Repository&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Size<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;"><span lang="EN-US">======================================================================================================================================================================================