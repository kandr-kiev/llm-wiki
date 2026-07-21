---
source_url: https://dbasoumya.blogspot.com/2026/05/changing-oracle-applications-user.html
ingested: 2026-07-17
sha256: 0bc5c5f22e03cd6a667b928406a2f61723c8627bfef64ab8e5193a5d9c055161
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
<link href='https://dbasoumya.blogspot.com/2026/05/changing-oracle-applications-user.html' rel='canonical'/>
<link rel="alternate" type="application/atom+xml" title="Soumya&#39;s Database Blog  - Atom" href="https://dbasoumya.blogspot.com/feeds/posts/default" />
<link rel="alternate" type="application/rss+xml" title="Soumya&#39;s Database Blog  - RSS" href="https://dbasoumya.blogspot.com/feeds/posts/default?alt=rss" />
<link rel="service.post" type="application/atom+xml" title="Soumya&#39;s Database Blog  - Atom" href="https://draft.blogger.com/feeds/8734340484599901680/posts/default" />

<link rel="alternate" type="application/atom+xml" title="Soumya&#39;s Database Blog  - Atom" href="https://dbasoumya.blogspot.com/feeds/4282862174590727151/comments/default" />
<!--Can't find substitution for tag [blog.ieCssRetrofitLinks]-->
<link href='https://blogger.googleusercontent.com/img/a/AVvXsEhFojtfW_Ja7tpuchJ0YnhHcBwHY37eHr04v3RuXKQeeKwEozEOtMedwRh2guSz1IFjXQnl5VvY87SpaBIa9Bct-YT4iuW3rLC0K4-Huj2RXkSaGvbrWiE2tUhvlLJELOn6jKJzfJlEIYCu-LoHxdfyFuWubB1oWmwZ3s4Z5vXoPC8_tlEXlJFHX0m5L2U=w640-h342' rel='image_src'/>
<meta content='https://dbasoumya.blogspot.com/2026/05/changing-oracle-applications-user.html' property='og:url'/>
<meta content='Changing Oracle Applications User Password Using FNDCPASS – Step-by-Step Guide' property='og:title'/>
<meta content='Find a solution for different databases such as Oracle, MSSQL,Mysql techniques and stay updated with new technologies related to them' property='og:description'/>
<meta content='https://blogger.googleusercontent.com/img/a/AVvXsEhFojtfW_Ja7tpuchJ0YnhHcBwHY37eHr04v3RuXKQeeKwEozEOtMedwRh2guSz1IFjXQnl5VvY87SpaBIa9Bct-YT4iuW3rLC0K4-Huj2RXkSaGvbrWiE2tUhvlLJELOn6jKJzfJlEIYCu-LoHxdfyFuWubB1oWmwZ3s4Z5vXoPC8_tlEXlJFHX0m5L2U=w1200-h630-p-k-no-nu' property='og:image'/>
<title>Soumya's Database Blog : Changing Oracle Applications User Password Using FNDCPASS &#8211; Step-by-Step Guide</title>
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
              url: 'https://draft.blogger.com/navbar/8734340484599901680?po\x3d4282862174590727151\x26origin\x3dhttps://dbasoumya.blogspot.com',
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
        
<h2 class='date-header'><span>May 23, 2026</span></h2>

          <div class="date-posts">
        
<div class='post-outer'>
<div class='post hentry uncustomized-post-template' itemprop='blogPost' itemscope='itemscope' itemtype='http://schema.org/BlogPosting'>
<meta content='https://blogger.googleusercontent.com/img/a/AVvXsEhFojtfW_Ja7tpuchJ0YnhHcBwHY37eHr04v3RuXKQeeKwEozEOtMedwRh2guSz1IFjXQnl5VvY87SpaBIa9Bct-YT4iuW3rLC0K4-Huj2RXkSaGvbrWiE2tUhvlLJELOn6jKJzfJlEIYCu-LoHxdfyFuWubB1oWmwZ3s4Z5vXoPC8_tlEXlJFHX0m5L2U=w640-h342' itemprop='image_url'/>
<meta content='8734340484599901680' itemprop='blogId'/>
<meta content='4282862174590727151' itemprop='postId'/>
<a name='4282862174590727151'></a>
<h3 class='post-title entry-title' itemprop='name'>
Changing Oracle Applications User Password Using FNDCPASS &#8211; Step-by-Step Guide
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-4282862174590727151' itemprop='description articleBody'>
<p></p><p class="MsoNormal">As an oracle apps dba , we often need to reset password for
apps user in E-Business suite . FNDCPASS is an Oracle E-Business Suite utility
used to change application user passwords, Oracle schema passwords, and
APPS/APPLSYS passwords while keeping Oracle EBS metadata synchronized.<span style="mso-tab-count: 1;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><o:p></o:p></p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal">Steps to change:-<o:p></o:p></p>

