---
source_url: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
ingested: 2026-07-21
sha256: 4b08ce13c58d3df78e9a759d4fb838b89cdc4580f262c326257571f40e3f2251
blog_source: Hacker News
---
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">

<head profile="http://gmpg.org/xfn/11">
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title>A digestion of the Jacobian conjecture counterexample | What&#039;s new</title>
	<link rel="pingback" href="https://terrytao.wordpress.com/xmlrpc.php" />
	<meta name='robots' content='max-image-preview:large' />
<meta name="google-site-verification" content="YnmTzeF3F_x_iP1LlMorwk_-PaRMR7FRkMea24K_cnY" />
<link rel='dns-prefetch' href='//widgets.wp.com' />
<link rel='dns-prefetch' href='//s2.wp.com' />
<link rel='dns-prefetch' href='//s1.wp.com' />
<link rel='dns-prefetch' href='//s0.wp.com' />
<link rel="alternate" type="application/rss+xml" title="What&#039;s new &raquo; Feed" href="https://terrytao.wordpress.com/feed/" />
<link rel="alternate" type="application/rss+xml" title="What&#039;s new &raquo; Comments Feed" href="https://terrytao.wordpress.com/comments/feed/" />
<link rel="alternate" type="application/rss+xml" title="What&#039;s new &raquo; A digestion of the Jacobian conjecture&nbsp;counterexample Comments Feed" href="https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/feed/" />
	<script type="text/javascript">
		/* <![CDATA[ */
		function addLoadEvent(func) {
			var oldonload = window.onload;
			if (typeof window.onload != 'function') {
				window.onload = func;
			} else {
				window.onload = function () {
					oldonload();
					func();
				}
			}
		}
		/* ]]> */
	</script>
	<style id="wp-img-auto-sizes-contain-inline-css">
img:is([sizes=auto i],[sizes^="auto," i]){contain-intrinsic-size:3000px 1500px}
/*# sourceURL=wp-img-auto-sizes-contain-inline-css */
</style>
<link crossorigin='anonymous' rel='stylesheet' id='all-css-2-1' href='/_static/??/wp-content/mu-plugins/likes/jetpack-likes.css,/wp-content/mu-plugins/infinity/themes/pub/tarski.css?m=1743883414j&cssminify=yes' type='text/css' media='all' />
<style id="wp-emoji-styles-inline-css">

	img.wp-smiley, img.emoji {
		display: inline !important;
		border: none !important;
		box-shadow: none !important;
		height: 1em !important;
		width: 1em !important;
		margin: 0 0.07em !important;
		vertical-align: -0.1em !important;
		background: none !important;
		padding: 0 !important;
	}
