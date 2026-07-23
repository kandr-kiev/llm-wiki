---
source_url: https://ohaodha.ie/blog/fretboard-memorisation-with-modular-arithmetic/
ingested: 2026-07-22
sha256: af8c2788b6e2cca78738d27c5a48c0375839d300df8b031ddd4c937e12ef1982
blog_source: Hacker News
---
<!doctype html><html lang=en-ie dir=ltr><head><meta charset=utf-8><meta name=viewport content="width=device-width"><link rel=stylesheet href=/css/syntax.css><title>Fretboard Memorisation with Modular Arithmetic | Ã hAoá¸a</title>
<link rel=stylesheet href=/css/main.min.d71ed76a886b96cd41fb2ee084299c40537beb13601792e84714b1ad6bb55873.css integrity="sha256-1x7Xaohrls1B+y7ghCmcQFN76xNgF5LoRxSxrWu1WHM=" crossorigin=anonymous><script src=/js/main.23cd0c7d837263b9eaeb96ee2d9ccfa2969daa3fa00fa1c1fe8701a9b87251a1.js integrity="sha256-I80MfYNyY7nq65buLZzPopadqj+gD6HB/ocBqbhyUaE=" crossorigin=anonymous></script><script id=MathJax-script async src=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js></script><script>MathJax={tex:{displayMath:[["\\[","\\]"],["$$","$$"]],inlineMath:[["\\(","\\)"],["$","$"]]},options:{enableMenu:!1}}</script></head><body><header><br><hr><h1 style=font-family:gadelica;font-weight:500>Ã hAoá¸a</h1><hr><nav class=navbar><ul style=display:flex;justify-content:space-between><li style=display:inline-block;margin-right:30pt><a href=/>Home</a></li><li style=display:inline-block;margin-right:30pt><a href=/gallery/>Gallery</a></li><li style=display:inline-block;margin-right:30pt><a aria-current=true class=ancestor href=/blog/>Blog</a></li><li style=display:inline-block;margin-right:30pt><a href=/tags/>Tags</a></li><li style=display:inline-block;margin-right:50pt><button class=theme-toggle id=theme-toggle title="Toggle dark theme">â¾</button></li></ul></nav><hr><script>const toggleButton=document.getElementById("theme-toggle"),body=document.body;toggleButton.addEventListener("click",()=>{body.classList.toggle("dark-theme"),toggleButton.innerText=body.classList.contains("dark-theme")?"â":"â¾",localStorage.setItem("theme",body.classList.contains("dark-theme")?"dark":"light")});const savedTheme=localStorage.getItem("theme");savedTheme==="dark"&&body.classList.add("dark-theme"),toggleButton.innerText=body.classList.contains("dark-theme")?"â":"â¾"</script><style>.navbar{word-break:normal;overflow-wrap:normal;white-space:nowrap}.theme-toggle{font-family:inherit;font-size:inherit;font-weight:700;background:0 0;border:none;color:none;text-decoration:underline;text-underline-offset:.18em}</style></header><main><h2 id=blogpost-title>Fretboard Memorisation with Modular Arithmetic</h2><time style=float:right;text-align:right datetime=2024-03-01T23:36:19+00:00>2024-03-01</time><br><details><summary><b>Table of Contents</b></summary><nav id=TableOfContents><ol><li><a href=#introduction>Introduction</a><ol><li><a href=#aside-what-is-modular-arithmetic>Aside: What is Modular Arithmetic?</a></li></ol></li><li><a href=#my-system>My System</a><ol><li><a href=#advantages-of-my-system>Advantages of My System</a></li><li><a href=#drawbacks-of-my-system>Drawbacks of My System</a></li></ol></li></ol></nav></details><h2 id=introduction>Introduction<a href=#introduction class=hanchor aria-label=Anchor>Â§</a></h2><p><span style=font-variant:small-caps;font-weight:700>Memorising</span> (or &ldquo;learning&rdquo;) the fretboard refers to when an individual learns which musical notes correspond to what
positions on the fretboard of their instrument, a skill that is useful for playing just about any instrument that
has frets.
In particular, &ldquo;learning the fretboard&rdquo; is a topic frequently discussed in guitar circles for its importance in
improvisation & soloing.
In general, the common approaches to learning the fretboard seem to consist of a combination of just committing it to
memory and using some tricks to help with that memorisation; however, I have a number of problems with this approach:</p><ol><li><strong>It&rsquo;s too much effort:</strong> I am far too lazy to memorise the note that corresponds to up to $24 \times 6 = 144$
positions on a 24-fret guitar (or $24 \times 5 = 120$ positions if you take account of the two $E$ strings
being identical except for their pitch).</li><li><strong>It doesn&rsquo;t translate to other tunings:</strong> it&rsquo;s all well & good memorising the note that corresponds to each
position in standard tuning, but your effort is rendered useless when you switch to a different tuning or a
different instrument.</li></ol><h3 id=aside-what-is-modular-arithmetic>Aside: What is Modular Arithmetic?<a href=#aside-what-is-modular-arithmetic class=hanchor aria-label=Anchor>Â§</a></h3><p>While I would encourage anyone not already familiar with modular arithmetic to read up on it in detail themselves, I&rsquo;ll
give a brief explanation here so that anyone can understand what I&rsquo;m talking about (a good overview can be found in the
book <em>Discrete Mathematics &ndash; An Open Introduction</em> by Oscar Levin
<a href=https://discrete.openmathbooks.org/dmoi3/sec_addtops-numbth.html#iyd>here</a>).
<strong>Modular arithmetic</strong> refers to number systems in which the values don&rsquo;t get higher and higher towards infinity, but
rather wrap around and start again from 0 once a certain maximum number called the <strong>modulus</strong> is reached.</p><p>Perhaps the most famous example of modular arithmetic is the 24-hour clock.
The 24-hour clock starts at 0, and goes up to 23 before starting at 0 again.
There is no way to exceed 23 on a 24-hour clock.
In this sense, the 24-hour clock is an arithmetic system <strong>modulo 24</strong>.
If an event start at 23:00 and takes 2 hours, we don&rsquo;t say that it finishes at &ldquo;25:00&rdquo;: instead, we say it finishes at
01:00 as $23 + 2 = 25 \equiv 1 \text{ mod } 24$ (25 is <em>congruent</em> to 1 modulo 24).</p><p>Modular arithmetic can also be thought of as dividing any given number by the modulus and getting the remainder.
For example, $30 \text{ mod } 24 \equiv 6 $ because $30 \div 24 = 1 \text{ remainder } 6.$</p><p>Incidentally, many resources refer to the 12-hour clock as a classic example of a system of modular arithmetic, but I think
that this is a poor example as the 12-hour clock starts at 1 and ends at 12, meaning that it&rsquo;s not quite modulo 12
(which starts at 0 and ends at 11) and also not quite modulo 13 (which start at 0 and ends at 12).</p><h2 id=my-system>My System<a href=#my-system class=hanchor aria-label=Anchor>Â§</a></h2><p>I realised when I was teaching myself guitar that the chromatic scale can be thought of as a system of modular
arithmetic modulo 12: there are 12 notes ($A$ through $G^\#$, including the sharps/flats).
If you assign each note a number starting with $A$ at 0 and ending with $G^\#$ at 11, you get a system of
modular arithmetic that corresponds perfectly to the frets on the $A$-string.
If you don&rsquo;t fret the string and pluck it, you get $A$, if you fret the string at the first fret and play it, you
get $A^\#$ (or $B^\flat$), et cetera.
If you fret the string at the 12<sup>th</sup> fret, you get $A$ again, and if you fret the string at the
13<sup>th</sup> fret, you get $A^\#$ again, in accordance with $12 \text{ mod } 12 \equiv 0$ and $13 \text{
mod } 12 \equiv 1.$
Hence, we already have a system for memorising all the notes on the $A$-string: it&rsquo;s just arithmetic modulo 12.
All we need to do is memorise a value for each note in the chromatic scale.
Then, to find out what note a certain fret corresponds to, we can just find its value modulo 12, and to find a certain
note on the string, we can just look at the frets at multiples of the value of the note.</p><table><thead><tr><th>$A$</th><th>$A^\#$ / $B^\flat$</th><th>$B$</th><th>$C$</th><th>$C^\#$ / $D^\flat$</th><th>$D$</th><th>$D^\#$ / $E^\flat$</th><th>$E$</th><th>$F$</th><th>$F^\#$ / $G^\flat$</th><th>$G$</th><th>$G^\#$ / $A^\flat$</th></tr></thead><tbody><tr><td>$0$</td><td>$1$</td><td>$2$</td><td>$3$</td><td>$4$</td><td>$5$</td><td>$6$</td><td>$7$</td><td>$8$</td><td>$9$</td><td>$10$</td><td>$11$</td></tr></tbody></table><p>This same system can actually be generalised to all the other strings on the guitar with little adaptation.
The only difference is that we need to remember at what number on the scale each string starts and add this to the
number of each fret on that string to get the integer value corresponding to the note at that fret.
Take for example one of the $E$ strings: this string is tuned to the note $E$ (which has value 7).
To find out what note is at the 5<sup>th</sup> fret of the $E$ string, we use the same approach as with the $A$
string, but add the value that the string starts at to the fret number before getting its value modulo 12:
$7 + 5 = 12 \text{ modulo } 12 \equiv 0$, indicating that the note at the 5<sup>th</sup> fret of the $E$ string
is an $A.$</p>$$
v \equiv r + f \text{ modulo } 12
$$<p>where $v$ is the value of the note at that fret, $r$ is the &ldquo;root value&rdquo; of the string (i.e., the value of the
note to which the string is tuned), and $f$ is the fret number.</p><p>This might appear quite complicated at first glance due to the formulae, but it&rsquo;s actually quite simple once you&rsquo;ve
memorised the values.
This system of fretboard memorisation can be generalised to any tuning, any number of strings, and any number of frets.
Furthermore, I would submit that this is actually also the most correct system, as it gets straight to the reasons <em>why</em>
a fret is a certain value: simply because of the number of increments it is from the note that the string is tuned to.</p><h3 id=advantages-of-my-system>Advantages of My System<a href=#advantages-of-my-system class=hanchor aria-label=Anchor>Â§</a></h3><ul><li>Requires only the memorisation of 12 key-value pairs, one for each of the musical notes, in contrast to the up to
144 positions that have to be memorised for the more conventional approach.</li><li>It&rsquo;s tuning-agnostic: you don&rsquo;t have to learn anything new to have the fretboard memorised in different tunings, you
just need to know the &ldquo;root value&rdquo; that each string is tuned to.</li><li>The number of strings don&rsquo;t matter: you don&rsquo;t have to learn anything new to have the fretboard memorised for a 6, 7,
8-string guitar or even a different instrument so long as it has frets at semi-tone intervals.</li><li>It could be adapted to a microtonal instrument so long as it has frets and that the intervals between the
micro-tones is consistent, although this would require memorising an entirely new set of key value pairs.</li></ul><h3 id=drawbacks-of-my-system>Drawbacks of My System<a href=#drawbacks-of-my-system class=hanchor aria-label=Anchor>Â§</a></h3><ul><li>It requires pre-existing knowledge of modular arithmetic and the ability to quickly do mental calculations modulo 12.
While this may seem overly-complicated to someone not familiar with modular arithmetic, modular arithmetic is
actually quite simple once you get your head around it, and is worth learning for its applications in mathematics
such as in encryption.</li><li>It still requires that you memorise 12 key-value pairs, one for each of the musical notes, although this is
considerably less memorisation that the conventional approach.</li><li>It is not applicable to fretless instruments, such as fretless guitars, cellos, violins, etc.</li></ul><p>While I&rsquo;m sure that I&rsquo;m not the first person in music history to think of this strategy, I have never seen it mentioned
anywhere online or in print, so I&rsquo;m sharing it here in the hope that it will be useful for others as it was for me.</p><hr><div id=tags><span>Tags:</span>
<a href=/tags/article/>Article</a> â 
<a href=/tags/music/>Music</a> â </div></main><footer><hr><div style=font-size:10pt><p style=text-align:center;font-variant:small-caps></p><p style=text-align:center>Copyright Â© 2024 AindrÃ©as Ã hAodha. Content licensed under <a href=https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en>CC BY-NC-SA 4.0</a>.
Code licensed under <a href=https://www.gnu.org/licenses/gpl-3.0.en.html>GPLv3</a>.</p>This site was last deployed using Hugo version <code style=color:inherit;font-size:8pt>0.141.0</code> on <code style=color:inherit;font-size:8pt>2026-07-22 23:27:47.849899826 +0100 IST m=+0.076199749</code>.</p></div></footer></body></html>