---
source_url: https://distill.pub/selforg/2021/adversarial
ingested: 2026-07-11
sha256: 03449c8761b6631c58b7022082e6396de5a8268eeedfe51cdeaf4453d1095d81
blog_source: Distill AI
---
<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1"><script>
window.addEventListener('WebComponentsReady', function() {
  console.warn('WebComponentsReady');
  const loaderTag = document.createElement('script');
  loaderTag.src = 'https://distill.pub/template.v2.js';
  document.head.insertBefore(loaderTag, document.head.firstChild);
});
</script><script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.0.17/webcomponents-loader.js"></script>
  
  
  <style id="distill-prerendered-styles" type="text/css">/*
 * Copyright 2018 The Distill Template Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

html {
  font-size: 14px;
	line-height: 1.6em;
  /* font-family: "Libre Franklin", "Helvetica Neue", sans-serif; */
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", Arial, sans-serif;
  /*, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";*/
  text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}

@media(min-width: 768px) {
  html {
    font-size: 16px;
  }
}

body {
  margin: 0;
}

a {
  color: #004276;
}

figure {
  margin: 0;
}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

table th {
	text-align: left;
}

table thead {
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

table thead th {
  padding-bottom: 0.5em;
}

table tbody :first-child td {
  padding-top: 0.5em;
}

pre {
  overflow: auto;
  max-width: 100%;
}

p {
  margin-top: 0;
  margin-bottom: 1em;
}

sup, sub {
  vertical-align: baseline;
  position: relative;
  top: -0.4em;
  line-height: 1em;
}

sub {
  top: 0.4em;
}

.kicker,
.marker {
  font-size: 15px;
  font-weight: 600;
  color: rgba(0, 0, 0, 0.5);
}


/* Headline */

@media(min-width: 1024px) {
  d-title h1 span {
    display: block;
  }
}

/* Figure */

figure {
  position: relative;
  margin-bottom: 2.5em;
  margin-top: 1.5em;
}

figcaption+figure {

}

figure img {
  width: 100%;
}

figure svg text,
figure svg tspan {
}

figcaption,
.figcaption {
  color: rgba(0, 0, 0, 0.6);
  font-size: 12px;
  line-height: 1.5em;
}

@media(min-width: 1024px) {
figcaption,
.figcaption {
    font-size: 13px;
  }
}

figure.external img {
  background: white;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 1px 8px rgba(0, 0, 0, 0.1);
  padding: 18px;
  box-sizing: border-box;
}

figcaption a {
  color: rgba(0, 0, 0, 0.6);
}

figcaption b,
figcaption strong, {
  font-weight: 600;
  color: rgba(0, 0, 0, 1.0);
}
/*
 * Copyright 2018 The Distill Template Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

@supports not (display: grid) {
  .base-grid,
  distill-header,
  d-title,
  d-abstract,
  d-article,
  d-appendix,
  distill-appendix,
  d-byline,
  d-footnote-list,
  d-citation-list,
  distill-footer {
    display: block;
    padding: 8px;
  }
}

.base-grid,
distill-header,
d-title,
d-abstract,
d-article,
d-appendix,
distill-appendix,
d-byline,
d-footnote-list,
d-citation-list,
distill-footer {
  display: grid;
  justify-items: stretch;
  grid-template-columns: [screen-start] 8px [page-start kicker-start text-start gutter-start middle-start] 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr [text-end page-end gutter-end kicker-end middle-end] 8px [screen-end];
  grid-column-gap: 8px;
}

.grid {
  display: grid;
  grid-column-gap: 8px;
}

@media(min-width: 768px) {
  .base-grid,
  distill-header,
  d-title,
  d-abstract,
  d-article,
  d-appendix,
  distill-appendix,
  d-byline,
  d-footnote-list,
  d-citation-list,
  distill-footer {
    grid-template-columns: [screen-start] 1fr [page-start kicker-start middle-start text-start] 45px 45px 45px 45px 45px 45px 45px 45px [ kicker-end text-end gutter-start] 45px [middle-end] 45px [page-end gutter-end] 1fr [screen-end];
    grid-column-gap: 16px;
  }

  .grid {
    grid-column-gap: 16px;
  }
}

@media(min-width: 1000px) {
  .base-grid,
  distill-header,
  d-title,
  d-abstract,
  d-article,
  d-appendix,
  distill-appendix,
  d-byline,
  d-footnote-list,
  d-citation-list,
  distill-footer {
    grid-template-columns: [screen-start] 1fr [page-start kicker-start] 50px [middle-start] 50px [text-start kicker-end] 50px 50px 50px 50px 50px 50px 50px 50px [text-end gutter-start] 50px [middle-end] 50px [page-end gutter-end] 1fr [screen-end];
    grid-column-gap: 16px;
  }

  .grid {
    grid-column-gap: 16px;
  }
}

@media(min-width: 1180px) {
  .base-grid,
  distill-header,
  d-title,
  d-abstract,
  d-article,
  d-appendix,
  distill-appendix,
  d-byline,
  d-footnote-list,
  d-citation-list,
  distill-footer {
    grid-template-columns: [screen-start] 1fr [page-start kicker-start] 60px [middle-start] 60px [text-start kicker-end] 60px 60px 60px 60px 60px 60px 60px 60px [text-end gutter-start] 60px [middle-end] 60px [page-end gutter-end] 1fr [screen-end];
    grid-column-gap: 32px;
  }

  .grid {
    grid-column-gap: 32px;
  }
}




.base-grid {
  grid-column: screen;
}

/* .l-body,
d-article > *  {
  grid-column: text;
}

.l-page,
d-title > *,
d-figure {
  grid-column: page;
} */

.l-gutter {
  grid-column: gutter;
}

.l-text,
.l-body {
  grid-column: text;
}

.l-page {
  grid-column: page;
}

.l-body-outset {
  grid-column: middle;
}

.l-page-outset {
  grid-column: page;
}

.l-screen {
  grid-column: screen;
}

.l-screen-inset {
  grid-column: screen;
  padding-left: 16px;
  padding-left: 16px;
}


/* Aside */

d-article aside {
  grid-column: gutter;
  font-size: 12px;
  line-height: 1.6em;
  color: rgba(0, 0, 0, 0.6)
}

@media(min-width: 768px) {
  aside {
    grid-column: gutter;
  }

  .side {
    grid-column: gutter;
  }
}
/*
 * Copyright 2018 The Distill Template Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

d-title {
  padding: 2rem 0 1.5rem;
  contain: layout style;
  overflow-x: hidden;
}

@media(min-width: 768px) {
  d-title {
    padding: 4rem 0 1.5rem;
  }
}

d-title h1 {
  grid-column: text;
  font-size: 40px;
  font-weight: 700;
  line-height: 1.1em;
  margin: 0 0 0.5rem;
}

@media(min-width: 768px) {
  d-title h1 {
    font-size: 50px;
  }
}

d-title p {
  font-weight: 300;
  font-size: 1.2rem;
  line-height: 1.55em;
  grid-column: text;
}

d-title .status {
  margin-top: 0px;
  font-size: 12px;
  color: #009688;
  opacity: 0.8;
  grid-column: kicker;
}

d-title .status span {
  line-height: 1;
  display: inline-block;
  padding: 6px 0;
  border-bottom: 1px solid #80cbc4;
  font-size: 11px;
  text-transform: uppercase;
}
/*
 * Copyright 2018 The Distill Template Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

d-byline {
  contain: style;
  overflow: hidden;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  font-size: 0.8rem;
  line-height: 1.8em;
  padding: 1.5rem 0;
  min-height: 1.8em;
}


d-byline .byline {
  grid-template-columns: 1fr 1fr;
  grid-column: text;
}

@media(min-width: 768px) {
  d-byline .byline {
    grid-template-columns: 1fr 1fr 1fr 1fr;
  }
}

d-byline .authors-affiliations {
  grid-column-end: span 2;
  grid-template-columns: 1fr 1fr;
  margin-bottom: 1em;
}

@media(min-width: 768px) {
  d-byline .authors-affiliations {
    margin-bottom: 0;
  }
}

d-byline h3 {
  font-size: 0.6rem;
  font-weight: 400;
  color: rgba(0, 0, 0, 0.5);
  margin: 0;
  text-transform: uppercase;
}

d-byline p {
  margin: 0;
}

d-byline a,
d-article d-byline a {
  color: rgba(0, 0, 0, 0.8);
  text-decoration: none;
  border-bottom: none;
}

d-article d-byline a:hover {
  text-decoration: underline;
  border-bottom: none;
}

d-byline p.author {
  font-weight: 500;
}

d-byline .affiliations {

}
/*
 * Copyright 2018 The Distill Template Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

d-article {
  contain: layout style;
  overflow-x: hidden;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  padding-top: 2rem;
  color: rgba(0, 0, 0, 0.8);
}

d-article > * {
  grid-column: text;
}

@media(min-width: 768px) {
  d-article {
    font-size: 16px;
  }
}

@media(min-width: 1024px) {
  d-article {
    font-size: 1.06rem;
    line-height: 1.7em;
  }
}


/* H2 */


d-article .marker {
  text-decoration: none;
  border: none;
  counter-reset: section;
  grid-column: kicker;
  line-height: 1.7em;
}

d-article .marker:hover {
  border: none;
}

d-article .marker span {
  padding: 0 3px 4px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
  position: relative;
  top: 4px;
}

d-article .marker:hover span {
  color: rgba(0, 0, 0, 0.7);
  border-bottom: 1px solid rgba(0, 0, 0, 0.7);
}

d-article h2 {
  font-weight: 600;
  font-size: 24px;
  line-height: 1.25em;
  margin: 2rem 0 1.5rem 0;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  padding-bottom: 1rem;
}

@media(min-width: 1024px) {
  d-article h2 {
    font-size: 36px;
  }
}

/* H3 */

d-article h3 {
  font-weight: 700;
  font-size: 18px;
  line-height: 1.4em;
  margin-bottom: 1em;
  margin-top: 2em;
}

@media(min-width: 1024px) {
  d-article h3 {
    font-size: 20px;
  }
}

/* H4 */

d-article h4 {
  font-weight: 600;
  text-transform: uppercase;
  font-size: 14px;
  line-height: 1.4em;
}

d-article a {
  color: inherit;
}

d-article p,
d-article ul,
d-article ol,
d-article blockquote {
  margin-top: 0;
  margin-bottom: 1em;
  margin-left: 0;
  margin-right: 0;
}

d-article blockquote {
  border-left: 2px solid rgba(0, 0, 0, 0.2);
  padding-left: 2em;
  font-style: italic;
  color: rgba(0, 0, 0, 0.6);
}

d-article a {
  border-bottom: 1px solid rgba(0, 0, 0, 0.4);
  text-decoration: none;
}

d-article a:hover {
  border-bottom: 1px solid rgba(0, 0, 0, 0.8);
}

d-article .link {
  text-decoration: underline;
  cursor: pointer;
}

d-article ul,
d-article ol {
  padding-left: 24px;
}

d-article li {
  margin-bottom: 1em;
  margin-left: 0;
  padding-left: 0;
}

d-article li:last-child {
  margin-bottom: 0;
}

d-article pre {
  font-size: 14px;
  margin-bottom: 20px;
}

d-article hr {
  grid-column: screen;
  width: 100%;
  border: none;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  margin-top: 60px;
  margin-bottom: 60px;
}

d-article section {
  margin-top: 60px;
  margin-bottom: 60px;
}

d-article span.equation-mimic {
  font-family: georgia;
  font-size: 115%;
  font-style: italic;
}

d-article > d-code,
d-article section > d-code  {
  display: block;
}

d-article > d-math[block],
d-article section > d-math[block]  {
  display: block;
}

@media (max-width: 768px) {
  d-article > d-code,
  d-article section > d-code,
  d-article > d-math[block],
  d-article section > d-math[block] {
      overflow-x: scroll;
      -ms-overflow-style: none;  // IE 10+
      overflow: -moz-scrollbars-none;  // Firefox
  }

  d-article > d-code::-webkit-scrollbar,
  d-article section > d-code::-webkit-scrollbar,
  d-article > d-math[block]::-webkit-scrollbar,
  d-article section > d-math[block]::-webkit-scrollbar {
    display: none;  // Safari and Chrome
  }
}

d-article .citation {
  color: #668;
  cursor: pointer;
}

d-include {
  width: auto;
  display: block;
}

d-figure {
  contain: layout style;
}

/* KaTeX */

.katex, .katex-prerendered {
  contain: style;
  display: inline-block;
}

/* Tables */

d-article table {
  border-collapse: collapse;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

d-article table th {
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

d-article table td {
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

d-article table tr:last-of-type td {
  border-bottom: none;
}

d-article table th,
d-article table td {
  font-size: 15px;
  padding: 2px 8px;
}

d-article table tbody :first-child td {
  padding-top: 2px;
}
/*
 * Copyright 2018 The Distill Template Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

span.katex-display {
  text-align: left;
  padding: 8px 0 8px 0;
  margin: 0.5em 0 0.5em 1em;
}

span.katex {
  -webkit-font-smoothing: antialiased;
  color: rgba(0, 0, 0, 0.8);
  font-size: 1.18em;
}
/*
 * Copyright 2018 The Distill Template Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

@media print {

  @page {
    size: 8in 11in;
    @bottom-right {
      content: counter(page) " of " counter(pages);
    }
  }

  html {
    /* no general margins -- CSS Grid takes care of those */
  }

  p, code {
    page-break-inside: avoid;
  }

  h2, h3 {
    page-break-after: avoid;
  }

  d-header {
    visibility: hidden;
  }

  d-footer {
    display: none!important;
  }

}
</style>
<link rel="stylesheet" href="https://distill.pub/third-party/katex/katex.min.css" crossorigin="anonymous">
    
    <link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA99JREFUeNrsG4t1ozDMzQSM4A2ODUonKBucN2hugtIJ6E1AboLcBiQTkJsANiAb9OCd/OpzMWBJBl5TvaeXPiiyJetry0J8wW3D3QpjRh3GjneXDq+fSQA9s2mH9x3KDhN4foJfCb8N/Jrv+2fnDn8vLRQOplWHVYdvHZYdZsBcZP1vBmh/n8DzEmhUQDPaOuP9pFuY+JwJHwHnCLQE2tnWBGEyXozY9xCUgHMhhjE2I4heVWtgIkZ83wL6Qgxj1obfWBxymPwe+b00BCCRNPbwfb60yleAkkBHGT5AEehIYz7eJrFDMF9CvH4wwhcGHiHMneFvLDQwlwvMLQq58trRcYBWfYn0A0OgHWQUSu25mE+BnoYKnnEJoeIWAifzOv7vLWd2ZKRfWAIme3tOiUaQ3UnLkb0xj1FxRIeEGKaGIHOs9nEgLaaA9i0JRYo1Ic67wJW86KSKE/ZAM8KuVMk8ITVhmxUxJ3Cl2xlm9Vtkeju1+mpCQNxaEGNCY8bs9X2YqwNoQeGjBWut/ma0QAWy/TqAsHx9wSya3I5IRxOfTC+leG+kA/4vSeEcGBtNUN6byhu3+keEZCQJUNh8MAO7HL6H8pQLnsW/Hd4T4lv93TPjfM7A46iEEqbB5EDOvwYNW6tGNZzT/o+CZ6sqZ6wUtR/wf7mi/VL8iNciT6rHih48Y55b4nKCHJCCzb4y0nwFmin3ZEMIoLfZF8F7nncFmvnWBaBj7CGAYA/WGJsUwHdYqVDwAmNsUgAx4CGgAA7GOOxADYOFWOaIKifuVYzmOpREqA21Mo7aPsgiY1PhOMAmxtR+AUbYH3Id2wc0SAFIQTsn9IUGWR8k9jx3vtXSiAacFxTAGakBk9UudkNECd6jLe+6HrshshvIuC6IlLMRy7er+JpcKma24SlE4cFZSZJDGVVrsNvitQhQrDhW0jfiOLfFd47C42eHT56D/BK0To+58Ahj+cAT8HT1UWlfLZCCd/uKawzU0Rh2EyIX/Icqth3niG8ybNroezwe6khdCNxRN+l4XGdOLVLlOOt2hTRJlr1ETIuMAltVTMz70mJrkdGAaZLSmnBEqmAE32JCMmuTlCnRgsBENtOUpHhvvsYIL0ibnBkaC6QvKcR7738GKp0AKnim7xgUSNv1bpS8QwhBt8r+EP47v/oyRK/S34yJ9nT+AN0Tkm4OdB9E4BsmXM3SnMlRFUrtp6IDpV2eKzdYvF3etm3KhQksbOLChGkSmcBdmcEwvqkrMy5BzL00NZeu3qPYJOOuCc+5NjcWKXQxFvTa3NoXJ4d8in7fiAUuTt781dkvuHX4K8AA2Usy7yNKLy0AAAAASUVORK5CYII=
">
    <link href="/rss.xml" rel="alternate" type="application/rss+xml" title="Articles from Distill">
  
    <title>Adversarial Reprogramming of Neural Cellular Automata</title>
    
    <link rel="canonical" href="https://distill.pub/selforg/2021/adversarial">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="Reprogramming Neural CA to exhibit novel behaviour, using adversarial attacks.">
    <meta property="article:published" itemprop="datePublished" content="2021-05-06">
    <meta property="article:created" itemprop="dateCreated" content="2021-05-06">
    
    <meta property="article:modified" itemprop="dateModified" content="2021-05-06T18:54:34.000Z">
    
    <meta property="article:author" content="Ettore Randazzo">
    <meta property="article:author" content="Alexander Mordvintsev">
    <meta property="article:author" content="Eyvind Niklasson">
    <meta property="article:author" content="Michael Levin">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="Adversarial Reprogramming of Neural Cellular Automata">
    <meta property="og:description" content="Reprogramming Neural CA to exhibit novel behaviour, using adversarial attacks.">
    <meta property="og:url" content="https://distill.pub/selforg/2021/adversarial">
    <meta property="og:image" content="https://distill.pub/selforg/2021/adversarial/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Adversarial Reprogramming of Neural Cellular Automata">
    <meta name="twitter:description" content="Reprogramming Neural CA to exhibit novel behaviour, using adversarial attacks.">
    <meta name="twitter:url" content="https://distill.pub/selforg/2021/adversarial">
    <meta name="twitter:image" content="https://distill.pub/selforg/2021/adversarial/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="Adversarial Reprogramming of Neural Cellular Automata">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/selforg/2021/adversarial">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="5">
    <meta name="citation_firstpage" content="e00027.004">
    <meta name="citation_doi" content="10.23915/distill.00027.004">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/05/06">
    <meta name="citation_publication_date" content="2021/05/06">
    <meta name="citation_author" content="Randazzo, Ettore">
    <meta name="citation_author_institution" content="Google">
    <meta name="citation_author" content="Mordvintsev, Alexander">
    <meta name="citation_author_institution" content="Google">
    <meta name="citation_author" content="Niklasson, Eyvind">
    <meta name="citation_author_institution" content="Google">
    <meta name="citation_author" content="Levin, Michael">
    <meta name="citation_author_institution" content="Allen Discovery Center at Tufts University">
    <meta name="citation_reference" content="citation_title=Growing Neural Cellular Automata;citation_author=Alexander Mordvintsev;citation_author=Ettore Randazzo;citation_author=Eyvind Niklasson;citation_author=Michael Levin;citation_publication_date=2020;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Self-classifying MNIST Digits;citation_author=Ettore Randazzo;citation_author=Alexander Mordvintsev;citation_author=Eyvind Niklasson;citation_author=Michael Levin;citation_author=Sam Greydanus;citation_publication_date=2020;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Herpes Simplex Virus: The Hostile Guest That Takes Over Your Home;citation_author=A. Banerjee;citation_author=S. Kulkarni;citation_author=A. Mukherjee;citation_publication_date=2020;citation_journal_title=Front Microbiol;citation_volume=11;">
    <meta name="citation_reference" content="citation_title=The role of gut microbiota (commensal bacteria) and the mucosal barrier in the pathogenesis of inflammatory and autoimmune diseases and cancer: contribution of germ-free and gnotobiotic animal models of human diseases;citation_author=H. Tlaskalová-Hogenová;citation_author=R. Stěpánková;citation_author=Kozáková H.;citation_author=T. Hudcovic;citation_author=L. Vannucci;citation_author=L. Tučková;citation_author=P. Rossmann;citation_author=T. Hrnčíř;citation_author=M. Kverka;citation_author=Z. Zákostelská;citation_author=K. Klimešová;citation_author=J. Přibylová;citation_author=J. Bártová;citation_author=D. Sanchez;citation_author=P. Fundová;citation_author=D. Borovská;citation_author=D. Srůtková;citation_author=Z. Zídek;citation_author=M. Schwarzer;citation_author=P. Drastich;citation_author=D. P. Funda;citation_publication_date=2011;citation_journal_title=Cell Mol Immunol;citation_volume=8;citation_number=2;">
    <meta name="citation_reference" content="citation_title=Regulation of axial and head patterning during planarian regeneration by a commensal bacterium;citation_author=K. B. Williams;citation_author=J. Bischof;citation_author=F. J. Lee;citation_author=K. A. Miller;citation_author=J. V. LaPalme;citation_author=B. E. Wolfe;citation_author=M. Levin;citation_publication_date=2020;citation_journal_title=Mech Dev;citation_volume=163;">
    <meta name="citation_reference" content="citation_title=Toxoplasma gondii infection and behavioral outcomes in humans: a systematic review;citation_author=Victor Otero Martinez;citation_author=Fernanda Washington Mendonça Lima;citation_author=Chrissie Ferreira Carvalho;citation_author=José Antônio Menezes-Filho;citation_publication_date=2018;citation_journal_title=Parasitology research;citation_volume=117;">
    <meta name="citation_reference" content="citation_title=Resting potential, oncogene-induced tumorigenesis, and metastasis: the bioelectric basis of cancer in vivo;citation_author=Maria Lobikin;citation_author=Brook Chernet;citation_author=Daniel Lobo;citation_author=Michael Levin;citation_publication_date=2012;citation_journal_title=Physical biology;citation_volume=9;">
    <meta name="citation_reference" content="citation_title=Transmembrane voltage potential of somatic cells controls oncogene-mediated tumorigenesis at long-range;citation_author=Brook T Chernet;citation_author=Michael Levin;citation_publication_date=2014;citation_journal_title=Oncotarget;">
    <meta name="citation_reference" content="citation_title=Cross-limb communication during Xenopus hindlimb regenerative response: non-local bioelectric injury signals;citation_author=Sera M Busse;citation_author=Patrick T McMillen;citation_author=Michael Levin;citation_publication_date=2018;citation_journal_title=Development;">
    <meta name="citation_reference" content="citation_title=Local and long-range endogenous resting potential gradients antagonistically regulate apoptosis and proliferation in the embryonic CNS;citation_author=Vaibhav P Pai;citation_author=Joan M Lemire;citation_author=Ying Chen;citation_author=Gufa Lin;citation_author=Michael Levin;citation_publication_date=2015;citation_journal_title=The International journal of developmental biology;">
    <meta name="citation_reference" content="citation_title=Top-down models in biology: explanation and control of complex living systems above the molecular level;citation_author=Giovanni Pezzulo;citation_author=Michael Levin;citation_publication_date=2016;citation_journal_title=Journal of the Royal Society, Interface;">
    <meta name="citation_reference" content="citation_title=Generative Adversarial Networks;citation_author=Ian J. Goodfellow;citation_author=Jean Pouget-Abadie;citation_author=Mehdi Mirza;citation_author=Bing Xu;citation_author=David Warde-Farley;citation_author=Sherjil Ozair;citation_author=Aaron Courville;citation_author=Yoshua Bengio;citation_publication_date=2014;">
    <meta name="citation_reference" content="citation_title=Adversarial Reprogramming of Neural Networks;citation_author=Gamaleldin F. Elsayed;citation_author=Ian Goodfellow;citation_author=Jascha Sohl-Dickstein;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Efficient Estimation of Word Representations in Vector Space;citation_author=Tomas Mikolov;citation_author=Kai Chen;citation_author=Greg Corrado;citation_author=Jeffrey Dean;citation_publication_date=2013;">
    <meta name="citation_reference" content="citation_title=Fader Networks: Manipulating Images by Sliding Attributes;citation_author=Guillaume Lample;citation_author=Neil Zeghidour;citation_author=Nicolas Usunier;citation_author=Antoine Bordes;citation_author=Ludovic Denoyer;citation_author=Marc'Aurelio Ranzato;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Maximizing the spread of influence through a social network;citation_author=David Kempe;citation_author=Jon Kleinberg;citation_author=Éva Tardos;citation_publication_date=2003;">
    <meta name="citation_reference" content="citation_title=The Independent Cascade and Linear Threshold Models;citation_author=Paulo Shakarian;citation_author=Abhinav Bhatnagar;citation_author=Ashkan Aleali;citation_author=Elham Shaabani;citation_author=Ruocheng Guo;citation_publication_date=2015;">
    <meta name="citation_reference" content="citation_title=A Survey on Influence Maximization in a Social Network;citation_author=Suman Banerjee;citation_author=Mamata Jenamani;citation_author=Dilip Kumar Pratihar;citation_publication_date=2018;citation_arxiv_id=1808.05502;">
    <meta name="citation_reference" content="citation_title=Simplicial models of social contagion;citation_author=Iacopo Iacopini;citation_author=Giovanni Petri;citation_author=Alain Barrat;citation_author=Vito Latora;citation_publication_date=2019;citation_journal_title=Nature communications;citation_volume=10;citation_number=1;">
    <meta name="citation_reference" content="citation_title=Cascading Behavior in Networks: Algorithmic and Economic Issues;citation_author=Jon Kleinberg;citation_publication_date=2007;">
    <meta name="citation_reference" content="citation_title=On the Approximability of Influence in Social Networks;citation_author=Ning Chen;citation_publication_date=2009;citation_journal_title=SIAM Journal on Discrete Mathematics;citation_volume=23;citation_number=3;">
    <meta name="citation_reference" content="citation_title=The Computational Boundary of a “Self”: Developmental Bioelectricity Drives Multicellularity and Scale-Free Cognition;citation_author=Michael Levin;citation_publication_date=2019;citation_journal_title=Frontiers in Psychology;citation_volume=10;">
</head>

<body distill-prerendered=""><distill-header distill-prerendered="">
<style>
distill-header {
  position: relative;
  height: 60px;
  background-color: hsl(200, 60%, 15%);
  width: 100%;
  box-sizing: border-box;
  z-index: 2;
  color: rgba(0, 0, 0, 0.8);
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.05);
}
distill-header .content {
  height: 70px;
  grid-column: page;
}
distill-header a {
  font-size: 16px;
  height: 60px;
  line-height: 60px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  padding: 22px 0;
}
distill-header a:hover {
  color: rgba(255, 255, 255, 1);
}
distill-header svg {
  width: 24px;
  position: relative;
  top: 4px;
  margin-right: 2px;
}
@media(min-width: 1080px) {
  distill-header {
    height: 70px;
  }
  distill-header a {
    height: 70px;
    line-height: 70px;
    padding: 28px 0;
  }
  distill-header .logo {
  }
}
distill-header svg path {
  fill: none;
  stroke: rgba(255, 255, 255, 0.8);
  stroke-width: 3px;
}
distill-header .logo {
  font-size: 17px;
  font-weight: 200;
}
distill-header .nav {
  float: right;
  font-weight: 300;
}
distill-header .nav a {
  font-size: 12px;
  margin-left: 24px;
  text-transform: uppercase;
}
</style>
<div class="content">
  <a href="/" class="logo">
    <svg viewBox="-607 419 64 64">
  <path d="M-573.4,478.9c-8,0-14.6-6.4-14.6-14.5s14.6-25.9,14.6-40.8c0,14.9,14.6,32.8,14.6,40.8S-565.4,478.9-573.4,478.9z"></path>
</svg>

    Distill
  </a>
  <nav class="nav">
    <a href="/about/">About</a>
    <a href="/prize/">Prize</a>
    <a href="/journal/">Submit</a>
  </nav>
</div>
</distill-header>

  <d-front-matter>
    <script type="text/json">{
      "title": "Adversarial Reprogramming of Neural Cellular Automata",
      "description": "Reprogramming Neural CA to exhibit novel behaviour, using adversarial attacks.",
      "authors": [
        {
          "author": "Ettore Randazzo",
          "authorURL": "https://oteret.github.io/",
          "affiliation": "Google",
          "affiliationURL": "https://ai.google/"
        },
        {
          "author": "Alexander Mordvintsev",
          "authorURL": "https://znah.net/",
          "affiliation": "Google",
          "affiliationURL": "https://ai.google/"
        },
        {
          "author": "Eyvind Niklasson",
          "authorURL": "https://eyvind.me/",
          "affiliation": "Google",
          "affiliationURL": "https://ai.google/"
        },
        {
          "author": "Michael Levin",
          "authorURL": "http://www.drmichaellevin.org",
          "affiliation": "Allen Discovery Center at Tufts University",
          "affiliationURL": "http://allencenter.tufts.edu"
        }
      ],
      "katex": {
        "delimiters": [
          {
            "left": "$",
            "right": "$",
            "display": false
          },
          {
            "left": "$$",
            "right": "$$",
            "display": true
          }
        ]
      }
    }</script>
  </d-front-matter>

  <style>
    figure {
      text-align: center;
      margin-bottom: 0.5em;
      margin-top: 0.5em;
    }
    figure img {
      max-width: 100%;
      width: unset;
    }
    video {
      max-width: 100%;
    }
    .colab-root {
      display: block;
      box-sizing: border-box;
      width: 160px;
      text-align: center;
      margin-top: 8px;
      background: rgba(255, 255, 255, 0.75);
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 11px!important;
      text-decoration: none;
      color: #aaa;
      border: none;
      font-weight: 300;
      border: solid 1px rgba(0, 0, 0, 0.08);
      border-bottom-color: rgba(0, 0, 0, 0.15);
      text-transform: uppercase;
      line-height: 16px;
    }

   span.colab-span {
      background-image: url(images/colab.svg);
      background-repeat: no-repeat;
      background-size: 20px;
      background-position-y: 2px;
      display: inline-block;
      padding-left: 24px;
      border-radius: 4px;
      text-decoration: none;
    }

    a.colab-root:hover{
      color: #666;
      background: white;
      border-color: rgba(0, 0, 0, 0.2);
    }

    /* TOC */
    @media(max-width: 1000px){
      d-contents {
        justify-self: start;
        align-self: start;
        grid-column: text;
        padding-bottom: 0.5em;
        margin-bottom: 1em;
        padding-left: 0.25em;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        border-bottom-width: 1px;
        border-bottom-style: solid;
        border-bottom-color: rgba(0, 0, 0, 0.1);
      }
    } 
    
    @media (min-width: 1000px){
      d-contents {
        align-self: start;
        grid-column-start: 1;
        grid-column-end: 4;
        justify-self: end;
        padding-right: 3em;
        padding-left: 2em;
        border-right: 1px solid rgba(0, 0, 0, 0.1);
        border-right-width: 1px;
        border-right-style: solid;
        border-right-color: rgba(0, 0, 0, 0.1);
      }
    }

    @media (min-width: 1180px){
      d-contents {
        grid-column-start: 1;
        grid-column-end: 4;
        justify-self: end;
        padding-right: 3em;
        padding-left: 2em;
        border-right: 1px solid rgba(0, 0, 0, 0.1);
        border-right-width: 1px;
        border-right-style: solid;
        border-right-color: rgba(0, 0, 0, 0.1);
      }
    }

    d-contents nav h3 {
      margin-top: 0;
      margin-bottom: 1em;
    }

    d-contents nav a {
      color: rgba(0, 0, 0, 0.8);
      border-bottom: none;
      text-decoration: none;
    }

    d-contents li {
      list-style-type: none;
    }

    d-contents ul {
      padding-left: 1em;
    }
    
    d-contents nav ul li {
      margin-bottom: .25em;
    }

    d-contents nav a:hover {
      text-decoration: underline solid rgba(0, 0, 0, 0.6);
    }

    d-contents nav ul {
      margin-top: 0;
      margin-bottom: 6px;
    }


    d-contents nav>div {
      display: block;
      outline: none;
      margin-bottom: 0.5em;
    }

    d-contents nav>div>a {
      font-size: 13px;
      font-weight: 600;
    }

    d-contents nav>div>a:hover,
    d-contents nav>ul>li>a:hover {
        text-decoration: none;
    }

    /* code blocks to margins */
    @media (min-width: 1600px) {
      d-code {
        margin-top: -10px;
        grid-column-start: 12;
        grid-column-end: 14; 
      }
    }
    /* so title is on one line */
    d-title h1, d-title p {
      grid-column: middle;
    }
 
    .vidoverlay {
        position: absolute;
        width: 100%;
        height: 100%;
        background-position: center;
        background-image: url(images/play.svg);
        background-repeat: no-repeat;
        background-size: 15%;
        cursor: pointer;
        opacity: 0.8;
        z-index: 1;
        transition: opacity 1s;
    }

    .vc {
      position: relative;
    }

    d-article {
      counter-reset: figure;
    }
    figure {
      counter-increment: figure;
    }
    figcaption::before {
      content: "Figure " counter(figure) ": ";
    }
    
      /* ****************************************
       * Thread Info
       ******************************************/

       .thread-info {
      background-color: hsl(54, 78%, 96%);
      border-left: solid hsl(54, 33%, 67%) 1px;
      padding: 1em;
      color: hsla(0, 0%, 0%, 0.67);
    }

    #thread-nav {
      margin-top: 20;
      margin-bottom: 1.5rem;
      display: grid;
      grid-template-columns: 45px 2fr 3fr;
      grid-template-areas:
        'thread-icon explanation explanation '
        'thread-icon prev next';
      grid-column-gap: 1.5em;
    }

    @media (min-width: 768px) {
      #thread-nav {
        grid-template-columns: 65px 3fr 2fr;
      }
    }

    #thread-nav .thread-icon {
      grid-area: thread-icon;
      padding: 0.5em;
      justify-self: center;
    }

    #thread-nav .explanation {
      grid-area: explanation;
      font-size: 85%;
      color: hsl(0, 0%, 0.33);
    }

    #thread-nav .prev {
      grid-area: prev;
    }

    #thread-nav .prev::before {
      content: '← Previous Article';
    }

    #thread-nav .overview {
      scroll-behavior: smooth;
    }

    #thread-nav .overview::before {
      content: '↑';
      white-space: nowrap;
      margin-right: 0.5em;
    }

    #thread-nav .next {
      grid-area: next;
      scroll-behavior: smooth;
    }

    #thread-nav .next::before {
      content: 'Next Article →';
    }

    #thread-nav .next::before,
    #thread-nav .prev::before {
      display: block;
      white-space: nowrap;
      padding: 0.5em 0;
      font-size: 80%;
      font-weight: bold;
      margin-top: 0px;
      margin-right: 0.5em;
      text-transform: uppercase;
    }

    #thread-nav .prev,
    #thread-nav .next,
    #thread-nav .overview {
      font-size: 80%;
      line-height: 1.5em;
      font-weight: 600;
      border-bottom: none;
      color: #2e6db7;
      /* margin-top: 0.25em; */
      letter-spacing: 0.25px;
    }
    
  .colab-root-toc {
    
    display: inline-block;
    background: rgba(255, 255, 255, 0.75);
    padding: 0px 4px;
    border-radius: 4px;
    font-size: 11px!important;
    text-decoration: none;
    color: #aaa;
    border: none;
    font-weight: 300;
    border: solid 1px rgba(0, 0, 0, 0.08);
    border-bottom-color: rgba(0, 0, 0, 0.15);
    text-transform: uppercase;
    line-height: 1.3;
}
    
   span.colab-span-toc {
      background-image: url(images/colab.svg);
      background-repeat: no-repeat;
      background-size: 16px;
      background-position-y: 3px;
      display: inline-block;
      padding-left: 16px;
      border-radius: 4px;
      text-decoration: none;
      width: 0px;
      height: 13px;

      text-align: center;
  }

  iframe {
    grid-column: page;
  }

  </style>
  <d-title>
    <h1>Adversarial Reprogramming of Neural Cellular Automata</h1>
    <p>A robustness investigation.</p>

