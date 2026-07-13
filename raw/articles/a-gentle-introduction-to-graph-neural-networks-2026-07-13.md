---
source_url: https://distill.pub/2021/gnn-intro
ingested: 2026-07-13
sha256: 3d9afb349cf648e9e9e3cf1d3aae5261ac60966875633446d6e3c2c6f707aedd
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

<!-- Import Vega & Vega-Lite (does not have to be from CDN) -->
<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4"></script>
<!-- Import vega-embed -->
<script src="https://cdn.jsdelivr.net/npm/vega-embed@v6"></script>


<!-- Mathjax -->
<script async="" src="https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>

<!-- End Mathjax -->

    
    <link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA99JREFUeNrsG4t1ozDMzQSM4A2ODUonKBucN2hugtIJ6E1AboLcBiQTkJsANiAb9OCd/OpzMWBJBl5TvaeXPiiyJetry0J8wW3D3QpjRh3GjneXDq+fSQA9s2mH9x3KDhN4foJfCb8N/Jrv+2fnDn8vLRQOplWHVYdvHZYdZsBcZP1vBmh/n8DzEmhUQDPaOuP9pFuY+JwJHwHnCLQE2tnWBGEyXozY9xCUgHMhhjE2I4heVWtgIkZ83wL6Qgxj1obfWBxymPwe+b00BCCRNPbwfb60yleAkkBHGT5AEehIYz7eJrFDMF9CvH4wwhcGHiHMneFvLDQwlwvMLQq58trRcYBWfYn0A0OgHWQUSu25mE+BnoYKnnEJoeIWAifzOv7vLWd2ZKRfWAIme3tOiUaQ3UnLkb0xj1FxRIeEGKaGIHOs9nEgLaaA9i0JRYo1Ic67wJW86KSKE/ZAM8KuVMk8ITVhmxUxJ3Cl2xlm9Vtkeju1+mpCQNxaEGNCY8bs9X2YqwNoQeGjBWut/ma0QAWy/TqAsHx9wSya3I5IRxOfTC+leG+kA/4vSeEcGBtNUN6byhu3+keEZCQJUNh8MAO7HL6H8pQLnsW/Hd4T4lv93TPjfM7A46iEEqbB5EDOvwYNW6tGNZzT/o+CZ6sqZ6wUtR/wf7mi/VL8iNciT6rHih48Y55b4nKCHJCCzb4y0nwFmin3ZEMIoLfZF8F7nncFmvnWBaBj7CGAYA/WGJsUwHdYqVDwAmNsUgAx4CGgAA7GOOxADYOFWOaIKifuVYzmOpREqA21Mo7aPsgiY1PhOMAmxtR+AUbYH3Id2wc0SAFIQTsn9IUGWR8k9jx3vtXSiAacFxTAGakBk9UudkNECd6jLe+6HrshshvIuC6IlLMRy7er+JpcKma24SlE4cFZSZJDGVVrsNvitQhQrDhW0jfiOLfFd47C42eHT56D/BK0To+58Ahj+cAT8HT1UWlfLZCCd/uKawzU0Rh2EyIX/Icqth3niG8ybNroezwe6khdCNxRN+l4XGdOLVLlOOt2hTRJlr1ETIuMAltVTMz70mJrkdGAaZLSmnBEqmAE32JCMmuTlCnRgsBENtOUpHhvvsYIL0ibnBkaC6QvKcR7738GKp0AKnim7xgUSNv1bpS8QwhBt8r+EP47v/oyRK/S34yJ9nT+AN0Tkm4OdB9E4BsmXM3SnMlRFUrtp6IDpV2eKzdYvF3etm3KhQksbOLChGkSmcBdmcEwvqkrMy5BzL00NZeu3qPYJOOuCc+5NjcWKXQxFvTa3NoXJ4d8in7fiAUuTt781dkvuHX4K8AA2Usy7yNKLy0AAAAASUVORK5CYII=
