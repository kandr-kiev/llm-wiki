---

source_url: https://distill.pub/selforg/2021/textures
ingested: 2026-07-10
sha256: 09183f79a81dd370e26df8eeab39b224c4be779395e2b28adaef1dd292c43422
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
  <!-- <script src="/template.v2.js"></script> -->
  <style>
  </style>
  <script src="twgl.min.js"></script>
  <script type="module" src="./ca.js"></script>
  <script type="module" src="./demo.js"></script>
<link rel="stylesheet" href="https://distill.pub/third-party/katex/katex.min.css" crossorigin="anonymous">
    
    <link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA99JREFUeNrsG4t1ozDMzQSM4A2ODUonKBucN2hugtIJ6E1AboLcBiQTkJsANiAb9OCd/OpzMWBJBl5TvaeXPiiyJetry0J8wW3D3QpjRh3GjneXDq+fSQA9s2mH9x3KDhN4foJfCb8N/Jrv+2fnDn8vLRQOplWHVYdvHZYdZsBcZP1vBmh/n8DzEmhUQDPaOuP9pFuY+JwJHwHnCLQE2tnWBGEyXozY9xCUgHMhhjE2I4heVWtgIkZ83wL6Qgxj1obfWBxymPwe+b00BCCRNPbwfb60yleAkkBHGT5AEehIYz7eJrFDMF9CvH4wwhcGHiHMneFvLDQwlwvMLQq58trRcYBWfYn0A0OgHWQUSu25mE+BnoYKnnEJoeIWAifzOv7vLWd2ZKRfWAIme3tOiUaQ3UnLkb0xj1FxRIeEGKaGIHOs9nEgLaaA9i0JRYo1Ic67wJW86KSKE/ZAM8KuVMk8ITVhmxUxJ3Cl2xlm9Vtkeju1+mpCQNxaEGNCY8bs9X2YqwNoQeGjBWut/ma0QAWy/TqAsHx9wSya3I5IRxOfTC+leG+kA/4vSeEcGBtNUN6byhu3+keEZCQJUNh8MAO7HL6H8pQLnsW/Hd4T4lv93TPjfM7A46iEEqbB5EDOvwYNW6tGNZzT/o+CZ6sqZ6wUtR/wf7mi/VL8iNciT6rHih48Y55b4nKCHJCCzb4y0nwFmin3ZEMIoLfZF8F7nncFmvnWBaBj7CGAYA/WGJsUwHdYqVDwAmNsUgAx4CGgAA7GOOxADYOFWOaIKifuVYzmOpREqA21Mo7aPsgiY1PhOMAmxtR+AUbYH3Id2wc0SAFIQTsn9IUGWR8k9jx3vtXSiAacFxTAGakBk9UudkNECd6jLe+6HrshshvIuC6IlLMRy7er+JpcKma24SlE4cFZSZJDGVVrsNvitQhQrDhW0jfiOLfFd47C42eHT56D/BK0To+58Ahj+cAT8HT1UWlfLZCCd/uKawzU0Rh2EyIX/Icqth3niG8ybNroezwe6khdCNxRN+l4XGdOLVLlOOt2hTRJlr1ETIuMAltVTMz70mJrkdGAaZLSmnBEqmAE32JCMmuTlCnRgsBENtOUpHhvvsYIL0ibnBkaC6QvKcR7738GKp0AKnim7xgUSNv1bpS8QwhBt8r+EP47v/oyRK/S34yJ9nT+AN0Tkm4OdB9E4BsmXM3SnMlRFUrtp6IDpV2eKzdYvF3etm3KhQksbOLChGkSmcBdmcEwvqkrMy5BzL00NZeu3qPYJOOuCc+5NjcWKXQxFvTa3NoXJ4d8in7fiAUuTt781dkvuHX4K8AA2Usy7yNKLy0AAAAASUVORK5CYII=