</d-title>

<d-byline>
  <div class="byline grid">
    <div class="authors-affiliations grid">
      <h3>Authors</h3>
      <h3>Affiliations</h3>
      
        <p class="author">
          
            <a class="name" href="https://oteret.github.io/">Ettore Randazzo</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://ai.google/">Google</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://znah.net/">Alexander Mordvintsev</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://ai.google/">Google</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://eyvind.me/">Eyvind Niklasson</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://ai.google/">Google</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="http://www.drmichaellevin.org">Michael Levin</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="http://allencenter.tufts.edu">Allen Discovery Center at Tufts University</a>
        </p>
      
    </div>
    <div>
      <h3>Published</h3>
      
        <p>May 6, 2021</p> 
    </div>
    <div>
      <h3>DOI</h3>
      
        <p><a href="https://doi.org/10.23915/distill.00027.004">10.23915/distill.00027.004</a></p>
    </div>
  </div>
</d-byline>


<d-article>

<d-contents>
  <nav class="l-text toc figcaption">
    <h3>Contents</h3>
    <div><a href="#adversarial-mnist-cas">Adversarial MNIST CAs</a> | <a href="https://colab.research.google.com/github/google-research/self-organising-systems/blob/master/adversarial_reprogramming_ca/adversarial_mnist_ca.ipynb" class="colab-root-toc"><span class="colab-span-toc"></span></a></div>
    <div><a href="#adversarial-injections-for-growing-cas">Adversarial Injections for Growing CAs</a> | <a href="https://colab.research.google.com/github/google-research/self-organising-systems/blob/master/adversarial_reprogramming_ca/adversarial_growing_ca.ipynb#scrollTo=ByHbsY0EuyqB" class="colab-root-toc"><span class="colab-span-toc"></span></a></div>
    <!-- <ul>
      <li><a href="#experiment-1">Self-classify, persist & mutate</a></li>
      <li><a href="#experiment-2">Stabilizing classification</a></li>
    </ul> -->
    <div><a href="#perturbing-the-states-of-growing-cas">Perturbing the states of Growing CAs</a> | <a href="https://colab.research.google.com/github/google-research/self-organising-systems/blob/master/adversarial_reprogramming_ca/adversarial_growing_ca.ipynb#scrollTo=JaITnQv0k1iY" class="colab-root-toc"><span class="colab-span-toc"></span></a></div>
    <div><a href="#related-work">Related Work</a></div>
    <div><a href="#discussion">Discussion</a></div>
    <br>
    <br>
  </nav>