">
    <link href="/rss.xml" rel="alternate" type="application/rss+xml" title="Articles from Distill">
  
    <title>A Gentle Introduction to Graph Neural Networks</title>
    
    <link rel="canonical" href="https://distill.pub/2021/gnn-intro">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="What components are needed for building learning algorithms that leverage the structure and properties of graphs?">
    <meta property="article:published" itemprop="datePublished" content="2021-09-02">
    <meta property="article:created" itemprop="dateCreated" content="2021-09-02">
    
    <meta property="article:modified" itemprop="dateModified" content="2021-09-08T21:19:59.000Z">
    
    <meta property="article:author" content="Benjamin Sanchez-Lengeling">
    <meta property="article:author" content="Emily Reif">
    <meta property="article:author" content="Adam Pearce">
    <meta property="article:author" content="Alexander B. Wiltschko">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="A Gentle Introduction to Graph Neural Networks">
    <meta property="og:description" content="What components are needed for building learning algorithms that leverage the structure and properties of graphs?">
    <meta property="og:url" content="https://distill.pub/2021/gnn-intro">
    <meta property="og:image" content="https://distill.pub/2021/gnn-intro/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="A Gentle Introduction to Graph Neural Networks">
    <meta name="twitter:description" content="What components are needed for building learning algorithms that leverage the structure and properties of graphs?">
    <meta name="twitter:url" content="https://distill.pub/2021/gnn-intro">
    <meta name="twitter:image" content="https://distill.pub/2021/gnn-intro/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="A Gentle Introduction to Graph Neural Networks">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/2021/gnn-intro">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="9">
    <meta name="citation_firstpage" content="e33">
    <meta name="citation_doi" content="10.23915/distill.00033">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/09/02">
    <meta name="citation_publication_date" content="2021/09/02">
    <meta name="citation_author" content="Sanchez-Lengeling, Benjamin">
    <meta name="citation_author" content="Reif, Emily">
    <meta name="citation_author" content="Pearce, Adam">
    <meta name="citation_author" content="Wiltschko, Alexander B.">
    <meta name="citation_reference" content="citation_title=Understanding Convolutions on Graphs;citation_author=Ameya Daigavane;citation_author=Balaraman Ravindran;citation_author=Gaurav Aggarwal;citation_publication_date=2021;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=The Graph Neural Network Model;citation_author=F Scarselli;citation_author=M Gori;citation_author=Ah Chung Tsoi;citation_author=M Hagenbuchner;citation_author=G Monfardini;citation_publication_date=2009;citation_journal_title=IEEE Transactions on Neural Networks;citation_volume=20;citation_number=1;">
    <meta name="citation_reference" content="citation_title=A Deep Learning Approach to Antibiotic Discovery;citation_author=Jonathan M Stokes;citation_author=Kevin Yang;citation_author=Kyle Swanson;citation_author=Wengong Jin;citation_author=Andres Cubillos-Ruiz;citation_author=Nina M Donghia;citation_author=Craig R MacNair;citation_author=Shawn French;citation_author=Lindsey A Carfrae;citation_author=Zohar Bloom-Ackermann;citation_author=Victoria M Tran;citation_author=Anush Chiappino-Pepe;citation_author=Ahmed H Badran;citation_author=Ian W Andrews;citation_author=Emma J Chory;citation_author=George M Church;citation_author=Eric D Brown;citation_author=Tommi S Jaakkola;citation_author=Regina Barzilay;citation_author=James J Collins;citation_publication_date=2020;citation_journal_title=Cell;citation_volume=181;citation_number=2;">
    <meta name="citation_reference" content="citation_title=Learning to simulate complex physics with graph networks;citation_author=Alvaro Sanchez-Gonzalez;citation_author=Jonathan Godwin;citation_author=Tobias Pfaff;citation_author=Rex Ying;citation_author=Jure Leskovec;citation_author=Peter W Battaglia;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Fake News Detection on Social Media using Geometric Deep Learning;citation_author=Federico Monti;citation_author=Fabrizio Frasca;citation_author=Davide Eynard;citation_author=Damon Mannion;citation_author=Michael M Bronstein;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=Traffic prediction with advanced Graph Neural Networks;citation_author=Oliver Lange *;citation_author=Luis Perez;">
    <meta name="citation_reference" content="citation_title=Pixie: A System for Recommending 3+ Billion Items to 200+ Million Users in {Real-Time};citation_author=Chantat Eksombatchai;citation_author=Pranav Jindal;citation_author=Jerry Zitao Liu;citation_author=Yuchen Liu;citation_author=Rahul Sharma;citation_author=Charles Sugnet;citation_author=Mark Ulrich;citation_author=Jure Leskovec;citation_publication_date=2017;">
    <meta name="citation_reference" content="citation_title=Convolutional Networks on Graphs for Learning Molecular Fingerprints;citation_author=David Duvenaud;citation_author=Dougal Maclaurin;citation_author=Jorge Aguilera-Iparraguirre;citation_author=Rafael Gomez-Bombarelli;citation_author=Timothy Hirzel;citation_author=Alan Aspuru-Guzik;citation_author=Ryan P Adams;citation_publication_date=2015;">
    <meta name="citation_reference" content="citation_title=Distributed Representations of Words and Phrases and their Compositionality;citation_author=Tomas Mikolov;citation_author=Ilya Sutskever;citation_author=Kai Chen;citation_author=Greg Corrado;citation_author=Jeffrey Dean;citation_publication_date=2013;">
    <meta name="citation_reference" content="citation_title=BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding;citation_author=Jacob Devlin;citation_author=Ming-Wei Chang;citation_author=Kenton Lee;citation_author=Kristina Toutanova;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Glove: Global Vectors for Word Representation;citation_author=Jeffrey Pennington;citation_author=Richard Socher;citation_author=Christopher Manning;citation_publication_date=2014;citation_journal_title=Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP);">
    <meta name="citation_reference" content="citation_title=Learning to Represent Programs with Graphs;citation_author=Miltiadis Allamanis;citation_author=Marc Brockschmidt;citation_author=Mahmoud Khademi;citation_publication_date=2017;">
    <meta name="citation_reference" content="citation_title=Deep Learning for Symbolic Mathematics;citation_author=Guillaume Lample;citation_author=Francois Charton;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=KONECT;citation_author=Jerome Kunegis;citation_publication_date=2013;citation_journal_title=Proceedings of the 22nd International Conference on World Wide Web - WWW &amp;#39;13 Companion;">
    <meta name="citation_reference" content="citation_title=An Information Flow Model for Conflict and Fission in Small Groups;citation_author=Wayne W Zachary;citation_publication_date=1977;citation_journal_title=J. Anthropol. Res.;citation_volume=33;citation_number=4;">
    <meta name="citation_reference" content="citation_title=Learning Latent Permutations with Gumbel-Sinkhorn Networks;citation_author=Gonzalo Mena;citation_author=David Belanger;citation_author=Scott Linderman;citation_author=Jasper Snoek;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Janossy Pooling: Learning Deep Permutation-Invariant Functions for Variable-Size Inputs;citation_author=Ryan L Murphy;citation_author=Balasubramaniam Srinivasan;citation_author=Vinayak Rao;citation_author=Bruno Ribeiro;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Neural Message Passing for Quantum Chemistry;citation_author=Justin Gilmer;citation_author=Samuel S Schoenholz;citation_author=Patrick F Riley;citation_author=Oriol Vinyals;citation_author=George E Dahl;citation_publication_date=2017;citation_volume=70;">
    <meta name="citation_reference" content="citation_title=Relational inductive biases, deep learning, and graph networks;citation_author=Peter W Battaglia;citation_author=Jessica B Hamrick;citation_author=Victor Bapst;citation_author=Alvaro Sanchez-Gonzalez;citation_author=Vinicius Zambaldi;citation_author=Mateusz Malinowski;citation_author=Andrea Tacchetti;citation_author=David Raposo;citation_author=Adam Santoro;citation_author=Ryan Faulkner;citation_author=Caglar Gulcehre;citation_author=Francis Song;citation_author=Andrew Ballard;citation_author=Justin Gilmer;citation_author=George Dahl;citation_author=Ashish Vaswani;citation_author=Kelsey Allen;citation_author=Charles Nash;citation_author=Victoria Langston;citation_author=Chris Dyer;citation_author=Nicolas Heess;citation_author=Daan Wierstra;citation_author=Pushmeet Kohli;citation_author=Matt Botvinick;citation_author=Oriol Vinyals;citation_author=Yujia Li;citation_author=Razvan Pascanu;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Deep Sets;citation_author=Manzil Zaheer;citation_author=Satwik Kottur;citation_author=Siamak Ravanbakhsh;citation_author=Barnabas Poczos;citation_author=Ruslan Salakhutdinov;citation_author=Alexander Smola;citation_publication_date=2017;">
    <meta name="citation_reference" content="citation_title=Molecular graph convolutions: moving beyond fingerprints;citation_author=Steven Kearnes;citation_author=Kevin McCloskey;citation_author=Marc Berndl;citation_author=Vijay Pande;citation_author=Patrick Riley;citation_publication_date=2016;citation_journal_title=J. Comput. Aided Mol. Des.;citation_volume=30;citation_number=8;">
    <meta name="citation_reference" content="citation_title=Feature-wise transformations;citation_author=Vincent Dumoulin;citation_author=Ethan Perez;citation_author=Nathan Schucher;citation_author=Florian Strub;citation_author=Harm de Vries;citation_author=Aaron Courville;citation_author=Yoshua Bengio;citation_publication_date=2018;citation_journal_title=Distill;citation_volume=3;citation_number=7;">
    <meta name="citation_reference" content="citation_title=Leffingwell Odor Dataset;citation_author=Benjamin Sanchez-Lengeling;citation_author=Jennifer N Wei;citation_author=Brian K Lee;citation_author=Richard C Gerkin;citation_author=Alan Aspuru-Guzik;citation_author=Alexander B Wiltschko;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Machine Learning for Scent: Learning Generalizable Perceptual Representations of Small Molecules;citation_author=Benjamin Sanchez-Lengeling;citation_author=Jennifer N Wei;citation_author=Brian K Lee;citation_author=Richard C Gerkin;citation_author=Alan Aspuru-Guzik;citation_author=Alexander B Wiltschko;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=Benchmarking Graph Neural Networks;citation_author=Vijay Prakash Dwivedi;citation_author=Chaitanya K Joshi;citation_author=Thomas Laurent;citation_author=Yoshua Bengio;citation_author=Xavier Bresson;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Design Space for Graph Neural Networks;citation_author=Jiaxuan You;citation_author=Rex Ying;citation_author=Jure Leskovec;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Principal Neighbourhood Aggregation for Graph Nets;citation_author=Gabriele Corso;citation_author=Luca Cavalleri;citation_author=Dominique Beaini;citation_author=Pietro Lio;citation_author=Petar Velickovic;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Graph Traversal with Tensor Functionals: A Meta-Algorithm for Scalable Learning;citation_author=Elan Markowitz;citation_author=Keshav Balasubramanian;citation_author=Mehrnoosh Mirtaheri;citation_author=Sami Abu-El-Haija;citation_author=Bryan Perozzi;citation_author=Greg Ver Steeg;citation_author=Aram Galstyan;citation_publication_date=2021;">
    <meta name="citation_reference" content="citation_title=Graph Neural Tangent Kernel: Fusing Graph Neural Networks with Graph Kernels;citation_author=Simon S Du;citation_author=Kangcheng Hou;citation_author=Barnabas Poczos;citation_author=Ruslan Salakhutdinov;citation_author=Ruosong Wang;citation_author=Keyulu Xu;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=Representation Learning on Graphs with Jumping Knowledge Networks;citation_author=Keyulu Xu;citation_author=Chengtao Li;citation_author=Yonglong Tian;citation_author=Tomohiro Sonobe;citation_author=Ken-Ichi Kawarabayashi;citation_author=Stefanie Jegelka;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Neural Execution of Graph Algorithms;citation_author=Petar Velickovic;citation_author=Rex Ying;citation_author=Matilde Padovano;citation_author=Raia Hadsell;citation_author=Charles Blundell;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=Graph Theory;citation_author=Frank Harary;citation_publication_date=1969;">
    <meta name="citation_reference" content="citation_title=A nested-graph model for the representation and manipulation of complex objects;citation_author=Alexandra Poulovassilis;citation_author=Mark Levene;citation_publication_date=1994;citation_journal_title=ACM Transactions on Information Systems;citation_volume=12;citation_number=1;">
    <meta name="citation_reference" content="citation_title=Modeling polypharmacy side effects with graph convolutional networks;citation_author=Marinka Zitnik;citation_author=Monica Agrawal;citation_author=Jure Leskovec;citation_publication_date=2018;citation_journal_title=Bioinformatics;citation_volume=34;citation_number=13;">
    <meta name="citation_reference" content="citation_title=Machine learning in chemical reaction space;citation_author=Sina Stocker;citation_author=Gabor Csanyi;citation_author=Karsten Reuter;citation_author=Johannes T Margraf;citation_publication_date=2020;citation_journal_title=Nat. Commun.;citation_volume=11;citation_number=1;">
    <meta name="citation_reference" content="citation_title=Graphs and Hypergraphs;citation_author=Claude Berge;citation_publication_date=1976;">
    <meta name="citation_reference" content="citation_title=HyperGCN: A New Method of Training Graph Convolutional Networks on Hypergraphs;citation_author=Naganand Yadati;citation_author=Madhav Nimishakavi;citation_author=Prateek Yadav;citation_author=Vikram Nitin;citation_author=Anand Louis;citation_author=Partha Talukdar;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Hierarchical Message-Passing Graph Neural Networks;citation_author=Zhiqiang Zhong;citation_author=Cheng-Te Li;citation_author=Jun Pang;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Little Ball of Fur;citation_author=Benedek Rozemberczki;citation_author=Oliver Kiss;citation_author=Rik Sarkar;citation_publication_date=2020;citation_journal_title=Proceedings of the 29th ACM International Conference on Information &amp;amp; Knowledge Management;">
    <meta name="citation_reference" content="citation_title=Sampling from large graphs;citation_author=Jure Leskovec;citation_author=Christos Faloutsos;citation_publication_date=2006;citation_journal_title=Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining - KDD &amp;#39;06;">
    <meta name="citation_reference" content="citation_title=Metropolis Algorithms for Representative Subgraph Sampling;citation_author=Christian Hubler;citation_author=Hans-Peter Kriegel;citation_author=Karsten Borgwardt;citation_author=Zoubin Ghahramani;citation_publication_date=2008;citation_journal_title=2008 Eighth IEEE International Conference on Data Mining;">
    <meta name="citation_reference" content="citation_title=Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks;citation_author=Wei-Lin Chiang;citation_author=Xuanqing Liu;citation_author=Si Si;citation_author=Yang Li;citation_author=Samy Bengio;citation_author=Cho-Jui Hsieh;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=GraphSAINT: Graph Sampling Based Inductive Learning Method;citation_author=Hanqing Zeng;citation_author=Hongkuan Zhou;citation_author=Ajitesh Srivastava;citation_author=Rajgopal Kannan;citation_author=Viktor Prasanna;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=How Powerful are Graph Neural Networks?;citation_author=Keyulu Xu;citation_author=Weihua Hu;citation_author=Jure Leskovec;citation_author=Stefanie Jegelka;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Rep the Set: Neural Networks for Learning Set Representations;citation_author=Konstantinos Skianis;citation_author=Giannis Nikolentzos;citation_author=Stratis Limnios;citation_author=Michalis Vazirgiannis;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=Message Passing Networks for Molecules with Tetrahedral Chirality;citation_author=Lagnajit Pattanaik;citation_author=Octavian-Eugen Ganea;citation_author=Ian Coley;citation_author=Klavs F Jensen;citation_author=William H Green;citation_author=Connor W Coley;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=N-Gram Graph: Simple Unsupervised Representation for Graphs, with Applications to Molecules;citation_author=Shengchao Liu;citation_author=Mehmet Furkan Demirel;citation_author=Yingyu Liang;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Dual-Primal Graph Convolutional Networks;citation_author=Federico Monti;citation_author=Oleksandr Shchur;citation_author=Aleksandar Bojchevski;citation_author=Or Litany;citation_author=Stephan Gunnemann;citation_author=Michael M Bronstein;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Viewing matrices &amp; probability as graphs;citation_author=Tai-Danae Bradley;">
    <meta name="citation_reference" content="citation_title=Graphs and Matrices;citation_author=Ravindra B Bapat;citation_publication_date=2014;">
    <meta name="citation_reference" content="citation_title=Modern Graph Theory;citation_author=Bela Bollobas;citation_publication_date=2013;">
    <meta name="citation_reference" content="citation_title=Attention Is All You Need;citation_author=Ashish Vaswani;citation_author=Noam Shazeer;citation_author=Niki Parmar;citation_author=Jakob Uszkoreit;citation_author=Llion Jones;citation_author=Aidan N Gomez;citation_author=Lukasz Kaiser;citation_author=Illia Polosukhin;citation_publication_date=2017;">
    <meta name="citation_reference" content="citation_title=Graph Attention Networks;citation_author=Petar Velickovic;citation_author=Guillem Cucurull;citation_author=Arantxa Casanova;citation_author=Adriana Romero;citation_author=Pietro Lio;citation_author=Yoshua Bengio;citation_publication_date=2017;">
    <meta name="citation_reference" content="citation_title=Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks;citation_author=Juho Lee;citation_author=Yoonho Lee;citation_author=Jungtaek Kim;citation_author=Adam R Kosiorek;citation_author=Seungjin Choi;citation_author=Yee Whye Teh;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Transformers are Graph Neural Networks;citation_author=Chaitanya Joshi;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Using Attribution to Decode Dataset Bias in Neural Network Models for Chemistry;citation_author=Kevin McCloskey;citation_author=Ankur Taly;citation_author=Federico Monti;citation_author=Michael P Brenner;citation_author=Lucy Colwell;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=GNNExplainer: Generating Explanations for Graph Neural Networks;citation_author=Zhitao Ying;citation_author=Dylan Bourgeois;citation_author=Jiaxuan You;citation_author=Marinka Zitnik;citation_author=Jure Leskovec;citation_publication_date=2019;citation_volume=32;">
    <meta name="citation_reference" content="citation_title=Explainability Methods for Graph Convolutional Neural Networks;citation_author=Phillip E Pope;citation_author=Soheil Kolouri;citation_author=Mohammad Rostami;citation_author=Charles E Martin;citation_author=Heiko Hoffmann;citation_publication_date=2019;citation_journal_title=2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR);">
    <meta name="citation_reference" content="citation_title=Evaluating Attribution for Graph Neural Networks;citation_author=Benjamin Sanchez-Lengeling;citation_author=Jennifer Wei;citation_author=Brian Lee;citation_author=Emily Reif;citation_author=Wesley Qian;citation_author=Yiliu Wang;citation_author=Kevin James McCloskey;citation_author=Lucy Colwell;citation_author=Alexander B Wiltschko;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Variational Graph Auto-Encoders;citation_author=Thomas N Kipf;citation_author=Max Welling;citation_publication_date=2016;">
    <meta name="citation_reference" content="citation_title=GraphRNN: Generating Realistic Graphs with Deep Auto-regressive Models;citation_author=Jiaxuan You;citation_author=Rex Ying;citation_author=Xiang Ren;citation_author=William L Hamilton;citation_author=Jure Leskovec;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Optimization of Molecules via Deep Reinforcement Learning;citation_author=Zhenpeng Zhou;citation_author=Steven Kearnes;citation_author=Li Li;citation_author=Richard N Zare;citation_author=Patrick Riley;citation_publication_date=2019;citation_journal_title=Sci. Rep.;citation_volume=9;citation_number=1;">
    <meta name="citation_reference" content="citation_title=Self-Referencing Embedded Strings (SELFIES): A 100% robust molecular string representation;citation_author=Mario Krenn;citation_author=Florian Hase;citation_author=Akshatkumar Nigam;citation_author=Pascal Friederich;citation_author=Alan Aspuru-Guzik;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=GraphGen: A Scalable Approach to Domain-agnostic Labeled Graph Generation;citation_author=Nikhil Goyal;citation_author=Harsh Vardhan Jain;citation_author=Sayan Ranu;citation_publication_date=2020;">
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
<title>A Gentle Introduction to Graph Neural Networks</title>

