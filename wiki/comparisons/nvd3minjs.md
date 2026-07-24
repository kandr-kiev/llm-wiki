---
title: "nv.d3.min.js"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - data
  - guide
  - use-case
---

# nv.d3.min.js

> **Source:** local-ai-education-provendorphpunitphp-code-coveragesrcreporthtmlrenderertemplatejsnvd3minjs-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/php-code-coverage/src/Report/Html/Renderer/Template/js/nv.d3.min.js ingested: 2026-07-20 sha256: 88c382915fd2cd7943bd7c17af4b...
> **Sources:**
>   - local-ai-education-provendorphpunitphp-code-coveragesrcreporthtmlrenderertemplatejsnvd3minjs-2026-07-20.md
> **Links:**
- [[jquery.min.js]]
- [[d3.min.js]]
- [[bootstrap.min.js]]
- [[agriculture-is-ready-for-ai-but-its-data-isnt]]
- [[fortune-david-siegel-open-source-aipdf]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/php-code-coverage/src/Report/Html/Renderer/Template/js/nv.d3.min.js
ingested: 2026-07-20
sha256: 88c382915fd2cd7943bd7c17af4b17efd0a706f963958bc4c6a43f251b64e738
blog_source: local:unknown
---
/* nvd3 version 1.8.1 (https://github.com/novus/nvd3) 2015-06-15 */
!function(){var a={};a.dev=!1,a.tooltip=a.tooltip||{},a.utils=a.utils||{},a.models=a.models||{},a.charts={},a.logs={},a.dom={},a.dispatch=d3.dispatch("render_start","render_end"),Function.prototype.bind||(Function.prototype.bind=function(a){if("function"!=typeof this)throw new TypeError("Function.prototype.bind - what is trying to be bound is not callable");var b=Array.prototype.slice.call(arguments,1),c=this,d=function(){},e=function(){return c.apply(this instanceof d&&a?this:a,b.concat(Array.prototype.slice.call(arguments)))};return d.prototype=this.prototype,e.prototype=new d,e}),a.dev&&(a.dispatch.on("render_start",function(){a.logs.startTime=+new Date}),a.dispatch.on("render_end",function(){a.logs.endTime=+new Date,a.logs.totalTime=a.logs.endTime-a.logs.startTime,a.log("total",a.logs.totalTime)})),a.log=function(){if(a.dev&&window.console&&console.log&&console.log.apply)console.log.apply(console,arguments);else if(a.dev&&window.console&&"function"==typeof console.log&&Function.prototype.bind){var b=Function.prototype.bind.call(console.log,console);b.apply(console,arguments)}return arguments[arguments.length-1]},a.deprecated=function(a,b){console&&console.warn&&console.warn("nvd3 warning: `"+a+"` has been deprecated. ",b||"")},a.render=function(b){b=b||1,a.render.active=!0,a.dispatch.render_start();var c=function(){for(var d,e,f=0;b>f&&(e=a.render.queue[f]);f++)d=e.generate(),typeof e.callback==typeof Function&&e.callback(d);a.render.queue.splice(0,f),a.render.queue.length?setTimeout(c):(a.dispatch.render_end(),a.render.active=!1)};setTimeout(c)},a.render.active=!1,a.render.queue=[],a.addGraph=function(b){typeof arguments[0]==typeof Function&&(b={generate:arguments[0],callback:arguments[1]}),a.render.queue.push(b),a.render.active||a.render()},"undefined"!=typeof module&&"undefined"!=typeof exports&&(module.exports=a),"undefined"!=typeof window&&(window.nv=a),a.dom.write=function(a){return void 0!==window.fastdom?fastdom.write(a):a()},a.dom.read=function(a){return void 0!==window.fastdom?fastdom.read(a):a()},a.interactiveGuideline=function(){"use strict";function b(l){l.each(function(l){function m(){var a=d3.mouse(this),d=a[0],e=a[1],i=!0,j=!1;if(k&&(d=d3.event.offsetX,e=d3.event.offsetY,"svg"!==d3.event.target.tagName&&(i=!1),d3.event.target.className.baseVal.match("nv-legend")&&(j=!0)),i&&(d-=f.left,e-=f.top),0>d||0>e||d>o||e>p||d3.event.relatedTarget&&void 0===d3.event.relatedTarget.ownerSVGElement||j){if(k&&d3.event.relatedTarget&&void 0===d3.event.relatedTarget.ownerSVGElement&&(void 0===d3.event.relatedTarget.className||d3.event.relatedTarget.className.match(c.nvPointerEventsClass)))return;return h.elementMo

## Summary

useout({mouseX:d,mouseY:e}),b.renderGuideLine(null),void c.hidden(!0)}c.hidden(!1);var l=g.invert(d);h.elementMousemove({mouseX:d,mouseY:e,pointXValue:l}),"dblclick"===d3.event.type&&h.elementDblclick({mouseX:d,mouseY:e,pointXValue:l}),"click"===d3.event.type&&h.elementClick({mouseX:d,mouseY:e,pointXValue:l})}var n=d3.select(this),o=d||960,p=e||400,q=n.selectAll("g.nv-wrap.nv-interactiveLineLayer").data([l]),r=q.enter().append("g").attr("class"," nv-wrap nv-interactiveLineLayer");r.append("g").attr("class","nv-interactiveGuideLine"),j&&(j.on("touchmove",m).on("mousemove",m,!0).on("mouseout",m,!0).on("dblclick",m).on("click",m),b.guideLine=null,b.renderGuideLine=function(c){i&&(b.guideLine&&b.guideLine.attr("x1")===c||a.dom.write(function(){var b=q.select(".nv-interactiveGuideLine").selectAll("line").data(null!=c?[a.utils.NaNtoZero(c)]:[],String);b.enter().append("line").attr("class","nv-guideline").attr("x1",function(a){return a}).attr("x2",function(a){return a}).attr("y1",p).attr("y2",0),b.exit().remove()}))})})}var c=a.models.tooltip();c.duration(0).hideDelay(0)._isInteractiveLayer(!0).hidden(!1);var d=null,e=null,f={left:0,top:0},g=d3.scale.linear(),h=d3.dispatch("elementMousemove","elementMouseout","elementClick","elementDblclick"),i=!0,j=null,k="ActiveXObject"in window;return b.dispatch=h,b.tooltip=c,b.margin=function(a){return arguments.length?(f.top="undefined"!=typeof a.top?a.top:f.top,f.left="undefined"!=typeof a.left?a.left:f.left,b):f},b.width=function(a){return arguments.length?(d=a,b):d},b.height=function(a){return arguments.length?(e=a,b):e},b.xScale=function(a){return arguments.length?(g=a,b):g},b.showGuideLine=function(a){return arguments.length?(i=a,b):i},b.svgContainer=function(a){return arguments.length?(j=a,b):j},b},a.interactiveBisect=function(a,b,c){"use strict";if(!(a instanceof Array))return null;var d;d="function"!=typeof c?function(a){return a.x}:c;var e=function(a,b){return d(a)-b},f=d3.bisector(e).left,g=d3.max([0,f(a,b)-1]),h=d(a[g]);if("undefined"==typeof h&&(h=g),h===b)return g;var i=d3.min([g+1,a.length-1]),j=d(a[i]);return"undefined"==typeof j&&(j=i),Math.abs(j-b)>=Math.abs(h-b)?g:i},a.nearestValueIndex=function(a,b,c){"use strict";var d=1/0,e=null;return a.forEach(function(a,f){var g=Math.abs(b-a);null!=a&&d>=g&&c>g&&(d=g,e=f)}),e},function(){"use strict";a.models.tooltip=function(){function b(){if(k){var a=d3.select(k);"svg"!==a.node().tagName&&(a=a.select("svg"));var b=a.node()?a.attr("viewBox"):null;if(b){b=b.split(" ");var c=parseInt(a.style("width"),10)/b[2];p.left=p.left*c,p.top=p.top*c}}}function c(){if(!n){var a;a=k?k:document.body,n=d3.select(a).append("div").attr("class","nvtooltip "+(j?j:"xy-tooltip")).attr("id",v),n.style("top",0).style("left",0),n.style("opacity",0),n.selectAll("div, table, td, tr").classed(w,!0),n.classed(w,!0),o=n.node()}}function d(){if(r&&B(e)){b();var f=p.left,g=null!==i?i:p.top;return a.dom.write(function(){c();var b=A(e);b&&(o.innerHTML=b),k&&u?a.dom.read(function(){var a=k.ge

## Related Articles

- [[jquery.min.js]]
- [[d3.min.js]]
- [[bootstrap.min.js]]
- [[agriculture-is-ready-for-ai-but-its-data-isnt]]
- [[fortune-david-siegel-open-source-aipdf]]