/*# sourceURL=wp-emoji-styles-inline-css */
</style>
<style id="wp-block-library-inline-css">
:root{--wp-block-synced-color:#7a00df;--wp-block-synced-color--rgb:122,0,223;--wp-bound-block-color:var(--wp-block-synced-color);--wp-editor-canvas-background:#ddd;--wp-admin-theme-color:#007cba;--wp-admin-theme-color--rgb:0,124,186;--wp-admin-theme-color-darker-10:#006ba1;--wp-admin-theme-color-darker-10--rgb:0,107,160.5;--wp-admin-theme-color-darker-20:#005a87;--wp-admin-theme-color-darker-20--rgb:0,90,135;--wp-admin-border-width-focus:2px}@media (min-resolution:192dpi){:root{--wp-admin-border-width-focus:1.5px}}.wp-element-button{cursor:pointer}:root .has-very-light-gray-background-color{background-color:#eee}:root .has-very-dark-gray-background-color{background-color:#313131}:root .has-very-light-gray-color{color:#eee}:root .has-very-dark-gray-color{color:#313131}:root .has-vivid-green-cyan-to-vivid-cyan-blue-gradient-background{background:linear-gradient(135deg,#00d084,#0693e3)}:root .has-purple-crush-gradient-background{background:linear-gradient(135deg,#34e2e4,#4721fb 50%,#ab1dfe)}:root .has-hazy-dawn-gradient-background{background:linear-gradient(135deg,#faaca8,#dad0ec)}:root .has-subdued-olive-gradient-background{background:linear-gradient(135deg,#fafae1,#67a671)}:root .has-atomic-cream-gradient-background{background:linear-gradient(135deg,#fdd79a,#004a59)}:root .has-nightshade-gradient-background{background:linear-gradient(135deg,#330968,#31cdcf)}:root .has-midnight-gradient-background{background:linear-gradient(135deg,#020381,#2874fc)}:root{--wp--preset--font-size--normal:16px;--wp--preset--font-size--huge:42px}.has-regular-font-size{font-size:1em}.has-larger-font-size{font-size:2.625em}.has-normal-font-size{font-size:var(--wp--preset--font-size--normal)}.has-huge-font-size{font-size:var(--wp--preset--font-size--huge)}:root .has-text-align-center{text-align:center}:root .has-text-align-left{text-align:left}:root .has-text-align-right{text-align:right}.has-fit-text{white-space:nowrap!important}#end-resizable-editor-section{display:none}.aligncenter{clear:both}.items-justified-left{justify-content:flex-start}.items-justified-center{justify-content:center}.items-justified-right{justify-content:flex-end}.items-justified-space-between{justify-content:space-between}.screen-reader-text{word-wrap:normal!important;border:0;clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px;word-break:normal!important}.screen-reader-text:focus{background-color:#ddd;clip-path:none;color:#444;display:block;font-size:1em;height:auto;left:5px;line-height:normal;padding:15px 23px 14px;text-decoration:none;top:5px;width:auto;z-index:100000}html :where(.has-border-color){border-style:solid}html :where([style^=border-color],[style*=";border-color"],[style*="; border-color"]){border-style:solid}html :where([style^=border-top-color],[style*=";border-top-color"],[style*="; border-top-color"]){border-top-style:solid}html :where([style^=border-right-color],[style*=";border-right-color"],[style*="; border-right-color"]){border-right-style:solid}html :where([style^=border-bottom-color],[style*=";border-bottom-color"],[style*="; border-bottom-color"]){border-bottom-style:solid}html :where([style^=border-left-color],[style*=";border-left-color"],[style*="; border-left-color"]){border-left-style:solid}html :where([style^=border-width],[style*=";border-width"],[style*="; border-width"]){border-style:solid}html :where([style^=border-top-width],[style*=";border-top-width"],[style*="; border-top-width"]){border-top-style:solid}html :where([style^=border-right-width],[style*=";border-right-width"],[style*="; border-right-width"]){border-right-style:solid}html :where([style^=border-bottom-width],[style*=";border-bottom-width"],[style*="; border-bottom-width"]){border-bottom-style:solid}html :where([style^=border-left-width],[style*=";border-left-width"],[style*="; border-left-width"]){border-left-style:solid}html :where(img[class*=wp-image-]){height:auto;max-width:100%}:where(figure){margin:0 0 1em}html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:var(--wp-admin--admin-bar--height,0px)}@media screen and (max-width:600px){html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:0px}}

/*# sourceURL=/wp-content/plugins/gutenberg-core/v23.5.3/build/styles/block-library/common.min.css */
</style>
<style id="wp-block-library-inline-css-extra">
.has-text-align-justify {
	text-align:justify;
}
.has-text-align-justify{text-align:justify;}
/*# sourceURL=wp-block-library-inline-css */
</style>

<style id="classic-theme-styles-inline-css">
.wp-block-button__link{background-color:#32373c;border-radius:9999px;box-shadow:none;color:#fff;font-size:1.125em;padding:calc(.667em + 2px) calc(1.333em + 2px);text-decoration:none}.wp-block-file__button{background:#32373c;color:#fff}.wp-block-accordion-heading{margin:0}.wp-block-accordion-heading__toggle{background-color:inherit!important;color:inherit!important}.wp-block-accordion-heading__toggle:not(:focus-visible){outline:none}.wp-block-accordion-heading__toggle:focus,.wp-block-accordion-heading__toggle:hover{background-color:inherit!important;border:none;box-shadow:none;color:inherit;padding:var(--wp--preset--spacing--20,1em) 0;text-decoration:none}.wp-block-accordion-heading__toggle:focus-visible{outline:auto;outline-offset:0}.wp-block-tab:not(.has-text-color){color:inherit!important}.wp-block-tab:not(.has-background){background-color:inherit!important}.wp-block-tab:focus,.wp-block-tab:hover{text-decoration:none}.wp-block-tab:focus-visible{outline:auto;outline-offset:0}
/*# sourceURL=/wp-content/plugins/gutenberg-core/v23.5.3/build/styles/block-library/classic.min.css */
</style>

<link crossorigin='anonymous' rel='stylesheet' id='all-css-10-1' href='/_static/??-eJx9jcEKg0AMRH+oaVhorR7Eb9E16IpZg8min2889FZ6GYbhPQYPgbhlo2zIBWQtU8qKcdvJd5be0AmmMfW0Ejv2jKoP/K0daZzIXNdvB6PzvyJ+A8MgO6mCJ6fCYLN/6e113IZXU9WfUL/DcgHSTkDo&cssminify=yes' type='text/css' media='all' />
<style id="global-styles-inline-css">
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--font-family--albert-sans: 'Albert Sans', sans-serif;--wp--preset--font-family--alegreya: Alegreya, serif;--wp--preset--font-family--arvo: Arvo, serif;--wp--preset--font-family--bodoni-moda: 'Bodoni Moda', serif;--wp--preset--font-family--bricolage-grotesque: 'Bricolage Grotesque', sans-serif;--wp--preset--font-family--cabin: Cabin, sans-serif;--wp--preset--font-family--chivo: Chivo, sans-serif;--wp--preset--font-family--commissioner: Commissioner, sans-serif;--wp--preset--font-family--cormorant: Cormorant, serif;--wp--preset--font-family--courier-prime: 'Courier Prime', monospace;--wp--preset--font-family--crimson-pro: 'Crimson Pro', serif;--wp--preset--font-family--dm-mono: 'DM Mono', monospace;--wp--preset--font-family--dm-sans: 'DM Sans', sans-serif;--wp--preset--font-family--dm-serif-display: 'DM Serif Display', serif;--wp--preset--font-family--domine: Domine, serif;--wp--preset--font-family--eb-garamond: 'EB Garamond', serif;--wp--preset--font-family--epilogue: Epilogue, sans-serif;--wp--preset--font-family--fahkwang: Fahkwang, sans-serif;--wp--preset--font-family--figtree: Figtree, sans-serif;--wp--preset--font-family--fira-sans: 'Fira Sans', sans-serif;--wp--preset--font-family--fjalla-one: 'Fjalla One', sans-serif;--wp--preset--font-family--fraunces: Fraunces, serif;--wp--preset--font-family--gabarito: Gabarito, system-ui;--wp--preset--font-family--ibm-plex-mono: 'IBM Plex Mono', monospace;--wp--preset--font-family--ibm-plex-sans: 'IBM Plex Sans', sans-serif;--wp--preset--font-family--ibarra-real-nova: 'Ibarra Real Nova', serif;--wp--preset--font-family--instrument-serif: 'Instrument Serif', serif;--wp--preset--font-family--inter: Inter, sans-serif;--wp--preset--font-family--josefin-sans: 'Josefin Sans', sans-serif;--wp--preset--font-family--jost: Jost, sans-serif;--wp--preset--font-family--libre-baskerville: 'Libre Baskerville', serif;--wp--preset--font-family--libre-franklin: 'Libre Franklin', sans-serif;--wp--preset--font-family--literata: Literata, serif;--wp--preset--font-family--lora: Lora, serif;--wp--preset--font-family--merriweather: Merriweather, serif;--wp--preset--font-family--montserrat: Montserrat, sans-serif;--wp--preset--font-family--newsreader: Newsreader, serif;--wp--preset--font-family--noto-sans-mono: 'Noto Sans Mono', sans-serif;--wp--preset--font-family--nunito: Nunito, sans-serif;--wp--preset--font-family--open-sans: 'Open Sans', sans-serif;--wp--preset--font-family--overpass: Overpass, sans-serif;--wp--preset--font-family--pt-serif: 'PT Serif', serif;--wp--preset--font-family--petrona: Petrona, serif;--wp--preset--font-family--piazzolla: Piazzolla, serif;--wp--preset--font-family--playfair-display: 'Playfair Display', serif;--wp--preset--font-family--plus-jakarta-sans: 'Plus Jakarta Sans', sans-serif;--wp--preset--font-family--poppins: Poppins, sans-serif;--wp--preset--font-family--raleway: Raleway, sans-serif;--wp--preset--font-family--roboto: Roboto, sans-serif;--wp--preset--font-family--roboto-slab: 'Roboto Slab', serif;--wp--preset--font-family--rubik: Rubik, sans-serif;--wp--preset--font-family--rufina: Rufina, serif;--wp--preset--font-family--sora: Sora, sans-serif;--wp--preset--font-family--source-sans-3: 'Source Sans 3', sans-serif;--wp--preset--font-family--source-serif-4: 'Source Serif 4', serif;--wp--preset--font-family--space-mono: 'Space Mono', monospace;--wp--preset--font-family--syne: Syne, sans-serif;--wp--preset--font-family--texturina: Texturina, serif;--wp--preset--font-family--urbanist: Urbanist, sans-serif;--wp--preset--font-family--work-sans: 'Work Sans', sans-serif;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);}.wp-block-button{--wp--preset--dimension--25: 25%;--wp--preset--dimension--50: 50%;--wp--preset--dimension--75: 75%;--wp--preset--dimension--100: 100%;}:where(body) { margin: 0; }:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;font-style: inherit;font-weight: inherit;letter-spacing: inherit;line-height: inherit;padding-top: calc(0.667em + 2px);padding-right: calc(1.333em + 2px);padding-bottom: calc(0.667em + 2px);padding-left: calc(1.333em + 2px);text-decoration: none;text-transform: inherit;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}.has-albert-sans-font-family{font-family: var(--wp--preset--font-family--albert-sans) !important;}.has-alegreya-font-family{font-family: var(--wp--preset--font-family--alegreya) !important;}.has-arvo-font-family{font-family: var(--wp--preset--font-family--arvo) !important;}.has-bodoni-moda-font-family{font-family: var(--wp--preset--font-family--bodoni-moda) !important;}.has-bricolage-grotesque-font-family{font-family: var(--wp--preset--font-family--bricolage-grotesque) !important;}.has-cabin-font-family{font-family: var(--wp--preset--font-family--cabin) !important;}.has-chivo-font-family{font-family: var(--wp--preset--font-family--chivo) !important;}.has-commissioner-font-family{font-family: var(--wp--preset--font-family--commissioner) !important;}.has-cormorant-font-family{font-family: var(--wp--preset--font-family--cormorant) !important;}.has-courier-prime-font-family{font-family: var(--wp--preset--font-family--courier-prime) !important;}.has-crimson-pro-font-family{font-family: var(--wp--preset--font-family--crimson-pro) !important;}.has-dm-mono-font-family{font-family: var(--wp--preset--font-family--dm-mono) !important;}.has-dm-sans-font-family{font-family: var(--wp--preset--font-family--dm-sans) !important;}.has-dm-serif-display-font-family{font-family: var(--wp--preset--font-family--dm-serif-display) !important;}.has-domine-font-family{font-family: var(--wp--preset--font-family--domine) !important;}.has-eb-garamond-font-family{font-family: var(--wp--preset--font-family--eb-garamond) !important;}.has-epilogue-font-family{font-family: var(--wp--preset--font-family--epilogue) !important;}.has-fahkwang-font-family{font-family: var(--wp--preset--font-family--fahkwang) !important;}.has-figtree-font-family{font-family: var(--wp--preset--font-family--figtree) !important;}.has-fira-sans-font-family{font-family: var(--wp--preset--font-family--fira-sans) !important;}.has-fjalla-one-font-family{font-family: var(--wp--preset--font-family--fjalla-one) !important;}.has-fraunces-font-family{font-family: var(--wp--preset--font-family--fraunces) !important;}.has-gabarito-font-family{font-family: var(--wp--preset--font-family--gabarito) !important;}.has-ibm-plex-mono-font-family{font-family: var(--wp--preset--font-family--ibm-plex-mono) !important;}.has-ibm-plex-sans-font-family{font-family: var(--wp--preset--font-family--ibm-plex-sans) !important;}.has-ibarra-real-nova-font-family{font-family: var(--wp--preset--font-family--ibarra-real-nova) !important;}.has-instrument-serif-font-family{font-family: var(--wp--preset--font-family--instrument-serif) !important;}.has-inter-font-family{font-family: var(--wp--preset--font-family--inter) !important;}.has-josefin-sans-font-family{font-family: var(--wp--preset--font-family--josefin-sans) !important;}.has-jost-font-family{font-family: var(--wp--preset--font-family--jost) !important;}.has-libre-baskerville-font-family{font-family: var(--wp--preset--font-family--libre-baskerville) !important;}.has-libre-franklin-font-family{font-family: var(--wp--preset--font-family--libre-franklin) !important;}.has-literata-font-family{font-family: var(--wp--preset--font-family--literata) !important;}.has-lora-font-family{font-family: var(--wp--preset--font-family--lora) !important;}.has-merriweather-font-family{font-family: var(--wp--preset--font-family--merriweather) !important;}.has-montserrat-font-family{font-family: var(--wp--preset--font-family--montserrat) !important;}.has-newsreader-font-family{font-family: var(--wp--preset--font-family--newsreader) !important;}.has-noto-sans-mono-font-family{font-family: var(--wp--preset--font-family--noto-sans-mono) !important;}.has-nunito-font-family{font-family: var(--wp--preset--font-family--nunito) !important;}.has-open-sans-font-family{font-family: var(--wp--preset--font-family--open-sans) !important;}.has-overpass-font-family{font-family: var(--wp--preset--font-family--overpass) !important;}.has-pt-serif-font-family{font-family: var(--wp--preset--font-family--pt-serif) !important;}.has-petrona-font-family{font-family: var(--wp--preset--font-family--petrona) !important;}.has-piazzolla-font-family{font-family: var(--wp--preset--font-family--piazzolla) !important;}.has-playfair-display-font-family{font-family: var(--wp--preset--font-family--playfair-display) !important;}.has-plus-jakarta-sans-font-family{font-family: var(--wp--preset--font-family--plus-jakarta-sans) !important;}.has-poppins-font-family{font-family: var(--wp--preset--font-family--poppins) !important;}.has-raleway-font-family{font-family: var(--wp--preset--font-family--raleway) !important;}.has-roboto-font-family{font-family: var(--wp--preset--font-family--roboto) !important;}.has-roboto-slab-font-family{font-family: var(--wp--preset--font-family--roboto-slab) !important;}.has-rubik-font-family{font-family: var(--wp--preset--font-family--rubik) !important;}.has-rufina-font-family{font-family: var(--wp--preset--font-family--rufina) !important;}.has-sora-font-family{font-family: var(--wp--preset--font-family--sora) !important;}.has-source-sans-3-font-family{font-family: var(--wp--preset--font-family--source-sans-3) !important;}.has-source-serif-4-font-family{font-family: var(--wp--preset--font-family--source-serif-4) !important;}.has-space-mono-font-family{font-family: var(--wp--preset--font-family--space-mono) !important;}.has-syne-font-family{font-family: var(--wp--preset--font-family--syne) !important;}.has-texturina-font-family{font-family: var(--wp--preset--font-family--texturina) !important;}.has-urbanist-font-family{font-family: var(--wp--preset--font-family--urbanist) !important;}.has-work-sans-font-family{font-family: var(--wp--preset--font-family--work-sans) !important;}
/*# sourceURL=global-styles-inline-css */
</style>