<link rel="stylesheet" href="style.e308ff8e.css">
<link rel="stylesheet" href="layerwise_trace.d38144f3.css">
<link rel="stylesheet" href="shuffle.90a7da43.css">
<link rel="stylesheet" href="text-as-graph.146f5ac8.css">
<link rel="stylesheet" href="pca-layers.889c7e67.css">
<link rel="stylesheet" href="gnn-playground.7fda89e6.css">
<link rel="stylesheet" href="mols-as-graph.f8d43714.css">
<link rel="stylesheet" href="shuffle-sm.e4a48acb.css">
<link rel="stylesheet" href="table.0b6daf45.css">
<link rel="stylesheet" href="graph-description.c0d85959.css">
<link rel="stylesheet" href="graph-description-embeddings.95e72025.css">


<d-front-matter>
  <script type="text/json">
    {
    "title": "A Gentle Introduction to Graph Neural Networks",
    "description": "What components are needed for building learning algorithms that leverage the structure and properties of graphs?",
    "authors": [{
      "author": "Benjamin Sanchez-Lengeling",
      "affiliations": [{
        "name": "Google Research",
        "affiliationURL": "https://research.google/teams/brain/"
      }]
    }, {
      "author": "Emily Reif",
      "affiliations": [{
        "name": "Google Research",
        "affiliationURL": "https://research.google/teams/brain/"
      }]
    }, {
      "author": "Adam Pearce",
      "authorURL": "https://roadtolarissa.com",
      "affiliations": [{
        "name": "Google Research",
        "affiliationURL": "https://research.google/teams/brain/"
      }]
    }, {
      "author": "Alexander B. Wiltschko",
      "affiliations": [{
        "name": "Google Research",
        "affiliationURL": "https://research.google/teams/brain/"
      }]
    }]
    }
  </script>
