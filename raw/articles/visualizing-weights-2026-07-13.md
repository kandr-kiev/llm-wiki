---
source_url: https://distill.pub/2020/circuits/visualizing-weights
ingested: 2026-07-13
sha256: 4859650e076697d203caefebbc588ee20a7ec78ed4a9cc6e69a914bbd17c2c79
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
	grid-template-columns: 45px 2fr 3fr;
	grid-template-areas:
		"icon explanation explanation "
		"icon prev next";
	grid-column-gap: 1.5em;
}

@media (min-width: 768px){
  #thread-nav {
	grid-template-columns: 65px 2fr 3fr;
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
	content: "← Previous Article";
}

#thread-nav .overview {
	scroll-behavior: smooth;
}

#thread-nav .overview::before {
	content: "↑";
	white-space: nowrap;
	margin-right: 0.5em;
}

#thread-nav .next {
	grid-area: next;
	scroll-behavior: smooth;
}

#thread-nav .next::before {
	content: "Next Article →";
}

#thread-nav .next::before, #thread-nav .prev::before {
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
  
    <title>Visualizing Weights</title>
    
    <link rel="canonical" href="https://distill.pub/2020/circuits/visualizing-weights">
    
    <!--  https://schema.org/Article -->
    <meta property="description" itemprop="description" content="We present techniques for visualizing, contextualizing, and understanding neural network weights.">
    <meta property="article:published" itemprop="datePublished" content="2021-02-04">
    <meta property="article:created" itemprop="dateCreated" content="2021-02-04">
    
    <meta property="article:modified" itemprop="dateModified" content="2021-04-08T04:48:56.000Z">
    
    <meta property="article:author" content="Chelsea Voss">
    <meta property="article:author" content="Nick Cammarata">
    <meta property="article:author" content="Gabriel Goh">
    <meta property="article:author" content="Michael Petrov">
    <meta property="article:author" content="Ludwig Schubert">
    <meta property="article:author" content="Ben Egan">
    <meta property="article:author" content="Swee Kiat Lim">
    <meta property="article:author" content="Chris Olah">
    <!--  https://developers.facebook.com/docs/sharing/webmasters#markup -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="Visualizing Weights">
    <meta property="og:description" content="We present techniques for visualizing, contextualizing, and understanding neural network weights.">
    <meta property="og:url" content="https://distill.pub/2020/circuits/visualizing-weights">
    <meta property="og:image" content="https://distill.pub/2020/circuits/visualizing-weights/thumbnail.jpg">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Distill">
  
    <!--  https://dev.twitter.com/cards/types/summary -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Visualizing Weights">
    <meta name="twitter:description" content="We present techniques for visualizing, contextualizing, and understanding neural network weights.">
    <meta name="twitter:url" content="https://distill.pub/2020/circuits/visualizing-weights">
    <meta name="twitter:image" content="https://distill.pub/2020/circuits/visualizing-weights/thumbnail.jpg">
    <meta name="twitter:image:width" content="560">
    <meta name="twitter:image:height" content="295">
  
      <!--  https://scholar.google.com/intl/en/scholar/inclusion.html#indexing -->
    <meta name="citation_title" content="Visualizing Weights">
    <meta name="citation_fulltext_html_url" content="https://distill.pub/2020/circuits/visualizing-weights">
    <meta name="citation_volume" content="6">
    <meta name="citation_issue" content="2">
    <meta name="citation_firstpage" content="e00024.007">
    <meta name="citation_doi" content="10.23915/distill.00024.007">
    <meta name="citation_journal_title" content="Distill">
    <meta name="citation_journal_abbrev" content="Distill">
    <meta name="citation_issn" content="2476-0757">
    <meta name="citation_fulltext_world_readable" content="">
    <meta name="citation_online_date" content="2021/02/04">
    <meta name="citation_publication_date" content="2021/02/04">
    <meta name="citation_author" content="Voss, Chelsea">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Cammarata, Nick">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Goh, Gabriel">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Petrov, Michael">
    <meta name="citation_author_institution" content="OpenAI">
    <meta name="citation_author" content="Schubert, Ludwig">
    <meta name="citation_author" content="Egan, Ben">
    <meta name="citation_author_institution" content="Mount Royal University">
    <meta name="citation_author" content="Lim, Swee Kiat">
    <meta name="citation_author_institution" content="Stanford University">
    <meta name="citation_author" content="Olah, Chris">
    <meta name="citation_reference" content="citation_title=Imagenet classification with deep convolutional neural networks;citation_author=Alex Krizhevsky;citation_author=Ilya Sutskever;citation_author=Geoffrey E Hinton;citation_publication_date=2012;citation_journal_title=Advances in neural information processing systems;citation_volume=25;">
    <meta name="citation_reference" content="citation_title=Understanding neural networks through deep visualization;citation_author=Jason Yosinski;citation_author=Jeff Clune;citation_author=Anh Nguyen;citation_author=Thomas Fuchs;citation_author=Hod Lipson;citation_publication_date=2015;citation_arxiv_id=1506.06579;">
    <meta name="citation_reference" content="citation_title=Visualizing and understanding convolutional networks;citation_author=Matthew D Zeiler;citation_author=Rob Fergus;citation_publication_date=2014;citation_arxiv_id=1311.2901;">
    <meta name="citation_reference" content="citation_title=The Building Blocks of Interpretability;citation_author=Chris Olah;citation_author=Arvind Satyanarayan;citation_author=Ian Johnson;citation_author=Shan Carter;citation_author=Ludwig Schubert;citation_author=Katherine Ye;citation_author=Alexander Mordvintsev;citation_publication_date=2018;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Zoom In: An Introduction to Circuits;citation_author=Chris Olah;citation_author=Nick Cammarata;citation_author=Ludwig Schubert;citation_author=Gabriel Goh;citation_author=Michael Petrov;citation_author=Shan Carter;citation_publication_date=2020;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=An Overview of Early Vision in InceptionV1;citation_author=Chris Olah;citation_author=Nick Cammarata;citation_author=Ludwig Schubert;citation_author=Gabriel Goh;citation_author=Michael Petrov;citation_author=Shan Carter;citation_publication_date=2020;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Curve Detectors;citation_author=Nick Cammarata;citation_author=Gabriel Goh;citation_author=Shan Carter;citation_author=Ludwig Schubert;citation_author=Michael Petrov;citation_author=Chris Olah;citation_publication_date=2020;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Feature Visualization;citation_author=Chris Olah;citation_author=Alexander Mordvintsev;citation_author=Ludwig Schubert;citation_publication_date=2017;citation_journal_title=Distill;">
    <meta name="citation_reference" content="citation_title=Multifaceted feature visualization: Uncovering the different types of features learned by each neuron in deep neural networks;citation_author=Anh Nguyen;citation_author=Jason Yosinski;citation_author=Jeff Clune;citation_publication_date=2016;citation_arxiv_id=1602.03616;">
    <meta name="citation_reference" content="citation_title=Visualizing and understanding recurrent networks;citation_author=Andrej Karpathy;citation_author=Justin Johnson;citation_author=Li Fei-Fei;citation_publication_date=2015;citation_arxiv_id=1506.02078;">
    <meta name="citation_reference" content="citation_title=Visualizing higher-layer features of a deep network;citation_author=Dumitru Erhan;citation_author=Yoshua Bengio;citation_author=Aaron Courville;citation_author=Pascal Vincent;citation_publication_date=2009;citation_journal_title=University of Montreal;citation_volume=1341;">
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
    "title": "Visualizing Weights",
    "description": "We present techniques for visualizing, contextualizing, and understanding neural network weights.",
    "authors": [
        {
            "author": "Chelsea Voss",
            "authorURL": "https://csvoss.com",
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
            "author": "Gabriel Goh",
            "authorURL": "https://gabgoh.github.io",
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
            "author": "Ben Egan",
            "affiliation": "Mount Royal University",
            "affiliationURL": "https://mtroyal.ca"
        },
        {
            "author": "Swee Kiat Lim",
            "authorURL": "https://greentfrapp.github.io/",
            "affiliation": "Stanford University",
            "affiliationURL": "https://stanford.edu"
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
    <h1>Visualizing Weights</h1>
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
          
            <span class="name">Ben Egan</span>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://mtroyal.ca">Mount Royal University</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://greentfrapp.github.io/">Swee Kiat Lim</a>
        </p>
        <p class="affiliation">
        <a class="affiliation" href="https://stanford.edu">Stanford University</a>
        </p>
      
        <p class="author">
          
            <a class="name" href="https://colah.github.io">Chris Olah</a>
        </p>
        <p class="affiliation">
        
        </p>
      
    </div>
    <div>
      <h3>Published</h3>
      
        <p>Feb. 4, 2021</p> 
    </div>
    <div>
      <h3>DOI</h3>
      
        <p><a href="https://doi.org/10.23915/distill.00024.007">10.23915/distill.00024.007</a></p>
    </div>
  </div>
</d-byline><d-article>

    <section id="thread-nav" class="thread-info" style="margin-top: 10px; margin-bottom: 40px;">
      <img class="icon" src="images/multiple-pages.svg" width="43px" height="50px">
      <p class="explanation">
          This article is part of the <a href="/2020/circuits/">Circuits thread</a>, an experimental format collecting invited short articles and critical commentary delving into the inner workings of neural networks.
      </p>
      <a class="prev" href="/2020/circuits/curve-circuits/">Curve Circuits</a>
      <a class="next" href="/2020/circuits/branch-specialization/">Branch Specialization</a>
    </section>

    <h2 style="display: none;">Introduction</h2>

    <p>The problem of understanding a neural network is a little bit like reverse engineering a large compiled binary of a computer program. In this analogy, the weights of the neural network are the compiled assembly instructions. At the end of the day, the weights are the fundamental thing you want to understand: how does this sequence of convolutions and matrix multiplications give rise to model behavior?</p>

    <p>Trying to understand artificial neural networks also has a lot in common with neuroscience, which tries to understand biological neural networks. As you may know, one major endeavor in modern neuroscience is mapping the <a href="https://en.wikipedia.org/wiki/Connectome">connectomes</a> of biological neural networks: which neurons connect to which. These connections, however, will only tell neuroscientists which weights are non-zero. Getting the weights – knowing whether a connection excites or inhibits, and by how much – would be a significant further step. One imagines neuroscientists might give a great deal to have the access to weights that those of us studying artificial neural networks get for free.</p>

    <p>And so, it’s rather surprising how little attention we actually give to looking at the weights of neural networks. There are a few exceptions to this, of course. It’s quite common for researchers to show pictures of the first layer weights in vision models<d-cite bibtex-key="krizhevsky2012imagenet"></d-cite> (these are directly connected to RGB channels, so they’re easy to understand as images). In some work, especially historically, we see researchers reason about the weights of toy neural networks by hand. And we quite often see researchers discuss aggregate statistics of weights. But actually looking at the weights of a neural network other than the first layer is quite uncommon – to the best of our knowledge, mapping weights between hidden layers to meaningful algorithms is novel to the circuits project.</p>

    <figure id="big-colab-button" class="fullscreen-diagram"></figure>

    <h2>What’s the difference between visualizing activations, weights, and attributions?</h2>

    <p>In this article, we’re focusing on visualizing weights. But people often visualize activations, attributions, gradients, and much more. How should we think about the meaning of visualizing these different objects?</p>

    <ul>
      <li>
        <b>Activations:</b> We generally think of these as being “what” the network saw. If understanding a neural network is like reverse compiling a computer program, the neurons are the variables, and the activations are the values of those variables.
      </li>
      <li>
        <b>Weights:</b> We generally think of these as being “how” the neural network computes one layer from the previous one. In the reverse engineering analogy, these are compiled assembly instructions.
      </li>
      <li>
        <b>Attributions:</b> Attributions try to tell us the extent to which one neuron influenced a later neuron.<d-cite bibtex-key="yosinski2015understanding,zeiler2014visualizing"></d-cite>We often think of this as “why” the neuron fired. We need to be careful with attributions, because they’re a human-defined object on top of a neural network rather than a fundamental object. They aren’t always well defined, and people mean different things by them. (They are very well defined if you are only operating across adjacent layers!)
      </li>
    </ul>

    <h2>Why it’s non-trivial to study weights in hidden layers</h2>

    <p>It seems to us that there are three main barriers to making sense of the weights in neural networks, which may have contributed to researchers tending to not directly inspect them:</p>

    <ul>
      <li>
        <b>Lack of Contextualization:</b> Researchers often visualize weights in the first layer, because they are linked to RGB values that we understand. That connection makes weights in the first layer meaningful. But weights between hidden layers are meaningless by default: knowing nothing about either the source or the destination, how can we make sense of them?
      </li>
      <li>
        <b>Indirect Interaction:</b> Sometimes, the meaningful weight interactions are between neurons which aren’t literally adjacent in a neural network. For example, in a residual network, the output of one neuron can pass through the additive residual stream and linearly interact with a neuron much later in the network. In other cases, neurons may interact through intermediate neurons without significant nonlinear interactions. How can we efficiently reason about these interactions?
      </li>
      <li>
        <b>Dimensionality and Scale:</b> Neural networks have lots of neurons. Those neurons connect to lots of other neurons. There’s a lot of data to display! How can we reduce it to a human-scale amount of information?
      </li>
    </ul>

    <p>Many of the methods we’ll use to address these problems were previously explored in <a href="https://distill.pub/2018/building-blocks/">Building Blocks</a> in the context of understanding activation vectors<d-cite bibtex-key="olah2018the"></d-cite>. The goal of this article is to show how similar ideas can be applied to weights instead of activations. Of course, we’ve already implicitly used these methods in various circuit articles<d-cite bibtex-key="olah2020zoom,olah2020an,cammarata2020curve"></d-cite>, but in those articles the methods have been of secondary interest to the results. It seems useful to give some dedicated discussion to the methods.</p>

    <h2 id="one-simple-trick">Aside: One Simple Trick</h2>

    <p>Interpretability methods often fail to take off because they’re hard to use. So before diving into sophisticated approaches, we wanted to offer a simple, easy to apply method.</p>

    <p>In a convolutional network, the input weights for a given neuron have shape <code>[width, height, input_channels]</code>. Unless this is the first convolutional layer, this probably can’t be easily visualized because <code>input_channels</code> is large. (If this is the first convolutional layer, visualize it as is!) However, one can use dimensionality reduction to collapse <code>input_channels</code> down to 3 dimensions. We find one-sided NMF especially effective for this.</p>

    <figure id="figure-1">
      <img src="images/screenshot_1.png" style="max-height: 220px; width: auto;">
      <figcaption class="figcaption l-body">
        <div class="colab-preface">
          <a href="#figure-1" class="figure-number">1</a>:
          NMF of input weights in InceptionV1 <code>mixed4d_5x5</code>, for a selection of ten neurons. The red, green, and blue channels on each grid indicate the weights for each of the 3 NMF factors.
        </div>
        <figure id="colab-button-1" class="fullscreen-diagram"></figure>
      </figcaption>
    </figure>

    <p>This visualization doesn’t tell you very much about what your weights are doing in the context of the larger model, but it does show you that they are learning nice spatial structures. This can be an easy sanity check that your neurons are learning, and a first step towards understanding your neuron’s behavior. We’ll also see later that this general approach of factoring weights can be extended into a powerful tool for studying neurons.</p>

    <p>Despite this lack of contextualization, one-sided NMF can be a great technique for investigating multiple channels at a glance. One thing you may quickly discover using this method is that, in models with global average pooling at the end of their convolutional layers, the last few layers will have all their weights be horizontal bands.</p>

    <figure id="figure-2">
      <img src="images/screenshot_2.png" style="max-height: 220px; width: auto;">
      <figcaption class="figcaption l-body">
        <p>
          <a href="#figure-2" class="figure-number">2</a>:
          Horizontally-banded weights in InceptionV1 <code>mixed5b_5x5</code>, for a selection of eight neurons. As in Figure 1, the red, green, and blue channels on each grid indicate the weights for each of the 3 NMF factors.
      </p>
      </figcaption>
    </figure>

    <p>We call this phenomenon <a href="/2020/circuits/weight-banding/"><i>weight banding</i></a>. One-sided NMF allows for quickly testing and validating hypotheses about phenomena such as weight banding.</p>

    <h2>Contextualizing Weights with Feature Visualization</h2>

    <p>Of course, looking at weights in a vacuum isn’t very interesting. In order to really understand what’s going on, we need to <i>contextualize</i> weights in the broader context of the network<d-cite bibtex-key="olah2018the"></d-cite>. The challenge of contextualization is a recurring challenge in understanding neural networks: we can easily observe every activation, every weight, and every gradient; the challenge lies in determining what those values represent.</p>

    <p>Recall that the weights between two convolutional layers are a four dimensional array of the shape:</p>

    <p><code>[relative x position, relative y position,
    input channels, output channels]</code></p>

    <p>If we fix the input channel and the output channel, we get a 2D array we can present with traditional data visualization. Let’s assume we know which neuron we’re interested in understanding, so we have the output channel. We can pick the input channels with high magnitude weights to our output channel.</p>

    <p>But what does the input represent? What about the output?</p>

    <p>The key trick is that techniques like feature visualization<d-cite bibtex-key="olah2017feature,nguyen2016multifaceted,karpathy2015visualizing,erhan2009visualizing"></d-cite> (or deeper investigations of neurons) can help us understand what the input and output neurons represent, contextualizing the graph. Feature visualizations are especially attractive because they’re automatic, and produce a single image which is often very informative about the neuron. As a result, we often represent neurons as feature visualizations in weight diagrams.</p>

    <figure id="figure-3">
      <svg width="1424" height="263" viewBox="0 0 1424 263" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="diagram-Figure_3" style="width: 100%; height: auto;">
<g id="Figure 3">
<rect width="1424" height="263" fill="white" class="pixelated"></rect>
<g id="Group 325">
<path id="Without context, these weights aren't very interesting." d="M16.9727 206.36L19.6045 192.449H23.6194L19.2822 212H15.2271L12.0447 198.921L8.8623 212H4.80713L0.469971 192.449H4.48486L7.13013 206.333L10.3528 192.449H13.7634L16.9727 206.36ZM29.6484 212H25.7544V197.471H29.6484V212ZM25.5261 193.711C25.5261 193.13 25.7186 192.651 26.1035 192.275C26.4974 191.899 27.03 191.711 27.7014 191.711C28.3639 191.711 28.892 191.899 29.2859 192.275C29.6798 192.651 29.8767 193.13 29.8767 193.711C29.8767 194.302 29.6753 194.786 29.2725 195.162C28.8786 195.538 28.3549 195.726 27.7014 195.726C27.0479 195.726 26.5198 195.538 26.1169 195.162C25.7231 194.786 25.5261 194.302 25.5261 193.711ZM37.5037 193.899V197.471H39.9878V200.318H37.5037V207.569C37.5037 208.106 37.6066 208.491 37.8125 208.724C38.0184 208.956 38.4123 209.073 38.9941 209.073C39.4238 209.073 39.8043 209.041 40.1355 208.979V211.919C39.3746 212.152 38.5913 212.269 37.7856 212.269C35.0643 212.269 33.6768 210.894 33.623 208.146V200.318H31.5015V197.471H33.623V193.899H37.5037ZM45.9363 199.056C46.9657 197.82 48.2593 197.203 49.8169 197.203C52.9679 197.203 54.5658 199.033 54.6106 202.695V212H50.73V202.802C50.73 201.969 50.5509 201.356 50.1929 200.962C49.8348 200.56 49.2395 200.358 48.407 200.358C47.2701 200.358 46.4465 200.797 45.9363 201.674V212H42.0557V191.375H45.9363V199.056ZM56.9336 204.601C56.9336 203.16 57.2111 201.875 57.7661 200.748C58.3211 199.62 59.1178 198.747 60.1562 198.129C61.2036 197.511 62.4166 197.203 63.7952 197.203C65.7556 197.203 67.3535 197.802 68.5889 199.002C69.8332 200.20