<link crossorigin='anonymous' rel='stylesheet' id='all-css-12-1' href='/wp-content/mu-plugins/jetpack-mu-wpcom-plugin/moon/jetpack_vendor/automattic/jetpack-mu-wpcom/src/build/verbum-comments/verbum-comments.css?m=1784324579i&cssminify=yes' type='text/css' media='all' />
<link rel='stylesheet' id='verbum-gutenberg-css-css' href='https://widgets.wp.com/verbum-block-editor/block-editor.css?ver=1771405207' media='all' />
<link crossorigin='anonymous' rel='stylesheet' id='all-css-14-1' href='/wp-content/themes/pub/tarski/style.css?m=1763135822i&cssminify=yes' type='text/css' media='all' />
<link crossorigin='anonymous' rel='stylesheet' id='print-css-15-1' href='/wp-content/themes/pub/tarski/print.css?m=1323834012i&cssminify=yes' type='text/css' media='print' />
<link crossorigin='anonymous' rel='stylesheet' id='all-css-16-1' href='/_static/??-eJzTLy/QTc7PK0nNK9HPLdUtyClNz8wr1i9KTcrJTwcy0/WTi5G5ekCujj52Temp+bo5+cmJJZn5eSgc3bScxMwikFb7XFtDE1NLExMLc0OTLACohS2q&cssminify=yes' type='text/css' media='all' />
<style id="jetpack-global-styles-frontend-style-inline-css">
:root { --font-headings: unset; --font-base: unset; --font-headings-default: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif; --font-base-default: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;}
/*# sourceURL=jetpack-global-styles-frontend-style-inline-css */
</style>
<link crossorigin='anonymous' rel='stylesheet' id='all-css-18-1' href='/_static/??-eJyNjcEKAjEMRH/ImhVlqwfxU6TbhrZrmhTTIv69u+JFvHgZ5sHwBh7VeOGG3KB0U6nHzAoztur87cNQRNYInVBBk7tjcCE83zVz3HrVDfxvumb2MPVMAVR8dmRIougX/DhbwrK8pwNEksnROriU884e9+PJDnaYXxwFS20=&cssminify=yes' type='text/css' media='all' />
<script id="wpcom-actionbar-placeholder-js-extra">
var actionbardata = {"siteID":"817149","postID":"17967","siteURL":"https://terrytao.wordpress.com","xhrURL":"https://terrytao.wordpress.com/wp-admin/admin-ajax.php","nonce":"7f65087b7e","isLoggedIn":"","statusMessage":"","subsEmailDefault":"instantly","proxyScriptUrl":"https://s0.wp.com/wp-content/js/wpcom-proxy-request.js?m=1513050504i&amp;ver=20211021","shortlink":"https://wp.me/p3qzP-4FN","i18n":{"followedText":"New posts from this site will now appear in your \u003Ca href=\"https://wordpress.com/reader\"\u003EReader\u003C/a\u003E","foldBar":"Collapse this bar","unfoldBar":"Expand this bar","shortLinkCopied":"Shortlink copied to clipboard."}};
//# sourceURL=wpcom-actionbar-placeholder-js-extra
</script>
<script id="jetpack-mu-wpcom-settings-js-before">
var JETPACK_MU_WPCOM_SETTINGS = {"assetsUrl":"https://s1.wp.com/wp-content/mu-plugins/jetpack-mu-wpcom-plugin/moon/jetpack_vendor/automattic/jetpack-mu-wpcom/src/build/"};
//# sourceURL=jetpack-mu-wpcom-settings-js-before
</script>
<script crossorigin='anonymous' type='text/javascript'  src='/wp-content/js/rlt-proxy.js?m=1720530689i'></script>
<script id="rlt-proxy-js-after">
	rltInitialize( {"token":null,"iframeOrigins":["https:\/\/widgets.wp.com"]} );
