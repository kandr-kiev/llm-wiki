---
title: "announcing vulnhunter"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - agent
  - ai
  - cloud
  - data
  - image-generation
  - news
  - open-source
  - performance
  - privacy
  - real-time
  - search
  - security
  - tool
  - use-case
---

# announcing vulnhunter

> **Source:** vulnhunter-capital-ones-agentic-ai-code-security-tool-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://www.capitalone.com/tech/open-source/announcing-vulnhunter/ ingested: 2026-07-17 sha256: b6f28877fcc61c555fe5c620dfc6a87cc0f2196e0850bd18101a0f6c12ef5f88 blog_source: Hacker New...
> **Sources:**
>   - vulnhunter-capital-ones-agentic-ai-code-security-tool-2026-07-17.md
> **Links:**
- [[article]]
- [[speculative-growth-ai-publicpdf]]
- [[fortune-david-siegel-open-source-aipdf]]
- [[bisbull120.pdf]]
- [[whats-important-14]]

## Key Findings

---
source_url: https://www.capitalone.com/tech/open-source/announcing-vulnhunter/
ingested: 2026-07-17
sha256: b6f28877fcc61c555fe5c620dfc6a87cc0f2196e0850bd18101a0f6c12ef5f88
blog_source: Hacker News AI
---
VulnHunter: an open-source, agentic AI code security tool | Capital One Tech
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- - 
(function () {
var host = window.location.hostname;
window._sequoia = {};
window._sequoia.scriptEnv =
/www[\w\d]*\.capitalone\.com/i.test(host) ||
/^cards\.discover\.com$/i.test(host)
? 'prod'
: 'dev';
var envLoc = window._sequoia.scriptEnv;
const webShell = 'www-capitalone-com';
const allowedHosts = [
'.capitalone.com',
'cards.discover.com',
`regression-${webShell}.cloud.capitalone`,
];
const queryParams = new URLSearchParams(window.location.search);
const prNumber = queryParams.get('nr');
const nrEnabledForPreview =
host.indexOf(`${prNumber}-${webShell}.cloud.capitalone`) >= 0;
// Exempt local dev and PR preview without nr query param
const isAllowedHost = allowedHosts.some(
(allowedHost) => host.indexOf(allowedHost) >= 0
);
if (!isAllowedHost && !nrEnabledForPreview) {
return;
}
var nrConf = {
runtime_app_id: {
prod: '461457245',
dev: '458554504',
},
runtime_account_id: {
prod: '1927717',
dev: '1927715',
},
runtime_trust_id: {
prod: '1356230',
dev: '1356230',
},
runtime_licence_id: {
prod: 'c344d59e90',
dev: '0a6015c82e',
},
};
window.NREUM || (NREUM = {});
NREUM.init = { privacy: { cookies_enabled: true } };
NREUM.loader_config = {
accountID: nrConf['runtime_account_id'][envLoc],
trustKey: nrConf['runtime_trust_id'][envLoc],
agentID: nrConf['runtime_app_id'][envLoc],
licenseKey: nrConf['runtime_licence_id'][envLoc],
applicationID: nrConf['runtime_app_id'][envLoc],
};
NREUM.info = {
beacon: 'bam.nr-data.net',
errorBeacon: 'bam.nr-data.net',
licenseKey: nrConf['runtime_licence_id'][envLoc],
applicationID: nrConf['runtime_app_id'][envLoc],
sa: 1,
};
;/*! For license information please see nr-loader-spa-1.278.3.min.js.LICENSE.txt */
(()=>{var e,t,r={8122:(e,t,r)=>{"use strict";r.d(t,{a:()=>i});var n=r(944);function i(e,t){try{if(!e||"object"!=typeof e)return(0,n.R)(3);if(!t||"object"!=typeof t)return(0,n.R)(4);const r=Object.create(Object.getPrototypeOf(t),Object.getOwnPropertyDescriptors(t)),o=0===Object.keys(r).length?e:r;for(let a in o)if(void 0!==e[a])try{if(null===e[a]){r[a]=null;continue}Array.isArray(e[a])&&Array.isArray(t[a])?r[a]=Array.from(new Set([...e[a],...t[a]])):"object"==typeof e[a]&&"object"==typeof t[a]?r[a]=i(e[a],t[a]):r[a]=e[a]}catch(e){(0,n.R)(1,e)}return r}catch(e){(0,n.R)(2,e)}}},2555:(e,t,r)=>{"use strict";r.d(t,{Vp:()=>c,fn:()=>s,x1:()=>u});var n=r(384),i=r(8122);const o={beacon:n.NT.beacon,errorBeacon:n.NT.errorBeacon,licenseKey:void 0,applicationID:void 0,sa:void 0,queueTime:void 0,applicationTime:void 0,ttGuid:void 0,user:void 0,account:void 0,product:void 0,extra:void 0,jsAttributes:{},userAttributes:void 0,atts:void 0,transactionName:void 0,tNamePlain:void 0},a={};func

## Summary

tion s(e){try{const t=c(e);return!!t.licenseKey&&!!t.errorBeacon&&!!t.applicationID}catch(e){return!1}}function c(e){if(!e)throw new Error("All info objects require an agent identifier!");if(!a[e])throw new Error("Info for ".concat(e," was never set"));return a[e]}function u(e,t){if(!e)throw new Error("All info objects require an agent identifier!");a[e]=(0,i.a)(t,o);const r=(0,n.nY)(e);r&&(r.info=a[e])}},9417:(e,t,r)=>{"use strict";r.d(t,{D0:()=>p,gD:()=>m,xN:()=>g});var n=r(3333),i=r(993);const o=e=>{if(!e||"string"!=typeof e)return!1;try{document.createDocumentFragment().querySelector(e)}catch{return!1}return!0};var a=r(2614),s=r(944),c=r(384),u=r(8122);const d="[data-nr-mask]",l=()=>{const e={feature_flags:[],experimental:{marks:!1,measures:!1,resources:!1},mask_selector:"*",block_selector:"[data-nr-block]",mask_input_options:{color:!1,date:!1,"datetime-local":!1,email:!1,month:!1,number:!1,range:!1,search:!1,tel:!1,text:!1,time:!1,url:!1,week:!1,textarea:!1,select:!1,password:!0}};return{ajax:{deny_list:void 0,block_internal:!0,enabled:!0,autoStart:!0},distributed_tracing:{enabled:void 0,exclude_newrelic_header:void 0,cors_use_newrelic_header:void 0,cors_use_tracecontext_headers:void 0,allowed_origins:void 0},get feature_flags(){return e.feature_flags},set feature_flags(t){e.feature_flags=t},generic_events:{enabled:!0,autoStart:!0},harvest:{interval:30},jserrors:{enabled:!0,autoStart:!0},logging:{enabled:!0,autoStart:!0,level:i.p_.INFO},metrics:{enabled:!0,autoStart:!0},obfuscate:void 0,page_action:{enabled:!0},page_view_event:{enabled:!0,autoStart:!0},page_view_timing:{enabled:!0,autoStart:!0},performance:{get capture_marks(){return e.feature_flags.includes(n.$v.MARKS)||e.experimental.marks},set capture_marks(t){e.experimental.marks=t},get capture_measures(){return e.feature_flags.includes(n.$v.MEASURES)||e.experimental.measures},set capture_measures(t){e.experimental.measures=t},resources:{get enabled(){return e.feature_flags.includes(n.$v.RESOURCES)||e.experimental.resources},set enabled(t){e.experimental.resources=t},asset_types:[],first_party_domains:[],ignore_newrelic:!0}},privacy:{cookies_enabled:!0},proxy:{assets:void 0,beacon:void 0},session:{expiresMs:a.wk,inactiveMs:a.BB},session_replay:{autoStart:!0,enabled:!1,preload:!1,sampling_rate:10,error_sampling_rate:100,collect_fonts:!1,inline_images:!1,fix_stylesheets:!0,mask_all_inputs:!0,get mask_text_selector(){return e.mask_selector},set mask_text_selector(t){o(t)?e.mask_selector="".concat(t,",").concat(d):""===t||null===t?e.mask_selector=d:(0,s.R)(5,t)},get block_class(){return"nr-block"},get ignore_class(){return"nr-ignore"},get mask_text_class(){return"nr-mask"},get block_selector(){return e.block_selector},set block_selector(t){o(t)?e.block_selector+=",".concat(t):""!==t&&(0,s.R)(6,t)},get mask_input_options(){return e.mask_input_options},set mask_input_options(t){t&&"object"==typeof t?e.mask_input_options={...t,password:!0}:(0,s.R)(7,t)}},session_trace:{enabled:!0,autoStart:!0},

## Related Articles

- [[article]]
- [[speculative-growth-ai-publicpdf]]
- [[fortune-david-siegel-open-source-aipdf]]
- [[bisbull120.pdf]]
- [[whats-important-14]]
