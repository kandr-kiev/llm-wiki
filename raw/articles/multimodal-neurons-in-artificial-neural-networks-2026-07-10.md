---

source_url: https://distill.pub/2021/multimodal-neurons
ingested: 2026-07-10
sha256: 3c1a33065305607ebc78ca5991c68b240f2e9e154205e7b96e174166bdaa37f4
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
  
  
  <style id="distill-article-specific-styles">
    @media (min-height: 900px) {
  d-article hr {
    margin-top: 120px !important;
    margin-bottom: 100px !important;
  }
}

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

.fullscreen-diagram {
  grid-column: screen;
  background: #f8f8fb;
  padding: 10px;
  padding-top: 40px;
  padding-bottom: 40px;
  border-top: 1px solid #f0f0f0;
  border-bottom: 1px solid #f0f0f0;
  margin-top: 40px;
  margin-bottom: 60px;
}

.margin-diagram {
  grid-column: 12 / 15;
  grid-row: auto / span 3;
  margin-top: 6px;
}
@media (min-width: 1800px) {
  .margin-diagram {
    margin-left: 60px;
  }
}

.placeholder {
  padding: 40px;
  font-size: 80%;
  background: #f8f8fb;
  border: 1px solid #f0f0f0;
  border-radius: 4px;
  grid-column: text;
  margin-top: 20px;
  margin-bottom: 20px;
}
.todo {
  margin-top: 8px;
  padding: 10px;
  font-size: 80%;
  line-height: 140%;
  background: rgb(250, 249, 242);
  border: 1px solid rgb(233, 230, 214);
  border-radius: 4px;
  max-width: 250px;
  margin-right: 4px;
  grid-column-start: gutter-start;
  grid-column-end: screen-end;
  height: fit-content;
}
/* .sensitivity-warn {
  margin-bottom: 16px;
  padding: 10px;
  font-size: 80%;
  line-height: 140%;
  background: #EEE;
  border: 1px solid #AAA;
  border-radius: 4px;
  height: fit-content;
} */

.sensitivity-warn {
  border-left: 8px solid hsl(40, 70%, 80%);
  padding: 12px;
  padding-left: 16px;
  margin-bottom: 16px;
  border-radius: 4px;
  background: hsl(40, 80%, 95%);
}

.sensitivity-warn:before {
  content: "Content Warning";
  font-weight: bold;
  display: block;
  padding-bottom: 4px;
}

d-footnote {
  margin-left: -1px;
  margin-right: 4px;
}
.footnote-sep {
  width: 0px;
}
.footnote-sep::before {
  line-height: 1em;
  top: -0.5em;
  font-size: 0.75em;
  color: #999;
  margin-left: -6px;
  margin-right: 1px;
  content: ',';
}

d-footnote[comma]::before {
  vertical-align: super;
  line-height: 1em;
  top: -0.5em;
  font-size: 0.75em;
  color: #999;
  margin-left: -6px;
  margin-right: 1px;
  content: ',';
}

d-article h2 {
  border-bottom: none;
}

/* ****************************************
 * TOC
 ******************************************/
@media (max-width: 1300px) {
  d-contents {
    display: none;
  }
}

/* d-article d-contents {
  align-self: start;
  grid-column: 1 / 4;
  grid-row: auto / span 3;
  width: calc(100% + 32px);
  margin-right: -16px;
  margin-top:  0em;
  display: grid;
  grid-template-columns: 
    minmax(8px, 1fr) [toc] auto 
    minmax(8px, 1fr) [toc-line] 1px
    minmax(32px, 2fr );
}

d-article d-contents nav {
  grid-column: toc;
}

d-article d-contents .toc-line {
  border-right: 1px solid rgba(0, 0, 0, 0.1);
  grid-column: toc-line;
} */
b i {
  display: inline;
}

d-article d-contents {
  align-self: start;
  grid-column: 1 / 4;
  grid-row: auto / span 4;
  justify-self: end;
  margin-top: 0em;
  padding-right: 3em;
  padding-left: 2em;
  border-right: 1px solid rgba(0, 0, 0, 0.1);
}