//# sourceURL=rlt-proxy-js-after
</script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://terrytao.wordpress.com/xmlrpc.php?rsd" />
<meta name="generator" content="WordPress.com" />
<link rel="canonical" href="https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/" />
<link rel='shortlink' href='https://wp.me/p3qzP-4FN' />
<link rel="alternate" type="application/json+oembed" href="https://public-api.wordpress.com/oembed/?format=json&amp;url=https%3A%2F%2Fterrytao.wordpress.com%2F2026%2F07%2F21%2Fa-digestion-of-the-jacobian-conjecture-counterexample%2F&amp;for=wpcom-auto-discovery" /><link rel="alternate" type="application/xml+oembed" href="https://public-api.wordpress.com/oembed/?format=xml&amp;url=https%3A%2F%2Fterrytao.wordpress.com%2F2026%2F07%2F21%2Fa-digestion-of-the-jacobian-conjecture-counterexample%2F&amp;for=wpcom-auto-discovery" />
<!-- Jetpack Open Graph Tags -->
<meta property="og:type" content="article" />
<meta property="og:title" content="A digestion of the Jacobian conjecture counterexample" />
<meta property="og:url" content="https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/" />
<meta property="og:description" content="The notorious Jacobian conjecture can be formulated concretely over the complex numbers as follows. Conjecture 1 (Jacobian Conjecture) Let $latex {F:{\bf C}^n \rightarrow {\bf C}^n}&amp;fg=000000$ …" />
<meta property="article:published_time" content="2026-07-21T21:04:44+00:00" />
<meta property="article:modified_time" content="2026-07-21T21:55:30+00:00" />
<meta property="og:site_name" content="What&#039;s new" />
<meta property="og:image" content="https://secure.gravatar.com/blavatar/bd4bda4207561b6998f10dec44b570f04ff4072b20f89162d525b186dfca3e49?s=200&#038;ts=1784678045" />
<meta property="og:image:width" content="200" />
<meta property="og:image:height" content="200" />
<meta property="og:image:alt" content="" />
<meta property="og:locale" content="en_US" />
<meta property="fb:app_id" content="249643311490" />
<meta property="article:publisher" content="https://www.facebook.com/WordPresscom" />
<meta name="twitter:text:title" content="A digestion of the Jacobian conjecture&nbsp;counterexample" />
<meta name="twitter:image" content="https://secure.gravatar.com/blavatar/bd4bda4207561b6998f10dec44b570f04ff4072b20f89162d525b186dfca3e49?s=240" />
<meta name="twitter:card" content="summary" />