">
    <link href="/rss.xml" rel="alternate" type="application/rss+xml" title="Articles from Distill">
  
    <title>Self-Organising Textures</title>
    
    <link rel="canonical" href="https://distill.pub/selforg/2021/textures">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="Neural Cellular Automata learn to generate textures, exhibiting surprising properties.">
    <meta property="article:published" itemprop="datePublished" content="2021-02-11">
    <meta property="article:created" itemprop="dateCreated" content="2021-02-11">
    
    <meta property="article:modified" itemprop="dateModified" content="2021-05-07T17:13:43.000Z">
    
    <meta property="article:author" content="Eyvind Niklasson">
    <meta property="article:author" content="Alexander Mordvintsev">
    <meta property="article:author" content="Ettore Randazzo">
    <meta property="article:author" content="Michael Levin">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="Self-Organising Textures">
    <meta property="og:description" content="Neural Cellular Automata learn to generate textures, exhibiting surprising properties.">
    <meta property="og:url" content="https://distill.pub/selforg/2021/textures">
    <meta property="og:image" content="https://distill.pub/selforg/2021/textures/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Self-Organising Textures">
    <meta name="twitter:description" content="Neural Cellular Automata learn to generate textures, exhibiting surprising properties.">
    <meta name="twitter:url" content="https://distill.pub/selforg/2021/textures">
    <meta name="twitter:image" content="https://distill.pub/selforg/2021/textures/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="Self-Organising Textures">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/selforg/2021/textures">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="2">
    <meta name="citation_firstpage" content="e00027.003">
    <meta name="citation_doi" content="10.23915/distill.00027.003">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/02/11">
    <meta name="citation_publication_date" content="2021/02/11">
    <meta name="citation_author" content="Niklasson, Eyvind">
    <meta name="citation_author_institution" content="Google">
    <meta name="citation_author" content="Mordvintsev, Alexander">
    <meta name="citation_author_institution" content="Google">
    <meta name="citation_author" content="Randazzo, Ettore">
    <meta name="citation_author_institution" content="Google">
    <meta name="citation_author" content="Levin, Michael">
    <meta name="citation_author_institution" content="Tufts">
    <meta name="citation_reference" content="citation_title=Growing Neural Cellular Automata;citation_author=Alexander Mordvintsev;citation_author=Ettore Randazzo;citation_author=Eyvind Niklasson;citation_author=Michael Levin;citation_publication_date=2020;citation_journal_title=Distill;citation_volume=5;citation_number=2;">
    <meta name="citation_reference" content="citation_title=Image segmentation via Cellular Automata;citation_author=Mark Sandler;citation_author=Andrey Zhmoginov;citation_author=Liangcheng Luo;citation_author=Alexander Mordvintsev;citation_author=Ettore Randazzo;citation_author=Blaise Agúera y. Arcas;citation_publication_date=2020;citation_arxiv_id=2008.04965;">
    <meta name="citation_reference" content="citation_title=Self-classifying MNIST Digits;citation_author=Ettore Randazzo;citation_author=Alexander Mordvintsev;citation_author=Eyvind Niklasson;citation_author=Michael Levin;citation_author=Sam Greydanus;citation_publication_date=2020;citation_journal_title=Distill;citation_volume=5;citation_number=8;">
    <meta name="citation_reference" content="citation_title=Differentiable Image Parameterizations;citation_author=Alexander Mordvintsev;citation_author=Nicola Pezzotti;citation_author=Ludwig Schubert;citation_author=Chris Olah;citation_publication_date=2018;citation_journal_title=Distill;citation_volume=3;citation_number=7;">
    <meta name="citation_reference" content="citation_title=The chemical basis of morphogenesis;citation_author=Alan Mathison Turing;citation_publication_date=1952;citation_journal_title=Philosophical transactions of the Royal Society of London. Series B, Biological sciences;citation_volume=237;citation_number=641;">
    <meta name="citation_reference" content="citation_title=Turing patterns in development: what about the horse part?;citation_author=Luciano Marcon;citation_author=James Sharpe;citation_publication_date=2012;citation_journal_title=Current opinion in genetics &amp;amp; development;citation_volume=22;citation_number=6;">
    <meta name="citation_reference" content="citation_title=A unified design space of synthetic stripe-forming networks;citation_author=Yolanda Schaerli;citation_author=Andreea Munteanu;citation_author=Magüi Gili;citation_author=James Cotterell;citation_author=James Sharpe;citation_author=Mark Isalan;citation_publication_date=2014;citation_journal_title=Nature communications;citation_volume=5;">
    <meta name="citation_reference" content="citation_title=On the Formation of Digits and Joints during Limb Development;citation_author=Tom W. Hiscock;citation_author=Patrick Tschopp;citation_author=Clifford J. Tabin;citation_publication_date=2017;citation_journal_title=Developmental cell;citation_volume=41;citation_number=5;">
    <meta name="citation_reference" content="citation_title=Modeling digits. Digit patterning is controlled by a Bmp-Sox9-Wnt Turing network modulated by morphogen gradients;citation_author=J. Raspopovic;citation_author=L. Marcon;citation_author=L. Russo;citation_author=J. Sharpe;citation_publication_date=2014;citation_journal_title=Science;citation_volume=345;citation_number=6196;">
    <meta name="citation_reference" content="citation_title=Pattern formation mechanisms of self-organizing reaction-diffusion systems;citation_author=Amit N. Landge;citation_author=Benjamin M. Jordan;citation_author=Xavier Diego;citation_author=Patrick Müller;citation_publication_date=2020;citation_journal_title=Developmental biology;citation_volume=460;citation_number=1;">
    <meta name="citation_reference" content="citation_title=Bioelectric gene and reaction networks: computational modelling of genetic, biochemical and bioelectrical dynamics in pattern regulation;citation_author=Alexis Pietak;citation_author=Michael Levin;citation_publication_date=2017;citation_journal_title=Journal of the Royal Society, Interface / the Royal Society;citation_volume=14;citation_number=134;">
    <meta name="citation_reference" content="citation_title=Turing-like patterns can arise from purely bioelectric mechanisms;citation_author=Micah Brodsky;citation_journal_title=Draft;">
    <meta name="citation_reference" content="citation_title=Dissipative structures in biological systems: bistability, oscillations, spatial patterns and waves;citation_author=Albert Goldbeter;citation_publication_date=2018;citation_journal_title=Philosophical transactions. Series A, Mathematical, physical, and engineering sciences;citation_volume=376;citation_number=2124;">
    <meta name="citation_reference" content="citation_title=Gene networks and liar paradoxes;citation_author=Mark Isalan;citation_publication_date=2009;citation_journal_title=BioEssays: news and reviews in molecular, cellular and developmental biology;citation_volume=31;citation_number=10;">
    <meta name="citation_reference" content="citation_title=Texture Synthesis Using Convolutional Neural Networks;citation_author=Leon A. Gatys;citation_author=Alexander S. Ecker;citation_author=Matthias Bethge;citation_publication_date=2015;citation_arxiv_id=1505.07376;">
    <meta name="citation_reference" content="citation_title=The chemical basis of morphogenesis. 1953;citation_author=A. M. Turing;citation_publication_date=1990;citation_journal_title=Bulletin of mathematical biology;citation_volume=52;citation_number=1-2;">
    <meta name="citation_reference" content="citation_title=Pattern formation by interacting chemical fronts;citation_author=K. J. Lee;citation_author=W. D. McCormick;citation_author=Q. Ouyang;citation_author=H. L. Swinney;citation_publication_date=1993;citation_journal_title=Science;citation_volume=261;citation_number=5118;">
    <meta name="citation_reference" content="citation_title=Complex patterns in a simple system;citation_author=J. E. Pearson;citation_publication_date=1993;citation_journal_title=Science;citation_volume=261;citation_number=5118;">
    <meta name="citation_reference" content="citation_title=Very Deep Convolutional Networks for Large-Scale Image Recognition;citation_author=Karen Simonyan;citation_author=Andrew Zisserman;citation_publication_date=2014;citation_arxiv_id=1409.1556;">
    <meta name="citation_reference" content="citation_title=Adam: A Method for Stochastic Optimization;citation_author=Diederik P. Kingma;citation_author=Jimmy Ba;citation_publication_date=2014;citation_arxiv_id=1412.6980;">
    <meta name="citation_reference" content="citation_title=Describing Textures in the Wild;citation_author=Mircea Cimpoi;citation_author=Subhransu Maji;citation_author=Iasonas Kokkinos;citation_author=Sammy Mohamed;citation_author=Andrea Vedaldi;citation_publication_date=2013;citation_arxiv_id=1311.3618;">
    <meta name="citation_reference" content="citation_title=The texture lexicon: Understanding the categorization of visual texture terms and their relationship to texture images;citation_author=Nalini Bhushan;citation_author=A. Ravishankar Rao;citation_author=Gerald L. Lohse;citation_publication_date=1997;citation_journal_title=Cognitive science;citation_volume=21;citation_number=2;">
    <meta name="citation_reference" content="citation_title=Re-membering the body: applications of computational neuroscience to the top-down control of regeneration of limbs and other complex organs;citation_author=G. Pezzulo;citation_author=M. Levin;citation_publication_date=2015;citation_journal_title=Integrative biology: quantitative biosciences from nano to macro;citation_volume=7;citation_number=12;">
    <meta name="citation_reference" content="citation_title=Embryonic Development and Induction;citation_author=Hans Speman;citation_publication_date=1938;citation_journal_title=The American Journal of the Medical Sciences;citation_volume=196;citation_number=5;">
    <meta name="citation_reference" content="citation_title=Communication, Memory, and Development;citation_author=Stephen Grossberg;citation_publication_date=1978;">
    <meta name="citation_reference" content="citation_title=WaveFunctionCollapse;citation_author=Maxim Gumin;">
    <meta name="citation_reference" content="citation_title=Texture Networks: Feed-forward Synthesis of Textures and Stylized Images;citation_author=Dmitry Ulyanov;citation_author=Vadim Lebedev;citation_author=Andrea Vedaldi;citation_author=Victor Lempitsky;citation_publication_date=2016;citation_arxiv_id=1603.03417;">
    <meta name="citation_reference" content="citation_title=TextureGAN: Controlling deep image synthesis with texture patches;citation_author=Wenqi Xian;citation_author=Patsorn Sangkloy;citation_author=Varun Agrawal;citation_author=Amit Raj;citation_author=Jingwan Lu;citation_author=Chen Fang;citation_author=Fisher Yu;citation_author=James Hays;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Interactive evolution of camouflage;citation_author=Craig Reynolds;citation_publication_date=2011;citation_journal_title=Artificial life;citation_volume=17;citation_number=2;">
    <meta name="citation_reference" content="citation_title=A parametric texture model based on joint statistics of complex wavelet coefficients;citation_author=Javier Portilla;citation_author=Eero P. Simoncelli;citation_publication_date=2000;">
    <meta name="citation_reference" content="citation_title=Trainable Nonlinear Reaction Diffusion: A Flexible Framework for Fast and Effective Image Restoration;citation_author=Yunjin Chen;citation_author=Thomas Pock;citation_publication_date=2017;citation_journal_title=IEEE transactions on pattern analysis and machine intelligence;citation_volume=39;citation_number=6;">
    <meta name="citation_reference" content="citation_title=The evolutionary significance of butterfly eyespots;citation_author=Ullasa Kodandaramaiah;citation_publication_date=2011;citation_journal_title=Behavioral ecology: official journal of the International Society for Behavioral Ecology;citation_volume=22;citation_number=6;">
    <meta name="citation_reference" content="citation_title=Live Cell Imaging of Butterfly Pupal and Larval Wings In Vivo;citation_author=Yoshikazu Ohno;citation_author=Joji M. Otaki;citation_publication_date=2015;citation_journal_title=PloS one;citation_volume=10;citation_number=6;">
    <meta name="citation_reference" content="citation_title=Focusing on butterfly eyespot focus: uncoupling of white spots from eyespot bodies in nymphalid butterflies;citation_author=Masaki Iwata;citation_author=Joji M. Otaki;citation_publication_date=2016;citation_journal_title=SpringerPlus;citation_volume=5;citation_number=1;">
    <meta name="citation_reference" content="citation_title=OpenAI Microscope;citation_author=Ludwig Schubert;citation_author=Michael Petrov;citation_author=Shan Carter;citation_author=Nick Cammarata;citation_author=Gabriel Goh;citation_author=Chris Olah;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=The neural origins of shell structure and pattern in aquatic mollusks;citation_author=Alistair Boettiger;citation_author=Bard Ermentrout;citation_author=George Oster;citation_publication_date=2009;citation_journal_title=Proceedings of the National Academy of Sciences of the United States of America;citation_volume=106;citation_number=16;">
    <meta name="citation_reference" content="citation_title=Emergent complexity in simple neural systems;citation_author=Alistair N. Boettiger;citation_author=George Oster;citation_publication_date=2009;citation_journal_title=Communicative &amp;amp; integrative biology;citation_volume=2;citation_number=6;">
    <meta name="citation_reference" content="citation_title=Going deeper with convolutions;citation_author=Christian Szegedy;citation_author=Wei Liu;citation_author=Yangqing Jia;citation_author=Pierre Sermanet;citation_author=Scott Reed;citation_author=Dragomir Anguelov;citation_author=Dumitru Erhan;citation_author=Vincent Vanhoucke;citation_author=Andrew Rabinovich;citation_publication_date=2015;citation_arxiv_id=1409.4842;">
    <meta name="citation_reference" content="citation_title=Stable and Controllable Neural Texture Synthesis and Style Transfer Using Histogram Losses;citation_author=Eric Risser;citation_author=Pierre Wilmot;citation_author=Connelly Barnes;citation_publication_date=2017;citation_arxiv_id=1701.08893;">
    <meta name="citation_reference" content="citation_title=Stem cell migration and mechanotransduction on linear stiffness gradient hydrogels;citation_author=William J. Hadden;citation_author=Jennifer L. Young;citation_author=Andrew W. Holle;citation_author=Meg L. McFetridge;citation_author=Du Yong Kim;citation_author=Philip Wijesinghe;citation_author=Hermes Taylor-Weiner;citation_author=Jessica H. Wen;citation_author=Andrew R. Lee;citation_author=Karen Bieback;citation_author=et al.;citation_publication_date=2017;citation_journal_title=Proceedings of the National Academy of Sciences of the United States of America;citation_volume=114;citation_number=22;">
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
      "title": "Self-Organising Textures",
      "description": "Neural Cellular Automata learn to generate textures, exhibiting surprising properties.",
      "authors": [
        {
          "author": "Eyvind Niklasson",
          "authorURL": "https://eyvind.me/",
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
          "author": "Ettore Randazzo",
          "authorURL": "",
          "affiliation": "Google",
          "affiliationURL": "https://ai.google/"
       },
       {
          "author": "Michael Levin",
          "authorURL": "https://ase.tufts.edu/biology/labs/levin/",
          "affiliation": "Tufts",
          "affiliationURL": "https://tufts.edu/"
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
      display: inline-block;
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

    span.tf-span {
      background-image: url(images/tf.svg);
      background-repeat: no-repeat;
      background-size: 15px;
      background-position-y: 0px;
      display: inline-block;
      padding-left: 19px;
      border-radius: 4px;
      text-decoration: none;
    }

    span.pytorch-span {
      background-image: url(images/pytorch.svg);
      background-repeat: no-repeat;
      background-size: 83px;
      background-position-x: -32px;
      background-position-y: -1px;
      display: inline-block;
      padding-left: 19px;
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
        grid-column-start: 2;
        grid-column-end: 6;
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

    /*remove h4 header uppercase (present in distill template)*/
    d-article h4 {
      text-transform:none;
    }

    /* so the headings in the appendix are on one line in narrow screens */
    @media(max-width: 1000px) {
      d-appendix h3 {
        grid-column: text !important; 
      } 
    }

  </style>
  <script>
  // hack to edit font size in code snippets. guaranteed a better way to do 
  // this, but I'm not a webdev
  window.onload = function() {
    setTimeout(() => { document.querySelectorAll("d-code").forEach(function(e) {e.shadowRoot.querySelector('#code-container').style.fontSize = "0.7em"}); }, 3000);
  }
  </script>
  <script>
    //Autoplay videos when they're in view
  </script>
  <d-title>
    <h1>Self-Organising Textures</h1>
    <p>Neural Cellular Automata Model of Pattern Formation</p>

  
<svg style="display: none;" xmlns="http://www.w3.org/2000/svg">
    <symbol id="playIcon" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path><path d="M0 0h24v24H0z" fill="none"></path></symbol>
    <symbol id="pauseIcon" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"></path><path d="M0 0h24v24H0z" fill="none"></path></symbol>
    <symbol id="resetIcon" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"></path><path d="M12 5V1L7 6l5 5V7c3.31 0 6 2.69 6 6s-2.69 6-6 6-6-2.69-6-6H4c0 4.42 3.58 8 8 8s8-3.58 8-8-3.58-8-8-8z"></path></symbol>
    <symbol id="zoomInIcon" viewBox="0 0 24 24"><path d="M0 0h24v24H0V0z" fill="none"></path><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path><path d="M12 10h-2v2H9v-2H7V9h2V7h1v2h2v1z"></path></symbol>
    <symbol id="zoomOutIcon" viewBox="0 0 24 24"><path d="M0 0h24v24H0V0z" fill="none"></path><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14zM7 9h5v1H7z"></path></symbol>
    <symbol id="mouse" viewBox="0 0 100 100"><path d="M32,41v18c0,9.9,8.1,18,18,18c9.9,0,18-8.1,18-18V41c0-9.9-8.1-18-18-18C40.1,23,32,31.1,32,41z M50,27c7.7,0,14,6.3,14,14  v18c0,7.7-6.3,14-14,14s-14-6.3-14-14V41C36,33.3,42.3,27,50,27z"></path><path d="M50,44c1.1,0,2-0.9,2-2v-6c0-1.1-0.9-2-2-2s-2,0.9-2,2v6C48,43.1,48.9,44,50,44z"></path><path d="M48.6,92.4C49,92.8,49.5,93,50,93s1-0.2,1.4-0.6l5-5c0.8-0.8,0.8-2,0-2.8s-2-0.8-2.8,0L50,88.2l-3.6-3.6  c-0.8-0.8-2-0.8-2.8,0c-0.8,0.8-0.8,2,0,2.8L48.6,92.4z"></path><path d="M48.6,7.6l-5,5c-0.8,0.8-0.8,2,0,2.8C44,15.8,44.5,16,45,16s1-0.2,1.4-0.6l3.6-3.6l3.6,3.6C54,15.8,54.5,16,55,16  s1-0.2,1.4-0.6c0.8-0.8,0.8-2,0-2.8l-5-5C50.6,6.8,49.4,6.8,48.6,7.6z"></path></symbol>
</svg>

<style>
#demo {
    font-size: 14px;
    user-select: none;
    grid-template-columns: auto;
    grid-template-rows: auto auto;
    grid-auto-flow: column;
    row-gap: 10px;
}

.hint a {
  color: inherit;
}

@media (min-width: 1180px) {
  #demo {
    grid-template-columns: 512px 1fr;
    grid-template-rows: auto;
  }
  #pattern-controls {
    grid-row: 1;
  }
}

