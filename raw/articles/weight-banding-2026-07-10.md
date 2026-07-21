---

source_url: https://distill.pub/2020/circuits/weight-banding
ingested: 2026-07-10
sha256: 07d54a400c4867946fc55241b6c6709fabbccd72ee380a815192b3b17c26b8fc
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
  <style>
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

figure > svg text, figure > svg tspan {
  font-family: Arial, sans-serif;
  font-size: 27.5px;
  --font: normal 27.5px sans-serif;
  color: rgba(0, 0, 0, 0.6);
}

figure > svg text[font-weight=bold], figure > svg text[font-weight=bold] tspan {
  font-size: 26px;
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

#simplified-network-diagram ul {
  font-size: x-small;
}

#simplified-network-diagram li {
  margin: 1px;
}

div.weight-banding-example {
  float: left;
}

div.weight-banding-example a {
  text-decoration: none;
  border: none;
}


div.weight-banding-example img {
  width: 100%;
}

div.weight-banding-example span.label {
  width: 100%;
  text-align: center;
  clear: both;
  display: block;
  font-size: smaller;
}

a.figure-number::before {
	content: "Figure ";
}

a.figure-number,
a.section-number {
	border-bottom-color: hsla(206, 90%, 20%, 0.3);
	text-transform: uppercase;
	font-size: 0.85em;
	color: hsla(206, 90%, 20%, 0.7);
}

a.figure-number:hover,
a.section-number:hover {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: hsla(206, 90%, 20%, 0.7);
}


/* ************
 * Thread Info
 * ************/

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
  grid-template-columns: 45px 3fr 2fr;
  grid-template-areas:
    'icon explanation explanation '
    'icon prev next';
  grid-column-gap: 1.5em;
}

@media (min-width: 768px) {
  #thread-nav {
    grid-template-columns: 65px 3fr 2fr;
  }
}

#thread-nav .icon {
  grid-area: icon;
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

  </style>

    
    <link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA99JREFUeNrsG4t1ozDMzQSM4A2ODUonKBucN2hugtIJ6E1AboLcBiQTkJsANiAb9OCd/OpzMWBJBl5TvaeXPiiyJetry0J8wW3D3QpjRh3GjneXDq+fSQA9s2mH9x3KDhN4foJfCb8N/Jrv+2fnDn8vLRQOplWHVYdvHZYdZsBcZP1vBmh/n8DzEmhUQDPaOuP9pFuY+JwJHwHnCLQE2tnWBGEyXozY9xCUgHMhhjE2I4heVWtgIkZ83wL6Qgxj1obfWBxymPwe+b00BCCRNPbwfb60yleAkkBHGT5AEehIYz7eJrFDMF9CvH4wwhcGHiHMneFvLDQwlwvMLQq58trRcYBWfYn0A0OgHWQUSu25mE+BnoYKnnEJoeIWAifzOv7vLWd2ZKRfWAIme3tOiUaQ3UnLkb0xj1FxRIeEGKaGIHOs9nEgLaaA9i0JRYo1Ic67wJW86KSKE/ZAM8KuVMk8ITVhmxUxJ3Cl2xlm9Vtkeju1+mpCQNxaEGNCY8bs9X2YqwNoQeGjBWut/ma0QAWy/TqAsHx9wSya3I5IRxOfTC+leG+kA/4vSeEcGBtNUN6byhu3+keEZCQJUNh8MAO7HL6H8pQLnsW/Hd4T4lv93TPjfM7A46iEEqbB5EDOvwYNW6tGNZzT/o+CZ6sqZ6wUtR/wf7mi/VL8iNciT6rHih48Y55b4nKCHJCCzb4y0nwFmin3ZEMIoLfZF8F7nncFmvnWBaBj7CGAYA/WGJsUwHdYqVDwAmNsUgAx4CGgAA7GOOxADYOFWOaIKifuVYzmOpREqA21Mo7aPsgiY1PhOMAmxtR+AUbYH3Id2wc0SAFIQTsn9IUGWR8k9jx3vtXSiAacFxTAGakBk9UudkNECd6jLe+6HrshshvIuC6IlLMRy7er+JpcKma24SlE4cFZSZJDGVVrsNvitQhQrDhW0jfiOLfFd47C42eHT56D/BK0To+58Ahj+cAT8HT1UWlfLZCCd/uKawzU0Rh2EyIX/Icqth3niG8ybNroezwe6khdCNxRN+l4XGdOLVLlOOt2hTRJlr1ETIuMAltVTMz70mJrkdGAaZLSmnBEqmAE32JCMmuTlCnRgsBENtOUpHhvvsYIL0ibnBkaC6QvKcR7738GKp0AKnim7xgUSNv1bpS8QwhBt8r+EP47v/oyRK/S34yJ9nT+AN0Tkm4OdB9E4BsmXM3SnMlRFUrtp6IDpV2eKzdYvF3etm3KhQksbOLChGkSmcBdmcEwvqkrMy5BzL00NZeu3qPYJOOuCc+5NjcWKXQxFvTa3NoXJ4d8in7fiAUuTt781dkvuHX4K8AA2Usy7yNKLy0AAAAASUVORK5CYII=
