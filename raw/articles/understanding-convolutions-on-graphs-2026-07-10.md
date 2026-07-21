---

source_url: https://distill.pub/2021/understanding-gnns
ingested: 2026-07-10
sha256: 065df483908d68e55a98c89c2a00efe76bebd8fccdf629f20b83d1410b82f9e0
blog_source: Distill AI
---

<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1200"><meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1"><script>
window.addEventListener('WebComponentsReady', function() {
  console.warn('WebComponentsReady');
  const loaderTag = document.createElement('script');
  loaderTag.src = 'https://distill.pub/template.v2.js';
  document.head.insertBefore(loaderTag, document.head.firstChild);
});
</script><script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.0.17/webcomponents-loader.js"></script>
  <title>Understanding Convolutions on Graphs</title>
  
  
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
  <style id="distill-article-specific-styles">
    .subgrid {
  grid-column: screen; 
  display: grid; 
  grid-template-columns: inherit;
  grid-template-rows: inherit;
  grid-column-gap: inherit;
  grid-row-gap: inherit;
}

d-figure.base-grid {
  grid-column: screen;
  background: hsl(0, 0%, 97%);
  padding: 20px 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

d-figure {
  margin-bottom: 1em;
  position: relative;
}

d-figure > figure {
  margin-top: 0;
  margin-bottom: 0;
}

.shaded-figure {
  background-color: hsl(0, 0%, 97%);
  border-top: 1px solid hsla(0, 0%, 0%, 0.1);
  border-bottom: 1px solid hsla(0, 0%, 0%, 0.1);
  padding: 30px 0;
}

.pointer {
  position: absolute;
  width: 26px;
  height: 26px;
  top: 26px;
  left: -48px;
}

div#observablehq {
  font-family: inherit;
  font-size: inherit;
}

button {
  font-family : inherit;
  font-size: 1em;
}

/* Alignment of KaTeX. */
#gnn-models span.katex-display {
  margin: 0.5em 0 0.5em 0em;
}

