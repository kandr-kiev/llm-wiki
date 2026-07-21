---

source_url: https://distill.pub/2020/circuits/curve-circuits
ingested: 2026-07-10
sha256: f843a35e79715fdf30887114bbf0bc1da4c137bf2aa7de3bdd53df786c8cba61
blog_source: Distill AI
---

<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1440"><meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1"><script>
window.addEventListener('WebComponentsReady', function() {
  console.warn('WebComponentsReady');
  const loaderTag = document.createElement('script');
  loaderTag.src = 'https://distill.pub/template.v2.js';
  document.head.insertBefore(loaderTag, document.head.firstChild);
});
</script><script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.0.17/webcomponents-loader.js"></script>
  
  
  <link rel="stylesheet" href="styles.css">
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

    
    <link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA99JREFUeNrsG4t1ozDMzQSM4A2ODUonKBucN2hugtIJ6E1AboLcBiQTkJsANiAb9OCd/OpzMWBJBl5TvaeXPiiyJetry0J8wW3D3QpjRh3GjneXDq+fSQA9s2mH9x3KDhN4foJfCb8N/Jrv+2fnDn8vLRQOplWHVYdvHZYdZsBcZP1vBmh/n8DzEmhUQDPaOuP9pFuY+JwJHwHnCLQE2tnWBGEyXozY9xCUgHMhhjE2I4heVWtgIkZ83wL6Qgxj1obfWBxymPwe+b00BCCRNPbwfb60yleAkkBHGT5AEehIYz7eJrFDMF9CvH4wwhcGHiHMneFvLDQwlwvMLQq58trRcYBWfYn0A0OgHWQUSu25mE+BnoYKnnEJoeIWAifzOv7vLWd2ZKRfWAIme3tOiUaQ3UnLkb0xj1FxRIeEGKaGIHOs9nEgLaaA9i0JRYo1Ic67wJW86KSKE/ZAM8KuVMk8ITVhmxUxJ3Cl2xlm9Vtkeju1+mpCQNxaEGNCY8bs9X2YqwNoQeGjBWut/ma0QAWy/TqAsHx9wSya3I5IRxOfTC+leG+kA/4vSeEcGBtNUN6byhu3+keEZCQJUNh8MAO7HL6H8pQLnsW/Hd4T4lv93TPjfM7A46iEEqbB5EDOvwYNW6tGNZzT/o+CZ6sqZ6wUtR/wf7mi/VL8iNciT6rHih48Y55b4nKCHJCCzb4y0nwFmin3ZEMIoLfZF8F7nncFmvnWBaBj7CGAYA/WGJsUwHdYqVDwAmNsUgAx4CGgAA7GOOxADYOFWOaIKifuVYzmOpREqA21Mo7aPsgiY1PhOMAmxtR+AUbYH3Id2wc0SAFIQTsn9IUGWR8k9jx3vtXSiAacFxTAGakBk9UudkNECd6jLe+6HrshshvIuC6IlLMRy7er+JpcKma24SlE4cFZSZJDGVVrsNvitQhQrDhW0jfiOLfFd47C42eHT56D/BK0To+58Ahj+cAT8HT1UWlfLZCCd/uKawzU0Rh2EyIX/Icqth3niG8ybNroezwe6khdCNxRN+l4XGdOLVLlOOt2hTRJlr1ETIuMAltVTMz70mJrkdGAaZLSmnBEqmAE32JCMmuTlCnRgsBENtOUpHhvvsYIL0ibnBkaC6QvKcR7738GKp0AKnim7xgUSNv1bpS8QwhBt8r+EP47v/oyRK/S34yJ9nT+AN0Tkm4OdB9E4BsmXM3SnMlRFUrtp6IDpV2eKzdYvF3etm3KhQksbOLChGkSmcBdmcEwvqkrMy5BzL00NZeu3qPYJOOuCc+5NjcWKXQxFvTa3NoXJ4d8in7fiAUuTt781dkvuHX4K8AA2Usy7yNKLy0AAAAASUVORK5CYII=