<p class="MsoListParagraphCxSpFirst" style="mso-list: l0 level1 lfo1; text-indent: -18.0pt;"><!--[if !supportLists]--><span style="mso-bidi-font-family: Aptos; mso-bidi-theme-font: minor-latin;"><span style="mso-list: Ignore;">1.<span style="font: 7.0pt &quot;Times New Roman&quot;;">&nbsp; &nbsp; &nbsp; </span></span></span>First ensure application is not running or shutdown
application by<o:p></o:p></p>

<p class="MsoListParagraphCxSpLast">Invoke application environment from run file
system<o:p></o:p></p><br /><p></p><p><table border="1" cellpadding="0" cellspacing="0" class="MsoTableGrid" style="border-collapse: collapse; border: none; margin-left: 36.0pt; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-yfti-tbllook: 1184;">
 <tbody><tr style="mso-yfti-firstrow: yes; mso-yfti-irow: 0; mso-yfti-lastrow: yes;">
  <td style="border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 450.8pt;" valign="top" width="601">
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;">[oracle@ebstest
  VIS]$ cd /u01/oracle/VIS/fs1/EBSapps/appl<o:p></o:p></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;">[oracle@ebstest
  VIS]$ . APPSVIS_ebstest.env<o:p></o:p></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;">[oracle@ebstest
  sql]$ cd $ADMIN_SCRIPTS_HOME<o:p></o:p></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm;">[oracle@ebstest
  sql]$ <span style="mso-spacerun: yes;">&nbsp;</span>./adstpall.sh <o:p></o:p></p>
  </td>
 </tr>
</tbody></table><br /></p><p><br /></p><p></p><p class="MsoListParagraph" style="mso-list: l0 level1 lfo1; text-indent: -18.0pt;"><!--[if !supportLists]--><span style="mso-bidi-font-family: Aptos; mso-bidi-theme-font: minor-latin;"><span style="mso-list: Ignore;">1.<span style="font: 7.0pt &quot;Times New Roman&quot;;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]-->Change the APPLSYS password using<o:p></o:p></p><table border="1" cellpadding="0" cellspacing="0" class="MsoTableGrid" style="border-collapse: collapse; border: none; margin-left: 36.0pt; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-yfti-tbllook: 1184;">
 <tbody><tr style="mso-yfti-firstrow: yes; mso-yfti-irow: 0; mso-yfti-lastrow: yes;">
  <td style="border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 414.8pt;" valign="top" width="553">
  <p class="MsoListParagraphCxSpFirst" style="line-height: normal; margin: 0cm; mso-add-space: auto;"><span style="color: black; font-family: &quot;Figtree-Regular&quot;,serif; font-size: 13.0pt;">Syntax:- FNDCPASS apps/&lt;appspwd&gt; 0 Y
  system/&lt;system_manager&gt; SYSTEM APPLSYS &lt;new_apps_passwd&gt;<o:p></o:p></span></p>
  <p class="MsoListParagraphCxSpMiddle" style="line-height: normal; margin: 0cm; mso-add-space: auto;"><span style="color: black; font-family: &quot;Figtree-Regular&quot;,serif; font-size: 13.0pt;"><o:p>&nbsp;</o:p></span></p>
  <p class="MsoListParagraphCxSpMiddle" style="line-height: normal; margin: 0cm; mso-add-space: auto;">[oracle@ebstest sql]$ <span style="mso-spacerun: yes;">&nbsp;</span><span style="color: black; font-family: &quot;Figtree-Regular&quot;,serif; font-size: 13.0pt;">FNDCPASS apps/apps 0 Y system/manager SYSTEM
  APPLSYS apps123#<o:p></o:p></span></p>
  <p class="MsoListParagraphCxSpLast" style="line-height: normal; margin: 0cm; mso-add-space: auto;"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