#demo-canvas {
    border: 1px solid lightgrey;
    image-rendering: pixelated;
    touch-action: none;
    width: 100%;
}

#pattern-controls {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: min-content minmax(0, 0.3fr) min-content minmax(0, 0.3fr) minmax(0, 0.32fr) minmax(0, 0.1fr);
    /*row-gap: 20px;*/
    overflow: hidden;
}

@media (max-width: 1180px) {
  #pattern-controls {
    grid-template-rows: min-content minmax(0, 0.4fr) min-content minmax(0, 0.4fr) min-content minmax(0, 0.1fr);
  }
}


.pattern-selector::-webkit-scrollbar {
    display: none;
}

#demo-tip{
    display: grid;
    grid-template-columns: 40px auto;
    align-items: center;
    column-gap: 10px;
    margin-bottom: 20px;
}
#pointer {
    width: 40px;
}
#status {
    font-size: 12px;
    color: rgba(0, 0, 0, 0.6);
    font-family: monospace;
}
#model-hints {
    color: rgba(0, 0, 0, 0.6);
    grid-column: 1/3;
}
#model-hints span {
    display: none;
}
.hint {
    color: rgba(0, 0, 0, 0.6);
    line-height: 1.4em;
    user-select: text;
}

input[type=range] {
  -webkit-appearance: none; /* Hides the slider so that custom slider can be made */
  width: 95%; /* Specific width is required for Firefox. */
  background: transparent; /* Otherwise white in Chrome */
  margin-bottom: 8px;
}