">
    <link href="/rss.xml" rel="alternate" type="application/rss+xml" title="Articles from Distill">
  
    <title>Curve Circuits</title>
    
    <link rel="canonical" href="https://distill.pub/2020/circuits/curve-circuits">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="Reverse engineering the curve detection algorithm from InceptionV1 and reimplementing it from scratch.">
    <meta property="article:published" itemprop="datePublished" content="2021-01-30">
    <meta property="article:created" itemprop="dateCreated" content="2021-01-30">
    
    <meta property="article:modified" itemprop="dateModified" content="2021-02-04T22:18:06.000Z">
    
    <meta property="article:author" content="Nick Cammarata">
    <meta property="article:author" content="Gabriel Goh">
    <meta property="article:author" content="Shan Carter">
    <meta property="article:author" content="Chelsea Voss">
    <meta property="article:author" content="Ludwig Schubert">
    <meta property="article:author" content="Chris Olah">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="Curve Circuits">
    <meta property="og:description" content="Reverse engineering the curve detection algorithm from InceptionV1 and reimplementing it from scratch.">
    <meta property="og:url" content="https://distill.pub/2020/circuits/curve-circuits">
    <meta property="og:image" content="https://distill.pub/2020/circuits/curve-circuits/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Curve Circuits">
    <meta name="twitter:description" content="Reverse engineering the curve detection algorithm from InceptionV1 and reimplementing it from scratch.">
    <meta name="twitter:url" content="https://distill.pub/2020/circuits/curve-circuits">
    <meta name="twitter:image" content="https://distill.pub/2020/circuits/curve-circuits/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="Curve Circuits">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/2020/circuits/curve-circuits">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="1">
    <meta name="citation_firstpage" content="e00024.006">
    <meta name="citation_doi" content="10.23915/distill.00024.006">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/01/30">
    <meta name="citation_publication_date" content="2021/01/30">
    <meta name="citation_author" content="Cammarata, Nick">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Goh, Gabriel">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Carter, Shan">
    <meta name="citation_author_institution" content="Observable">
    <meta name="citation_author" content="Voss, Chelsea">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Schubert, Ludwig">
    <meta name="citation_author" content="Olah, Chris">
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
  <d-front-matter><script type="text/json">{"title":"Curve Circuits","description":"Reverse engineering the curve detection algorithm from InceptionV1 and reimplementing it from scratch.","authors":[{"author":"Nick Cammarata","authorURL":"http://nickcammarata.com","affiliation":"OpenAI","affiliationURL":"https://openai.com"},{"author":"Gabriel Goh","authorURL":"http://gabgoh.github.io","affiliation":"OpenAI","affiliationURL":"https://openai.com"},{"author":"Shan Carter","authorURL":"http://shancarter.com","affiliation":"Observable","affiliationURL":"https://observablehq.com"},{"author":"Chelsea Voss","authorURL":"https://twitter.com/cvoss","affiliation":"OpenAI","affiliationURL":"https://openai.com"},{"author":"Ludwig Schubert","authorURL":"https://schubert.io/","affiliation":"","affiliationURL":"https://openai.com"},{"author":"Chris Olah","authorURL":"https://colah.github.io","affiliation":"","affiliationURL":"https://openai.com"}]}</script></d-front-matter>

  <d-title>
    <h1>Curve Circuits</h1>
    <p style="font-size: 1.4rem; margin-bottom: -5px">
      We reverse engineer a non-trivial learned algorithm from the weights of a
      neural network and use its core ideas to craft an 
      <i>artificial artificial neural network</i> from scratch that reimplements
      it.
    </p>
    <div style="display: flex; flex-flow: column; grid-column: screen; align-items: center; align-self:center;padding-top:20px; background: rgb(252, 252, 252); margin-top: 40px; border-top: 1px solid rgba(0, 0, 0, 0.1);">
    <div style="display: grid; align-self:center; flex-flow: column; grid-template-columns: [natural] 500px [aann] 500px; grid-template-rows: [label] auto [figure] auto; grid-gap: 20px;">
      <div style="border-bottom: 1px solid rgba(0, 0, 0, 0.1); padding-bottom: 3px; grid-column: aann; padding-left: 3px; font-size: 18px; grid-row: label;">
        Artificial Curve Neurons
  </div>
      <div style="border-bottom: 1px solid rgba(0, 0, 0, 0.1); padding-bottom: 3px; grid-column: natural; padding-left: 3px; font-size: 18px; grid-row: label;">
        Natural InceptionV1 Curve Neurons
      </div>
      <img src="banner-artificial.png" style="grid-row: figure; grid-column: aann; width: 500px; mix-blend-mode: darken;">
      <img src="banner-natural.png" style="grid-row: figure; grid-column: natural; width: 500px; mix-blend-mode: darken;">
    </div>
    <figcaption style="align-self: center; margin-top: 20px; margin-bottom: 25px; width: 704px">
      We can compare the curve detectors in a neural network we hand-crafted
      with the curve detectors in InceptionV1 by measuring how they activate
      to synthetic curve stimuli. We see that across a range of radii and
      orientations, our artificial curve neurons approximate the natural ones.
    </figcaption>
    </div>

  </d-title>

  <d-byline>
  <div class="byline grid">
    <div class="authors-affiliations grid">
      <h3>Authors</h3>
      <h3>Affiliations</h3>
      
        <p class="author">
          
            <a class="name" href="http://nickcammarata.com">Nick Cammarata</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="http://gabgoh.github.io">Gabriel Goh</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="http://shancarter.com">Shan Carter</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://observablehq.com">Observable</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://twitter.com/cvoss">Chelsea Voss</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://schubert.io/">Ludwig Schubert</a>
        </p>
        <p class="affiliation">
        
        </p>
      
        <p class="author">
          
            <a class="name" href="https://colah.github.io">Chris Olah</a>
        </p>
        <p class="affiliation">
        
        </p>
      
    </div>
    <div>
      <h3>Published</h3>
      
        <p>Jan. 30, 2021</p> 
    </div>
    <div>
      <h3>DOI</h3>
      
        <p><a href="https://doi.org/10.23915/distill.00024.006">10.23915/distill.00024.006</a></p>
    </div>
  </div>