</tbody></table><br /><p></p><p><br /></p><p></p><p class="MsoListParagraph" style="mso-list: l0 level1 lfo1; text-indent: -18.0pt;"><!--[if !supportLists]--><span style="mso-bidi-font-family: Aptos; mso-bidi-theme-font: minor-latin;"><span style="mso-list: Ignore;">1.<span style="font: 7.0pt &quot;Times New Roman&quot;;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]-->Run autoconfig on appstier<o:p></o:p></p><table border="1" cellpadding="0" cellspacing="0" class="MsoTableGrid" style="border-collapse: collapse; border: none; margin-left: 36.0pt; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-yfti-tbllook: 1184;">
 <tbody><tr style="mso-yfti-firstrow: yes; mso-yfti-irow: 0; mso-yfti-lastrow: yes;">
  <td style="border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 450.8pt;" valign="top" width="601">
  <p class="MsoNormal" style="background: white; line-height: normal; margin-bottom: 0cm; margin-left: 18.0pt; mso-margin-top-alt: auto;"><span style="color: black; font-family: &quot;Times New Roman&quot;,serif; font-size: 13.0pt; mso-fareast-font-family: &quot;Times New Roman&quot;; mso-fareast-language: EN-IN; mso-font-kerning: 0pt; mso-ligatures: none;">[oracle@ebstest VIS]$ cd
  /u01/oracle/VIS/fs1/EBSapps/appl<o:p></o:p></span></p>
  <p class="MsoNormal" style="background: white; line-height: normal; margin-bottom: 0cm; margin-left: 18.0pt; mso-margin-top-alt: auto;"><span style="color: black; font-family: &quot;Times New Roman&quot;,serif; font-size: 13.0pt; mso-fareast-font-family: &quot;Times New Roman&quot;; mso-fareast-language: EN-IN; mso-font-kerning: 0pt; mso-ligatures: none;">[oracle@ebstest VIS]$ . APPSVIS_ebstest.env<o:p></o:p></span></p>
  <p class="MsoNormal" style="background: white; line-height: normal; margin-bottom: 0cm; margin-left: 18.0pt; mso-margin-top-alt: auto;"><span style="color: black; font-family: &quot;Times New Roman&quot;,serif; font-size: 13.0pt; mso-fareast-font-family: &quot;Times New Roman&quot;; mso-fareast-language: EN-IN; mso-font-kerning: 0pt; mso-ligatures: none;">[oracle@ebstest scripts]$ cd $ADMIN_SCRIPTS_HOME<o:p></o:p></span></p>
  <p class="MsoNormal" style="background: white; line-height: normal; margin-bottom: 0cm; margin-left: 18.0pt; mso-margin-top-alt: auto;"><span style="color: black; font-family: &quot;Times New Roman&quot;,serif; font-size: 13.0pt; mso-fareast-font-family: &quot;Times New Roman&quot;; mso-fareast-language: EN-IN; mso-font-kerning: 0pt; mso-ligatures: none;">[oracle@ebstest scripts]$ adautocfg.sh<o:p></o:p></span></p>
  <p class="MsoNormal" style="background: white; line-height: normal; margin-bottom: 0cm; margin-left: 18.0pt; mso-margin-top-alt: auto;"><span style="color: black; font-family: &quot;Times New Roman&quot;,serif; font-size: 13.0pt; mso-fareast-font-family: &quot;Times New Roman&quot;; mso-fareast-language: EN-IN; mso-font-kerning: 0pt; mso-ligatures: none;">&#8230;&#8230;<o:p></o:p></span></p>
  <p class="MsoNormal" style="background: white; line-height: normal; margin-bottom: 0cm; margin-left: 18.0pt; mso-margin-top-alt: auto;"><span style="color: black; font-family: &quot;Times New Roman&quot;,serif; font-size: 13.0pt; mso-fareast-font-family: &quot;Times New Roman&quot;; mso-fareast-language: EN-IN; mso-font-kerning: 0pt; mso-ligatures: none;">&#8230;&#8230;<o:p></o:p></span></p>
  <p class="MsoNormal" style="background: white; line-height: normal; margin-bottom: 0cm; margin-left: 18.0pt; mso-margin-top-alt: auto;"><span style="color: black; font-family: &quot;Times New Roman&quot;,serif; font-size: 13.0pt; mso-fareast-font-family: &quot;Times New Roman&quot;; mso-fareast-language: EN-IN; mso-font-kerning: 0pt; mso-ligatures: none;">AutoConfig completed successfully<o:p></o:p></span></p>
  <p class="MsoNormal" style="line-height: normal; margin-bottom: 0cm; margin-left: 18.0pt; margin-right: 0cm; margin-top: 0cm;"><o:p>&nbsp;</o:p></p>
  </td>
 </tr>