<!-- End Jetpack Open Graph Tags -->
<link rel="shortcut icon" type="image/x-icon" href="https://secure.gravatar.com/blavatar/bd4bda4207561b6998f10dec44b570f04ff4072b20f89162d525b186dfca3e49?s=32" sizes="16x16" />
<link rel="icon" type="image/x-icon" href="https://secure.gravatar.com/blavatar/bd4bda4207561b6998f10dec44b570f04ff4072b20f89162d525b186dfca3e49?s=32" sizes="16x16" />
<link rel="apple-touch-icon" href="https://secure.gravatar.com/blavatar/bd4bda4207561b6998f10dec44b570f04ff4072b20f89162d525b186dfca3e49?s=114" />
<link rel='openid.server' href='https://terrytao.wordpress.com/?openidserver=1' />
<link rel='openid.delegate' href='https://terrytao.wordpress.com/' />
<link rel="search" type="application/opensearchdescription+xml" href="https://terrytao.wordpress.com/osd.xml" title="What&#039;s new" />
<link rel="search" type="application/opensearchdescription+xml" href="https://s1.wp.com/opensearch.xml" title="WordPress.com" />
<style>.recentcomments a{display:inline !important;padding:0 !important;margin:0 !important;}</style>		<style type="text/css">
			.recentcomments a {
				display: inline !important;
				padding: 0 !important;
				margin: 0 !important;
			}

			table.recentcommentsavatartop img.avatar, table.recentcommentsavatarend img.avatar {
				border: 0px;
				margin: 0;
			}

			table.recentcommentsavatartop a, table.recentcommentsavatarend a {
				border: 0px !important;
				background-color: transparent !important;
			}

			td.recentcommentsavatarend, td.recentcommentsavatartop {
				padding: 0px 0px 1px 0px;
				margin: 0px;
			}

			td.recentcommentstextend {
				border: none !important;
				padding: 0px 0px 2px 10px;
			}

			.rtl td.recentcommentstextend {
				padding: 0px 10px 2px 0px;
			}

			td.recentcommentstexttop {
				border: none;
				padding: 0px 0px 0px 10px;
			}

			.rtl td.recentcommentstexttop {
				padding: 0px 10px 0px 0px;
			}
		</style>
					<link rel="stylesheet" id="custom-css-css" type="text/css" href="https://s0.wp.com/?custom-css=1&#038;csblog=3qzP&#038;cscache=6&#038;csrev=4" />
			<link crossorigin='anonymous' rel='stylesheet' id='all-css-0-4' href='/wp-content/mu-plugins/jetpack-plugin/moon/modules/widgets/top-posts/style.css?m=1753284714i&cssminify=yes' type='text/css' media='all' />