</d-contents>
<section id="thread-nav" class="thread-info" style="margin-top: 10px; margin-bottom: 40px">
  <img class="thread-icon" src="images/multiple-pages.svg" width="43px" height="50px">
  <p class="explanation">
    This article is part of the
    <a href="/2020/selforg/">Differentiable Self-organizing Systems Thread</a>,
    an experimental format collecting invited short articles delving into
    differentiable self-organizing systems, interspersed with critical
    commentary from several experts in adjacent fields.
  </p>
  <a class="prev" href="/selforg/2021/textures/">Self-Organising Textures</a>
</section>

<p style="color:rgba(0,0,0,0.3); font-size:10px"> This article makes strong use of colors in figures and demos. Click <a href="#colorwheel">here</a> to adjust the color palette.</p>

<p>In a complex system, whether biological, technological, or social, how can we discover signaling events that will alter system-level behavior in desired ways? Even when the rules governing the individual components of these complex systems are known, the inverse problem - going from desired behaviour to system design - is at the heart of many barriers for the advance of biomedicine, robotics, and other fields of importance to society.</p>

<p>Biology, specifically, is transitioning from a focus on mechanism (what is required for the system to work) to a focus on information (what algorithm is sufficient to implement adaptive behavior). Advances in machine learning represent an exciting and largely untapped source of inspiration and tooling to assist the biological sciences. Growing Neural Cellular Automata <d-cite key="mordvintsev2020growing"></d-cite> and Self-classifying MNIST Digits <d-cite key="randazzo2020self-classifying"></d-cite> introduced the Neural Cellular Automata (Neural CA) model and demonstrated how tasks requiring self-organisation, such as pattern growth and self-classification of digits, can be trained in an end-to-end, differentiable fashion. The resulting models were robust to various kinds of perturbations: the growing CA expressed regenerative capabilities when damaged; the MNIST CA were responsive to changes in the underlying digits, triggering reclassification whenever necessary. These computational frameworks represent quantitative models with which to understand important biological phenomena, such as scaling of single cell behavior rules into reliable organ-level anatomies. The latter is a kind of anatomical homeostasis, achieved by feedback loops that must recognize deviations from a correct target morphology and progressively reduce anatomical error.</p>