</tbody></table><br /><p></p><p><br /></p><p></p><p class="MsoListParagraph" style="mso-list: l0 level1 lfo1; text-indent: -18.0pt;"><!--[if !supportLists]--><span style="mso-bidi-font-family: Aptos; mso-bidi-theme-font: minor-latin;"><span style="mso-list: Ignore;">1.<span style="font: 7.0pt &quot;Times New Roman&quot;;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]-->Now start weblogic admin server using following
script<o:p></o:p></p><table border="0" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="background: white; border-collapse: collapse; margin-left: 20.8pt; mso-padding-alt: 0cm 0cm 0cm 0cm; mso-yfti-tbllook: 1184;">
 <tbody><tr style="mso-yfti-firstrow: yes; mso-yfti-irow: 0; mso-yfti-lastrow: yes;">
  <td style="border: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 429.5pt;" valign="top" width="573">
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">[oracle@ebstest
  scripts]$ pwd</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">/u01/oracle/VIS/fs1/inst/apps/VIS_ebstest/admin/scripts&nbsp;</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">[oracle@ebstest
  scripts]$ sh adadminsrvctl.sh start</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">You are
  running adadminsrvctl.sh version 120.10.12020000.2</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">&nbsp;Enter
  the WebLogic Admin password:</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">Enter
  the APPS Schema password:</span><o:p></o:p></p>
  <p class="MsoListParagraph"><span style="color: black; mso-color-alt: windowtext;">&nbsp;</span><o:p></o:p></p>
  </td>
 </tr>
</tbody></table><br /><p></p><p><span style="font-family: &quot;Aptos&quot;,sans-serif; font-size: 12.0pt; line-height: 115%; mso-ansi-language: EN-IN; mso-ascii-theme-font: minor-latin; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-language: AR-SA; mso-bidi-theme-font: minor-bidi; mso-fareast-font-family: Aptos; mso-fareast-language: EN-US; mso-fareast-theme-font: minor-latin; mso-hansi-theme-font: minor-latin;">Confirm
the admin server running status. Don&#8217;t start any other application services.</span></p><p><span style="font-family: &quot;Aptos&quot;,sans-serif; font-size: 12.0pt; line-height: 115%; mso-ansi-language: EN-IN; mso-ascii-theme-font: minor-latin; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-language: AR-SA; mso-bidi-theme-font: minor-bidi; mso-fareast-font-family: Aptos; mso-fareast-language: EN-US; mso-fareast-theme-font: minor-latin; mso-hansi-theme-font: minor-latin;"><table border="0" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="background: white; border-collapse: collapse; mso-padding-alt: 0cm 0cm 0cm 0cm; mso-yfti-tbllook: 1184;">
 <tbody><tr style="mso-yfti-firstrow: yes; mso-yfti-irow: 0; mso-yfti-lastrow: yes;">
  <td style="border: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 450.8pt;" valign="top" width="601">
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">[oracle@ebstest
  scripts]$ sh adadminsrvctl.sh status&nbsp;</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">You are
  running adadminsrvctl.sh version 120.10.12020000.2</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">&nbsp;Enter
  the WebLogic Admin password:</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">Enter
  the APPS Schema password:</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">&nbsp;&nbsp;The
  AdminServer is running&nbsp;</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">adadminsrvctl.sh:
  exiting with status 0</span><o:p></o:p></p>
  <p class="MsoNormal"><span style="color: black; mso-color-alt: windowtext;">&nbsp;adadminsrvctl.sh:
  check the logfile
  /u01/oracle/VIS/fs1/inst/apps/VIS_ebstest/logs/appl/admin/log/adadminsrvctl.txt
  for more information ...</span><o:p></o:p></p>
  <p class="MsoListParagraph"><span style="color: black; mso-color-alt: windowtext;">&nbsp;</span><o:p></o:p></p>
  </td>
 </tr>