.hint a {
  font-size: 90%;
}

@media (max-width: 350px) {
  .hint a {
    font-size: 75%;
  }
}

input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
}

input[type=range]:focus {
  outline: none; /* Removes the blue border. You should probably do some kind of focus styling for accessibility reasons though. */
}

input[type=range]::-ms-track {
  width: 100%;
  cursor: pointer;

  /* Hides the slider so custom styles can be added */
  background: transparent;
  border-color: transparent;
  color: transparent;
}

/* Thumb */

/* Special styling for WebKit/Blink */
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  height: 14px;
  width: 14px;
  border-radius: 50%;
  background: steelblue;
  cursor: pointer;
  margin-top: -6px; /* You need to specify a margin in Chrome, but in Firefox and IE it is automatic */
}

/* All the same stuff for Firefox */
input[type=range]::-moz-range-thumb {
  height: 14px;
  width: 14px;
  border-radius: 50%;
  background: steelblue;
  cursor: pointer;
  border: none;
}

/* All the same stuff for IE */
input[type=range]::-ms-thumb {
  height: 14px;
  width: 14px;
  border-radius: 50%;
  background: grey;
  cursor: pointer;
}

/* Track */

input[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 3px;
  cursor: pointer;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 2px;
  border: none;
}

input[type=range]:focus::-webkit-slider-runnable-track {
  background: rgba(0, 0, 0, 0.15);
}

input[type=range]::-moz-range-track {
  width: 100%;
  height: 3px;
  cursor: pointer;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 2px;
  border: none;
}

input[type=range]::-ms-track {
  width: 100%;
  height: 3px;
  cursor: pointer;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 2px;
  border: none;
}
input[type=range]::-ms-fill-lower {
  background: rgba(0, 0, 0, 0.1);
}
input[type=range]:focus::-ms-fill-lower {
  background: rgba(0, 0, 0, 0.1);
}
input[type=range]::-ms-fill-upper {
  background: rgba(0, 0, 0, 0.1);
}
input[type=range]:focus::-ms-fill-upper {
  background: rgba(0, 0, 0, 0.1);
}

input[type="radio"] {
    background-color: steelblue;
}

#colab-hero-div { 
  /*grid-column: 1/3;*/
  border-top: 1px solid rgba(0, 0, 0, 0.1);