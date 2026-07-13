---
source_url: https://distill.pub/2020/circuits/branch-specialization
ingested: 2026-07-13
sha256: dcf01e20364fc716025a99760ffa16acacb0003728425ed6c51594c2f14b90b9
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
  
  
  <style id="distill-article-specific-styles">
    d-article a.undecorated {
	border-bottom: none;
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
	margin-top: 1.5em;
	margin-bottom: 2.5em;
	position: relative;
}

d-figure > figure {
	margin-top: 0;
	margin-bottom: 0;
}

d-title > figure:last-child {
	margin-bottom: 1.5em;
}

figure > svg text, figure > svg tspan {
  font-family: "Roboto", Arial, sans-serif;
  /* font-size: 27.5px;
  --font: normal 27.5px sans-serif; */
  color: rgba(0, 0, 0, 0.6);
}

figure > svg text[font-weight=bold], figure > svg text[font-weight=bold] tspan {
  font-size: 26px;
}

a.section-number::before {
	content: "Section ";
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

.todo {
	padding: 0.5em;
	background-color: hsla(50, 100%, 50%, 0.25);
	border: 1px solid hsla(50, 100%, 50%, 0.5);
	border-radius: 4px;
	color: hsl(45, 100%, 20%);
}

.todo::before {
	display: inline-block;
	content: "⚠️";
	vertical-align: baseline;
	position: relative;
	font-size: 135%;
	top: 4px;
	margin: 0 0.25em;

	text-decoration: none !important;
}

.todo.done::before {
	content: "✅";
}

.todo.done {
	background-color: hsla(120, 20%, 60%, 0.25);
	border: 1px solid hsla(120, 20%, 60%, 0.5);
	color: hsl(45, 0%, 20%);
	text-decoration: line-through;
	text-decoration-color: hsla(45, 0%, 20%, 50%);
}

/* Color Legends */

.color-legend {
	display: inline-block;
	width: 64px;
	width: 4em;
	height: 8px;
	height: calc(1ex + 1px);
	position: relative;
	bottom: 1px;
	vertical-align: baseline;
}
.color-legend.viridis {
	background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQAAAAABCAYAAAAxWXB3AAAA7ElEQVQ4T4WRi23EMAxDSXu1jtD9R4kPIiVbTosWh0Ci+PRJjl/8XuAAB9EjpAmOoYgdCXKg/MsLTmzGN9e8pRzm83nXulZO8yv7VuqoF1tceY7QTZW/vR9a82Nm7ssZd3/5uXvzvbczeUfjFn6p1b3/zDv3xZCzp9f3u3Ptd7/6tCu9vMU9K7913Wfdvfg7Lg5mmL0nmgvtv/lw/rzHGzs3W3rgpZML394Sez34q/aY3cyDubW9KS9zeVWv2qP+KebZfPXNxospFt5lP/pqd0TrYjVLfs13n3f4RudwBDCVM/OITE1Mho5f5M4+UeiJCh70oMIAAAAASUVORK5CYII=");
	background-size: contain;
}
.color-legend.pn {
	background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAAACCAIAAABnm03uAAAAL0lEQVR4nGNkqP/PwcKAB3Gy4pXFq5eDhYGV4TfDnx940Xd8sr/xyv75wcQwxAEA8tZAggq3EssAAAAASUVORK5CYII=");
	background-size: contain;
}

.legend-label {
	padding: 1px 4px;
	border-radius: 2px;
	color: rgba(0, 0, 0, 0.8);
}

.legend-label.support {
	background-color: #EE880088;
}

.legend-label.inhibit {
	background-color: #0088EE88;
}

.legend-label.support-rb {
	color: white;
	background-color: #CE1E34CC;
}

.legend-label.inhibit-rb {
	color: white;
	background-color: #0571B0CC;
}

#figure-3 > figure {
	display: grid;
	grid-row-gap: 0.5em;
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
  
    <title>Branch Specialization</title>
    
    <link rel="canonical" href="https://distill.pub/2020/circuits/branch-specialization">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="When a neural network layer is divided into multiple branches, neurons self-organize into coherent groupings.">
    <meta property="article:published" itemprop="datePublished" content="2021-04-05">
    <meta property="article:created" itemprop="dateCreated" content="2021-04-05">
    
    <meta property="article:modified" itemprop="dateModified" content="2021-04-08T04:56:47.000Z">
    
    <meta property="article:author" content="Chelsea Voss">
    <meta property="article:author" content="Gabriel Goh">
    <meta property="article:author" content="Nick Cammarata">
    <meta property="article:author" content="Michael Petrov">
    <meta property="article:author" content="Ludwig Schubert">
    <meta property="article:author" content="Chris Olah">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="Branch Specialization">
    <meta property="og:description" content="When a neural network layer is divided into multiple branches, neurons self-organize into coherent groupings.">
    <meta property="og:url" content="https://distill.pub/2020/circuits/branch-specialization">
    <meta property="og:image" content="https://distill.pub/2020/circuits/branch-specialization/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Branch Specialization">
    <meta name="twitter:description" content="When a neural network layer is divided into multiple branches, neurons self-organize into coherent groupings.">
    <meta name="twitter:url" content="https://distill.pub/2020/circuits/branch-specialization">
    <meta name="twitter:image" content="https://distill.pub/2020/circuits/branch-specialization/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="Branch Specialization">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/2020/circuits/branch-specialization">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="4">
    <meta name="citation_firstpage" content="e00024.008">
    <meta name="citation_doi" content="10.23915/distill.00024.008">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/04/05">
    <meta name="citation_publication_date" content="2021/04/05">
    <meta name="citation_author" content="Voss, Chelsea">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Goh, Gabriel">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Cammarata, Nick">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Petrov, Michael">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Schubert, Ludwig">
    <meta name="citation_author" content="Olah, Chris">
    <meta name="citation_reference" content="citation_title=Imagenet classification with deep convolutional neural networks;citation_author=Alex Krizhevsky;citation_author=Ilya Sutskever;citation_author=Geoffrey E Hinton;citation_publication_date=2012;citation_journal_title=Advances in neural information processing systems;citation_volume=25;">
    <meta name="citation_reference" content="citation_title=Visualizing higher-layer features of a deep network;citation_author=Dumitru Erhan;citation_author=Yoshua Bengio;citation_author=Aaron Courville;citation_author=Pascal Vincent;citation_publication_date=2009;citation_journal_title=University of Montreal;citation_volume=1341;">
    <meta name="citation_reference" content="citation_title=Deep inside convolutional networks: Visualising image classification models and saliency maps;citation_author=Karen Simonyan;citation_author=Andrea Vedaldi;citation_author=Andrew Zisserman;citation_publication_date=2013;citation_arxiv_id=1312.6034;">
    <meta name="citation_reference" content="citation_title=Multifaceted feature visualization: Uncovering the different types of features learned by each neuron in deep neural networks;citation_author=Anh Nguyen;citation_author=Jason Yosinski;citation_author=Jeff Clune;citation_publication_date=2016;citation_arxiv_id=1602.03616;">
    <meta name="citation_reference" content="citation_title=Feature Visualization;citation_author=Chris Olah;citation_author=Alexander Mordvintsev;citation_author=Ludwig Schubert;citation_publication_date=2017;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Going deeper with convolutions;citation_author=Christian Szegedy;citation_author=Wei Liu;citation_author=Yangqing Jia;citation_author=Pierre Sermanet;citation_author=Scott Reed;citation_author=Dragomir Anguelov;citation_author=Dumitru Erhan;citation_author=Vincent Vanhoucke;citation_author=Andrew Rabinovich;citation_publication_date=2015;">
    <meta name="citation_reference" content="citation_title=Neural architecture search with reinforcement learning;citation_author=Barret Zoph;citation_author=Quoc V Le;citation_publication_date=2016;citation_arxiv_id=1611.01578;">
    <meta name="citation_reference" content="citation_title=Neural networks are surprisingly modular;citation_author=Daniel Filan;citation_author=Shlomi Hod;citation_author=Cody Wild;citation_author=Andrew Critch;citation_author=Stuart Russell;citation_publication_date=2020;citation_arxiv_id=2003.04881;">
    <meta name="citation_reference" content="citation_title=Are Neural Nets Modular? Inspecting Functional Modularity Through Differentiable Weight Masks;citation_author=Róbert Csordás;citation_author=Sjoerd van Steenkiste;citation_author=Jürgen Schmidhuber;citation_publication_date=2020;">
    <meta name="citation_reference" content="citation_title=Segregation of form, color, and stereopsis in primate area 18;citation_author=DH Hubel;citation_author=MS Livingstone;citation_publication_date=1987;citation_journal_title=Journal of Neuroscience;citation_volume=7;citation_number=11;">
    <meta name="citation_reference" content="citation_title=Representation of Angles Embedded within Contour Stimuli in Area V2 of Macaque Monkeys;citation_author=Minami Ito;citation_author=Hidehiko Komatsu;citation_publication_date=2004;citation_journal_title=Journal of Neuroscience;citation_volume=24;citation_number=13;">
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
    "title": "Branch Specialization",
    "description": "When a neural network layer is divided into multiple branches, neurons self-organize into coherent groupings.",
    "authors": [
        {
            "author": "Chelsea Voss",
            "authorURL": "https://csvoss.com",
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
            "author": "Nick Cammarata",
            "authorURL": "http://nickcammarata.com",
            "affiliation": "OpenAI",
            "affiliationURL": "https://openai.com"
        },
        {
            "author": "Michael Petrov",
            "authorURL": "https://twitter.com/mpetrov",
            "affiliation": "OpenAI",
            "affiliationURL": "https://openai.com"
        },
        {
            "author": "Ludwig Schubert",
            "authorURL": "https://schubert.io"
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

  <style>
  .header-self-link {
    border-bottom: none;
  }
  .header-self-link:hover {
    border-bottom: none;
  }

  .pixelated {
    image-rendering:optimizeSpeed;             /* Legal fallback */
    image-rendering:-moz-crisp-edges;          /* Firefox        */
    image-rendering:-o-crisp-edges;            /* Opera          */
    image-rendering:-webkit-optimize-contrast; /* Safari         */
    image-rendering:optimize-contrast;         /* CSS3 Proposed  */
    image-rendering:crisp-edges;               /* CSS4 Proposed  */
    image-rendering:pixelated;                 /* CSS4 Proposed  */
    -ms-interpolation-mode:nearest-neighbor;   /* IE8+           */
  }

  .colab-reproduction {
    padding: 2px 4px;
    background: rgba(255, 255, 255, 0.75);
    border-radius: 4px;
    color: #aaa;
    font-weight: 300;
    border: solid 1px rgba(0, 0, 0, 0.08);
    border-bottom-color: rgba(0, 0, 0, 0.15);
    text-transform: uppercase;
    display: inline-block;
    cursor: pointer;
    text-decoration: none;
    /* float: right; */
  }

  .colab-reproduction:hover {
    text-decoration: none;
    border-bottom-color: rgba(0, 0, 0, 0.15);
  }

  .colab-reproduction-first {
    float: left;
    font-size: 9.5pt;
  }

  .colab-reproduction-inline {
    line-height: 100%;
    font-size: 8pt;
  }

  .colab-preface {
    display: inline;
    margin-right: 1em;
  }

  .colab-reproduction-logo {
    transform: translateY(1px);
    height: 10px;
    width: 16px;
  }
  </style>

  <d-title>
    <h1>Branch Specialization</h1>
  </d-title>

  <d-byline>
  <div class="byline grid">
    <div class="authors-affiliations grid">
      <h3>Authors</h3>
      <h3>Affiliations</h3>
      
        <p class="author">
          
            <a class="name" href="https://csvoss.com">Chelsea Voss</a>
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
          
            <a class="name" href="http://nickcammarata.com">Nick Cammarata</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://twitter.com/mpetrov">Michael Petrov</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://openai.com">OpenAI</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://schubert.io">Ludwig Schubert</a>
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
      
        <p>April 5, 2021</p> 
    </div>
    <div>
      <h3>DOI</h3>
      
        <p><a href="https://doi.org/10.23915/distill.00024.008">10.23915/distill.00024.008</a></p>
    </div>
  </div>
</d-byline><d-article>

    <section id="thread-nav" class="thread-info" style="margin-top: 10px; margin-bottom: 40px;">
      <img class="icon" src="images/multiple-pages.svg" width="43px" height="50px">
      <p class="explanation">
          This article is part of the <a href="/2020/circuits/">Circuits thread</a>, an experimental format collecting invited short articles and critical commentary delving into the inner workings of neural networks.
      </p>
      <a class="prev" href="/2020/circuits/visualizing-weights/">Visualizing Weights</a>
      <a class="next" href="/2020/circuits/weight-banding/">Weight Banding</a>
    </section>

    <h2 style="display: none;">Introduction</h2>

    <p>
      If we think of interpretability as a kind of “anatomy of neural networks,” most of the circuits thread has involved studying tiny little veins – looking at the small-scale, at individual neurons and how they connect. However, there are many natural questions that the small-scale approach doesn’t address.
    </p>

    <p>
      In contrast, the most prominent abstractions in biological anatomy involve larger-scale structures: individual organs like the heart, or entire organ systems like the respiratory system. And so we wonder: is there a “respiratory system” or “heart” or “brain region” of an artificial neural network? Do neural networks have any emergent structures that we could study that are larger-scale than circuits?
    </p>

    <p>
      This article describes <i>branch specialization</i>, one of three larger “structural phenomena” we’ve been able observe in neural networks. (The other two, <a href="https://distill.pub/2020/circuits/equivariance/">equivariance</a> and <a href="https://distill.pub/2020/circuits/weight-banding/">weight banding</a>, have separate dedicated articles.) Branch specialization occurs when neural network layers are split up into branches. The neurons and circuits tend to self-organize, clumping related functions into each branch and forming larger functional units – a kind of “neural network brain region.” We find evidence that these structures implicitly exist in neural networks without branches, and that branches are simply reifying structures that otherwise exist.
    </p>

    <p>
      The earliest example of branch specialization that we’re aware of comes from AlexNet<d-cite bibtex-key="krizhevsky2012imagenet"></d-cite>. AlexNet is famous as a jump in computer vision, arguably starting the deep learning revolution, but buried in the paper is a fascinating, rarely-discussed detail.

      The first two layers of AlexNet are split into two branches which can’t communicate until they rejoin after the second layer. This structure was used to maximize the efficiency of training the model on two GPUs, but the authors noticed something very curious happened as a result. The neurons in the first layer organized themselves into two groups: black-and-white Gabor filters formed on one branch and low-frequency color detectors formed on the other branch.
    </p>

    <figure id="figure-1">
      <img src="images/Figure_1.png" style="max-width: 100%; width: auto;">
      <figcaption class="figcaption l-body">
        <p>
          <a href="#figure-1" class="figure-number">1</a>. Branch specialization in the first two layers of AlexNet. Krizhevsky et al.<d-cite bibtex-key="krizhevsky2012imagenet"></d-cite> observed the phenomenon we call branch specialization in the first layer of AlexNet by visualizing their weights to RGB channels; here, we use <a href="https://distill.pub/2017/feature-visualization/">feature visualization</a><d-cite bibtex-key="erhan2009visualizing,simonyan2013deep,nguyen2016multifaceted,olah2017feature"></d-cite> to show how this phenomenon extends to the second layer of each branch.
        </p>
      </figcaption>
    </figure>

    <p>
      Although the first layer of AlexNet is the only example of branch specialization we’re aware of being discussed in the literature, it seems to be a common phenomenon. We find that branch specialization happens in later hidden layers, not just the first layer. It occurs in both low-level and high-level features. It occurs in a wide range of models, including places you might not expect it – for example, residual blocks in resnets can functionally be branches and specialize. Finally, branch specialization appears to surface as a structural phenomenon in plain convolutional nets, even without any particular structure causing it.
    </p>

    <p>
      Is there a large-scale structure to how neural networks operate? How are features and circuits organized within the model? Does network architecture influence the features and circuits that form? Branch specialization hints at an exciting story related to all of these questions.
    </p>

    <h2>What is a branch?</h2>

    <p>
      Many neural network architectures have <i>branches</i>, sequences of layers which temporarily don’t have access to “parallel” information which is still passed to later layers.
    </p>

    <figure id="figure-2">
      <svg width="1377" height="788" viewBox="0 0 1377 788" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="diagram-Figure_2" style="width: 100%; height: auto;">
<g id="Figure_2" --disabled-clip-path="url(#clip0)">
<rect width="1377" height="788" fill="white" class="pixelated"></rect>
<g id="Group 75">
<g id="InceptionV1 has nine sets of four-way branches called â€œInception blocks.â€">
<text fill="#676767" xml:space="preserve" style="white-space: pre" font-family="Roboto" font-size="27.5" font-weight="bold" letter-spacing="0em"><tspan x="0" y="273.399">InceptionV1</tspan></text>
<text fill="#676767" xml:space="preserve" style="white-space: pre" font-family="Roboto" font-size="27.5" letter-spacing="0em"><tspan x="149.504" y="273.399"> has </tspan><tspan x="0" y="305.399">nine sets of four-way </tspan><tspan x="0" y="337.399">branches called </tspan><tspan x="0" y="369.399">“Inception blocks.”</tspan></text>
</g>
<path id="Vector 109" d="M341 237L341 501" stroke="#B0B0B0"></path>
<g id="Group 73">
<g id="Group 46">
<path id="Vector 103" d="M601.115 371.467C570.332 372.672 578.102 407.921 545.825 407.319" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104" d="M601.115 371.467C570.663 370.262 578.35 335.012 546.42 335.615" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 61">
<path id="Vector 103_2" d="M1033.97 371.467C1003.19 372.672 1010.96 407.921 978.681 407.319" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_2" d="M1033.97 371.467C1003.52 370.262 1011.21 335.012 979.275 335.615" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 56">
<path id="Vector 103_3" d="M818.305 371.467C787.522 372.672 795.293 407.921 763.016 407.319" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_3" d="M818.305 371.467C787.853 370.262 795.54 335.012 763.61 335.615" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 62">
<path id="Vector 103_4" d="M1251.16 371.467C1220.38 372.672 1228.15 407.921 1195.87 407.319" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_4" d="M1251.16 371.467C1220.71 370.262 1228.4 335.012 1196.47 335.615" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 47">
<path id="Vector 103_5" d="M601.115 370.64C570.332 374.114 578.102 475.715 545.825 473.978" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_5" d="M601.115 370.64C570.663 367.167 578.35 265.566 546.42 267.302" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 63">
<path id="Vector 103_6" d="M1033.97 370.64C1003.19 374.114 1010.96 475.715 978.681 473.978" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_6" d="M1033.97 370.64C1003.52 367.167 1011.21 265.566 979.275 267.302" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 57">
<path id="Vector 103_7" d="M818.305 370.64C787.522 374.114 795.293 475.715 763.016 473.978" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_7" d="M818.305 370.64C787.853 367.167 795.54 265.566 763.61 267.302" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 64">
<path id="Vector 103_8" d="M1251.16 370.64C1220.38 374.114 1228.15 475.715 1195.87 473.978" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_8" d="M1251.16 370.64C1220.71 367.167 1228.4 265.566 1196.47 267.302" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 43">
<path id="Vector 103_9" d="M622.748 371.467C653.531 372.672 645.76 407.921 678.037 407.319" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_9" d="M622.748 371.467C653.2 370.262 645.513 335.012 677.443 335.615" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 65">
<path id="Vector 103_10" d="M1055.6 371.467C1086.39 372.672 1078.62 407.921 1110.89 407.319" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_10" d="M1055.6 371.467C1086.05 370.262 1078.37 335.012 1110.3 335.615" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 58">
<path id="Vector 103_11" d="M839.938 371.467C870.721 372.672 862.951 407.921 895.228 407.319" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_11" d="M839.938 371.467C870.39 370.262 862.703 335.012 894.633 335.615" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 48">
<path id="Vector 103_12" d="M399 371.467C433.739 372.672 424.97 407.921 461.395 407.319" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_12" d="M399 371.467C433.365 370.262 424.691 335.012 460.724 335.615" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 45">
<path id="Vector 103_13" d="M622.748 370.64C653.531 374.114 645.76 475.715 678.037 473.978" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_13" d="M622.748 370.64C653.2 367.167 645.513 265.566 677.443 267.302" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 67">
<path id="Vector 103_14" d="M1055.6 370.64C1086.39 374.114 1078.62 475.715 1110.89 473.978" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_14" d="M1055.6 370.64C1086.05 367.167 1078.37 265.566 1110.3 267.302" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 59">
<path id="Vector 103_15" d="M839.938 370.64C870.721 374.114 862.951 475.715 895.228 473.978" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_15" d="M839.938 370.64C870.39 367.167 862.703 265.566 894.633 267.302" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<g id="Group 49">
<path id="Vector 103_16" d="M399 370.64C433.739 374.114 424.97 475.715 461.395 473.978" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 104_16" d="M399 370.64C433.365 367.167 424.691 265.566 460.724 267.302" stroke="#DDDDDD" stroke-width="5"></path>
</g>
<rect id="Rectangle 187" x="597.162" y="334" width="32" height="71" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 189" x="1030.16" y="334" width="32" height="71" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 188" x="814.162" y="334" width="32" height="71" rx="6" fill="#D6D8DC"></rect>
<g id="Group 54">
<path id="Vector 130" d="M688.266 336H749.636" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 132" d="M688.266 268H749.636" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 131" d="M691.334 407H756.796" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 133" d="M694.403 474H761.91" stroke="#DDDDDD" stroke-width="5"></path>
<rect id="Rectangle 169" x="674.969" y="309" width="31.7081" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 188_2" x="674.969" y="241" width="31.7081" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 190" x="674.969" y="446" width="31.7081" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 173" x="674.969" y="378" width="31.7081" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 176" x="732.248" y="309" width="32.731" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 189_2" x="732.248" y="241" width="32.731" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 191" x="732.248" y="446" width="32.731" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 180" x="732.248" y="378" width="32.731" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 186" x="669.854" y="237" width="101.261" height="58" rx="10" fill="#FFB661" fill-opacity="0.3"></rect>
<rect id="Rectangle 192" x="669.854" y="305" width="101.261" height="58" rx="10" fill="#FFB661" fill-opacity="0.3"></rect>
<rect id="Rectangle 193" x="669.854" y="374" width="101.261" height="58" rx="10" fill="#FFB661" fill-opacity="0.3"></rect>
<rect id="Rectangle 194" x="669.854" y="443" width="101.261" height="58" rx="10" fill="#FFB661" fill-opacity="0.3"></rect>
</g>
<g id="Group 69">
<path id="Vector 130_2" d="M1121.12 336H1182.49" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 132_2" d="M1121.12 268H1182.49" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 131_2" d="M1124.19 407H1189.65" stroke="#DDDDDD" stroke-width="5"></path>
<path id="Vector 133_2" d="M1127.26 474H1194.77" stroke="#DDDDDD" stroke-width="5"></path>
<rect id="Rectangle 169_2" x="1107.82" y="309" width="31.7081" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 188_3" x="1107.82" y="241" width="31.7081" height="50" rx="6" fill="#D6D8DC"></rect>
<rect id="Rectangle 190_2" x="1107.82" y="446" width="31.7081" height="50" rx="6" fill="#D6D8DC"></rect>
<rect