d-contents a:hover {
  border-bottom: none;
}

d-contents nav h3 {
  margin-top: 0;
  margin-bottom: 1em;
}

d-contents nav div {
  color: rgba(0, 0, 0, 0.8);
  font-weight: bold;
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

d-contents nav > div > a:hover,
d-contents nav > ul > li > a:hover {
  text-decoration: none;
}

d-article h2 {
  border-bottom: none !important;
}

d-article h3 {
  font-size: 26px !important;
}

  </style>
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
  
    <title>Multimodal Neurons in Artificial Neural Networks</title>
    
    <link rel="canonical" href="https://distill.pub/2021/multimodal-neurons">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="We report the existence of multimodal neurons in artificial neural networks, similar to those found in the human brain.">
    <meta property="article:published" itemprop="datePublished" content="2021-03-04">
    <meta property="article:created" itemprop="dateCreated" content="2021-03-04">
    
    <meta property="article:modified" itemprop="dateModified" content="2021-03-22T15:04:13.000Z">
    
    <meta property="article:author" content="Gabriel Goh">
    <meta property="article:author" content="Nick Cammarata †">
    <meta property="article:author" content="Chelsea Voss †">
    <meta property="article:author" content="Shan Carter">
    <meta property="article:author" content="Michael Petrov">
    <meta property="article:author" content="Ludwig Schubert">
    <meta property="article:author" content="Alec Radford">
    <meta property="article:author" content="Chris Olah">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="Multimodal Neurons in Artificial Neural Networks">
    <meta property="og:description" content="We report the existence of multimodal neurons in artificial neural networks, similar to those found in the human brain.">
    <meta property="og:url" content="https://distill.pub/2021/multimodal-neurons">
    <meta property="og:image" content="https://distill.pub/2021/multimodal-neurons/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Multimodal Neurons in Artificial Neural Networks">
    <meta name="twitter:description" content="We report the existence of multimodal neurons in artificial neural networks, similar to those found in the human brain.">
    <meta name="twitter:url" content="https://distill.pub/2021/multimodal-neurons">
    <meta name="twitter:image" content="https://distill.pub/2021/multimodal-neurons/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="Multimodal Neurons in Artificial Neural Networks">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/2021/multimodal-neurons">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="3">
    <meta name="citation_firstpage" content="e30">
    <meta name="citation_doi" content="10.23915/distill.00030">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/03/04">
    <meta name="citation_publication_date" content="2021/03/04">
    <meta name="citation_author" content="Goh, Gabriel">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="†, Nick Cammarata">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="†, Chelsea Voss">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Carter, Shan">
    <meta name="citation_author_institution" content="Observable">
    <meta name="citation_author" content="Petrov, Michael">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Schubert, Ludwig">
    <meta name="citation_author" content="Radford, Alec">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Olah, Chris">
    <meta name="citation_reference" content="citation_title=Invariant visual representation by single neurons in the human brain;citation_author=R Quian Quiroga;citation_author=Leila Reddy;citation_author=Gabriel Kreiman;citation_author=Christof Koch;citation_author=Itzhak Fried;citation_publication_date=2005;citation_journal_title=Nature;citation_volume=435;citation_number=7045;">
    <meta name="citation_reference" content="citation_title=Explicit encoding of multimodal percepts by single neurons in the human brain;citation_author=Rodrigo Quian Quiroga;citation_author=Alexander Kraskov;citation_author=Christof Koch;citation_author=Itzhak Fried;citation_publication_date=2009;citation_journal_title=Current Biology;citation_volume=19;citation_number=15;">
    <meta name="citation_reference" content="citation_title=Learning Transferable Visual Models From Natural Language Supervision;citation_author=Alec Radford;citation_author=Jong Wook Kim;citation_author=Chris Hallacy;citation_author=Aditya Ramesh;citation_author=Gabriel Goh;citation_author=Sandhini Agarwal;citation_author=Girish Sastry;citation_author=Amanda Askell;citation_author=Pamela Mishkin;citation_author=Jack Clark;citation_author=Gretchen Krueger;citation_author=Ilya Sutskever;citation_publication_date=2021;">
    <meta name="citation_reference" content="citation_title=Deep Residual Learning for Image Recognition;citation_author=Kaiming He;citation_author=Xiangyu Zhang;citation_author=Shaoqing Ren;citation_author=Jian Sun;citation_publication_date=2015;citation_arxiv_id=1512.03385;">
    <meta name="citation_reference" content="citation_title=Attention is all you need;citation_author=Ashish Vaswani;citation_author=Noam Shazeer;citation_author=Niki Parmar;citation_author=Jakob Uszkoreit;citation_author=Llion Jones;citation_author=Aidan N Gomez;citation_author=Lukasz Kaiser;citation_author=Illia Polosukhin;citation_publication_date=2017;">
    <meta name="citation_reference" content="citation_title=Improved deep metric learning with multi-class n-pair loss objective;citation_author=Kihyuk Sohn;citation_publication_date=2016;">
    <meta name="citation_reference" content="citation_title=Contrastive multiview coding;citation_author=Yonglong Tian;citation_author=Dilip Krishnan;citation_author=Phillip Isola;citation_publication_date=2019;citation_arxiv_id=1906.05849;">
    <meta name="citation_reference" content="citation_title=Linear algebraic structure of word senses, with applications to polysemy;citation_author=Sanjeev Arora;citation_author=Yuanzhi Li;citation_author=Yingyu Liang;citation_author=Tengyu Ma;citation_author=Andrej Risteski;citation_publication_date=2018;citation_journal_title=Transactions of the Association for Computational Linguistics;citation_volume=6;">
    <meta name="citation_reference" content="citation_title=Visualizing and understanding recurrent networks;citation_author=Andrej Karpathy;citation_author=Justin Johnson;citation_author=Li Fei-Fei;citation_publication_date=2015;citation_arxiv_id=1506.02078;">
    <meta name="citation_reference" content="citation_title=Object detectors emerge in deep scene cnns;citation_author=Bolei Zhou;citation_author=Aditya Khosla;citation_author=Agata Lapedriza;citation_author=Aude Oliva;citation_author=Antonio Torralba;citation_publication_date=2014;citation_arxiv_id=1412.6856;">
    <meta name="citation_reference" content="citation_title=Network Dissection: Quantifying Interpretability of Deep Visual Representations;citation_author=David Bau;citation_author=Bolei Zhou;citation_author=Aditya Khosla;citation_author=Aude Oliva;citation_author=Antonio Torralba;citation_publication_date=2017;citation_arxiv_id=1704.05796;">
    <meta name="citation_reference" content="citation_title=Zoom In: An Introduction to Circuits;citation_author=Chris Olah;citation_author=Nick Cammarata;citation_author=Ludwig Schubert;citation_author=Gabriel Goh;citation_author=Michael Petrov;citation_author=Shan Carter;citation_publication_date=2020;citation_journal_title=Distill;citation_volume=5;citation_number=3;">
    <meta name="citation_reference" content="citation_title=Multifaceted feature visualization: Uncovering the different types of features learned by each neuron in deep neural networks;citation_author=Anh Nguyen;citation_author=Jason Yosinski;citation_author=Jeff Clune;citation_publication_date=2016;citation_arxiv_id=1602.03616;">
    <meta name="citation_reference" content="citation_title=Sparse but not ‘grandmother-cell’ coding in the medial temporal lobe;citation_author=R Quian Quiroga;citation_author=Gabriel Kreiman;citation_author=Christof Koch;citation_author=Itzhak Fried;citation_publication_date=2008;citation_journal_title=Trends in cognitive sciences;citation_volume=12;citation_number=3;">
    <meta name="citation_reference" content="citation_title=Concept cells: the building blocks of declarative memory functions;citation_author=Rodrigo Quian Quiroga;citation_publication_date=2012;citation_journal_title=Nature Reviews Neuroscience;citation_volume=13;citation_number=8;">
    <meta name="citation_reference" content="citation_title=Emotional expressions reconsidered: Challenges to inferring emotion from human facial movements;citation_author=Lisa Feldman Barrett;citation_author=Ralph Adolphs;citation_author=Stacy Marsella;citation_author=Aleix M Martinez;citation_author=Seth D Pollak;citation_publication_date=2019;citation_journal_title=Psychological science in the public interest;citation_volume=20;citation_number=1;">
    <meta name="citation_reference" content="citation_title=Geographical evaluation of word embeddings;citation_author=Michal Konkol;citation_author=Toma{\v{s}} Brychc{\'\i}n;citation_author=Michal Nykl;citation_author=Toma{\v{s}} Hercig;citation_publication_date=2017;">
    <meta name="citation_reference" content="citation_title=Using Artificial Intelligence to Augment Human Intelligence;citation_author=Shan Carter;citation_author=Michael Nielsen;citation_publication_date=2017;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Visualizing Representations: Deep Learning and Human Beings;citation_author=Chris Olah;citation_publication_date=2015;">
    <meta name="citation_reference" content="citation_title=Natural language processing (almost) from scratch;citation_author=Ronan Collobert;citation_author=Jason Weston;citation_author=Leon Bottou;citation_author=Michael Karlen;citation_author=Koray Kavukcuoglu;citation_author=Pavel Kuksa;citation_publication_date=2011;citation_journal_title=Journal of machine learning research;citation_volume=12;citation_number=ARTICLE;">
    <meta name="citation_reference" content="citation_title=Linguistic regularities in continuous space word representations;citation_author=Toma{\v{s}} Mikolov;citation_author=Wen-tau Yih;citation_author=Geoffrey Zweig;citation_publication_date=2013;">
    <meta name="citation_reference" content="citation_title=Man is to computer programmer as woman is to homemaker? debiasing word embeddings;citation_author=Tolga Bolukbasi;citation_author=Kai-Wei Chang;citation_author=James Y Zou;citation_author=Venkatesh Saligrama;citation_author=Adam T Kalai;citation_publication_date=2016;">
    <meta name="citation_reference" content="citation_title=Intriguing properties of neural networks;citation_author=Christian Szegedy;citation_author=Wojciech Zaremba;citation_author=Ilya Sutskever;citation_author=Joan Bruna;citation_author=Dumitru Erhan;citation_author=Ian Goodfellow;citation_author=Rob Fergus;citation_publication_date=2013;citation_arxiv_id=1312.6199;">
    <meta name="citation_reference" content="citation_title=Visualizing higher-layer features of a deep network;citation_author=Dumitru Erhan;citation_author=Yoshua Bengio;citation_author=Aaron Courville;citation_author=Pascal Vincent;citation_publication_date=2009;citation_journal_title=University of Montreal;citation_volume=1341;">
    <meta name="citation_reference" content="citation_title=Feature Visualization;citation_author=Chris Olah;citation_author=Alexander Mordvintsev;citation_author=Ludwig Schubert;citation_publication_date=2017;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=How does the brain solve visual object recognition?;citation_author=James J DiCarlo;citation_author=Davide Zoccolan;citation_author=Nicole C Rust;citation_publication_date=2012;citation_journal_title=Neuron;citation_volume=73;citation_number=3;">
    <meta name="citation_reference" content="citation_title=Imagenet: A large-scale hierarchical image database;citation_author=Jia Deng;citation_author=Wei Dong;citation_author=Richard Socher;citation_author=Li-Jia Li;citation_author=Kai Li;citation_author=Li Fei-Fei;citation_publication_date=2009;">
    <meta name="citation_reference" content="citation_title=BREEDS: Benchmarks for Subpopulation Shift;citation_author=Shibani Santurkar;citation_author=Dimitris Tsipras;citation_author=Aleksander Madry;citation_publication_date=2020;citation_arxiv_id=2008.04859;">
    <meta name="citation_reference" content="citation_title=Global Weighted Average Pooling Bridges Pixel-level Localization and Image-level Classification;citation_author=Suo Qiu;citation_publication_date=2018;citation_arxiv_id=1809.08264;">
    <meta name="citation_reference" content="citation_title=Separating style and content with bilinear models;citation_author=Joshua B Tenenbaum;citation_author=William T Freeman;citation_publication_date=2000;citation_journal_title=Neural computation;citation_volume=12;citation_number=6;">
    <meta name="citation_reference" content="citation_title=The feeling wheel: A tool for expanding awareness of emotions and increasing spontaneity and intimacy;citation_author=Gloria Willcox;citation_publication_date=1982;citation_journal_title=Transactional Analysis Journal;citation_volume=12;citation_number=4;">
    <meta name="citation_reference" content="citation_title=Activation atlas;citation_author=Shan Carter;citation_author=Zan Armstrong;citation_author=Ludwig Schubert;citation_author=Ian Johnson;citation_author=Chris Olah;citation_publication_date=2019;citation_journal_title=Distill;citation_volume=4;citation_number=3;">
    <meta name="citation_reference" content="citation_title=Adversarial Patch;citation_author=Tom Brown;citation_author=Dandelion Mané;citation_author=Aurko Roy;citation_author=Martín Abadi;citation_author=Justin Gilmer;citation_publication_date=2017;citation_arxiv_id=1712.09665;">
    <meta name="citation_reference" content="citation_title=Synthesizing Robust Adversarial Examples;citation_author=Anish Athalye;citation_author=Logan Engstrom;citation_author=Andrew Ilyas;citation_author=Kevin Kwok;citation_publication_date=2017;citation_arxiv_id=1707.07397;">
    <meta name="citation_reference" content="citation_title=Studies of interference in serial verbal reactions.;citation_author=J Ridley Stroop;citation_publication_date=1935;citation_journal_title=Journal of experimental psychology;citation_volume=18;citation_number=6;">
    <meta name="citation_reference" content="citation_title=Curve Detectors;citation_author=Nick Cammarata;citation_author=Gabriel Goh;citation_author=Shan Carter;citation_author=Ludwig Schubert;citation_author=Michael Petrov;citation_author=Chris Olah;citation_publication_date=2020;citation_journal_title=Distill;citation_volume=5;citation_number=6;">
    <meta name="citation_reference" content="citation_title=An overview of early vision in inceptionv1;citation_author=Chris Olah;citation_author=Nick Cammarata;citation_author=Ludwig Schubert;citation_author=Gabriel Goh;citation_author=Michael Petrov;citation_author=Shan Carter;citation_publication_date=2020;citation_journal_title=Distill;citation_volume=5;citation_number=4;">
    <meta name="citation_reference" content="citation_title=Deep inside convolutional networks: Visualising image classification models and saliency maps;citation_author=Karen Simonyan;citation_author=Andrea Vedaldi;citation_author=Andrew Zisserman;citation_publication_date=2013;citation_arxiv_id=1312.6034;">
    <meta name="citation_reference" content="citation_title=Deep neural networks are easily fooled: High confidence predictions for unrecognizable images;citation_author=Anh Nguyen;citation_author=Jason Yosinski;citation_author=Jeff Clune;citation_publication_date=2015;citation_arxiv_id=1412.1897;">
    <meta name="citation_reference" content="citation_title=Inceptionism: Going deeper into neural networks;citation_author=Alexander Mordvintsev;citation_author=Christopher Olah;citation_author=Mike Tyka;citation_publication_date=2015;citation_journal_title=Google Research Blog;">
    <meta name="citation_reference" content="citation_title=Plug &amp; play generative networks: Conditional iterative generation of images in latent space;citation_author=Anh Nguyen;citation_author=Jeff Clune;citation_author=Yoshua Bengio;citation_author=Alexey Dosovitskiy;citation_author=Jason Yosinski;citation_publication_date=2016;citation_arxiv_id=1612.00005;">
    <meta name="citation_reference" content="citation_title=Sun database: Large-scale scene recognition from abbey to zoo;citation_author=Jianxiong Xiao;citation_author=James Hays;citation_author=Krista A Ehinger;citation_author=Aude Oliva;citation_author=Antonio Torralba;citation_publication_date=2010;">
    <meta name="citation_reference" content="citation_title=The pascal visual object classes (voc) challenge;citation_author=Mark Everingham;citation_author=Luc Van Gool;citation_author=Christopher KI Williams;citation_author=John Winn;citation_author=Andrew Zisserman;citation_publication_date=2010;citation_journal_title=International journal of computer vision;citation_volume=88;citation_number=2;">
    <meta name="citation_reference" content="citation_title=Fairface: Face attribute dataset for balanced race, gender, and age;citation_author=Kimmo Kärkkäinen;citation_author=Jungseock Joo;citation_publication_date=2019;citation_arxiv_id=1908.04913;">
    <meta name="citation_reference" content="citation_title=A style-based generator architecture for generative adversarial networks;citation_author=Tero Karras;citation_author=Samuli Laine;citation_author=Timo Aila;citation_publication_date=2019;">
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
    "title": "Multimodal Neurons in Artificial Neural Networks",
    "description": "We report the existence of multimodal neurons in artificial neural networks, similar to those found in the human brain.",
    "authors": [
        {
            "author": "Gabriel Goh",
            "authorURL": "http://gabgoh.github.io",
            "affiliation": "OpenAI",
            "affiliationURL": "http://openai.com"
        },
        {
            "author": "Nick Cammarata †",
            "authorURL": "http://nickcammarata.com",
            "affiliation": "OpenAI",
            "affiliationURL": "http://openai.com"
        },
        {
            "author": "Chelsea Voss †",
            "authorURL": "https://csvoss.com",
            "affiliation": "OpenAI",
            "affiliationURL": "http://openai.com"
        },
        {
            "author": "Shan Carter",
            "authorURL": "http://shancarter.com",
            "affiliation": "Observable",
            "affiliationURL": "https://observablehq.com"
        },
        {
            "author": "Michael Petrov",
            "authorURL": "http://michaelpetrov.com",
            "affiliation": "OpenAI",
            "affiliationURL": "http://openai.com"
        },
        {
            "author": "Ludwig Schubert",
            "authorURL": "https://schubert.io/",
            "affiliation": "",
            "affiliationURL": ""
        },
        {
            "author": "Alec Radford",
            "authorURL": "http://newmu.github.io/",
            "affiliation": "OpenAI",
            "affiliationURL": "http://openai.com"
        },
        {
            "author": "Chris Olah",
            "authorURL": "https://colah.github.io",
            "affiliation": "",
            "affiliationURL": ""
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
    <h1>Multimodal Neurons in Artificial Neural Networks</h1>
  </d-title>

  <d-byline>
  <div class="byline grid">
    <div class="authors-affiliations grid">
      <h3>Authors</h3>
      <h3>Affiliations</h3>
      
        <p class="author">
          
            <a class="name" href="http://gabgoh.github.io">Gabriel Goh</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="http://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="http://nickcammarata.com">Nick Cammarata †</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="http://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://csvoss.com">Chelsea Voss †</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="http://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="http://shancarter.com">Shan Carter</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://observablehq.com">Observable</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="http://michaelpetrov.com">Michael Petrov</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="http://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://schubert.io/">Ludwig Schubert</a>
        </p>
        <p class="affiliation">
        
        </p>
      
        <p class="author">
          
            <a class="name" href="http://newmu.github.io/">Alec Radford</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="http://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://colah.github.io">Chris Olah</a>
        </p>
        <p class="affiliation">
        
        </p>
      
    </div>
    <div>
      <h3>Published</h3>
      
        <p>March 4, 2021</p> 
    </div>
    <div>
      <h3>DOI</h3>
      
        <p><a href="https://doi.org/10.23915/distill.00030">10.23915/distill.00030</a></p>
    </div>
  </div>
</d-byline><d-article> </d-article>

  <div style="display: none">
    <!-- Due to build system issues we include d-cite tags manually. -->
    <!-- extracted 2021-03-22 by Ludwig from dev build via `[...document.querySelectorAll("#references-list > li")].map(node => node.id)` -->
    <d-cite bibtex-key="quiroga2005invariant"></d-cite>
    <d-cite bibtex-key="quiroga2009explicit"></d-cite>
    <d-cite bibtex-key="radford2020clip"></d-cite>
    <d-cite bibtex-key="kaiming2015resnet"></d-cite>
    <d-cite bibtex-key="vaswani2017attention"></d-cite>
    <d-cite bibtex-key="sohn2016improved"></d-cite>
    <d-cite bibtex-key="tian2019contrastive"></d-cite>
    <d-cite bibtex-key="arora2018linear"></d-cite>
    <d-cite bibtex-key="karpathy2015visualizing"></d-cite>
    <d-cite bibtex-key="zhou2014object"></d-cite>
    <d-cite bibtex-key="netdissect2017"></d-cite>
    <d-cite bibtex-key="olah2020zoom"></d-cite>
    <d-cite bibtex-key="nguyen2016multifaceted"></d-cite>
    <d-cite bibtex-key="quiroga2008sparse"></d-cite>
    <d-cite bibtex-key="quiroga2012concept"></d-cite>
    <d-cite bibtex-key="barrett2019emotional"></d-cite>
    <d-cite bibtex-key="konkol2017geographical"></d-cite>
    <d-cite bibtex-key="carter2017using"></d-cite>
    <d-cite bibtex-key="olah2015visualizing"></d-cite>
    <d-cite bibtex-key="collobert2011natural"></d-cite>
    <d-cite bibtex-key="mikolov2013linguistic"></d-cite>
    <d-cite bibtex-key="bolukbasi2016man"></d-cite>
    <d-cite bibtex-key="szegedy2013intriguing"></d-cite>
    <d-cite bibtex-key="erhan2009visualizing"></d-cite>
    <d-cite bibtex-key="olah2017feature"></d-cite>
    <d-cite bibtex-key="dicarlo2012does"></d-cite>
    <d-cite bibtex-key="deng2009imagenet"></d-cite>
    <d-cite bibtex-key="santurkar2020breeds"></d-cite>
    <d-cite bibtex-key="abs180908264"></d-cite>
    <d-cite bibtex-key="tenenbaum2000separating"></d-cite>
    <d-cite bibtex-key="willcox1982feeling"></d-cite>
    <d-cite bibtex-key="carter2019activation"></d-cite>
    <d-cite bibtex-key="brown2017adversarialpatch"></d-cite>
    <d-cite bibtex-key="athalye2017adversarialturtle"></d-cite>
    <d-cite bibtex-key="stroop1935studies"></d-cite>
    <d-cite bibtex-key="cammarata2020curve"></d-cite>
    <d-cite bibtex-key="olah2020overview"></d-cite>
    <d-cite bibtex-key="simonyan2013deep"></d-cite>
    <d-cite bibtex-key="nguyen2015deep"></d-cite>
    <d-cite bibtex-key="mordvintsev2015inceptionism"></d-cite>
    <d-cite bibtex-key="nguyen2016plug"></d-cite>
    <d-cite bibtex-key="xiao2010sun"></d-cite>
    <d-cite bibtex-key="everingham2010pascal"></d-cite>
    <d-cite bibtex-key="karkkainen2019fairface"></d-cite>
    <d-cite bibtex-key="karras2019style"></d-cite>
  </div>

  <d-appendix>
    <h3>Acknowledgments</h3>
    <p>
      We are deeply grateful to Sandhini Agarwal, Daniela Amodei, Dario Amodei,
      Tom Brown, Jeff Clune, Steve Dowling, Gretchen Krueger, Brice Menard,
      Reiichiro Nakano, Aditya Ramesh, Pranav Shyam, Ilya Sutskever and Martin
      Wattenberg.
    </p>

    <h3>Author Contributions</h3>
    <div 