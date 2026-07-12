---
source_url: https://distill.pub/2021/distill-hiatus
ingested: 2026-07-11
sha256: 4c0b2a830d48fabf13b4b6a48cff8c6581505a5bf23d245b85feeb9926c64663
blog_source: Distill AI
---
<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1300"><meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1"><script>
window.addEventListener('WebComponentsReady', function() {
  console.warn('WebComponentsReady');
  const loaderTag = document.createElement('script');
  loaderTag.src = 'https://distill.pub/template.v2.js';
  document.head.insertBefore(loaderTag, document.head.firstChild);
});
</script><script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.0.17/webcomponents-loader.js"></script>
  
  
  <style id="distill-article-specific-styles"></style>
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
  
    <title>Distill Hiatus</title>
    
    <link rel="canonical" href="https://distill.pub/2021/distill-hiatus">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="After five years, Distill will be taking a break.">
    <meta property="article:published" itemprop="datePublished" content="2021-07-02">
    <meta property="article:created" itemprop="dateCreated" content="2021-07-02">
    
    <meta property="article:modified" itemprop="dateModified" content="2021-07-09T04:30:59.000Z">
    
    <meta property="article:author" content="Editorial Team">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="Distill Hiatus">
    <meta property="og:description" content="After five years, Distill will be taking a break.">
    <meta property="og:url" content="https://distill.pub/2021/distill-hiatus">
    <meta property="og:image" content="https://distill.pub/2021/distill-hiatus/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Distill Hiatus">
    <meta name="twitter:description" content="After five years, Distill will be taking a break.">
    <meta name="twitter:url" content="https://distill.pub/2021/distill-hiatus">
    <meta name="twitter:image" content="https://distill.pub/2021/distill-hiatus/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="Distill Hiatus">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/2021/distill-hiatus">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="7">
    <meta name="citation_firstpage" content="e31">
    <meta name="citation_doi" content="10.23915/distill.00031">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/07/02">
    <meta name="citation_publication_date" content="2021/07/02">
    <meta name="citation_author" content="Team, Editorial">
    <meta name="citation_author_institution" content="Distill">
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
      "title": "Distill Hiatus",
      "description": "After five years, Distill will be taking a break.",
      "authors": [
        {
          "author": "Editorial Team",
          "authorURL": "http://distill.pub",
          "affiliation": "Distill",
          "affiliationURL": "http://distill.pub"
        }
      ]
    }</script>
  </d-front-matter>

  <d-title>
    <h1>Distill Hiatus</h1>
  </d-title>

  <d-byline>
  <div class="byline grid">
    <div class="authors-affiliations grid">
      <h3>Authors</h3>
      <h3>Affiliations</h3>
      
        <p class="author">
          
            <a class="name" href="http://distill.pub">Editorial Team</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="http://distill.pub">Distill</a>
        </p>
      
    </div>
    <div>
      <h3>Published</h3>
      
        <p>July 2, 2021</p> 
    </div>
    <div>
      <h3>DOI</h3>
      
        <p><a href="https://doi.org/10.23915/distill.00031">10.23915/distill.00031</a></p>
    </div>
  </div>