</d-byline><d-article>
  </d-article>

  <d-appendix>
    <d-footnote-list></d-footnote-list>
    <d-citation-list style="display: none;" distill-prerendered="true"></d-citation-list>

    <h3>Author Contributions</h3>
    <p>As we mentioned in Curve Detectors, our first investigation into curve neurons, it’s hard to separate author contributions between different papers in the Circuits project. Much of the original research on curve neurons came before we decided to separate the publications into the behavior of curve neurons and how they are built. In this section we’ve tried to isolate contributions specific to the mechanics of the curve neurons.</p>

    <p><b>Interface Design &amp; Prototyping.</b> Many weight diagrams were first prototyped by Chris during his first investigations of different families of neurons in early early vision, and some of these were turned into presentations. Nick extended them for use in this paper. Chris designed and implemented the decomposed feature visualization figure in the first section. Many of the other interfaces were designed by Nick with the help of Shan and Chris. In particular, Shan helped to design the figure showing how the different families of early vision connect leading up to the curve family.</p>

    <p><b>Conceptual Contributions.</b> The earliest understandings of how curve neurons are built from lines and edges came from Chris, and the details came from further investigation by Nick. Nick investigated the line families in detail, including finding cliff line neurons and studying they are used. Nick studied through neuron families in the early layers, studying how shape neurons incrementally incorporate increasingly sophisticated texture and cosmetic neurons, working towards the neuron families diagram in the first section. The artificial artificial neural network was done by Chris and Nick expanded on it for use in the article. Gabe was instrumental in helping discover many of the techniques used for closely studying Circuits, and provided input and suggestions at many steps throughout our investigation of the curve circuit.</p>

    <p><b>Writing.</b> Nick and Chris wrote the text of the article with significant help editing from Chelsea.</p>

    <p><b>Infrastructure.</b> Nick built the infrastructure for extracting figures from the paper for reproduction in Colab. Ludwig is responsible for the distributed infrastructure that was used for many experiments.</p>

    <h3>Acknowledgements</h3>

    <p>Our article was greatly improved thanks to the detailed feedback by Patricia Robinson, Jennifer Lin, Adam Shimi, Sam Havens, Stefan Sietzen, Dave Vladman, Maxim Liu, Fred Hohman, Vincent Tjeng, and Humza Iqbal.</p>

    <p>We also really appreciate the conversations in the #circuits channel of the open <a href="http://slack.distill.pub/">Distill Slack</a>, which at the time of publishing contains more than 600 people.</p>

  <distill-appendix>
