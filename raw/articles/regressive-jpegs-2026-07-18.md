---
source_url: https://maurycyz.com/projects/bad_jpeg/
ingested: 2026-07-18
sha256: 174aa1c94679156fff38f32d70b3cbf210bdf518bfee3864234091d0899f5d1e
blog_source: Hacker News
---
<!DOCTYPE html>
<html lang=en-us>
	<head>
		<meta charset=utf-8 />
		<meta name=viewport content='width=device-width, initial-scale=1' />
		<link rel='icon' type='image/x-icon' href='/favicon.ico'>
		<meta name=robots content='noarchive'>
		<meta name=generator content='mksite.c and my keyboard'>
		<style>
			<!--
			/* Theme colors */
			:root {
				--font: sans-serif;
				--fg-color: #fff;
				--bg-color: #111;
				--em-color: #ffbb00;
				--link-color1: #4ee;
				--link-color2: #4eafaf;
				--box-color: #21ff00;
				--table-color1: #000;
				--table-color2: #222;
				color-scheme: dark;
			}
			:root :has(#lightmode:checked) {
				--fg-color: #000;
				--bg-color: #fff;
				--em-color: #f00;
				--link-color1: #0000EE;
				--link-color2: #551A8B;
				--box-color: #000;
				--table-color1: #FFF;
				--table-color2: #CCC;
				color-scheme: light;
			}
			:root :has(#ttymode:checked) {
				--fg-color: #ff9300;
				--font: monospace, monospace;
				--bg-color: #000000;
				--em-color: #ff9300;
				--link-color1: none;
				--link-color2: none;
				--box-color: #ff9300;
				--table-color1: none;
				--table-color2: none;
				color-scheme: dark;
			}

			/* Column */
			body {background-color: var(--bg-color); color: var(--fg-color); font-family: var(--font)}
			main, footer {max-width: 40em; margin: auto;}
			img {width: 100%; height: auto;}

			/* Navigation box */
			fieldset {
				border: var(--box-color) 1px solid;
				color: var(--fg-color);;
				padding: 1em;
				margin: 1em;
				background-color: var(--bg-color);;
			}
			legend {
				border: var(--box-color) 1px solid;
				padding: .3em;
				background-color: var(--bg-color);
			}
			nav {
				position: static;
				width: 100%;
				display: flex;
				justify-content: center;
				align-items: center;
			}
			@media (min-width: 67em) {
				nav {
					position: fixed;
					display: block;
					width: auto;
				}
			}

			/* Kitten */
			@media (max-width: 66em) {
				#oneko {
					display: none;
				}
			}

			/* Link colors */
			a         {color: var(--link-color1);}
			a:visited {color: var(--link-color2);}

			/* Code blocks. Inline and block. */
			/* Do not follow theme */
			pre {
				background-color: #222;
				color: #eee;
				display: block;
				width: calc(100% - 1em);
				padding: 0.5em;
				overflow: auto;
				border: 1px #666 solid;
				font-family: monospace;
			}
			code {display: inline; background-color: #111; color: #eee; padding: 1px;}

			/* Inline notes: Warnings, etc */
			note-box {
				display: block;
				padding: 0.5em;
				border: 2px var(--em-color) solid;
			}

			details {
				border-left: 2px var(--em-color) solid;
				padding-left: 1em;
			}
			details img {margin-top: 1em;}
			summary {
				text-decoration: underline;
				user-select: none;
			}

			/* Use accent color for lines */
			hr {border-color: var(--em-color);}

			/* Image captions */
			center {color: #888;}

			/* Zebra striping */
			th {padding-right: 1em; background-color: var(--bg-color);}
			tr:nth-child(odd) {background-color: var(--table-color1);}
			tr:nth-child(even) {background-color: var(--table-color2);}

			/* Scrolled tables */
			.math {text-wrap: nowrap; display: block; overflow: auto;}

			/* Large initial letters */
			p.dropcap:first-letter {
				color: var(--em-color);
			}

			/* Text rubrication */
			em {color: var(--em-color); font-style: normal;}
			dt {color: var(--em-color);}

			/* Syntax highlighting. */
			h-n {color: #F27;}
			h-v {color: #B8F;}
			h-s {color: #AEE;}
			h-c {color: #777;}
			h-e {color: #F6F;}

			link-box {border-left: 2px var(--em-color) solid; display: block; word-wrap: break-word}

			/* CSS Only theme picker */
			theme-picker {
				border: 1px solid var(--fg-color);
				border-radius: 5px;
				display: flex;
				margin-top: 5px;
				overflow: clip;
				input {opacity: 0; position: absolute; pointer-events: none;}
				label {
					cursor: pointer;
					width: 50%;
					text-align: center;
					padding: 5px;
					/* Make the checked button look like it's pushed in. */
					&:has(input:checked) {box-shadow: inset 0px 0px 7px 0px var(--fg-color);}
					/* Hover indication so the user knows that it is clickable */
					&:hover {color: var(--em-color);}
					user-select: none;
				}
			}

			/* Monochrome CRT styling */
			@keyframes interlace {0% {top: 1px;}50% {top: 1px;}51% {top: 0px;}100% {top: 0px;}}
			:root :has(#ttymode:checked) {
				h1, h2, h3, h4, h5 {font-size: 100%;}
				nav {
					position: static !important;
					display: block !important;
					max-width: 40em;
					margin: auto;
				}
				fieldset {display: block;}
				legend {border-style: none !important;}
				theme-picker {border-radius: 5px !important;}
				img, video, center, pre, code, #oneko {filter: url(#mono)}
				theme-picker {border-radius: 0 !important;}
				screen-overlay {position: fixed; top: 0; left: 0;
					height: 100lvh; width: 100lvw;
					opacity: 0.15; z-index: 20;
					pointer-events: none;
					animation: interlace 0.05s infinite;
					background-image: repeating-linear-gradient(to bottom,
						var(--bg-color),
						var(--bg-color) 1px,
						var(--fg-color) 1px,
						var(--fg-color) 2px
					);
				}
			}

			/* Missing adblocker warning */
			#ad-note-hidden, #ad-note {display: none;}
			@media (min-height: 30em) { @media (min-width: 75em) {
				#ad-note {
					display: block; position: fixed;
					bottom: 1em; right: 1em; width: 14em;
					border: var(--em-color) 1px solid;
					background-color: var(--bg-color);
					padding: 1em;
				}
				#ad-note-content-wrapper {margin-top: 0em; margin-bottom: 0em}
			}}

			-->
		</style>
		<title>Regressive JPEGs: (Maurycy's blog) </title>
	</head>
	<body>
		<screen-overlay></screen-overlay>
		<nav><fieldset>
			<legend>Navigation:</legend>
			<a href='/'>Homepage</a><br/>
			&nbsp;&nbsp;&nbsp;&nbsp;<a href='/topics.html'>Index</a><br/>
			&nbsp;&nbsp;&nbsp;&nbsp;<a href='/archive'>Yearly archives</a><br/>
			<a href='/fun/'>Fun</a><br>
			<a href='/tags/astro'>Astrophotography</a><br/>
			&nbsp;&nbsp;&nbsp;&nbsp;<a href='/astro/catalog.html'>(catalog)</a><br/>
			<a href='/about.html'>About this site</a><br/>
			<a href='/real_pages'>Real pages</a><br>
			<theme-picker>
				<label>Dark<input type=radio id=darkmode   name=theme checked></label>
				<label>Light<input type=radio id=lightmode name=theme></label>
				<label>TTY<input type=radio id=ttymode     name=theme></label>
			</theme-picker>
		</fieldset></nav>
		<script>
			<!--
			/* Inlined for speed because this is needed to correctly render the page */
			var checkbox1 = document.getElementById('lightmode')
			var checkbox2 = document.getElementById('ttymode')
			function save_mode() {
				var state1 = checkbox1.checked;
				window.localStorage.setItem('light_mode', state1);
				var state2 = checkbox2.checked;
				window.localStorage.setItem('tty_mode', state2);
			}
			if (window.localStorage.getItem('light_mode') == 'true') {
				checkbox1.checked = true;
			}
			if (window.localStorage.getItem('tty_mode') == 'true') {
				checkbox2.checked = true;
			}
			document.getElementsByTagName('label')[0].onclick = save_mode;
			document.getElementsByTagName('label')[1].onclick = save_mode;
			document.getElementsByTagName('label')[2].onclick = save_mode;
			-->
		</script>
		<main>
			<h1><em>Regressive JPEGs:</em></h1>
<b title='Publication'><time>2026-07-17</time></b> 
<!-- mksite: start of content -->
<p>

One of the cool features of JPEG files is that there's the option to save low frequency components first.
This means that a partially downloaded image will be displayed at low resolution instead of being cut off.
</p><p>
In the file, this works by breaking up the compressed data into multiple "scans", each prefixed with a header.
Here's the first scan of a representive image:
<!-- snip -->
</p>
<p>
</p>
<pre>
<h-n>FF DA</h-n> - "start of scan" marker
<h-s>00 0C</h-s> - Big endian length field (12 bytes) <h-c>Includes itself</h-c>
<h-s>03</h-s> - Number of channels in scan (3)
  <h-v>01</h-v> - Global id of first included channel
  <h-v>00</h-v> - Huffman table index #1 (DC: 0, AC: 0)
  <h-v>02</h-v> - Global id of second included channel
  <h-v>10</h-v> - Huffman table index #2 (DC: 1, AC: 0)
  <h-v>03</h-v> - Global id of third included channel
  <h-v>10</h-v> - Huffman table index #2 (DC: 0, AC: 0)
<h-v>00</h-v> - Starting DCT bin (DC)
<h-v>00</h-v> - Ending DCT bin (also DC)
<h-v>01</h-v> - Precision: half, no pre-existing data. 

f8ad 512d d3f1 cd96 <h-c>- Huffman coded DCT coefficients</h-c>
bcb0 58df 53d5 5d97
<h-c>[...and a lot more]</h-c>
</pre>
<p>
</p><p>
... this one includes the lowest (DC) Fourier bin for all three color channels.
</p><p>
<note-box>
The three color channels are YCbCr instead of the usual RGB.
The luminance (Y) seperated because it must be high quality, but the color can be fudged quite a bit while looking fine.
<br><br>
Very roughly: Y = G, Cb = B - G, Cr = R - G
</note-box>
</p><p>
After it, the file contains eight more scans to fill in the rest of the data:
</p><p>
<table>
  <tr><th>Scan number</th><th>Channels</th><th>DCT bin range</th><th>Precision</th><tr>
  <tr><td>0</td><td>Y Cb Cr</td><td>0 - 0</td><td>Half (-1 bit)</td></tr>
  <tr><td>1</td><td>Y</td><td>1 - 5</td><td>Quarter (-2 bits)</td></tr>
  <tr><td>2</td><td>Cb</td><td>1 - 63</td><td>Half</td></tr>
  <tr><td>3</td><td>Cr</td><td>1 - 63</td><td>Half</td></tr>
  <tr><td>4</td><td>Y</td><td><em>6 - 63</em></td><td>Quarter</td></tr>
  <tr><td>5</td><td>Y</td><td>1 - 63</td><td>Half</td></tr>
  <tr><td>6</td><td>Y Cr Cb</td><td>0 - 0</td><td>Full</td></tr>
  <tr><td>7</td><td>Cr</td><td>1 - 63</td><td>Full</td></tr>
  <tr><td>8</td><td>Cb</td><td>1 - 63</td><td>Full</td></tr>
  <tr><td>9</td><td>Y</td><td>1 - 63</td><td>Full</td></tr>
</table>
</p><p>
Scan #0 contains a very low resolution preview of the image.
</p><p>
Scan #1 adds some details to the luminance.
</p><p>
Scans number two through five contain full low precision data.
</p><p>
Scan 4 has an unusual spectral range because it's filling in the gap left by #1.
That way, number 5 has full quarter precision data to build on.
</p><p>
Scans six through nine add the final missing bit to bring the image to full quality.
</p><p>
<note-box>
Given what I said about color being less important, it might seem weird that my example has the color data first:
This works because the the chrominance is saved at half resolution (quarter pixel count).
As a result, full chrominance data (Cr + Cb) only weighs half as much as luminance.
</note-box>
</p><p>
<em>Since each scan explicitly sets its spectral range</em>,
it should be possible to construct a JPEG file
where future scans overwrite already rendered image data.
</p><p>
Actually, it's very easy to do this:
</p><p>
Concatenate multiple images with the same resolution and filter out the start-of-image, start-of-frame and end-of-image markers.
This can be done in a hex editor, but I used a quick and dirty C program.
</p><p>
<em>When served over a slow network</em>, this concatenated file will switch between multiple images:
</p><p>
<a href=/projects/bad_jpeg/cats.jpg target=_blank>
<img src=/projects/bad_jpeg/cats.jpg alt="An image of a cat that switches between a cat sitting in grass and a different one on concrete as it loads" width=753 height=503>
</a>
<center>Click to open in new tab</center>
</p><p>
<em>But, most decoders will give up after some number of scans</em>:
I think this is done to avoid a zip bomb style problem...
but it prevents this from working on more than 9 frames, which is not enough for a proper animation.
</p><p>
To do that, I'd have to minimize the number of scans in each frame. 
The simplest idea is to start with baseline JPEGs that only have a single scan.
</p><p>
... but it doesn't work:
</p><p>
In progressive mode, a scan can't contain both AC (bins above 0) and DC (bin 0) data at the same time.
This limitation doesn't exist for baseline mode, but the baseline decoder stops after the first scan.
</p><p>
Since AC data must follow DC data, the smallest possible "progressive" JPEG contains a single DC-only scan.
Because the DCT runs on 16x16 blocks, such an image won't a solid color:
</p><p>
it'll be 1/16th of the original resolution.
</p><p>
<table>
  <tr><th>Scan number</th><th>Channels</th><th>DCT bins</th><th>Precision</th><tr>
  <tr><td>0</td><td>Y Cb Cr</td><td>0 - 0</td><td>Full</td></tr>
</table>
</p><p>
Doing this, I can get Chrome to render around 90 frames before giving up.
Other browsers like Firefox have more patience, but a 90 scan image seems to work almost everywhere.
</p><p>
As a bonus, this avoids the ghosting of the naive attempt:
that happened because AC scans are supposed to refine old data.
Normally, this allows images to include multiple precision levels without inflating file size...
but doesn't play nicely with my tricks.
</p><p>
If the file only includes DC scans with no actual progression, this isn't a problem.
</p><p>
<em>Since a "DC-only" frame is a standards-compliant images</em>, creating them doesn't require anything special:
</p><p>
<pre>
<h-n>cat</h-n> &gt; <h-s>frame.scans</h-s>&lt;&lt;EOF
<h-v># DC only scan:
0,1,2:0-0,0,0;
# and nothing else</h-v>
EOF
<h-n>jpegtran</h-n> -scans <h-s>frame.scans</h-s> -outfile <h-s>out.jpg in.jpg</h-s>
</pre>
</p><p>
Using these, it's possible to pack a whole video inside a single image:
</p><p>
<a href=/projects/bad_jpeg/cat.jpg>
<img src=/projects/bad_jpeg/cat.jpg alt="A 'video' of a black cat walking towards the camera." width=1280 height=720>
</a>
<center>Click to open in new tab</center>
</p><p>
Besides unconventional rickrolls and other trolling, this has no practical applications:
there's no way to add timing information, so playback is entirely dependent on network delay.
</p><p>
... although there is a lot of fun to be had using partial rendering:
</p><p>
This is a pure HTML video using &lt;dialog&gt; tags: <a href=http://badapple.rose.systems/>badapple.rose.systems</a>
</p><p>
Of course, there's no rule that the data must be hardcoded:
here's a <a href=/fun/chat>interactive single-page application</a> with no CSS or JavaScript.
(seems slighty broken, I'll investigate later)
</p><p>
<h1><em>Related</em>:</h1>
<link-box>
  <ul>
    <li><a href=/projects/bad_jpeg/merge.c>/projects/bad_jpeg/merge.c</a>: The code used to generate these images</li>
  </ul>
</link-box>

</p>
<!-- mksite: end of content -->
		</main>
		<footer>
			<hr>
			Site wide <a href=https://maurycyz.com/index.xml>RSS feed</a>.
			<br><br>
			Proudly supporting IPv6!
			<a href=http://v6.maurycyz.com/whoami title='If this loads, you have IPv6 support.'>Check your network</a>
			<br><br>
			You may use this content under the <a rel=license href=https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en>CC BY-NC-SA 4.0 License</a>.
			This website is <b>not</b> licensed for ML/LLM training or content creation.
			<br><br>
			Questions, comments, and technical issues can be sent in <a href='mailto:blog@%6daurycyz%2ecom'>by email</a>.
		</footer>
		<script defer src='/nativeads.js'></script>
		<div
			id='ad-note-hidden'
			class='ftf-dma-note ad native-ad native-ad-1 ytd-j yxd-j yxd-jd aff-content-col aff-inner-col aff-item-list ark-ad-message inplayer-ad inplayer_banners in_stream_banner trafficjunky-float-right dbanner preroll-blocker happy-inside-player blocker-notice blocker-overlay exo-horizontal ave-pl bottom-hor-block brs-block advboxemb wgAdBlockMessage glx-watermark-container overlay-advertising-new header-menu-bottom-ads rkads mdp-deblocker-wrapper amp-ad-inner imggif bloc-pub bloc-pub2 hor_banner aan_fake aan_fake__video-units rps_player_ads fints-block__row full-ave-pl full-bns-block vertbars video-brs player-bns-block wps-player__happy-inside gallery-bns-bl stream-item-widget adsbyrunactive happy-under-player adde_modal_detector adde_modal-overlay ninja-recommend-block aoa_overlay message'
		>
			<p id='ad-note-content-wrapper'>
			</p>
		</div>
		<!-- svg filter for images -->
		<svg width=0 height=0><defs><filter id=mono><feColorMatrix type=matrix values="
			.33 .33 .33  0  0 
			.15 .15 .15 0  0 
			0   0   0  0  0 
			0   0   0  1  0" in=SourceGraphic/></feColorMatrix>
		</filter></defs></svg>
	</body>
</html>