</d-byline><d-article><p><em>Over the past five years, Distill has supported authors in publishing artifacts that push beyond the traditional expectations of scientific papers. From Gabriel Goh’s <a href="">interactive exposition of momentum</a>, to an <a href="https://distill.pub/2020/growing-ca/">ongoing collaboration exploring self-organizing systems</a>, to a <a href="https://distill.pub/2019/advex-bugs-discussion/">community discussion of a highly debated paper</a>, Distill has been a venue for authors to experiment in scientific communication.</em></p><p><em>But over this time, the editorial team has become less certain whether it makes sense to run Distill as a journal, rather than encourage authors to self-publish. Running Distill as a journal creates a great deal of structural friction, making it hard for us to focus on the aspects of scientific publishing we’re most excited about. Distill is volunteer run and these frictions have caused our team to struggle with burnout.</em></p><p><em>Starting today Distill will be taking a one year hiatus, which may be extended indefinitely. Papers actively under review are not affected by this change, published threads can continue to add to their exploration, and we may publish commentary articles in limited cases. Authors can continue to write Distill-style papers using the <a href="https://github.com/distillpub/template">Distill template</a>, and either self-publish or submit to venues like <a href="https://visxai.io/">VISxAI</a>.</em></p><hr><p>The Distill journal was founded as an adapter between traditional and online scientific publishing. We believed that many valuable scientific contributions — such as explanations, interactive articles, and visualizations — were held back by not being seen as “real scientific publications.” Our theory was that if a journal were to publish such artifacts, it would allow authors to benefit from the traditional academic incentive system and enable more of this kind of work.</p><p>After four years, we no longer believe this theory of impact. First, we don’t think that publishing in a journal like Distill significantly affects how seriously most institutions take non-traditional publications. Instead, it seems that more liberal institutions will take high-quality articles seriously regardless of their venue and style, while more conservative institutions remain unmoved. Secondly, we don’t believe that having a venue is the primary bottleneck to authors producing more Distill-style articles. Instead, we believe the primary bottleneck is the amount of effort it takes to produce these articles and the unusual combination of scientific and design expertise required.</p><p>We’re proud of the authors Distill has been able to support and the articles it has been able to publish. And we do think that Distill has produced a lot of value. But we don’t think this value has been a product of Distill’s status as a journal. Instead, we believe Distill’s impact has been through:</p><ul><li>Providing mentorship to authors and potential authors.</li><li>Providing the Distill template (which is used by many non-Distill authors)</li><li>Individuals involved in Distill producing excellent articles.</li><li>Providing encouragement and community to authors.</li></ul><p>Our sense is that Distill’s journal structure may limit, rather than support, these benefits. It creates a great deal of overhead, political concerns, and is in direct tension with some of these goals.</p><p>Instead, we think the future for most types of articles is probably self-publication, either on one-off websites or on a hypothetical “Distill Arxiv.” There are a few exceptions where we think centralized journal-like entities probably have an important enduring role, but we think the majority of papers are best served by self-publication.</p><h2>Changes in How We Think About Distill</h2><h3>Mentorship is in Tension with Being a Journal</h3><p>Behind the scenes, the largest function of Distill is providing feedback and mentorship. For some of our early articles, we provided more than 50 hours of help with designing diagrams, improving writing style, and shaping scientific communication. Although we’ve generally dialed this down over time, each article still requires significant work. All of this is done by our editors in a volunteer capacity, on top of their regular work responsibilities.</p><p>The first problem with providing mentorship through an editorial role is that it’s not a very good mechanism for distributing mentorship. Ideally, one wants to provide mentorship early on in projects, to mentees with similar interests, and to a number of mentees that one is capable of providing good mentorship to. Providing mentorship to everyone who submits an article to Distill is overwhelming. Another problem is that our advice is often too late because the article’s foundation is already set. Finally, many authors don’t realize the amount of effort it takes to publish a Distill article.</p><p>Providing mentorship also creates a challenging dual relationship for an editor. They have both the role of closely supporting and championing the author while also having to accept or reject them in the end. We’ve found this to be difficult for both the mentor and mentee.</p><p>Finally, the kind of deeply-engaged editing and mentorship that we sometimes provide can often amount to an authorship level contribution, with authors offering co-authorship to editors. This is especially true when an editor was a mentor from early on. In many ways, co-authorship would create healthy incentives, rewarding the editor for spending tens of hours improving the article. But it creates a conflict of interest if the editor is to be an independent decision maker, as the journal format suggests they should be. And even if another editor takes over, it’s a political risk: Distill is sometimes criticized for publishing too many articles with editors as authors.</p><h3>Editor Articles are in Tension with Being a Journal</h3><p>Another important impact of Distill has been articles written by the editors themselves. Distill’s editorial team consists of volunteer researchers who are deeply excited about explanations and interactive articles and have a long history of doing so. Since the set of people with these interests is small, a non-trivial fraction of Distill’s publications have come from editors. In other cases, authors of existing Distill articles were later invited to become an editor.</p><p>Editor articles are sometimes cited as a sign of a kind of corruption for Distill, that Distill is a vehicle for promoting editors. We can see how it might seem dubious for a journal to publish articles by people running it, even if editorial decisions are made by an editor who is at arms-length. This has led Distill to avoid publishing several editor articles despite believing that they are of value to readers.</p><p>We believe that editor articles are actually a good thing about Distill. Each one represents an immense amount of effort in trying new things scientific publishing. Given the large volume of readers and the positive informal comments we receive, we suspect that for every critic there are many silent but happy readers.</p><p>When a structure turns a public good into an appearance of corruption, it suggests it might not be such a good structure. As editors, we want to share our work with the world in a way that is not seen as corrupt.</p><h3>Neutral venues can be achieved in other ways</h3><p>The vast majority of Distill articles are written by multiple authors, often from multiple institutions. As a result, an important function of Distill is providing somewhere to publish that isn’t someone’s home turf. If a Distill article were published on one person or organization’s blog, it could lead to a perception that it is primarily theirs and make other authors feel less comfortable with collaboration. Arxiv normally fills this role, but it only supports PDFs.</p><p>But it turns out there’s a simpler solution: self publication on one-off websites. David Ha and his collaborators have done a great job demonstrating this, using the Distill template and GitHub pages to self-publish articles (eg. the <a href="https://worldmodels.github.io/">world models</a> article). In these cases, the articles are standalone rather than being with a particular author or institution.</p><h3>Self-Publication Seems Like the Future (in most cases)</h3><p>In many areas of physics, self publishing on Arxiv has become the dominant mode of publication. A great deal of machine learning research is also published on Arxiv. We think this type of self-publication is likely the future for a large fraction of publication, possibly along with alternative models of review that are separated from a publisher.</p><p>Journal-led peer review provides many benefits. It can protect against scientific misinformation and non-reproducible results. It can save the research community time by filtering out papers that aren’t worth engaging with. It can provide feedback to junior researchers who may not have other sources of feedback. It can push research groups studying similar topics across institutions to engage with each other’s criticism. And double-blind review may support equity and fairness.</p><p>But is traditional journal-led peer review the most effective way to achieve these benefits? And is it worth the enormous costs it imposes on editors, reviewers, authors, and readers?</p><p>For example, avoiding scientific errors, non-reproducible results, and misinformation is certainly important. But for every paper where there’s a compelling public interest in avoiding misinformation (eg. papers about COVID), there are thousands of papers whose audience is a handful of the same researchers we ask to perform review. Additionally, it’s not clear how effective peer review actually is at catching errors. We suspect that a structure which focuses on reviewing controversial and important papers would be more effective at this goal. Our experience from <a href="https://distill.pub/2019/advex-bugs-discussion/">discussion articles</a> is that reviewers are willing to spend orders of magnitude more energy when they feel like reviewing a paper genuinely matters to the community, rather than being pro-forma, and their work will be seen as a scientific contribution.</p><p>Similarly, we suspect that journal-led review isn’t a very effective way of providing feedback to junior researchers or of promoting equity. These are all very worthy aims, and we’d like to free energy to pursue them in effective ways.</p><p>We also think there’s a lot of upside to self-publication. Self-publication can move very fast. It doesn’t require a paper to fit into the scope of an existing journal. It allows for more innovation in the format of the paper, such as using interactive diagrams as Distill does. And it aligns incentives better.<d-footnote>Self-publication may align certain incentives better than traditional publishing. Many papers go through an informal review process before they’re submitted to a journal or self-published, with authors soliciting feedback from colleagues. This informal review process is often smoother, faster, and provides more constructive and more relevant feedback than a traditional review process. Why is that? In a normal review process, the authors have the highest stakes, but little agency in the process. Meanwhile, neither the reviewers nor the editors share the authors’ incentive to move quickly. And the reviewers are often horribly over-subscribed. In contrast, in an informal review process, the authors have a strong incentive to quickly organize the process and reviewers are focused on providing helpful feedback to someone they know, rather than arbitrating a gatekeeping decision.</d-footnote></p><h3>A Half-hearted Distill May Cause Harm</h3><p>Distill isn’t living up to our standards of author experience. Originally, we had a vision of a much more engaged, responsive, and rapid review process with editors deeply involved in helping authors improve their article. But the truth is that, with us being quite burnt out, our review process has become much slower and more similar to a typical journal. It’s unclear to us whether the value added by our present review process is worth the time costs we impose on authors.</p><p>Distill also occupies institutional space, potentially discouraging others from starting similar projects. It’s possible that there are others who could execute something like Distill better than us, but aren’t starting their project because Distill exists.</p><p>On the flip side, Distill often comes up in conversations about the future of publishers and journals in machine learning, as a positive example of the role a journal can play. But if we no longer believe in our model, Distill may be unintentionally supporting something we don’t really stand behind. We may also be setting unrealistic aspirations: if Distill’s level of editorial engagement and editing was unsustainable, even with a deeply passionate set of volunteers and a relatively small number of articles, we should at least be clearly communicating how difficult it is.</p><h2>Why a Hiatus?</h2><p>We think that Distill is a really beautiful artifact which illustrates a vision of scientific publishing. But it is not sustainable for us to continue running the journal in its current form. We think preserving it in its present state is more valuable than diluting it with lower quality editing. We also think that it’s a lot healthier for us and frees up our energy to do new projects that provide value to the community.</p><p>We’ve considered trying to find others to hand Distill off to. But a lot of the value of Distill is illustrating a weird and idiosyncratic vision. We think there’s value in preserving Distill’s original flavor. We are open to changes to better structure Distill, but we feel protective of Distill’s vision and quirkiness.</p><p>Although Distill is going on hiatus, the <a href="https://github.com/distillpub/template">Distill template</a> is open source, and we’d love to see others run with it!</p><h3>Burnout</h3><p>Over the last few years, Distill has experienced a significant amount of volunteer burnout. The fact that multiple volunteers experienced burnout makes us think it’s partly caused by the issues described in previous sections.</p><p>One of the biggest risk factors in burnout is having conflicting goals, and as the previous sections describe, we’ve had many conflicting goals. We wanted to mentor people, but we also needed to reject them. We wanted to write beautiful articles ourselves, but we also wanted to be an independent venue.</p><p>Another significant risk factor is having unachievable goals. We set extremely high standards for ourselves: with early articles, volunteer editors would often spend 50 or more hours improving articles that were submitted to Distill and bringing them up to the level of quality we aspired to. This invisible effort was comparable to the work of writing a short article of one’s own. It wasn’t sustainable, and this left us with a constant sense that we were falling short. A related issue is that we had trouble setting well-defined boundaries of what we felt we owed to authors who submitted to us.</p><p>By discussing these challenges, we hope that future projects like Distill will be able to learn from our experiences and find ways to balance these competing values.</p></d-article>

  <d-appendix>
    <h3>Author Contributions</h3>
    <p>This article was drafted by Chris Olah, Nick Cammarata, Sam Greydanus, and Janelle Tam.</p>
    <h3>Acknowledgements</h3>
    <p>Distill has been supported by too many people over the years to have any hope of thanking everyone. We’re especially grateful to Distill’s authors for investing so much in their articles, and to our reviewers for generously giving so much time to help Distill.
    We’re also grateful to the many people who helped us as we struggled with this decision over the last few years. Many people took time to talk with us about burn out, about whether Distill was a good structure, about how to wind Distill down graciously, and about this essay. We’re also grateful to past and present Distill authors for being so understanding of our decision.</p>

    <d-footnote-list></d-footnote-list>
    <d-citation-list style="display: none;" distill-prerendered="true"></d-citation-list>

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
    If you see mistakes or want to suggest changes, please <a href="https://github.com/distillpub/post--distill-hiatus/issues/new">create an issue on GitHub</a>. </p>
    
    <h3 id="reuse">Reuse</h3>
    <p>Diagrams and text are licensed under Creative Commons Attribution <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</a> with the <a class="github" href="https://github.com/distillpub/post--distill-hiatus">source available on GitHub</a>, unless noted otherwise. The figures that have been reused from other sources don’t fall under this license and can be recognized by a note in their caption: “Figure from …”.</p>
    
    <h3 id="citation">Citation</h3>
    <p>For attribution in academic contexts, please cite this work as</p>
    <pre class="citation short">Team, "Distill Hiatus", Distill, 2021.</pre>
    <p>BibTeX citation</p>
    <pre class="citation long">@article{team2021distill,
  author = {Team, Editorial},
  title = {Distill Hiatus},
  journal = {Distill},
  year = {2021},
  note = {https://distill.pub/2021/distill-hiatus},
  doi = {10.23915/distill.00031}
}</pre>
    </distill-appendix></d-appendix>
  <d-bibliography><script type="text/json">[]</script></d-bibliography>
<distill-footer>
<style>

:host {
  color: rgba(255, 255, 255, 0.5);
  font-weight: 300;
  padding: 2rem 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  background-color: hsl(180, 5%, 15%); /*hsl(200, 60%, 15%);*/
  text-align: left;
  contain: content;
}

.footer-container .logo svg {
  width: 24px;
  position: relative;
  top: 4px;
  margin-right: 2px;
}

.footer-container .logo svg path {
  fill: none;
  stroke: rgba(255, 255, 255, 0.8);
  stroke-width: 3px;
}

.footer-container .logo {
  font-size: 17px;
  font-weight: 200;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  margin-right: 6px;
}

.footer-container {
  grid-column: text;
}

.footer-container .nav {
  font-size: 0.9em;
  margin-top: 1.5em;
}

.footer-container .nav a {
  color: rgba(255, 255, 255, 0.8);
  margin-right: 6px;
  text-decoration: none;
}

</style>

<div class="footer-container">

  <a href="/" class="logo">
    <svg viewBox="-607 419 64 64">
  <path d="M-573.4,478.9c-8,0-14.6-6.4-14.6-14.5s14.6-25.9,14.6-40.8c0,14.9,14.6,32.8,14.6,40.8S-565.4,478.9-573.4,478.9z"></path>
</svg>

    Distill
  </a> is dedicated to clear explanations of machine learning

  <div class="nav">
    <a href="https://distill.pub/about/">About</a>
    <a href="https://distill.pub/journal/">Submit</a>
    <a href="https://distill.pub/prize/">Prize</a>
    <a href="https://distill.pub/archive/">Archive</a>
    <a href="https://distill.pub/rss.xml">RSS</a>
    <a href="https://github.com/distillpub">GitHub</a>
    <a href="https://twitter.com/distillpub">Twitter</a>
    &nbsp;&nbsp;&nbsp;&nbsp; ISSN 2476-0757
  </div>

</div>

</distill-footer><script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-83741880-1', 'auto');
  ga('send', 'pageview');
</script></body></html>