<p>In this work, we <i>train adversaries </i>whose goal is to reprogram CA into doing something other than what they were trained to do. In order to understand what kinds of lower-level signals  alter system-level behavior of our CA, it is important to understand how these CA are constructed and where local versus global information resides.</p>

<p>The system-level behavior of Neural CA is affected by:</p>
<ul><li><strong>Individual cell states. </strong>States store information which is used for both diversification among cell behaviours and for communication with neighbouring cells.</li>
<li><strong>The model parameters. </strong>These describe the input/output behavior of a cell and are shared by every cell of the same family. The model parameters can be seen as <i>the way the system works</i>.</li>
<li><strong>The perceptive field. </strong>This is how cells perceive their environment. In Neural CA, we always restrict the perceptive field to be the eight nearest neighbors and the cell itself. The way cells are perceived by each other is different between the Growing CA and MNIST CA. The Growing CA perceptive field is a set of weights fixed both during training and inference, while the MNIST CA perceptive field is learned as part of the model parameters.</li></ul>
<p>
Perturbing any of these components will result in system-level behavioural changes.</p>

<p>We will explore two kinds of adversarial attacks: 1) injecting a few adversarial cells into an existing grid running a pretrained model; and 2) perturbing the global state of all cells on a grid.</p>

<p>For the first type of adversarial attacks we train a new CA model that, when placed in an environment running one of the original models described in the previous articles, is able to hijack the behavior of the collective mix of adversarial and non-adversarial CA. This is an example of injecting CA with differing <i>model parameters</i> into the system. In biology, numerous forms of hijacking are known, including viruses that take over genetic and biochemical information flow <d-cite key="pmid32457704"></d-cite>, bacteria that take over physiological control mechanisms <d-cite key="pmid21278760"></d-cite> and even regenerative morphology of whole bodies <d-cite key="pmid32439577"></d-cite>, and fungi and toxoplasma that modulate host behavior <d-cite key="pmid30109417"></d-cite>. Especially fascinating are the many cases of non-cell-autonomous signaling developmental biology and cancer, showing that some cell behaviors can significantly alter host properties both locally and at long range. For example, bioelectrically-abnormal cells can trigger metastatic conversion in an otherwise normal body (with no genetic defects) <d-cite key="pmid23196890"></d-cite>, while management of bioelectrical state in one area of the body can suppress tumorigenesis on the other side of the organism <d-cite key="pmid24830454"></d-cite>. Similarly, amputation damage in one leg initiates changes to ionic properties of cells in the contralateral leg <d-cite key="pmid30126906"></d-cite>, while the size of the developing brain is in part dictated by the activity of ventral gut cells <d-cite key="pmid26198142"></d-cite>. All of these phenomena underlie the importance of understanding how cell groups make collective decisions, and how those tissue-level decisions can be subverted by the activity of a small number of cells. It is essential to develop quantitative models of such dynamics, in order to drive meaningful progress in regenerative medicine that controls system-level outcomes top-down, where cell- or molecular-level micromanagement is infeasible <d-cite key="pmid27807271"></d-cite>.</p>