</head>

<body class="wp-singular post-template-default single single-post postid-17967 single-format-standard wp-theme-pubtarski center customizer-styles-applied jetpack-reblog-enabled"><div id="wrapper">

<div id="header">

		<div id="header-image">
		<a title="Return to front page" href="https://terrytao.wordpress.com/"><img alt="" src="https://terrytao.wordpress.com/wp-content/uploads/2020/03/cropped-covid-19-curves-graphic-social-v3.gif" /></a>	</div>
	
	<div id="title">
		<a title="Return to front page" href="https://terrytao.wordpress.com/"><span id="blog-title">What&#039;s new</span></a>		<p id="tagline">Updates on my research and expository papers, discussion of open problems, and other maths-related topics.  By Terence Tao</p>	</div>

	<div id="navigation">
		<ul id="nav-1">
	<li><a title="Return to front page" href="https://terrytao.wordpress.com/">Home</a></li>
	<li class="page_item page-item-2 page_item_has_children"><a href="https://terrytao.wordpress.com/about/">About</a></li>
<li class="page_item page-item-51 page_item_has_children"><a href="https://terrytao.wordpress.com/career-advice/">Career advice</a></li>
<li class="page_item page-item-78 page_item_has_children"><a href="https://terrytao.wordpress.com/advice-on-writing-papers/">On writing</a></li>
<li class="page_item page-item-134 page_item_has_children"><a href="https://terrytao.wordpress.com/books/">Books</a></li>
<li class="page_item page-item-14513"><a href="https://terrytao.wordpress.com/mastodon-posts/">Mastodon+</a></li>
<li class="page_item page-item-5886"><a href="https://terrytao.wordpress.com/applets/">Applets</a></li>
</ul>

		<ul id="nav-2">
			<li><a class="feed" title="Subscribe to the What&#039;s new feed" href="https://terrytao.wordpress.com/feed/">Subscribe to feed</a></li>
		</ul>
	</div>