</d-front-matter>




<d-title>
  <h1>A Gentle Introduction to Graph Neural Networks</h1>
  <p>Neural networks have been adapted to leverage the structure and properties of graphs. We explore the components needed for building a graph neural network - and motivate the design choices behind them.</p>

  <figure class="teaser">
    <div id="layerwise-trace"> </div>
    <figcaption>
Hover over a node in the diagram below to see how it accumulates information from nodes around it through the layers of the network.
    </figcaption>
</figure>
</d-title>
<d-byline>
  <div class="byline grid">
    <div class="authors-affiliations grid">
      <h3>Authors</h3>
      <h3>Affiliations</h3>
      
        <p class="author">
          
            <span class="name">Benjamin Sanchez-Lengeling</span>
        </p>
        <p class="affiliation">
        <span class="affiliation">Google Research</span>
        </p>
      
        <p class="author">
          
            <span class="name">Emily Reif</span>
        </p>
        <p class="affiliation">
        <span class="affiliation">Google Research</span>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://roadtolarissa.com">Adam Pearce</a>
        </p>
        <p class="affiliation">
        <span class="affiliation">Google Research</span>
        </p>
      
        <p class="author">
          
            <span class="name">Alexander B. Wiltschko</span>
        </p>
        <p class="affiliation">
        <span class="affiliation">Google Research</span>
        </p>
      
    </div>
    <div>
      <h3>Published</h3>
      
        <p>Sept. 2, 2021</p> 
    </div>
    <div>
      <h3>DOI</h3>
      
        <p><a href="https://doi.org/10.23915/distill.00033">10.23915/distill.00033</a></p>
    </div>
  </div>