</tbody></table><br /></span></p><p><span style="font-family: &quot;Aptos&quot;,sans-serif; font-size: 12.0pt; line-height: 115%; mso-ansi-language: EN-IN; mso-ascii-theme-font: minor-latin; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-language: AR-SA; mso-bidi-theme-font: minor-bidi; mso-fareast-font-family: Aptos; mso-fareast-language: EN-US; mso-fareast-theme-font: minor-latin; mso-hansi-theme-font: minor-latin;"></span></p><p class="MsoListParagraph" style="mso-list: l0 level1 lfo1; text-indent: -18.0pt;"><!--[if !supportLists]-->1.<span style="font-family: &quot;Times New Roman&quot;; font-feature-settings: normal; font-kerning: auto; font-language-override: normal; font-optical-sizing: auto; font-size-adjust: none; font-size: 7pt; font-stretch: normal; font-style: normal; font-variant: normal; font-variation-settings: normal; line-height: normal;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span><!--[endif]-->Now login to weblogic console from browser<o:p></o:p></p><p class="MsoListParagraph" style="mso-list: l0 level1 lfo1; text-indent: -18.0pt;"><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEhFojtfW_Ja7tpuchJ0YnhHcBwHY37eHr04v3RuXKQeeKwEozEOtMedwRh2guSz1IFjXQnl5VvY87SpaBIa9Bct-YT4iuW3rLC0K4-Huj2RXkSaGvbrWiE2tUhvlLJELOn6jKJzfJlEIYCu-LoHxdfyFuWubB1oWmwZ3s4Z5vXoPC8_tlEXlJFHX0m5L2U" style="margin-left: auto; margin-right: auto;"><img data-original-height="844" data-original-width="1581" height="342" src="https://blogger.googleusercontent.com/img/a/AVvXsEhFojtfW_Ja7tpuchJ0YnhHcBwHY37eHr04v3RuXKQeeKwEozEOtMedwRh2guSz1IFjXQnl5VvY87SpaBIa9Bct-YT4iuW3rLC0K4-Huj2RXkSaGvbrWiE2tUhvlLJELOn6jKJzfJlEIYCu-LoHxdfyFuWubB1oWmwZ3s4Z5vXoPC8_tlEXlJFHX0m5L2U=w640-h342" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;"></td></tr></tbody></table><br /></p><p class="MsoNormal" style="margin-left: 18.0pt;">Click on Lock and Edit button<o:p></o:p></p><p class="MsoNormal" style="margin-left: 18.0pt;"></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEht8CNCScfwH6uN_CJIEOMBcIOfsuyiHuV9AB4Ce0iVi-MEwFaYDTlsDSPQg0QFnQgqzgva28O99HMsW0IoKWA25P6zsXwPD8ijslfwvdvlih2klcVMojNqE16UU0b6hw7IfqQYzNqOWEfcMCqMiZVcQ-9IsZxEvpa6XZQoIcnCp7K8j1SavG6wuYmd7e4" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="591" data-original-width="1645" height="230" src="https://blogger.googleusercontent.com/img/a/AVvXsEht8CNCScfwH6uN_CJIEOMBcIOfsuyiHuV9AB4Ce0iVi-MEwFaYDTlsDSPQg0QFnQgqzgva28O99HMsW0IoKWA25P6zsXwPD8ijslfwvdvlih2klcVMojNqE16UU0b6hw7IfqQYzNqOWEfcMCqMiZVcQ-9IsZxEvpa6XZQoIcnCp7K8j1SavG6wuYmd7e4=w640-h230" width="640" /></a></div><br /><br /><p></p><p class="MsoNormal" style="margin-left: 18.0pt;">Now under Domain structure, click
on services - &gt; Data Sources<o:p></o:p></p><p class="MsoNormal" style="margin-left: 18.0pt;"></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEgnwqxgVpRg-VGuDbJec3VBsEQrb9Eei-c7BWKLwOEFpPpgCLRSk1yooWzibpy9zhfBjPRAEsRCmv_r7O8zTHsrFI3_Wr-bEtka6NAgiDTQxeaXL4FoxhtWZVy8XyC_TuYuBLS5DuASvkldOctrmlkh3C1j7gl1Wtg9gyxfJiaG1qpP2OrxdSCJRwLaj4Y" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="707" data-original-width="1035" height="438" src="https://blogger.googleusercontent.com/img/a/AVvXsEgnwqxgVpRg-VGuDbJec3VBsEQrb9Eei-c7BWKLwOEFpPpgCLRSk1yooWzibpy9zhfBjPRAEsRCmv_r7O8zTHsrFI3_Wr-bEtka6NAgiDTQxeaXL4FoxhtWZVy8XyC_TuYuBLS5DuASvkldOctrmlkh3C1j7gl1Wtg9gyxfJiaG1qpP2OrxdSCJRwLaj4Y=w640-h438" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: center;"><p class="MsoNormal" style="margin-left: 18pt; text-align: left;">Now click on &#8220;EBSDataSource&#8221;<o:p></o:p></p></div><br /><br /><p></p><p class="MsoListParagraph" style="mso-list: l0 level1 lfo1; text-indent: -18.0pt;"></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEgWDqIVj6UxRUvoNniKdoeX4XSR_-yWpqB2LkbpUK0rW90eQCBoUwGjbk5IiBO8yseTJ5hTClhdQC5CyXJqZwfQRapESe3uGGt8FVlg0QRodBxvtfonly6M9a3DtEXeXWxXaH-HK-vnDYrf5sUa50pi_ncIOI2TmmcUo_UubOM6pmLVh446i9aNcLBN2UI" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="553" data-original-width="1678" height="210" src="https://blogger.googleusercontent.com/img/a/AVvXsEgWDqIVj6UxRUvoNniKdoeX4XSR_-yWpqB2LkbpUK0rW90eQCBoUwGjbk5IiBO8yseTJ5hTClhdQC5CyXJqZwfQRapESe3uGGt8FVlg0QRodBxvtfonly6M9a3DtEXeXWxXaH-HK-vnDYrf5sUa50pi_ncIOI2TmmcUo_UubOM6pmLVh446i9aNcLBN2UI=w640-h210" width="640" /></a></div><p></p><p class="MsoNormal" style="margin-left: 18.0pt;"><br /></p><p class="MsoNormal" style="margin-left: 18.0pt;">Now on the page of &#8220;Settings of
EBSDataSoure&#8221; click on connection pool and&nbsp;&nbsp;provide the changed apps
password and save it.<o:p></o:p></p><p class="MsoListParagraph" style="mso-list: l0 level1 lfo1; text-indent: -18.0pt;"><br /></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEigOz7xHJO1cdevhWNOPd17z89usksj6DaSVHjWV77y4O4o8z_tNjygH032z2LAHgE2CcYKnMgqvcZ7T_emKVfPRulF5qmQ-zKqsANYgFh6SSwnCYBDIb-XokDXVlphRZ7ZpE4Tf_wBQ2oBa_NaT-6Ak-j6p-eUmSzVMAK8nKp_npbJEiNyzRruuQaEm48" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="607" data-original-width="940" height="414" src="https://blogger.googleusercontent.com/img/a/AVvXsEigOz7xHJO1cdevhWNOPd17z89usksj6DaSVHjWV77y4O4o8z_tNjygH032z2LAHgE2CcYKnMgqvcZ7T_emKVfPRulF5qmQ-zKqsANYgFh6SSwnCYBDIb-XokDXVlphRZ7ZpE4Tf_wBQ2oBa_NaT-6Ak-j6p-eUmSzVMAK8nKp_npbJEiNyzRruuQaEm48=w640-h414" width="640" /></a></div><div class="separator" style="clear: both; text-align: center;"><br /></div><div class="separator" style="clear: both; text-align: left;"><br /></div><br /><br /><p></p><p class="MsoNormal" style="margin-left: 18.0pt;">Click on Activate changes.<o:p></o:p></p><p class="MsoNormal" style="margin-left: 18.0pt;"></p><div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEg1z7yoQ2YbweROld9-_GzMwhmqf7HSqnfCmW6fvjqTgKP6tYDyzFAMSnNG5Is4daNDFfUc1ULs0LZa1tDLWL3eT-khQfM2B8Be7BSt_ZxWggp3O6cvXrTNVFlGUz4XyMTV_HTQFwPLUbqlqU09ADp8I-SYG5WGdm1D2xRxgvs1Cvn6zroDHi9DKOwMQs4" style="margin-left: 1em; margin-right: 1em;"><img data-original-height="556" data-original-width="803" height="444" src="https://blogger.googleusercontent.com/img/a/AVvXsEg1z7yoQ2YbweROld9-_GzMwhmqf7HSqnfCmW6fvjqTgKP6tYDyzFAMSnNG5Is4daNDFfUc1ULs0LZa1tDLWL3eT-khQfM2B8Be7BSt_ZxWggp3O6cvXrTNVFlGUz4XyMTV_HTQFwPLUbqlqU09ADp8I-SYG5WGdm1D2xRxgvs1Cvn6zroDHi9DKOwMQs4=w640-h444" width="640" /></a></div><p class="MsoNormal" style="margin-left: 18.0pt;"><br /></p><p class="MsoNormal" style="margin-left: 18.0pt;"><br /></p><span style="font-family: &quot;Aptos&quot;,sans-serif; font-size: 12.0pt; line-height: 115%; mso-ansi-language: EN-IN; mso-ascii-theme-font: minor-latin; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-bidi-language: AR-SA; mso-bidi-theme-font: mi