</div>

<div id="content">
	
<div id="primary">



	<div class="entry">
	<div class="post-meta">
		<h1 class="post-title" id="post-17967">A digestion of the Jacobian conjecture&nbsp;counterexample</h1>
		<p class="post-metadata">21 July, 2026 in <a href="https://terrytao.wordpress.com/category/mathematics/mathag/" rel="category tag">math.AG</a> | Tags: <a href="https://terrytao.wordpress.com/tag/jacobian-conjecture/" rel="tag">Jacobian conjecture</a>, <a href="https://terrytao.wordpress.com/tag/polynomials/" rel="tag">polynomials</a> | by <a href="https://terrytao.wordpress.com/author/teorth/" rel="author">Terence Tao</a>		</p>
	</div>
	<div class="post-content">
		
<p>
 The notorious <a href="https://en.wikipedia.org/wiki/Jacobian_conjecture">Jacobian conjecture</a> can be formulated concretely over the complex numbers as follows.
</p><p>

</p><blockquote><b>Conjecture 1 (Jacobian Conjecture)</b>  Let <img src="https://s0.wp.com/latex.php?latex=%7BF%3A%7B%5Cbf+C%7D%5En+%5Crightarrow+%7B%5Cbf+C%7D%5En%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7BF%3A%7B%5Cbf+C%7D%5En+%5Crightarrow+%7B%5Cbf+C%7D%5En%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7BF%3A%7B%5Cbf+C%7D%5En+%5Crightarrow+%7B%5Cbf+C%7D%5En%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{F:{&#92;bf C}^n &#92;rightarrow {&#92;bf C}^n}" class="latex" /> be a polynomial map in <img src="https://s0.wp.com/latex.php?latex=%7Bn%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7Bn%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7Bn%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{n}" class="latex" /> complex variables, whose Jacobian <img src="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{&#92;mathrm{det} DF}" class="latex" /> is a non-zero constant. Then <img src="https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{F}" class="latex" /> is invertible (with polynomial inverse). </blockquote>

<p></p><p>


</p><p>
The condition that the Jacobian <img src="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{&#92;mathrm{det} DF}" class="latex" /> is non-zero is equivalent to <img src="https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{F}" class="latex" /> being locally invertible. (The implication of local invertibility from non-vanishing Jacobian follows from the inverse function theorem; the converse implication can be derived from the <a href="https://en.wikipedia.org/wiki/Weierstrass_preparation_theorem">Weierstrass preparation theorem</a>, but is omitted here.) Also, from the fundamental theorem of algebra, once the Jacobian polynomial <img src="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{&#92;mathrm{det} DF}" class="latex" /> is non-zero, it must be constant. So the hypothesis &#8220;Jacobian <img src="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{&#92;mathrm{det} DF}" class="latex" /> is a non-zero constant&#8221; can be replaced with &#8220;<img src="https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{F}" class="latex" /> is locally invertible&#8221;. So the Jacobian conjecture can be viewed as an assertion that local invertibility implies global invertibility. The complex numbers can be easily replaced with other fields of characteristic zero by the <a href="https://en.wikipedia.org/wiki/Algebraic_geometry_and_analytic_geometry#The_Lefschetz_principle">Lefschetz principle</a>, but I prefer to work in the concrete setting of the complex numbers.
</p><p>
Recently, it was <a href="https://www.newscientist.com/article/2580374-ais-solution-to-87-year-old-riddle-takes-mathematicians-by-surprise/">recently shown</a> (using the Fable AI) that the conjecture is false in three dimensions (and thus in higher dimensions as well):
</p><p>

</p><blockquote><b>Theorem 2 (Counterexample to conjecture)</b> <a name="jac1"></a> There exists a polynomial <img src="https://s0.wp.com/latex.php?latex=%7BF+%3A+%7B%5Cbf+C%7D%5E3+%5Crightarrow+%7B%5Cbf+C%7D%5E3%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7BF+%3A+%7B%5Cbf+C%7D%5E3+%5Crightarrow+%7B%5Cbf+C%7D%5E3%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7BF+%3A+%7B%5Cbf+C%7D%5E3+%5Crightarrow+%7B%5Cbf+C%7D%5E3%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{F : {&#92;bf C}^3 &#92;rightarrow {&#92;bf C}^3}" class="latex" /> which has non-zero constant Jacobian, but is not invertible. </blockquote>

<p></p><p>