<style>
  distill-appendix {
    contain: layout style;
  }

  distill-appendix .citation {
    font-size: 11px;
    line-height: 15px;
    border-left: 1px solid rgba(0, 0, 0, 0.1);
    padding-left: 18px;
    border: 1px solid rgba(0,0,0,0.1);
    background: rgba(0, 0, 0, 0.02);
    padding: 10px 18px;
    border-radius: 3px;
    color: rgba(150, 150, 150, 1);
    overflow: hidden;
    margin-top: -12px;
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  distill-appendix > * {
    grid-column: text;
  }
</style>

    <h3 id="updates-and-corrections">Updates and Corrections</h3>
    <p>
    If you see mistakes or want to suggest changes, please <a href="https://github.com/distillpub/post--circuits-curve-circuits/issues/new">create an issue on GitHub</a>. </p>
    
    <h3 id="reuse">Reuse</h3>
    <p>Diagrams and text are licensed under Creative Commons Attribution <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</a> with the <a class="github" href="https://github.com/distillpub/post--circuits-curve-circuits">source available on GitHub</a>, unless noted otherwise. The figures that have been reused from other sources don’t fall under this license and can be recognized by a note in their caption: “Figure from …”.</p>
    
    <h3 id="citation">Citation</h3>
    <p>For attribution in academic contexts, please cite this work as</p>
    <pre class="citation short">Cammarata, et al., "Curve Circuits", Distill, 2021.</pre>
    <p>BibTeX citation</p>
    <pre class="citation long">@article{cammarata2021curve,
  author = {Cammarata, Nick and Goh, Gabriel and Carter, Shan and Voss, Chelsea and Schubert, Ludwig and Olah, Chris},
  title = {Curve Circuits},
  journal = {Distill},
  year = {2021},
  note = {https://distill.pub/2020/circuits/curve-circuits},
  doi = {10.23915/distill.00024.006}
}</pre>
    </distill-appendix></d-appendix>

  <d-bibliography><script type="text/json">[["olah2017feature",{"author":"Olah, Chris and Mordvintsev, Alexander and Schubert, Ludwig","title":"Feature Visualization","journal":"Distill","year":"2017","url":"https://distill.pub/2017/feature-visualization","doi":"10.23915/distill.00007","type":"article"}],["1326611",{"author":"K. {Raghupathy} and T. W. {Parks}","booktitle":"2004 IEEE International Conference on Acoustics, Speech, and Signal Processing","title":"Improved curve tracing in images","year":"2004","volume":"3","number":"","pages":"iii-581","type":"INPROCEEDINGS"}],["ballard1987generalizing",{"title":"Generalizing the Hough transform to detect arbitrary shapes","author":"Ballard, Dana H","booktitle":"Readings in computer vision","pages":"714--725","year":"1987","publisher":"Elsevier","type":"incollection"}],["lecun2015deep",{"title":"Deep learning","author":"LeCun, Yann and Bengio, Yoshua and Hinton, Geoffrey","url":"https://s3.us-east-2.amazonaws.com/hkg-website-assets/static/pages/files/DeepLearning.pdf","journal":"nature","volume":"521","number":"7553","pages":"436--444","year":"2015","publisher":"Nature Publishing Group","type":"article"}],["mikolov2013distributed",{"title":"Distributed representations of words and phrases and their compositionality","author":"Mikolov, Tomas and Sutskever, Ilya and Chen, Kai and Corrado, Greg S and Dean, Jeff","booktitle":"Advances in neural information processing systems","pages":"3111--3119","url":"https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf","year":"2013","type":"inproceedings"}],["karpathy2015visualizing",{"title":"Visualizing and understanding recurrent networks","author":"Karpathy, Andrej and Johnson, Justin and Fei-Fei, Li","journal":"arXiv preprint arXiv:1506.02078","url":"https://arxiv.org/pdf/1506.02078.pdf","year":"2015","type":"article"}],["radford2017learning",{"title":"Learning to generate reviews and discovering sentiment","author":"Radford, Alec and Jozefowicz, Rafal and Sutskever, Ilya","journal":"arXiv preprint arXiv:1704.01444","url":"https://arxiv.org/pdf/1704.01444.pdf","year":"2017","type":"article"}],["zhou2014object",{"title":"Object detectors emerge in deep scene cnns","author":"Zhou, Bolei and Khosla, Aditya and Lapedriza, Agata and Oliva, Aude and Torralba, Antonio","journal":"arXiv preprint arXiv:1412.6856","url":"https://arxiv.org/pdf/1412.6856.pdf","year":"2014","type":"article"}],["netdissect2017",{"title":"Network Dissection: Quantifying Interpretability of Deep Visual Representations","author":"Bau, David and Zhou, Bolei and Khosla, Aditya and Oliva, Aude and Torralba, Antonio","booktitle":"Computer Vision and Pattern Recognition","url":"https://arxiv.org/pdf/1704.05796.pdf","year":"2017","type":"inproceedings"}],["jo2017measuring",{"title":"Measuring the tendency of CNNs to Learn Surface Statistical Regularities","author":"Jo, Jason and Bengio, Yoshua","journal":"arXiv preprint arXiv:1711.11561","year":"2017","url":"https://arxiv.org/pdf/1711.11561.pdf","type":"article"}],["geirhos2018imagenet",{"title":"ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness","author":"Geirhos, Robert and Rubisch, Patricia and Michaelis, Claudio and Bethge, Matthias and Wichmann, Felix A and Brendel, Wieland","journal":"arXiv preprint arXiv:1811.12231","url":"https://arxiv.org/pdf/1811.12231.pdf","year":"2018","type":"article"}],["brendel2019approximating",{"title":"Approximating cnns with bag-of-local-features models works surprisingly well on imagenet","author":"Brendel, Wieland and Bethge, Matthias","journal":"arXiv preprint arXiv:1904.00760","url":"https://arxiv.org/pdf/1904.00760.pdf","year":"2019","type":"article"}],["morcos2018importance",{"title":"On the importance of single directions for generalization","author":"Morcos, Ari S and Barrett, David GT and Rabinowitz, Neil C and Botvinick, Matthew","journal":"arXiv preprint arXiv:1803.06959","url":"https://arxiv.org/pdf/1803.06959.pdf","year":"2018","type":"article"}],["donnelly2019interpretability",{"title":"On Interpretability and Feature Representations: An Analysis of the Sentiment Neuron","author":"Donnelly, Jonathan and Roegiest, Adam","booktitle":"European Conference on Information Retrieval","pages":"795--802","year":"2019","organization":"Springer","type":"inproceedings"}],["ilyas2019adversarial",{"title":"Adversarial examples are not bugs, they are features","author":"Ilyas, Andrew and Santurkar, Shibani and Tsipras, Dimitris and Engstrom, Logan and Tran, Brandon and Madry, Aleksander","booktitle":"Advances in Neural Information Processing Systems","url":"https://arxiv.org/pdf/1905.02175.pdf","pages":"125--136","year":"2019","type":"inproceedings"}],["zhou2016learning",{"title":"Learning deep features for discriminative localization","author":"Zhou, Bolei and Khosla, Aditya and Lapedriza, Agata and Oliva, Aude and Torralba, Antonio","booktitle":"Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition","pages":"2921--2929","year":"2016","url":"http://cnnlocalization.csail.mit.edu/Zhou_Learning_Deep_Features_CVPR_2016_paper.pdf","doi":"10.1109/cvpr.2016.319","type":"inproceedings"}],["selvaraju2016grad",{"title":"Grad-cam: Why did you say that? visual explanations from deep networks via gradient-based localization","author":"Selvaraju, Ramprasaath R and Das, Abhishek and Vedantam, Ramakrishna and Cogswell, Michael and Parikh, Devi and Batra, Dhruv","journal":"arXiv preprint arXiv:1610.02391","year":"2016","url":"https://arxiv.org/pdf/1610.02391.pdf","type":"article"}],["kim2017tcav",{"title":"TCAV: Relative concept importance testing with Linear Concept Activation Vectors","author":"Kim, Been and Gilmer, Justin and Viegas, Fernanda and Erlingsson, Ulfar and Wattenberg, Martin","journal":"arXiv preprint arXiv:1711.11279","year":"2017","url":"https://arxiv.org/pdf/1711.11279.pdf","type":"article"}],["raghu2017svcca",{"title":"SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability","author":"Raghu, Maithra and Gilmer, Justin and Yosinski, Jason and Sohl-Dickstein, Jascha","booktitle":"Advances in Neural Information Processing Systems 30","editor":"I. Guyon and U. V. Luxburg and S. Bengio and H. Wallach and R. Fergus and S. Vishwanathan and R. Garnett","pages":"6078--6087","year":"2017","publisher":"Curran Associates, Inc.","url":"http://papers.nips.cc/paper/7188-svcca-singular-vector-canonical-correlation-analysis-for-deep-learning-dynamics-and-interpretability.pdf","type":"incollection"}],["yosinski2015understanding",{"title":"Understanding neural networks through deep visualization","author":"Yosinski, Jason and Clune, Jeff and Nguyen, Anh and Fuchs, Thomas and Lipson, Hod","journal":"arXiv preprint arXiv:1506.06579","year":"2015","url":"http://yosinski.com/media/papers/Yosinski__2015__ICML_DL__Understanding_Neural_Networks_Through_Deep_Visualization__.pdf","type":"article"}],["nielsen2016thought",{"title":"Thought as a Technology","author":"Michael Nielsen","year":"2016","url":"http://cognitivemedium.com/tat/index.html","type":"article"}],["carter2017using",{"title":"Using Artificial Intelligence to Augment Human Intelligence","author":"Carter, Shan and Nielsen, Michael","journal":"Distill","year":"2017","url":"https://distill.pub/2017/aia/","doi":"10.23915/distill.00009","type":"article"}],["olah2015visualizing",{"title":"Visualizing Representations: Deep Learning and Human Beings","author":"Olah, Chris","year":"2015","url":"http://colah.github.io/posts/2015-01-Visualizing-Representations/","type":"article"}],["erhan2009visualizing",{"title":"Visualizing higher-layer features of a deep network","author":"Erhan, Dumitru and Bengio, Yoshua and Courville, Aaron and Vincent, Pascal","journal":"University of Montreal","volume":"1341","pages":"3","year":"2009","url":"https://www.researchgate.net/profile/Aaron_Courville/publication/265022827_Visualizing_Higher-Layer_Features_of_a_Deep_Network/links/53ff82b00cf24c81027da530.pdf","type":"article"}],["nguyen2015deep",{"title":"Deep neural networks are easily fooled: High confidence predictions for unrecognizable images","author":"Nguyen, Anh and Yosinski, Jason and Clune, Jeff","booktitle":"Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition","pages":"427--436","year":"2015","doi":"10.1109/cvpr.2015.7298640","url":"https://arxiv.org/pdf/1412.1897.pdf","type":"inproceedings"}],["mordvintsev2015inceptionism",{"title":"Inceptionism: Going deeper into neural networks","author":"Mordvintsev, Alexander and Olah, Christopher and Tyka, Mike","journal":"Google Research Blog","year":"2015","url":"https://research.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html","type":"article"}],["simonyan2013deep",{"title":"Deep inside convolutional networks: Visualising image classification models and saliency maps","author":"Simonyan, Karen and Vedaldi, Andrea and Zisserman, Andrew","journal":"arXiv preprint arXiv:1312.6034","year":"2013","url":"https://arxiv.org/pdf/1312.6034.pdf","type":"article"}],["nguyen2016plug",{"title":"Plug & play generative networks: Conditional iterative generation of images in latent space","author":"Nguyen, Anh and Clune, Jeff and Bengio, Yoshua and Dosovitskiy, Alexey and Yosinski, Jason","journal":"arXiv preprint arXiv:1612.00005","year":"2016","url":"https://arxiv.org/pdf/1612.00005.pdf","type":"article"}],["fong2017interpretable",{"title":"Interpretable Explanations of Black Boxes by Meaningful Perturbation","author":"Fong, Ruth and Vedaldi, Andrea","journal":"arXiv preprint arXiv:1704.03296","year":"2017","url":"https://arxiv.org/pdf/1704.03296.pdf","type":"article"}],["kindermans2017patternnet",{"title":"PatternNet and PatternLRP--Improving the interpretability of neural networks","author":"Kindermans, Pieter-Jan and Schutt, Kristof T and Alber, Maximilian and Muller, Klaus-Robert and Dahne, Sven","journal":"arXiv preprint arXiv:1705.05598","year":"2017","url":"https://arxiv.org/pdf/1705.05598.pdf","doi":"10.1007/978-3-319-10590-1_53","type":"article"}],["zeiler2014visualizing",{"title":"Visualizing and understanding convolutional networks","author":"Zeiler, Matthew D and Fergus, Rob","booktitle":"European conference on computer vision","pages":"818--833","year":"2014","organization":"Springer","url":"https://arxiv.org/pdf/1311.2901.pdf","type":"inproceedings"}],["springenberg2014striving",{"title":"Striving for simplicity: The all convolutional net","author":"Springenberg, Jost Tobias and Dosovitskiy, Alexey and Brox, Thomas and Riedmiller, Martin","journal":"arXiv preprint arXiv:1412.6806","year":"2014","url":"https://arxiv.org/pdf/1412.6806.pdf","type":"article"}],["kindermans2017reliability",{"title":"The (Un)reliability of saliency methods","author":"Kindermans, Pieter-Jan and Hooker, Sara and Adebayo, Julius and Alber, Maximilian and Schutt, Kristof T and Dahne, Sven and Erhan, Dumitru and Kim, Been","journal":"arXiv preprint arXiv:1711.00867","year":"2017","url":"https://arxiv.org/pdf/1711.00867.pdf","type":"article"}],["maaten2008visualizing",{"title":"Visualizing data using t-SNE","author":"Maaten, Laurens van der and Hinton, Geoffrey","journal":"Journal of Machine Learning Research","volume":"9","number":"Nov","pages":"2579--2605","year":"2008","url":"http://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf","type":"article"}],["koh2017understanding",{"author":"P. W. Koh and P. Liang","booktitle":"International Conference on Machine Learning (ICML)","title":"Understanding Black-box Predictions via Influence Functions","year":"2017","url":"https://arxiv.org/pdf/1703.04730.pdf","type":"inproceedings"}],["pirolli1999information",{"title":"Information foraging","author":"Pirolli, Peter and Card, Stuart","journal":"Psychological review","volume":"106","number":"4","pages":"643","year":"1999","publisher":"American Psychological Association","url":"http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.31.5407&rep=rep1&type=pdf","doi":"10.1037//0033-295x.106.4.643","type":"article"}],["bau2017network",{"title":"Network dissection: Quantifying interpretability of deep visual representations","author":"Bau, David and Zhou, Bolei and Khosla, Aditya and Oliva, Aude and Torralba, Antonio","booktitle":"Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on","pages":"3319--3327","year":"2017","organization":"IEEE","url":"https://arxiv.org/pdf/1704.05796.pdf","doi":"10.1109/cvpr.2017.354","type":"inproceedings"}],["mackinlay1986automating",{"title":"Automating the design of graphical presentations of relational information","author":"Mackinlay, Jock","journal":"Acm Transactions On Graphics (Tog)","volume":"5","number":"2","pages":"110--141","year":"1986","publisher":"ACM","url":"http://www2.parc.com/istl/groups/uir/publications/items/UIR-1986-02-Mackinlay-TOG-Automating.pdf","doi":"10.1145/22949.22950","type":"article"}],["nguyen2016multifaceted",{"title":"Multifaceted feature visualization: Uncovering the different types of features learned by each neuron in deep neural networks","author":"Nguyen, Anh and Yosinski, Jason and Clune, Jeff","journal":"arXiv preprint arXiv:1602.03616","year":"2016","url":"https://arxiv.org/pdf/1602.03616.pdf","type":"article"}],["strobelt2018lstmvis",{"title":"LSTMVis: A tool for visual analysis of hidden state dynamics in recurrent neural networks","author":"Strobelt, Hendrik and Gehrmann, Sebastian and Pfister, Hanspeter and Rush, Alexander M","journal":"IEEE Transactions on Visualization and Computer Graphics","volume":"24","number":"1","pages":"667--676","year":"2018","publisher":"IEEE","url":"https://arxiv.org/pdf/1606.07461.pdf","doi":"10.1109/tvcg.2017.2744158","type":"article"}],["kahng2018cti",{"title":"ActiVis: Visual Exploration of Industry-Scale Deep Neural Network Models","author":"Kahng, Minsuk and Andrews, Pierre Y and Kalro, Aditya and Chau, Duen Horng Polo","journal":"IEEE Transactions on Visualization and Computer Graphics","volume":"24","number":"1","pages":"88--97","year":"2018","publisher":"IEEE","url":"https://arxiv.org/pdf/1704.01942.pdf","doi":"10.1109/tvcg.2017.2744718","type":"article"}],["bilal2018convolutional",{"title":"Do convolutional neural networks learn class hierarchy?","author":"Bilal, Alsallakh and Jourabloo, Amin and Ye, Mao and Liu, Xiaoming and Ren, Liu","journal":"IEEE Transactions on Visualization and Computer Graphics","volume":"24","number":"1","pages":"152--162","year":"2018","publisher":"IEEE","url":"https://arxiv.org/pdf/1710.06501.pdf","doi":"10.1109/tvcg.2017.2744683","type":"article"}],["amershi2015modeltracker",{"title":"Modeltracker: Redesigning performance analysis tools for machine learning","author":"Amershi, Saleema and Chickering, Max and Drucker, Steven M and Lee, Bongshin and Simard, Patrice and Suh, Jina","booktitle":"Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems","pages":"337--346","year":"2015","organization":"ACM","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/amershi.CHI2015.ModelTracker.pdf","doi":"10.1145/2702123.2702509","type":"inproceedings"}],["kapoor2010interactive",{"title":"Interactive optimization for steering machine classification","author":"Kapoor, Ashish and Lee, Bongshin and Tan, Desney and Horvitz, Eric","booktitle":"Proceedings of the SIGCHI Conference on Human Factors in Computing Systems","pages":"1343--1352","year":"2010","organization":"ACM","url":"http://erichorvitz.com/steering_classification_2010.pdf","doi":"10.1145/1753326.1753529","type":"inproceedings"}],["krause2016interacting",{"title":"Interacting with predictions: Visual inspection of black-box machine learning models","author":"Krause, Josua and Perer, Adam and Ng, Kenney","booktitle":"Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems","pages":"5686--5697","year":"2016","organization":"ACM","url":"http://perer.org/papers/adamPerer-Prospector-CHI2016.pdf","doi":"10.1145/2858036.2858529","type":"inproceedings"}],["szegedy2015going",{"title":"Going deeper with convolutions","author":"Szegedy, Christian and Liu, Wei and Jia, Yangqing and Sermanet, Pierre and Reed, Scott and Anguelov, Dragomir and Erhan, Dumitru and Vanhoucke, Vincent and Rabinovich, Andrew and others","year":"2015","organization":"CVPR","url":"https://arxiv.org/pdf/1409.4842.pdf","doi":"10.1109/cvpr.2015.7298594","type":"inproceedings"}],["szegedy2013intriguing",{"title":"Intriguing properties of neural networks","author":"Szegedy, Christian and Zaremba, Wojciech and Sutskever, Ilya and Bruna, Joan and Erhan, Dumitru and Goodfellow, Ian and Fergus, Rob","journal":"arXiv preprint arXiv:1312.6199","year":"2013","url":"https://arxiv.org/pdf/1312.6199.pdf","type":"article"}],["mikolov2013efficient",{"title":"Efficient estimation of word representations in vector space","author":"Mikolov, Tomas and Chen, Kai and Corrado, Greg and Dean, Jeffrey","journal":"arXiv preprint arXiv:1301.3781","year":"2013","url":"https://arxiv.org/pdf/1301.3781.pdf","type":"article"}],["sabour2015adversarial",{"title":"Adversarial manipulation of deep representations","author":"Sabour, Sara and Cao, Yanshuai and Faghri, Fartash and Fleet, David J","journal":"arXiv preprint arXiv:1511.05122","year":"2015","url":"https://arxiv.org/pdf/1511.05122.pdf","type":"article"}],["radford2015unsupervised",{"title":"Unsupervised representation learning with deep convolutional gene