<p>The second type of adversarial attacks interact with previously trained growing CA models by <i>perturbing the states within cells</i>. We apply a global state perturbation to all living cells. This can be seen as inhibiting or enhancing combinations of state values, in turn hijacking proper communications among cells and within the cell’s own states. Models like this represent not only ways of thinking about adversarial relationships in nature (such as parasitism and evolutionary arms races of genetic and physiological mechanisms), but also a roadmap for the development of regenerative medicine strategies. Next-generation biomedicine will need computational tools for inferring minimal, least-effort interventions that can be applied to biological systems to predictively change their large-scale anatomical and behavioral properties.</p>
<h2 id="adversarial-mnist-ca">Adversarial MNIST CA <a href="https://colab.research.google.com/github/google-research/self-organising-systems/blob/master/adversarial_reprogramming_ca/adversarial_mnist_ca.ipynb" class="colab-root">Try in a <span class="colab-span">Notebook</span></a></h2>
<p>Recall how the Self-classifying MNIST digits task consisted of placing CA cells on a plane forming the shape of an MNIST digit. The cells then had to communicate among themselves in order to come to a complete consensus as to which digit they formed.</p>
<figure>
<img src="images/local_global_figure.svg" style="width: 650px">
<figcaption>Diagram showing the local vs. global information available in the cell collective. <br> (a) Local information neighbourhood - each cell can only observe itself and its neighbors’ states, or the absence of neighbours.<br> (b) Globally, the cell collective aggregates information from all parts of itself. <br> (c) It is able to distinguish certain shapes that compose a specific digit 