</p><p>
The conjecture remains open in two dimensions, and is easy to establish in one dimension.
</p><p>
The example can be stated completely explicitly: one can take <a name="explicit-ex"></a></p><p align="center"><a name="explicit-ex"><img src="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%28z_1%2Cz_2%2Cz_3%29+%3D+%5CBig%28%281%2Bz_1+z_2%29%5E3+z_3+%2B+z_2%5E2+%281%2Bz_1z_2%29+%284%2B3z_1z_2%29%2C+%5C+%5C+%5C+%5C+%5C+%281%29&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%28z_1%2Cz_2%2Cz_3%29+%3D+%5CBig%28%281%2Bz_1+z_2%29%5E3+z_3+%2B+z_2%5E2+%281%2Bz_1z_2%29+%284%2B3z_1z_2%29%2C+%5C+%5C+%5C+%5C+%5C+%281%29&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%28z_1%2Cz_2%2Cz_3%29+%3D+%5CBig%28%281%2Bz_1+z_2%29%5E3+z_3+%2B+z_2%5E2+%281%2Bz_1z_2%29+%284%2B3z_1z_2%29%2C+%5C+%5C+%5C+%5C+%5C+%281%29&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="&#92;displaystyle  F(z_1,z_2,z_3) = &#92;Big((1+z_1 z_2)^3 z_3 + z_2^2 (1+z_1z_2) (4+3z_1z_2), &#92; &#92; &#92; &#92; &#92; (1)" class="latex" /></a></p><a name="explicit-ex">
</a> <p></p><p align="center"><img src="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++z_2+%2B+3+z_1+%281%2Bz_1z_2%29%5E2+z_3+%2B+3+z_1+z_2%5E2+%284%2B3z_1z_2%29%2C+&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++z_2+%2B+3+z_1+%281%2Bz_1z_2%29%5E2+z_3+%2B+3+z_1+z_2%5E2+%284%2B3z_1z_2%29%2C+&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++z_2+%2B+3+z_1+%281%2Bz_1z_2%29%5E2+z_3+%2B+3+z_1+z_2%5E2+%284%2B3z_1z_2%29%2C+&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="&#92;displaystyle  z_2 + 3 z_1 (1+z_1z_2)^2 z_3 + 3 z_1 z_2^2 (4+3z_1z_2), " class="latex" /></p>
 <p align="center"><img src="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle+2+z_1+-+3+z_1%5E2+z_2+-+z_1%5E3+z_3%5CBig%29&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle+2+z_1+-+3+z_1%5E2+z_2+-+z_1%5E3+z_3%5CBig%29&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%5Cdisplaystyle+2+z_1+-+3+z_1%5E2+z_2+-+z_1%5E3+z_3%5CBig%29&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="&#92;displaystyle 2 z_1 - 3 z_1^2 z_2 - z_1^3 z_3&#92;Big)" class="latex" /></p>
 and one can verify by a brief calculation that <p align="center"><img src="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%5Cmathrm%7Bdet%7D+DF+%3D+-2&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%5Cmathrm%7Bdet%7D+DF+%3D+-2&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%5Cmathrm%7Bdet%7D+DF+%3D+-2&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="&#92;displaystyle  &#92;mathrm{det} DF = -2" class="latex" /></p>
 and <p align="center"><img src="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%280%2C0%2C-1%2F4%29+%3D+F%281%2C-3%2F2%2C+13%2F2%29+%3D+F%28-1%2C3%2F2%2C13%2F2%29&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%280%2C0%2C-1%2F4%29+%3D+F%281%2C-3%2F2%2C+13%2F2%29+%3D+F%28-1%2C3%2F2%2C13%2F2%29&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++F%280%2C0%2C-1%2F4%29+%3D+F%281%2C-3%2F2%2C+13%2F2%29+%3D+F%28-1%2C3%2F2%2C13%2F2%29&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="&#92;displaystyle  F(0,0,-1/4) = F(1,-3/2, 13/2) = F(-1,3/2,13/2)" class="latex" /></p>
 <p align="center"><img src="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%3D+%28-1%2F4%2C0%2C0%29.&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%3D+%28-1%2F4%2C0%2C0%29.&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%5Cdisplaystyle++%3D+%28-1%2F4%2C0%2C0%29.&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="&#92;displaystyle  = (-1/4,0,0)." class="latex" /></p>
 While this is an extremely quick verification, the construction presented in this fashion appears like a massive miracle. The polynomial <img src="https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7BF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{F}" class="latex" /> has degree seven, so <em>a priori</em> the Jacobian <img src="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7B%5Cmathrm%7Bdet%7D+DF%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{&#92;mathrm{det} DF}" class="latex" /> ought to be a polynomial in three variables of degree as large as <img src="https://s0.wp.com/latex.php?latex=%7B3+%5Ctimes+6+%3D+18%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7B3+%5Ctimes+6+%3D+18%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7B3+%5Ctimes+6+%3D+18%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002&#038;zoom=4.5 4x" alt="{3 &#92;times 6 = 18}" class="latex" />, so the fact that all non-constant coefficients of this polynomial vanish looks like a massive cancellation involving <img src="https://s0.wp.com/latex.php?latex=%7B%5Cbinom%7B18%2B3%7D%7B3%7D-1+%3D+1329%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002" srcset="https://s0.wp.com/latex.php?latex=%7B%5Cbinom%7B18%2B3%7D%7B3%7D-1+%3D+1329%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038;c=20201002 1x, https://s0.wp.com/latex.php?latex=%7B%5Cbinom%7B18%2B3%7D%7B3%7D-1+%3D+1329%7D&#038;bg=ffffff&#038;fg=000000&#038;s=0&#038