">
    <link href="/rss.xml" rel="alternate" type="application/rss+xml" title="Articles from Distill">
  
    <title>Weight Banding</title>
    
    <link rel="canonical" href="https://distill.pub/2020/circuits/weight-banding">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="Weights in the final layer of common visual models appear as horizontal bands. We investigate how and why.">
    <meta property="article:published" itemprop="datePublished" content="2021-04-08">
    <meta property="article:created" itemprop="dateCreated" content="2021-04-08">
    
    <meta property="article:modified" itemprop="dateModified" content="2021-04-08T00:02:09.000Z">
    
    <meta property="article:author" content="Michael Petrov">
    <meta property="article:author" content="Chelsea Voss">
    <meta property="article:author" content="Ludwig Schubert">
    <meta property="article:author" content="Nick Cammarata">
    <meta property="article:author" content="Gabriel Goh">
    <meta property="article:author" content="Chris Olah">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="Weight Banding">
    <meta property="og:description" content="Weights in the final layer of common visual models appear as horizontal bands. We investigate how and why.">
    <meta property="og:url" content="https://distill.pub/2020/circuits/weight-banding">
    <meta property="og:image" content="https://distill.pub/2020/circuits/weight-banding/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Weight Banding">
    <meta name="twitter:description" content="Weights in the final layer of common visual models appear as horizontal bands. We investigate how and why.">
    <meta name="twitter:url" content="https://distill.pub/2020/circuits/weight-banding">
    <meta name="twitter:image" content="https://distill.pub/2020/circuits/weight-banding/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="Weight Banding">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/2020/circuits/weight-banding">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="4">
    <meta name="citation_firstpage" content="e00024.009">
    <meta name="citation_doi" content="10.23915/distill.00024.009">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/04/08">
    <meta name="citation_publication_date" content="2021/04/08">
    <meta name="citation_author" content="Petrov, Michael">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Voss, Chelsea">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Schubert, Ludwig">
    <meta name="citation_author" content="Cammarata, Nick">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Goh, Gabriel">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Olah, Chris">
    <meta name="citation_reference" content="citation_title=Muscle Tissue: Cardiac Muscle;citation_author=Berkshire Community College Bioscience Image Library;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Epithelial Tissues: Stratified Squamous Epithelium;citation_author=Berkshire Community College Bioscience Image Library;citation_publication_date=2018;">
    <meta name="citation_reference" content="citation_title=Deconvolution and Checkerboard Artifacts;citation_author=Augustus Odena;citation_author=Vincent Dumoulin;citation_author=Chris Olah;citation_publication_date=2016;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Going Deeper with Convolutions;citation_author=Christian Szegedy;citation_author=Wei Liu;citation_author=Yangqing Jia;citation_author=Pierre Sermanet;citation_author=Scott Reed;citation_author=Dragomir Anguelov;citation_author=Dumitru Erhan;citation_author=Vincent Vanhoucke;citation_author=Andrew Rabinovich;citation_publication_date=2015;">
    <meta name="citation_reference" content="citation_title=Deep Residual Learning for Image Recognition;citation_author=Kaiming He;citation_author=Xiangyu Zhang;citation_author=Shaoqing Ren;citation_author=Jian Sun;citation_publication_date=2016;">
    <meta name="citation_reference" content="citation_title=Very Deep Convolutional Networks for Large-Scale Image Recognition;citation_author=Karen Simonyan;citation_author=Andrew Zisserman;citation_publication_date=2014;citation_arxiv_id=1409.1556;">
    <meta name="citation_reference" content="citation_title=ImageNet Classification with Deep Convolutional Neural Networks;citation_author=Alex Krizhevsky;citation_author=Ilya Sutskever;citation_author=Geoffrey E. Hinton;citation_publication_date=2012;">
    <meta name="citation_reference" content="citation_title=An Intriguing Failing of Convolutional Neural Networks and the CoordConv Solution;citation_author=Rosanne Liu;citation_author=Joel Lehman;citation_author=Piero Molino;citation_author=Felipe Petroski Such;citation_author=Eric Frank;citation_author=Alex Sergeev;citation_author=Jason Yosinski;citation_publication_date=2018;citation_arxiv_id=1807.03247;">
    <meta name="citation_reference" content="citation_title=Visualizing and Understanding Convolutional Networks;citation_author=Matthew D Zeiler;citation_author=Rob Fergus;citation_publication_date=2014;">
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
        "title": "Weight Banding",
        "description": "Weights in the final layer of common visual models appear as horizontal bands. We investigate how and why.",
        "authors": [
          {
            "author": "Michael Petrov",
            "authorURL": "http://twitter.com/mpetrov",
            "affiliation": "OpenAI",
            "affiliationURL": "https://openai.com"
          },
          {
            "author": "Chelsea Voss",
            "authorURL": "https://csvoss.com",
            "affiliation": "OpenAI",
            "affiliationURL": "https://openai.com"
          },
          {
            "author": "Ludwig Schubert",
            "authorURL": "https://schubert.io/"
          },
          {
            "author": "Nick Cammarata",
            "authorURL": "http://nickcammarata.com",
            "affiliation": "OpenAI",
            "affiliationURL": "https://openai.com"
          },
          {
            "author": "Gabriel Goh",
            "authorURL": "https://gabgoh.github.io",
            "affiliation": "OpenAI",
            "affiliationURL": "https://openai.com"
          },
          {
            "author": "Chris Olah",
            "authorURL": "https://colah.github.io"
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

  <d-title><h1>Weight Banding</h1></d-title>

  <d-byline>
  <div class="byline grid">
    <div class="authors-affiliations grid">
      <h3>Authors</h3>
      <h3>Affiliations</h3>
      
        <p class="author">
          
            <a class="name" href="http://twitter.com/mpetrov">Michael Petrov</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://csvoss.com">Chelsea Voss</a>
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
          
            <a class="name" href="http://nickcammarata.com">Nick Cammarata</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://gabgoh.github.io">Gabriel Goh</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://colah.github.io">Chris Olah</a>
        </p>
        <p class="affiliation">
        
        </p>
      
    </div>
    <div>
      <h3>Published</h3>
      
        <p>April 8, 2021</p> 
    </div>
    <div>
      <h3>DOI</h3>
      
        <p><a href="https://doi.org/10.23915/distill.00024.009">10.23915/distill.00024.009</a></p>
    </div>
  </div>
</d-byline><d-article>
    <section id="thread-nav" class="thread-info" style="margin-top: 10px; margin-bottom: 40px;">
      <img class="icon" src="images/multiple-pages.svg" width="43px" height="50px">
      <p class="explanation">
          This article is part of the <a href="/2020/circuits/">Circuits thread</a>, an experimental format collecting invited short articles and critical commentary delving into the inner workings of neural networks.
      </p>
      <a class="prev" href="/2020/circuits/branch-specialization/">Branch Specialization</a>
    </section>

    <h2 style="display: none;">Introduction</h2>

    <p>
      Open up any ImageNet conv net and look at the weights in the last layer. You’ll find a uniform spatial pattern to them, dramatically unlike anything we see elsewhere in the network. No individual weight is unusual, but the uniformity is so striking that when we first discovered it we thought it must be a bug. Just as different biological tissue types jump out as distinct under a microscope, the weights in this final layer jump out as distinct when visualized with NMF. We call this phenomenon <i>weight banding</i>.
    </p>

    <figure id="figure-1" style="grid-column-start: page-start; grid-column-end: page-end;">
      <svg width="1808" height="430" viewBox="0 0 1808 430" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="diagram-Intro_Figure" style="width: 100%; height: auto;">
<rect width="1808" height="430" fill="white" class="pixelated"></rect>
<text fill="black" xml:space="preserve" style="white-space: pre" font-family="Roboto" font-size="27.5" font-weight="bold" letter-spacing="0em"><tspan x="0" y="27.3994">Microscope slides of different tissues</tspan></text>
<text fill="black" xml:space="preserve" style="white-space: pre" font-family="Roboto" font-size="27.5" letter-spacing="0em"><tspan x="445" y="78.3994">Muscle tissue</tspan></text>
<rect x="445" y="95" width="418.569" height="335" rx="10" fill="url(#patternIntro_Figure0)" class="pixelated"></rect>
<text fill="black" xml:space="preserve" style="white-space: pre" font-family="Roboto" font-size="27.5" letter-spacing="0em"><tspan x="0" y="78.3994">Epithelial tissue
</tspan></text>
<rect y="95" width="418.569" height="335" rx="10" fill="url(#patternIntro_Figure1)" class="pixelated"></rect>
<text fill="black" xml:space="preserve" style="white-space: pre" font-family="Roboto" font-size="27.5" letter-spacing="0em"><tspan x="928" y="78.3994">Typical layer</tspan></text>
<text fill="black" xml:space="preserve" style="white-space: pre" font-family="Roboto" font-size="27.5" letter-spacing="0em"><tspan x="1373" y="78.3994">Layer with weight banding</tspan></text>
<text fill="black" xml:space="preserve" style="white-space: pre" font-family="Roboto" font-size="27.5" font-weight="bold" letter-spacing="0em"><tspan x="928" y="27.3994">NMF of weights at different layers</tspan></text>
<rect x="1373.5" y="95.5" width="417.569" height="334" rx="9.5" fill="#E5E5E5" stroke="#DDDDDD" class="pixelated"></rect>
<rect x="1386.96" y="108.958" width="390.652" height="307.083" fill="url(#patternIntro_Figure2)" class="pixelated"></rect>
<rect x="928.5" y="94.5" width="417.569" height="334" rx="9.5" fill="#E5E5E5" stroke="#DDDDDD" class="pixelated"></rect>
<rect x="941.958" y="109.354" width="390.652" height="307.083" fill="url(#patternIntro_Figure3)" class="pixelated"></rect>
<defs>
<pattern id="patternIntro_Figure0" patternContentUnits="objectBoundingBox" width="1" height="1">
<use xlink:href="#imageIntro_Figure0" transform="translate(-0.0262334) scale(0.000536425 0.000670241)" class="pixelated"></use>
</pattern>
<pattern id="patternIntro_Figure1" patternContentUnits="objectBoundingBox" width="1" height="1">
<use xlink:href="#imageIntro_Figure1" transform="translate(-0.209842) scale(0.000887302 0.00110865)" class="pixelated"></use>
</pattern>
<pattern id="patternIntro_Figure2" patternContentUnits="objectBoundingBox" width="1" height="1">
<use xlink:href="#imageIntro_Figure2" transform="scale(0.00169779 0.00215983)" class="pixelated"></use>
</pattern>
<pattern id="patternIntro_Figure3" patternContentUnits="objectBoundingBox" width="1" height="1">
<use xlink:href="#imageIntro_Figure3" transform="scale(0.00169779 0.00215983)" class="pixelated"></use>
</pattern>
<image id="imageIntro_Figure0" width="1962" height="1492" xlink:href="generated_images/fe26c4ecf6104f.png" class="pixelated"></image>
<image id="imageIntro_Figure1" width="1600" height="902" xlink:href="generated_images/3098f7d2808197.png" class="pixelated"></image>
<image id="imageIntro_Figure2" width="589" height="463" xlink:href="generated_images/9684ecaa42e1f.png" class="pixelated"></image>
<image id="imageIntro_Figure3" width="589" height="463" xlink:href="generated_images/1e3ec78d5e3c63.png" class="pixelated"></image>
</defs>
</svg>

      <figcaption class="figcaption">
        <p>
          <a href="#figure-1" class="figure-number">1</a>. When <a href="https://drafts.distill.pub/distillpub/post--circuits-visualizing-weights#one-simple-trick">visualized with NMF</a>, the weight banding in layer <code>mixed_5b</code> is as visually striking compared to any other layer in InceptionV1 (here shown: <code>mixed_3a</code>) as the smooth, regular striation of muscle tissue is when compared to any other tissue (here shown: cardiac muscle tissue<d-cite bibtex-key="wikitissue2"></d-cite> and epithelial tissue<d-cite bibtex-key="wikitissue1"></d-cite>).
        </p>
      </figcaption>
    </figure>

    <p>
      So far, the <a href="https://distill.pub/2020/circuits/">Circuits thread</a> has mostly focused on studying very small pieces of neural network – <a href="https://distill.pub/2020/circuits/early-vision/">individual neurons</a> and small circuits. In contrast, weight banding is an example of what we call a “structural phenomenon,” a larger-scale pattern in the circuits and features of a neural network. Other examples of structural phenomena are the recurring symmetries we see in <a href="https://distill.pub/2020/circuits/equivariance/">equivariance</a> motifs and the specialized slices of neural networks we see in <a href="https://distill.pub/2020/circuits/branch-specialization/">branch specialization</a>.

      In the case of weight banding, we think of it as a structural phenomenon because the pattern appears at the scale of an entire layer.

    </p>
    <aside>
      <p>
        Weight banding also seems similar in flavor to the <a href="https://distill.pub/2016/deconv-checkerboard/">checkerboard artifacts</a><d-cite bibtex-key="odena2016deconvolution"></d-cite> that form during deconvolution.
      </p>
    </aside>


    <p>
      In addition to describing weight banding, we’ll explore when and why it occurs. We find that there appears to be a causal link between whether a model uses global average pooling or fully connected layers at the end, suggesting that weight banding is part of an algorithm for preserving information about larger scale structure in images. Establishing causal links like this is a step towards closing the loop between practical decisions in training neural networks and the phenomena we observe inside them.
    </p>


    <h2>Where weight banding occurs</h2>

    <p>
      Weight banding consistently forms in the final convolutional layer of vision models with global average pooling.
    </p>

    <p>
      In order to see the bands, we need to visualize the spatial structure of the weights, as shown below. We typically do this using NMF, <a href="https://drafts.distill.pub/distillpub/post--circuits-visualizing-weights/#one-simple-trick">as described in</a> Visualizing Weights. For each neuron, we take the weights connecting it to the previous layer. We then use NMF to reduce the number of dimensions corresponding to channels in the previous layer down to 3 factors, which we can map to RGB channels. Since which factor is which is arbitrary, we use a heuristic to make the mapping consistent across neurons. This reveals a very prominent pattern of horizontal<d-footnote>The stripes aren’t always perfectly horizontal - sometimes they exhibit a slight preference for extra weight in the center of the central band, as seen in some examples below.</d-footnote> stripes.
    </p>

    <figure id="figure-2" class="subgrid">
      <figcaption class="figcaption" style="grid-column: kicker">
        <p><a href="#figure-2" class="figure-number">2</a>.
          These common networks have pooling operations before their fully
          connected layers and consistently show banding at their last
          convolutional layers.</p>
      </figcaption>
      <div class="l-body">
        <div class="weight-banding-example" style="width: 30%">
          <reducedweights weights_url="diagrams/upscaled_weights/InceptionV1_-_modelzoo-mixed5b_5x5_w.json"></reducedweights>
          <span class="label">InceptionV1<d-cite bibtex-key="szegedy2015going"></d-cite><br>mixed 5b</span>
        </div>
        <div class="weight-banding-example" style="width: 30%">
          <reducedweights weights_url="diagrams/upscaled_weights/ResNet50_-_modelzoo-resnet_v2_50%2Fblock4%2Funit_3%2Fbottleneck_v2%2Fconv2%2Fweights%2Fread.json"></reducedweights>
          <span class="label">ResNet50<d-cite bibtex-key="he2016deep"></d-cite><br>block 4 unit 3</span>
        </div>
        <div class="weight-banding-example" style="width: 30%">
          <reducedweights weights_url="diagrams/upscaled_weights/VGG19_-_modelzoo-conv5_3%2Fweights%2Fread.json"></reducedweights>
          <span class="label">VGG19<d-cite bibtex-key="simonyan2014very"></d-cite><br>conv5</span>
        </div>
      </div>
    </figure>

    <p>
      Interestingly, AlexNet<d-cite bibtex-key="krizhevsky2012"></d-cite> does not exhibit this phenomenon.
    </p>

    <figure id="figure-3" class="subgrid">
      <figcaption class="figcaption" style="grid-column: kicker">
        <!-- <span class="figure-number">1:</span> -->
        <p><a href="#figure-3" class="figure-number">3</a>.
          AlexNet does not have a pooling operation before its fully connected
          layers and does not show banding at its last convolutional
          layer.</p>
        <br>
        <p>
            To make it easier to look for groups of similar weights, we
            sorted the neurons at each layer by similarity of their reduced
            forms.
          </p>
      </figcaption>
      <div class="l-body">
        <div class="weight-banding-example">
          <reducedweights weights_url="diagrams/upscaled_weights/AlexNet_-_modelzoo-conv5%2Fweights%2Fread.json" num_to_show="96"></reducedweights>
          <span class="label">AlexNet<br>conv5</span>
        </div>
      </div>
    </figure>

    <p>
      Unlike most modern vision models, AlexNet does not use global average pooling. Instead, it has a fully connected layer directly connected to its final convolutional layer, allowing it to treat different positions differently. If one looks at the weights of this fully connected layer, the weights strongly vary as a function of the global y position.
    </p>
    <p>
      The horizontal stripes in weight banding mean that the filters don’t care about horizontal position, but are strongly encoding relative vertical position. Our hypothesis is that weight banding is a learned way to preserve spatial information as it gets lost through various pooling operations.
    </p>
    <p>
      In the next section, we will construct our own simplified vision network and investigate variations on its architecture in order to understand exactly which conditions are necessary to produce weight banding.
    </p>

    <h2 id="what-affects-banding">What affects banding</h2>

    <p>
      We’d like to understand which architectural decisions affect weight banding. This will involve trying out different architectures and seeing whether weight banding persists.

      Since we will only want to change a single architectural parameter at a time, we will need a consistent baseline to apply our modifications to. Ideally, this baseline would be as simple as possible.
    </p>
    <p>
      We created a simplified network architecture with 6 groups of convolutions, separated by L2 pooling layers. At the end, it has a global average pooling operation that reduces the input to 512 values that are then fed to a fully connected layer with 1001 outputs.
      <!-- To study the phenomenon of weight banding, we used a simplified network architecture compared to Inception, ResNet, or VGG. In our architecture there are 6 groups of convolutions, separated by L2 pooling layers. At the end, there is a global average pooling operation that reduces the input to 512 values that are then fed to a fully connected layer with 1001 outputs. -->
    </p>

    <figure id="figure-4" class="subgrid">
      <figcaption class="figcaption" style="grid-column: kicker">
        <p>
          <a href="#figure-4" class="figure-number">4</a>. Our simplified vision network architecture.
        </p>
      </figcaption>
      <div class="l-body">
        <svg width="720" height="162" viewBox="0 0 720 162" fill="none" xmlns="http://www.w3.org/2000/svg" id="diagram-Network_Architecture" style="width: 100%; height: auto;">
<g --disabled-clip-path="url(#clip0)">
<rect width="720" height="162" fill="white" class="pixelated"></rect>
<rect x="575" y="25" width="50" height="70" rx="10" transform="rotate(90 575 25)" fill="#F2F2F2" class="pixelated"></rect>
<rect x="480" y="25" width="50" height="175" rx="10" transform="rotate(90 480 25)" fill="#F2F2F2" class="pixelated"></rect>
<rect x="280" y="25" width="50" height="70" rx="10" transform="rotate(90 280 25)" fill="#F2F2F2" class="pixelated"></rect>
<rect x="185" y="25" width="50" height="35" rx="10" transform="rotate(90 185 25)" fill="#F2F2F2" class="pixelated"></rect>
<rect x="65" y="25" width="50" height="35" rx="10" transform="rotate(90 65 25)" fill="#F2F2F2" class="pixelated"></rect>
<rect x="125" y="25" width="50" height="35" rx="10" transform="rotate(90 125 25)" fill="#F2F2F2" class="pixelated"></rect>
<rect x="24" y="31" width="38" height="23" rx="9" transform="rotate(90 24 31)" fill="white" stroke="#CCCCCC" stroke-width="2" stroke-dasharray="3.5 3.5" class="pixelated"></rect>
<path d="M677.707 50.7071C678.098 50.3166 678.098 49.6834 677.707 49.2929L671.343 42.9289C670.953 42.5384 670.319 42.5384 669.929 42.9289C669.538 43.3195 669.538 43.9526 669.929 44.3431L675.586 50L669.929 55.6569C669.538 56.0474 669.538 56.6805 669.929 57.0711C670.319 57.4616 670.953 57.4616 671.343 57.0711L677.707 50.7071ZM11 51L677 51V49L11 49V51Z" fill="#CCCCCC" class="pixelated"></path>
<path d="M10.0698 86.4336L9.30326 85.6672L13.7862 81.1842L14.5527 81.9507L10.0698 86.4336ZM14.9132 79.933C15.0375 79.8087 15.1797 79.741 15.3399 79.7299C15.5029 79.7217 15.6589 79.7921 15.8081 79.9412C15.9572 80.0904 16.0277 80.2465 16.0194 80.4094C16.0111 80.5724 15.9448 80.716 15.8205 80.8403C15.6962 80.9646 15.554 81.0295 15.3938 81.0351C15.2336 81.0406 15.0789 80.9688 14.9297 80.8196C14.7806 80.6705 14.7088 80.5158 14.7143 80.3556C14.7226 80.1981 14.7889 80.0573 14.9132 79.933ZM16.5083 83.9063L15.9697 84.4946C16.7431 84.4062 17.406 84.6383 17.9584 85.1907C18.9058 86.1381 18.8492 87.1504 17.7885 88.2277L14.8261 91.19L14.0597 90.4236L17.0262 87.457C17.3466 87.1311 17.5109 86.8176 17.5192 86.5165C17.5303 86.2182 17.3825 85.9157 17.0759 85.6092C16.8273 85.3606 16.5428 85.2086 16.2224 85.1534C15.902 85.0982 15.5816 85.1258 15.2612 85.2363L12.0668 88.4307L11.3003 87.6642L15.7832 83.1812L16.5083 83.9063ZM21.9607 93.9411C21.2785 94.6234 20.5728 95.017 19.8436 95.1219C19.1144 95.2269 18.4832 95.0128 17.9501 94.4797C17.406 93.9356 17.1505 93.3348 17.1836 92.6775L15.025 94.8361L14.2585 94.0696L20.465 87.8631L21.1653 88.5633L20.7054 89.0977C21.4042 89.0231 22.0312 89.2635 22.5864 89.8186C23.125 90.3573 23.3473 90.9856 23.2534 91.7038C23.1623 92.4247 22.7549 93.147 22.0312 93.8707L21.9607 93.9411ZM21.2813 93.0876C21.7867 92.5822 22.0781 92.0753 22.1555 91.5671C22.2328 91.0588 22.0837 90.6169 21.708 90.2413C21.244 89.7772 20.6902 89.635 20.0466 89.8145L17.9046 91.9565C17.725 92.5946 17.8714 93.1498 18.3437 93.6221C18.7111 93.9895 19.1475 94.1359 19.653 94.0613C20.164 93.9867 20.7067 93.6622 21.2813 93.0876ZM23.9578 99.435C23.3087 99.4875 22.6955 99.2251 22.1182 98.6478C21.6403 98.17 21.4138 97.6673 21.4387 97.1397C21.4691 96.6121 21.755 96.0749 22.2963 95.528L25.2132 92.6112L25.9797 93.3777L23.0836 96.2738C22.4041 96.9532 22.3405 97.5692 22.893 98.1216C23.4785 98.7072 24.0862 98.8785 24.716 98.6354L27.9767 95.3747L28.7432 96.1412L24.2602 100.624L23.531 99.8949L23.9578 99.435ZM32.037 97.264L30.9515 98.3495L31.7884 99.1864L31.1959 99.7789L30.359 98.942L27.5789 101.722C27.3994 101.902 27.3013 102.074 27.2848 102.24C27.271 102.403 27.3538 102.574 27.5334 102.754C27.6217 102.842 27.7599 102.947 27.9477 103.069L27.3262 103.69C27.0693 103.544 26.8456 103.375 26.655 103.185C26.3125 102.842 26.1578 102.48 26.191 102.099C26.2241 101.718 26.4313 101.337 26.8124 100.956L29.5925 98.1755L28.7763 97.3593L29.3688 96.7668L30.185 97.583L31.2705 96.4975L32.037 97.264ZM32.7289 104.196C33.3532 103.571 34.0354 103.055 34.7757 102.646C35.5187 102.24 36.2907 101.968 37.0917 101.83C37.8927 101.692 38.5681 101.704 39.1178 101.867L38.7697 102.53C38.0571 102.436 37.2533 102.577 36.3584 102.953C35.4662 103.331 34.6141 103.901 33.802 104.664L33.4457 105.012C32.3795 106.078 31.6489 107.198 31.254 108.372C31.0192 109.076 30.9308 109.723 30.9888 110.311L30.3632 110.622C30.2002 110.05 30.1919 109.357 30.3383 108.542C30.6256 106.951 31.4224 105.502 32.7289 104.196ZM37.0834 113.447L33.1308 109.495