</d-byline>

<d-article>

<p><em>This article is one of two Distill publications about graph neural networks. Take a look at <a href="https://distill.pub/2021/understanding-gnns/">Understanding Convolutions on Graphs</a><d-cite key="daigavane2021understanding"></d-cite> to understand how convolutions over images generalize naturally to convolutions over graphs.</em></p>
<p>Graphs are all around us; real world objects are often defined in terms of their connections to other things. A set of objects, and the connections between them, are naturally expressed as a <em>graph</em>. Researchers have developed neural networks that operate on graph data (called graph neural networks, or GNNs) for over a decade<d-cite key="Scarselli2009-ku"></d-cite>. Recent developments have increased their capabilities and expressive power. We are starting to see practical applications in areas such as antibacterial discovery <d-cite key="Stokes2020-az"></d-cite>, physics simulations  <d-cite key="Sanchez-Gonzalez2020-yo"></d-cite>, fake news detection <d-cite key="Monti2019-tf"></d-cite>, traffic prediction <d-cite key="undated-sy"></d-cite> and recommendation systems <d-cite key="Eksombatchai2017-il"></d-cite>.</p>
<p>This article explores and explains modern graph neural networks. We divide this work into four parts. First, we look at what kind of data is most naturally phrased as a graph, and some common examples. Second, we explore what makes graphs different from other types of data, and some of the specialized choices we have to make when using graphs. Third, we build a modern GNN, walking through each of the parts of the model, starting with historic modeling innovations in the field. We move gradually from a bare-bones implementation to a state-of-the-art GNN model. Fourth and finally, we provide a GNN playground where you can play around with a real-word task and dataset to build a stronger intuition of how each component of a GNN model contributes to the predictions it makes.</p>
<p>To start, let’s establish what a graph is. A graph represents the relations (<em>edges</em>) between a collection of entities (<em>nodes</em>). </p>
<figure><div id="graph-description" style="margin-bottom:0.25cm;"></div>
<figcaption>
Three types of attributes we might find in a graph, hover over to highlight each attribute. Other types of graphs and attributes are explored in the <a href="#other-types-of-graphs-multigraphs-hypergraphs-hypernodes">Other types of graphs</a> section.
</figcaption></figure>


<p>To further describe each node, edge or the entire graph, we can store information in each of these pieces of