@media (max-width: 1000px) {
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

@media (min-width: 1000px) {
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

@media (min-width: 1180px) {
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
  margin-bottom: 0.25em;
}

d-contents nav a:hover {
  text-decoration: underline solid rgba(0, 0, 0, 0.6);
}

d-contents nav ul {
  margin-top: 0;
  margin-bottom: 6px;
}

d-contents nav > div {
  display: block;
  outline: none;
  margin-bottom: 0.5em;
}

d-contents nav > div > a {
  font-size: 13px;
  font-weight: 600;
}

d-contents nav > div > a:hover, d-contents nav > ul > li > a:hover {
  text-decoration: none;
}

input[type="radio"] {
  vertical-align: unset !important;
}

.math-details {
  padding-left: 1em;
  padding-right: 1em;
  padding-bottom: 0em;
  padding-top: 1em;
  margin-bottom: 1em;
}
  </style>
<link rel="stylesheet" href="https://distill.pub/third-party/katex/katex.min.css" crossorigin="anonymous">
    
    <link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA99JREFUeNrsG4t1ozDMzQSM4A2ODUonKBucN2hugtIJ6E1AboLcBiQTkJsANiAb9OCd/OpzMWBJBl5TvaeXPiiyJetry0J8wW3D3QpjRh3GjneXDq+fSQA9s2mH9x3KDhN4foJfCb8N/Jrv+2fnDn8vLRQOplWHVYdvHZYdZsBcZP1vBmh/n8DzEmhUQDPaOuP9pFuY+JwJHwHnCLQE2tnWBGEyXozY9xCUgHMhhjE2I4heVWtgIkZ83wL6Qgxj1obfWBxymPwe+b00BCCRNPbwfb60yleAkkBHGT5AEehIYz7eJrFDMF9CvH4wwhcGHiHMneFvLDQwlwvMLQq58trRcYBWfYn0A0OgHWQUSu25mE+BnoYKnnEJoeIWAifzOv7vLWd2ZKRfWAIme3tOiUaQ3UnLkb0xj1FxRIeEGKaGIHOs9nEgLaaA9i0JRYo1Ic67wJW86KSKE/ZAM8KuVMk8ITVhmxUxJ3Cl2xlm9Vtkeju1+mpCQNxaEGNCY8bs9X2YqwNoQeGjBWut/ma0QAWy/TqAsHx9wSya3I5IRxOfTC+leG+kA/4vSeEcGBtNUN6byhu3+keEZCQJUNh8MAO7HL6H8pQLnsW/Hd4T4lv93TPjfM7A46iEEqbB5EDOvwYNW6tGNZzT/o+CZ6sqZ6wUtR/wf7mi/VL8iNciT6rHih48Y55b4nKCHJCCzb4y0nwFmin3ZEMIoLfZF8F7nncFmvnWBaBj7CGAYA/WGJsUwHdYqVDwAmNsUgAx4CGgAA7GOOxADYOFWOaIKifuVYzmOpREqA21Mo7aPsgiY1PhOMAmxtR+AUbYH3Id2wc0SAFIQTsn9IUGWR8k9jx3vtXSiAacFxTAGakBk9UudkNECd6jLe+6HrshshvIuC6IlLMRy7er+JpcKma24SlE4cFZSZJDGVVrsNvitQhQrDhW0jfiOLfFd47C42eHT56D/BK0To+58Ahj+cAT8HT1UWlfLZCCd/uKawzU0Rh2EyIX/Icqth3niG8ybNroezwe6khdCNxRN+l4XGdOLVLlOOt2hTRJlr1ETIuMAltVTMz70mJrkdGAaZLSmnBEqmAE32JCMmuTlCnRgsBENtOUpHhvvsYIL0ibnBkaC6QvKcR7738GKp0AKnim7xgUSNv1bpS8QwhBt8r+EP47v/oyRK/S34yJ9nT+AN0Tkm4OdB9E4BsmXM3SnMlRFUrtp6IDpV2eKzdYvF3etm3KhQksbOLChGkSmcBdmcEwvqkrMy5BzL00NZeu3qPYJOOuCc+5NjcWKXQxFvTa3NoXJ4d8in7fiAUuTt781dkvuHX4K8AA2Usy7yNKLy0AAAAASUVORK5CYII=
">
    <link href="/rss.xml" rel="alternate" type="application/rss+xml" title="Articles from Distill">
  
    <title>Understanding Convolutions on Graphs</title>
    
    <link rel="canonical" href="https://distill.pub/2021/understanding-gnns">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="Understanding the building blocks and design choices of graph neural networks.">
    <meta property="article:published" itemprop="datePublished" content="2021-09-02">
    <meta property="article:created" itemprop="dateCreated" content="2021-09-02">
    
    <meta property="article:modified" itemprop="dateModified" content="2022-02-21T03:59:28.000Z">
    
    <meta property="article:author" content="Ameya Daigavane">
    <meta property="article:author" content="Balaraman Ravindran">
    <meta property="article:author" content="Gaurav Aggarwal">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="Understanding Convolutions on Graphs">
    <meta property="og:description" content="Understanding the building blocks and design choices of graph neural networks.">
    <meta property="og:url" content="https://distill.pub/2021/understanding-gnns">
    <meta property="og:image" content="https://distill.pub/2021/understanding-gnns/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Understanding Convolutions on Graphs">
    <meta name="twitter:description" content="Understanding the building blocks and design choices of graph neural networks.">
    <meta name="twitter:url" content="https://distill.pub/2021/understanding-gnns">
    <meta name="twitter:image" content="https://distill.pub/2021/understanding-gnns/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="Understanding Convolutions on Graphs">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/2021/understanding-gnns">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="9">
    <meta name="citation_firstpage" content="e32">
    <meta name="citation_doi" content="10.23915/distill.00032">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/09/02">
    <meta name="citation_publication_date" content="2021/09/02">
    <meta name="citation_author" content="Daigavane, Ameya">
    <meta name="citation_author_institution" content="Google Research">
    <meta name="citation_author" content="Ravindran, Balaraman">
    <meta name="citation_author_institution" content="Google Research">
    <meta name="citation_author" content="Aggarwal, Gaurav">
    <meta name="citation_author_institution" content="Google Research">
    <meta name="citation_reference" content="citation_title=A Gentle Introduction to Graph Neural Networks;citation_author=Benjamin Sanchez-Lengeling;citation_author=Emily Reif;citation_author=Adam Pearce;citation_author=Alex Wiltschko;citation_publication_date=2021;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Graph Kernels;citation_author=S.V.N. Vishwanathan;citation_author=Nicol N. Schraudolph;citation_author=Risi Kondor;citation_author=Karsten M. Borgwardt;citation_publication_date=2010;citation_journal_title=Journal of Machine Learning Research;citation_volume=11;citation_number=40;">
    <meta name="citation_reference" content="citation_title=Node2vec: Scalable Feature Learning for Networks;citation_author=Aditya Grover;citation_author=Jure Leskovec;citation_publication_date=2016;">
    <meta name="citation_reference" content="citation_title=DeepWalk: Online Learning of Social Representations;citation_author=Bryan Perozzi;citation_author=Rami Al-Rfou;citation_author=Steven Skiena;citation_publication_date=2014;">
    <meta name="citation_reference" content="citation_title=Convolutional Networks on Graphs for Learning Molecular Fingerprints;citation_author=David K Duvenaud;citation_author=Dougal Maclaurin;citation_author=Jorge Iparraguirre;citation_author=Rafael Bombarell;citation_author=Timothy Hirzel;citation_author=Alan Aspuru-Guzik;citation_author=Ryan P Adams;citation_publication_date=2015;citation_volume=28;">
    <meta name="citation_reference" content="citation_title=Neural Message Passing for Quantum Chemistry;citation_author=Justin Gilmer;citation_author=Samuel S. Schoenholz;citation_author=Patrick F. Riley;citation_author=Oriol Vinyals;citation_author=George E. Dahl;citation_publication_date=2017;citation_volume=70;">
    <meta name="citation_reference" content="citation_title=Learning Convolutional Neural Networks for Graphs;citation_author=Mathias Niepert;citation_author=Mohamed Ahmed;citation_author=Konstantin Kutzkov;citation_publication_date=2016;">
    <meta name="citation_reference" content="citation_title=A Tutorial on Spectral Clustering;citation_author=Ulrike von Luxburg;citation_publication_date=2007;citation_arxiv_id=0711.0189;">
    <meta name="citation_reference" content="citation_title=Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering;citation_author=Micha\&quot;{e}l Defferrard;citation_author=Xavier Bresson;citation_author=Pierre Vandergheynst;citation_publication_date=2016;citation_volume=29;">
    <meta name="citation_reference" content="citation_title=Wavelets on Graphs via Spectral Graph Theory;citation_author=David K. Hammond;citation_author=Pierre Vandergheynst;citation_author=Rémi Gribonval;citation_publication_date=2011;citation_journal_title=Applied and Computational Harmonic Analysis;citation_volume=30;citation_number=2;">
    <meta name="citation_reference" content="citation_title=Chebyshev Polynomials;citation_author=J.C. Mason;citation_author=D.C. Handscomb;citation_publication_date=2002;">
    <meta name="citation_reference" content="citation_title=Semi-Supervised Classification with Graph Convolutional Networks;citation_author=Thomas N. Kipf;citation_author=Max Welling;citation_publication_date=2017;">
    <meta name="citation_reference" content="citation_title=Graph Attention Networks;citation_author=Petar Veličković;citation_author=Guillem Cucurull;citation_author=Arantxa Casanova;citation_author=Adriana Romero;citation_author=Pietro Liò;citation_author=Yoshua Bengio;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Inductive Representation Learning on Large Graphs;citation_author=Will Hamilton;citation_author=Zhitao Ying;citation_author=Jure Leskovec;citation_publication_date=2017;citation_volume=30;">
    <meta name="citation_reference" content="citation_title=How Powerful are Graph Neural Networks?;citation_author=Keyulu Xu;citation_author=Weihua Hu;citation_author=Jure Leskovec;citation_author=Stefanie Jegelka;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=Relational inductive biases, deep learning, and graph networks;citation_author=Peter W. Battaglia;citation_author=Jessica B. Hamrick;citation_author=Victor Bapst;citation_author=Alvaro Sanchez-Gonzalez;citation_author=Vin{\'i}cius Flores Zambaldi;citation_author=Mateusz Malinowski;citation_author=Andrea Tacchetti;citation_author=David Raposo;citation_author=Adam Santoro;citation_author=Ryan Faulkner;citation_author=Caglar Gulcehre;citation_author=H. Francis Song;citation_author=Andrew J. Ballard;citation_author=Justin Gilmer;citation_author=George E. Dahl;citation_author=Ashish Vaswani;citation_author=Kelsey R. Allen;citation_author=Charles Nash;citation_author=Victoria Langston;citation_author=Chris Dyer;citation_author=Nicolas Heess;citation_author=Daan Wierstra;citation_author=Pushmeet Kohli;citation_author=Matthew Botvinick;citation_author=Oriol Vinyals;citation_author=Yujia Li;citation_author=Razvan Pascanu;citation_publication_date=2018;citation_arxiv_id=1806.01261;">
    <meta name="citation_reference" content="citation_title=Spectral Networks and Locally Connected Networks on Graphs;citation_author=Joan Bruna;citation_author=Wojciech Zaremba;citation_author=Arthur Szlam;citation_author=Yann LeCun;citation_publication_date=2014;citation_arxiv_id=1312.6203;">
    <meta name="citation_reference" content="citation_title=ImageNet: A Large-Scale Hierarchical Image Database;citation_author=J. Deng;citation_author=W. Dong;citation_author=R. Socher;citation_author=L.-J. Li;citation_author=K. Li;citation_author=L. Fei-Fei;citation_publication_date=2009;">
    <meta name="citation_reference" content="citation_title=On the Transferability of Spectral Graph Filters;citation_author=Ron Levie;citation_author=Elvin Isufi;citation_author=Gitta Kutyniok;citation_publication_date=2019;citation_volume=;citation_number=;">
    <meta name="citation_reference" content="citation_title=Directional Graph Networks;citation_author=Dominique Beaini;citation_author=Saro Passaro;citation_author=Vincent Létourneau;citation_author=William L. Hamilton;citation_author=Gabriele Corso;citation_author=Pietro Liò;citation_publication_date=2021;">
    <meta name="citation_reference" content="citation_title=Deep contextualized word representations;citation_author=Matthew E. Peters;citation_author=Mark Neumann;citation_author=Mohit Iyyer;citation_author=Matt Gardner;citation_author=Christopher Clark;citation_author=Kenton Lee;citation_author=Luke Zettlemoyer;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding;citation_author=Jacob Devlin;citation_author=Ming-Wei Chang;citation_author=Kenton Lee;citation_author=Kristina Toutanova;citation_publication_date=2019;">
    <meta name="citation_reference" content="citation_title=Strategies for Pre-training Graph Neural Networks;citation_author=Weihua Hu*;citation_author=Bowen Liu*;citation_author=Joseph Gomes;citation_author=Marinka Zitnik;citation_author=Percy Liang;citation_author=Vijay Pande;citation_author=Jure Leskovec;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Multi-Stage Self-Supervised Learning for Graph Convolutional Networks on Graphs with Few Labeled Nodes;citation_author=Ke Sun;citation_author=Zhouchen Lin;citation_author=Zhanxing Zhu;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=When Does Self-Supervision Help Graph Convolutional Networks?;citation_author=Yuning You;citation_author=Tianlong Chen;citation_author=Zhangyang Wang;citation_author=Yang Shen;citation_publication_date=2020;citation_arxiv_id=2006.09136;">
    <meta name="citation_reference" content="citation_title=Self-supervised Learning on Graphs: Deep Insights and New Direction;citation_author=Wei Jin;citation_author=Tyler Derr;citation_author=Haochen Liu;citation_author=Yiqi Wang;citation_author=Suhang Wang;citation_author=Zitao Liu;citation_author=Jiliang Tang;citation_publication_date=2020;citation_arxiv_id=2006.10141;">
    <meta name="citation_reference" content="citation_title=Noise-Contrastive Estimation of Unnormalized Statistical Models, with Applications to Natural Image Statistics;citation_author=Michael U. Gutmann;citation_author=Aapo Hyvärinen;citation_publication_date=2012;citation_journal_title=Journal of Machine Learning Research;citation_volume=13;citation_number=11;">
    <meta name="citation_reference" content="citation_title=Learning word embeddings efficiently with noise-contrastive estimation;citation_author=Andriy Mnih;citation_author=Koray Kavukcuoglu;citation_publication_date=2013;citation_volume=26;">
    <meta name="citation_reference" content="citation_title=A Comprehensive Survey on Graph Neural Networks;citation_author=Z. Wu;citation_author=S. Pan;citation_author=F. Chen;citation_author=G. Long;citation_author=C. Zhang;citation_author=P. S. Yu;citation_publication_date=2020;citation_journal_title=IEEE Transactions on Neural Networks and Learning Systems;">
    <meta name="citation_reference" content="citation_title=Graph Neural Networks: A Review of Methods and Applications;citation_author=Jie Zhou;citation_author=Ganqu Cui;citation_author=Zhengyan Zhang;citation_author=Cheng Yang;citation_author=Zhiyuan Liu;citation_author=Maosong Sun;citation_publication_date=2018;citation_arxiv_id=1812.08434;">
    <meta name="citation_reference" content="citation_title=Dropout: A Simple Way to Prevent Neural Networks from Overfitting;citation_author=Nitish Srivastava;citation_author=Geoffrey Hinton;citation_author=Alex Krizhevsky;citation_author=Ilya Sutskever;citation_author=Ruslan Salakhutdinov;citation_publication_date=2014;citation_journal_title=Journal of Machine Learning Research;citation_volume=15;citation_number=56;">
    <meta name="citation_reference" content="citation_title=DropEdge: Towards Deep Graph Convolutional Networks on Node Classification;citation_author=Yu Rong;citation_author=Wenbing Huang;citation_author=Tingyang Xu;citation_author=Junzhou Huang;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=An End-to-End Deep Learning Architecture for Graph Classification;citation_author=Muhan Zhang;citation_author=Zhicheng Cui;citation_author=Marion Neumann;citation_author=Yixin Chen;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Hierarchical Graph Representation Learning with Differentiable Pooling;citation_author=Zhitao Ying;citation_author=Jiaxuan You;citation_author=Christopher Morris;citation_author=Xiang Ren;citation_author=Will Hamilton;citation_author=Jure Leskovec;citation_publication_date=2018;citation_volume=31;">
    <meta name="citation_reference" content="citation_title=Self-Attention Graph Pooling;citation_author=Junhyun Lee;citation_author=Inyeop Lee;citation_author=Jaewoo Kang;citation_publication_date=2019;citation_volume=97;">
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
    <script type="text/json">
      {
    "title": "Understanding Convolutions on Graphs",
    "description": "Understanding the building blocks and design choices of graph neural networks.",
    "authors": [
        {
            "author": "Ameya Daigavane",
            "authorURL": "https://ameya98.github.io/",
            "affiliation": "Google Research",
            "affiliationURL": "https://research.google/"
        },
        {
            "author": "Balaraman Ravindran",
            "authorURL": "https://www.cse.iitm.ac.in/~ravi/",
            "affiliation": "Google Research",
            "affiliationURL": "https://research.google/"
        },
        {
            "author": "Gaurav Aggarwal",
            "authorURL": "https://research.google/people/GauravAggarwal/",
            "affiliation": "Google Research",
            "affiliationURL": "https://research.google/"
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
}
    </script>
  </d-front-matter>

  <d-title>
    <h1>Understanding Convolutions on Graphs</h1>
    <p>Understanding the building blocks and design choices of graph neural networks.</p>
  </d-title>

  <d-byline>
  <div class="byline grid">
    <div class="authors-affiliations grid">
      <h3>Authors</h3>
      <h3>Affiliations</h3>
      
        <p class="author">
          
            <a class="name" href="https://ameya98.github.io/">Ameya Daigavane</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://research.google/">Google Research</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://www.cse.iitm.ac.in/~ravi/">Balaraman Ravindran</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://research.google/">Google Research</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://research.google/people/GauravAggarwal/">Gaurav Aggarwal</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://research.google/">Google Research</a>
        </p>
      
    </div>
    <div>
      <h3>Published</h3>
      
        <p>Sept. 2, 2021</p> 
    </div>
    <div>
      <h3>DOI</h3>
      
        <p><a href="https://doi.org/10.23915/distill.00032">10.23915/distill.00032</a></p>
    </div>
  </div>
</d-byline><d-article>
    <d-contents>
      <nav class="l-text figcaption">
        <h3>Contents</h3>
        <div><a href="#introduction">Introduction</a></div>
        <div><a href="#challenges">The Challenges of Computation on Graphs</a></div>
        <ul>
          <li><a href="#lack-of-consistent-structure">Lack of Consistent Structure</a></li>
          <li><a href="#node-order">Node-Order Equivariance</a></li>
          <li><a href="#scalability">Scalability</a></li>
        </ul>
        <div><a href="#problem-and-notation">Problem Setting and Notation</a></div>
        <div><a href="#extending">Extending Convolutions to Graphs</a></div>
        <div><a href="#polynomial-filters">Polynomial Filters on Graphs</a></div>
        <div><a href="#modern-gnns">Modern Graph Neural Networks</a></div>
        <div><a href="#interactive">Interactive Graph Neural Networks</a></div>
        <div><a href="#from-local-to-global">From Local to Global Convolutions</a></div>
        <ul>
          <li><a href="#spectral">Spectral Convolutions</a></li>
          <li><a href="#graph-embeddings">Global Propagation via Graph Embeddings</a></li>
        </ul>
        <div><a href="#learning">Learning GNN Parameters</a></div>
        <!-- <div><a href="#gnns-vs-cnns">Are GNNs 'better' than CNNs?</a></div> -->
        <div><a href="#further-reading">Conclusions and Further Reading</a></div>
        <ul>
          <li><a href="#practical-techniques">GNNs in Practice</a></li>
          <li><a href="#different-kinds-of-graphs">Different Kinds of Graphs</a></li>
          <li><a href="#pooling">Pooling</a></li>
        </ul>
        <div><a href="#supplementary">Supplementary Material</a></div>
        <ul>
          <li><a href="#experiments-notebooks">Reproducing Experiments</a></li>
          <li><a href="#visualizations-notebooks">Recreating Visualizations</a></li>
        </ul>
      </nav>
    </d-contents>
    <div>
      <p><em>
        This article is one of two Distill publications about graph neural networks.
        Take a look at
        <a href="https://distill.pub/2021/gnn-intro/">A Gentle Introduction to Graph Neural Networks</a>
        <d-cite key="gnn-intro"></d-cite>
        for a companion view on many things graph and neural network related.
      </em></p>
      <p id="introduction">
        Many systems and interactions - social networks, molecules, organizations, citations, physical models, transactions - can be represented quite naturally as graphs.
        How can we reason about and make predictions within these systems?
      </p>
      <p>
        One idea is to look at tools that have worked well in other domains: neural networks have shown immense predictive power in a variety of learning tasks.
        However, neural networks have been traditionally used to operate on fixed-size and/or regular-structured inputs (such as sentences, images and video).
        This makes them unable to elegantly process graph-structured data.
      </p>
      <figure id="standard-neural-networks" class="l-page">
        <img src="images/standard-neural-networks.svg" style="width: 100%;" alt="Neural networks generally operate on fixed-size input vectors. How do we input a graph to a neural network?" title="How do we input a graph to a neural network?">
      </figure>
    </div>
    
    <p>
      Graph neural networks (GNNs) are a family of neural networks that can operate naturally on graph-structured data. 
      By extracting and utilizing features from the underlying graph,
      GNNs can make more informed predictions about entities in these interactions,
      as compared to models that consider individual entities in isolation.
    </p>
    <p>
      GNNs are not the only tools available to model graph-structured data:
      graph kernels <d-cite key="graph-kernels"></d-cite>
      and random-walk methods <d-cite key="node2vec,deepwalk"></d-cite>
      were some of the most popular ones.
      Today, however, GNNs have largely replaced these techniques
      because of their inherent flexibility to model the underlying systems
      better.
    </p>
    <p>
      In this article, we will illustrate
      the challenges of computing over graphs, 
      describe the origin and design of graph neural networks,
      and explore the most popular GNN variants in recent times.
      Particularly, we will see that many of these variants
      are composed of similar building blocks.
    </p>
    <p>
      First, let’s discuss some of the complications that graphs come with.
    </p>

    <h2 id="challenges">
      The Challenges of Computation on Graphs
    </h2>

    <h3 id="lack-of-consistent-structure">
      Lack of Consistent Structure
    </h3>
      <p>
        Graphs are extremely flexible mathematical models; but this means they lack consistent structure across instances.
        Consider the task of predicting whether a given chemical molecule is toxic <d-cite key="molecules-gnn,neural-message-passing"></d-cite>&nbsp;:
      </p>
      <figure class="l-page-outset" id="menthyl-nicotinate-molecule" style="display: inline-flex;">
        <img src="images/1,2,6-trigalloyl-glucose-molecule.svg" style="width: 50%;" alt="The molecular structure of non-toxic 1,2,6-trigalloyl-glucose.">
        <img src="images/caramboxin-molecule.svg" style="width: 25%; height: 60%; margin-top: 8%; margin-left: 10%;" alt="The molecular structure of toxic caramboxin.">
      </figure>
      <figure class="l-page-outset" style="display: flex; margin-top: 0%; margin-bottom: 3%;">
        <figure style="width: 50%; margin-left: 1%; margin-bottom: 0%;">
          <figcaption><b>Left:</b> A <span style="color: green;">non-toxic</span> 1,2,6-trigalloyl-glucose molecule.</figcaption>
        </figure>
        <figure style="width: 50%; margin-right: 15%; margin-bottom: 0%; text-align: right;">
          <figcaption><b>Right:</b> A <span style="color: rgba(228, 35, 35, 0.911);">toxic</span> caramboxin molecule.</figcaption>
        </figure>
      </figure>
      <p>
        Looking at a few examples, the following issues quickly become apparent:
      </p>
      <ul>
        <li>Molecules may have different numbers of atoms.</li>
        <li>The atoms in a molecule may be of different types.</li>
        <li>Each of these atoms may have different number of connections.</li>
        <li>These connections can have different strengths.</li>
      </ul>
      <p>
        Representing graphs in a format that can be computed over is non-trivial,
        and the final representation chosen often depends significantly on the actual problem.
      </p>

    <h3 id="node-order">
      Node-Order Equivariance
    </h3>
    <p>
      Extending the point above: graphs often have no inherent ordering present amongst the nodes.
      Compare this to images, where every pixel is uniquely determined by its absolute position within the image!
    </p>

      <figure id="node-order-alternatives" class="l-page" style="margin-bottom: 1em;">
        <img src="images/node-order-alternatives.svg" style="margin-bottom: 1em; margin-left: 15%; width: 70%;" alt="Representing the graph as one vector requires us to fix an order on the nodes. But what do we do when the nodes have no inherent order?">
        <figcaption style="text-align: center; margin-left: 10%; width: 80%;">
          Representing the graph as one vector requires us to fix an order on the nodes.
          But what do we do when the nodes have no inherent order?
          <b>Above:</b> 
          The same graph labelled in two different ways. The alphabets indicate the ordering of the nodes.
        </figcaption>
      </figure>
  
    <p>
      As a result, we would like our algorithms to be node-order equivariant:
      they should not depend on the ordering of the nodes of the graph.
      If we permute the nodes in some way, the resulting representations of 
      the nodes as computed by our algorithms should also be permuted in the same way.
    </p>

    <h3 id="scalability">
      Scalability
    </h3>
      <p>
        Graphs can be really large! Think about social networks like Facebook and Twitter, which have over a billion users. 
        Operating on data this large is not easy.
      </p>
      <p>
        Luckily, most naturally occuring graphs are ‘sparse’:
        they tend to have their number of edges linear in their number of vertices.
        We will see that this allows the use of clever methods
        to efficiently compute representations of nodes within the graph.
        Further, the methods that we look at here will have significantly fewer parameters
        in comparison to the size of the graphs they operate on.
      </p>

    <h2 id="problem-and-notation">
      Problem Setting and Notation
    </h2>
      <p>
        There are many useful problems that can be formulated over graphs:
      </p>
        <ul>
          <li><b>Node Classification:</b> Classifying individual nodes.</li>
          <li><b>Graph Classification:</b> Classifying entire graphs. </li>
          <li><b>Node Clustering:</b> Grouping together similar nodes based on connectivity.</li>
          <li><b>Link Prediction:</b> Predicting missing links.</li>
          <li><b>Influence Maximization:</b> Identifying influential nodes.</li>
        </ul>
      <figure id="graph-tasks" class="l-page">
        <img src="images/graph-tasks.svg" style="width: 100%;" alt="Examples of problems that can be defined over graphs.">
        <figcaption style="text-align: center;">
          Examples of problems that can be defined over graphs.
          This list is not exhaustive!
        </figcaption>
      </figure>
      <p>
        A common precursor in solving many of these problems is <b>node representation learning</b>:
        learning to map individual nodes to fixed-size real-valued vectors (called ‘representations’ or ‘embeddings’).
      </p>
      <p>
        In <a href="#learning">Learning GNN Parameters</a>, we will see how the learnt embeddings can be used for these tasks.
      </p>
      <p>
        Different GNN variants are distinguished by the way these representations are computed.
        Generally, however, GNNs compute node representations in an iterative process.
        We will use the notation <span><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mi>h</mi><mi>v</mi><mrow><mo>(</mo><mi>k</mi><mo>)</mo></mrow></msubsup></mrow><annotation encoding="application/x-tex