---
source_url: https://words.filippo.io/passkey-record/
ingested: 2026-07-21
sha256: 52544975d544d92396b287201f378c7454d348e2a77fa1fe026b101ca1db8a4c
blog_source: Hacker News
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://abyssdomain.expert/@filippo" rel="me">
    <link href="https://bsky.app/profile/filippo.abyssdomain.expert" rel="me">
    <link rel="alternate" type="application/rss+xml" href="https://words.filippo.io/rss/">
    <meta property="og:type" content="article">
    <meta name="fediverse:creator" content="@filippo@abyssdomain.expert">
    
    <title>Opaque, Interoperable Passkey Records (and a Go API)</title>
    <meta name="description" content="Passkey records are an interoperable format for WebAuthn credentials, similar to password hash strings. I propose a potential crypto/passkey Go API based on them.">
    <meta property="og:image" content="https://assets.buttondown.email/images/15df3c3e-98e0-486d-97e4-7542a638e7f4.jpeg?w=960&amp;fit=max">
    <meta property="article:published_time" content="2026-07-20T22:33:32.950000Z">
    <link rel="canonical" href="https://words.filippo.io/passkey-record/">

    <style>
        :root {
            font-family: Avenir, Montserrat, Corbel, 'URW Gothic', source-sans-pro, sans-serif;
            color-scheme: light dark;
        }
        p, li {
            line-height: 1.8em;
        }
        sub, sup {
            line-height: 0;
        }
        a {
            color: inherit;
        }
        header {
            margin: 4rem auto 0;
            max-width: 350px;
            padding: 0 10px;
        }
        main {
            width: auto;
            max-width: 700px;
            padding: 0 15px;
            margin: 5rem auto;
        }
        h1 {
            text-transform: uppercase;
            margin-top: 0.25em;
            font-size: 2em;
        }
        h2, h3, h4, h5, h6 {
            margin-top: 1.5em;
        }
        code, pre {
            color: Canvas;
            background-color: CanvasText;
            font-family: ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace;
            -webkit-font-smoothing: antialiased;
        }
        :not(pre) > code {
            font-size: 0.8em;
            padding: 4px 5px;
        }
        pre {
            padding: 1em;
            overflow-x: auto;
            line-height: 1.5em;
            font-size: 0.8em;
        }
		img {
			max-width: 100%;
			height: auto;
            margin: 0 auto;
            display: block;
		}
        li + li {
            margin-top: 0.5em;
        }
        .subscribe {
            border: 1px solid;
            padding: 0 1em;
            margin: 1em 0;
        }
        .subscribe p {
            text-align: center;
        }
        .subscribe form {
            display: flex;
            gap: 0.5em;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            margin: 1em 0;
        }
        .subscribe form input[type="email"] {
            padding: 0.3em 0.5em;
            font: inherit;
            flex: 1;
            min-width: 12em;
            max-width: 20em;
            border: 1px solid;
        }
        .subscribe form button {
            padding: 0.3em 0.8em;
            font: inherit;
            cursor: pointer;
            background-color: CanvasText;
            color: Canvas;
            border: 1px solid transparent;
        }
        .bsky-card {
            border: 1px solid;
            border-radius: 8px;
            padding: 1em;
            margin: 1em auto;
            max-width: 400px;
            font-size: 0.9em;
        }
        .bsky-head {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .bsky-profile {
            display: flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
            color: inherit;
        }
        .bsky-avatar {
            width: 42px;
            height: 42px;
            border-radius: 50%;
        }
        .bsky-name {
            font-weight: 600;
        }
        .bsky-handle {
            color: gray;
            font-size: 0.85em;
        }
        .bsky-logo {
            color: #1185fe;
        }
        .bsky-text {
            white-space: pre-line;
            line-height: initial;
        }
        .bsky-link {
            display: block;
            border: 1px solid;
            border-radius: 6px;
            padding: 0.6em 0.8em;
            text-decoration: none;
            margin: 1em 0;
        }
        .bsky-link-title {
            font-weight: 600;
            font-size: 0.9em;
        }
        .bsky-link-desc {
            font-size: 0.85em;
            color: gray;
            margin-top: 2px;
        }
        .bsky-link-domain {
            font-size: 0.8em;
            color: gray;
            margin-top: 4px;
        }
        .bsky-foot {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            font-size: 0.85em;
            color: gray;
        }
        .bsky-foot a {
            color: inherit;
            text-decoration: none;
        }
    </style>

    <script defer data-domain="blog.filippo.io" src="https://filippo.io/js/script.js"></script>
    <script>
        window.plausible = window.plausible || function () {
            (window.plausible.q = window.plausible.q || []).push(arguments)
        }

        document.addEventListener("DOMContentLoaded", (event) => {
            let trigger = document.createElement("div");
            let footnotes = document.querySelector(".footnotes");
            if (footnotes) {
                footnotes.before(trigger);
            } else {
                document.querySelector("article").after(trigger);
            }

            new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (!entry.isIntersecting) return;
                    observer.disconnect();
                    plausible("Finished");
                })
            }).observe(trigger);

            new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) return;
                    observer.disconnect();
                    plausible("Scrolled");
                })
            }).observe(document.querySelector("h1"));
        });
    </script>
</head>
<body>

<header>
    <a href="https://filippo.io"><picture>
        <source srcset="https://assets.buttondown.email/images/72e03d2e-fcb2-4893-ab9c-8f561c0b07c7.png" media="(prefers-color-scheme: dark)">
        <img src="https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png" alt="Filippo Valsorda">
    </picture></a>
</header>

<main>
    <article>
        <time datetime="2026-07-20">
            20 Jul 2026</time>
        <h1>Opaque, Interoperable Passkey Records (and a Go API)</h1>
        <section>
            <!-- buttondown-editor-mode: plaintext -->
<p>Passkeys are the most important thing happening in information security right now because they are the only principled solution to the overwhelming effectiveness of phishing attacks. Just like memory safety is the only principled solution to memory corruption attacks.</p>
<p>Unfortunately, implementing them on the server side can appear more complex than using password hashes. Part of this is unavoidable because passkeys require interaction with the browser to get their phishing resistance properties. Part of it, however, could be abstracted away a little more effectively by defining interoperable passkey record encodings.</p>
<p>The WebAuthn specification <a href="https://www.w3.org/TR/webauthn-3/#reg-ceremony-create-credential-record">defines</a> a <em>credential record</em> as an abstract concept with a number of components such as <code>type</code>, <code>id</code>, <code>publicKey</code>, <code>backupState</code>, <code>transports</code>, and other flags. Google <a href="https://developers.google.com/identity/passkeys/developer-guides/server-registration#store_the_public_key">recommends</a> a database table with a Credential ID primary key, and <code>public_key</code>, <code>backed_up</code>, and <code>transports</code> columns. Adam Langley’s stellar <a href="https://www.imperialviolet.org/tourofwebauthn/tourofwebauthn.html#the-server-side">Tour of WebAuthn</a> similarly recommends a <code>cred_id</code> primary key, and separate <code>public_key_spki</code> and <code>backed_up</code> columns.</p>
<p>All guidance recommends using libraries to handle WebAuthn authentication, but that still leaves applications with a potentially non-interoperable database schema. It might also be impractical to defer the whole authentication flow and database interaction to a library or framework.</p>
<p>Interoperable, well-specified passkey records that the application can handle as opaque strings, like password hashes, can be a middle-ground abstraction layer.</p>
<p><a href="https://github.com/C2SP/C2SP/blob/push-oxkkyrwpqxot/passkey-record.md">c2sp.org/passkey-record</a> is a specification proposal which borrows the syntax of <a href="https://c2sp.org/phc-strings">Password Hashing Competition (PHC) Strings</a> and reuses the existing authenticator data encoding for the bulk of the work. A record looks like this:</p>
<pre><code>$webauthn$v=1$transports=hybrid+internal$&lt;base64 authenticator data&gt;
</code></pre>
<p>The payload is the authenticator data, a CTAP2 CBOR encoding of most of the credential record fields that is already <a href="https://www.w3.org/TR/webauthn-3/#sctn-authenticator-data">specified by WebAuthn</a> and included in the JSON encoding of an <a href="https://developer.mozilla.org/en-US/docs/Web/API/AuthenticatorAttestationResponse">AuthenticatorAttestationResponse</a> (which is the return type of <a href="https://developer.mozilla.org/en-US/docs/Web/API/CredentialsContainer/create"><code>navigator.credentials.create()</code></a> even if attestation is not in use). Transports are the only missing field, and they are stored as PHC parameters.</p>
<p>The application is then only in charge of keeping track of what passkey records are associated with a user account, which is a task that is familiar to web developers because it is not dissimilar to implementing password authentication (except there are multiple passkeys per account). These opaque strings can be passed to a library to verify the login assertion (or to generate a registration request with the appropriate <code>excludedCredentials</code>).</p>
<p>With a well-specified interoperable storage format, it will hopefully be possible to switch passkey library (or even backend language) while preserving a credentials database.</p>
<h2 id="other-fields-you-might-want-to-store">Other fields you might want to store</h2>
<p>Along with the passkey record, applications might still wish to store metadata fields like a user-selected nickname and creation and last use timestamps, to provide pretty passkey management UIs. None of these require any special treatment by the WebAuthn library.</p>
<p>The one exception is the backed up state flag. Passkeys report to the server whether they are backed up (e.g. to iCloud Keychain or a Google account), and servers can use that signal to suggest removing a password from an account. This flag can change across logins, while the passkey record is immutable, so it would have to be stored separately and updated on every login. I think this logic is overrated for the average website, which will keep supporting email password resets anyway.</p>
<h2 id="a-potential-cryptopasskey-api">A potential crypto/passkey API</h2>
<p>Building on top of these passkey records, I drafted <a href="https://godoc-play.exe.xyz/chibklhpf6nn">a potential <code>crypto/passkey</code> stateless Go package API</a>.</p>
<p>The registration flow is</p>
<ol>
<li>call <a href="https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.NewRegistration"><code>RelyingParty.NewRegistration</code></a> with the logged-in (or otherwise identified) user details and any existing passkey records</li>
<li>pass the returned JSON to <code>parseCreationOptionsFromJSON()</code> and then to <code>navigator.credentials.create()</code></li>
<li>pass the returned JSON-encoded PublicKeyCredential to <a href="https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.Register"><code>RelyingParty.Register</code></a></li>
<li>store the returned passkey record in the database</li>
</ol>
<p>The login flow is</p>
<ol>
<li>call <a href="https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.NewLogin"><code>RelyingParty.NewLogin</code></a> while generating the log-in page</li>
<li>store the returned request in a key-value cache with a short TTL, under <a href="https://godoc-play.exe.xyz/chibklhpf6nn#RequestID"><code>RequestID(request)</code></a>, and pass the returned JSON to <code>parseRequestOptionsFromJSON()</code> and then to <code>navigator.credentials.get()</code></li>
<li>pass the returned JSON-encoded PublicKeyCredential to <a href="https://godoc-play.exe.xyz/chibklhpf6nn#Inspect"><code>Inspect</code></a>, and use the returned requestID to retrieve the request from the key-value cache and use the returned userID to retrieve the passkey records from the database</li>
<li>pass the JSON PublicKeyCredential, the request, and the passkey records to <a href="https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.Login"><code>RelyingParty.Login</code></a></li>
</ol>
<p>The application is in charge of</p>
<ul>
<li>associating an opaque, permanent, privacy-preserving user ID with each user;</li>
<li>storing passkey records associated with a user; and</li>
<li>caching request challenges produced by <code>RelyingParty.NewLogin</code>.</li>
</ul>
<p>The library provides JSON values that can be passed straight to <a href="https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredential/parseCreationOptionsFromJSON_static"><code>parseCreationOptionsFromJSON()</code></a> and <a href="https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredential/parseRequestOptionsFromJSON_static"><code>parseRequestOptionsFromJSON()</code></a>, and accepts JSON values returned by <a href="https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredential/toJSON">calling <code>JSON.stringify()</code> on a PublicKeyCredential</a>.</p>
<p>This is optimized for the discoverable credential flow (a.k.a. passkeys, where the authenticator stores and provides to the server the user ID) but the <a href="https://godoc-play.exe.xyz/chibklhpf6nn#RelyingParty.NewLoginForUser"><code>RelyingParty.NewLoginForUser</code></a> method can also be used for second-factor flows or re-authentication prompts. The API works for both modal and conditional UI (autofill) flows.</p>
<p>There are a few helpers to extract information from the passkey record (<a href="https://godoc-play.exe.xyz/chibklhpf6nn#AAGUID"><code>AAGUID</code></a>, <a href="https://godoc-play.exe.xyz/chibklhpf6nn#BackedUp"><code>BackedUp</code></a>) and from the JSON-encoded PublicKeyCredential (<a href="https://godoc-play.exe.xyz/chibklhpf6nn#ResponseBackedUp"><code>ResponseBackedUp</code></a>).</p>
<p>Currently, there is no implementation; I would like to get feedback on the <a href="https://github.com/C2SP/C2SP/blob/push-oxkkyrwpqxot/passkey-record.md">passkey record format</a> and on <a href="https://godoc-play.exe.xyz/chibklhpf6nn">the Go API</a>, before potentially making a proposal for Go 1.28.</p>
<h2 id="on-duplicate-credential-ids">On duplicate Credential IDs</h2>
<p>One thing you can’t do with this storage model is ensure that different accounts don’t share passkeys with the same Credential ID, which the spec says you SHOULD do.</p>
<p>The reason for that check is avoiding attacks where you look up a credential by its ID and land at the wrong public key or user ID because the attacker intentionally injected a colliding Credential ID through their own account.</p>
<p>This attack simply can’t happen if you don’t have a Credential ID index in the first place! The index is only needed to mitigate an attack introduced by the existence of the index.</p>
<p>Login attempts carry the user ID, and if you use that to look up the user’s passkey records to verify the login against, it doesn’t matter if some <em>other</em> user has a passkey with the same Credential ID, just like it doesn’t matter if two users share a password.</p>
<p>Don’t let the attacker dictate your PRIMARY KEY and you won’t have PRIMARY KEY collision attacks.</p>
<p>For more Go API previews, follow me on Bluesky at <a href="https://bsky.app/profile/filippo.abyssdomain.expert">@filippo.abyssdomain.expert</a> or on Mastodon at <a href="https://abyssdomain.expert/@filippo">@filippo@abyssdomain.expert</a>.</p>
<h2 id="the-picture">The picture</h2>
<p>More from this year&rsquo;s <a href="https://www.centopassi.net/">CENTOPASSI</a> (a GPS-tracked motorcycle competition involving careful planning, 100 coordinates, and 1700 km of secondary roads over three and a half days). Here&rsquo;s a glimpse of Castel del Monte (AQ), after climbing down from a deserted and still snowy Campo Imperatore.</p>
<p><img alt="A medieval town is seen from above, framed by trees. In the distance, woods, hills, and then a snow-streaked peak. The sky is grey and overcast." src="https://assets.buttondown.email/images/15df3c3e-98e0-486d-97e4-7542a638e7f4.jpeg?w=960&amp;fit=max" /></p>
<p>My work is made possible by <a href="https://geomys.org">Geomys</a>, an organization of professional Go maintainers, which is funded by <a href="https://www.avalabs.org/">Ava Labs</a>, <a href="https://goteleport.com/">Teleport</a>, <a href="https://www.datadoghq.com/">Datadog</a>, <a href="https://tailscale.com/">Tailscale</a>, and <a href="https://sentry.io/">Sentry</a>. Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in the <a href="https://words.filippo.io/geomys">Geomys announcement</a>.)
Here are a few words from some of them!</p>
<p>Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing. <a href="https://goteleport.com/platform/identity/?utm=filippo">Teleport Identity</a> is designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.</p>
<p>Ava Labs — We at <a href="https://www.avalabs.org">Ava Labs</a>, maintainer of <a href="https://github.com/ava-labs/avalanchego">AvalancheGo</a> (the most widely used client for interacting with the <a href="https://www.avax.network">Avalanche Network</a>), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.</p>
        </section>
    </article>
    <aside class="subscribe">
        <form action="https://buttondown.com/api/emails/embed-subscribe/cryptography-dispatches" method="post">
            <input type="email" name="email" id="bd-email" placeholder="alice@example.com" autocomplete="email" required>
            <input type="hidden" value="1" name="embed">
            <button type="submit">Subscribe</button>
        </form>
        <p>
            <a href="https://words.filippo.io/rss/">Feed</a>&nbsp;📡&ensp;|&ensp;<a href="https://bsky.app/profile/filippo.abyssdomain.expert" rel="me">Bluesky</a>&nbsp;🦋&ensp;|&ensp;<a href="https://abyssdomain.expert/@filippo" rel="me">Mastodon</a>&nbsp;🐘
        </p>
    </aside>
    <aside class="bsky">
        <div class="bsky-card">
<div class="bsky-head">
<a href="https://bsky.app/profile/filippo.abyssdomain.expert" class="bsky-profile">
<img src="https://cdn.bsky.app/img/avatar/plain/did:plc:x2nsupeeo52oznrmplwapppl/bafkreifth4anopszp3maih7b3ople7tj77tirmpgmiu2vinou4pjhnewo4" class="bsky-avatar" alt="">
<div><div class="bsky-name">Filippo Valsorda</div>
<div class="bsky-handle">@filippo.abyssdomain.expert</div></div>
</a>
<a href="https://bsky.app/profile/did:plc:x2nsupeeo52oznrmplwapppl/post/3mr4gv7zs222d" aria-label="View on Bluesky" class="bsky-logo"><svg width="32" height="32" viewBox="0 0 16 16" fill="currentColor"><path d="M3.468 1.948C5.303 3.325 7.276 6.118 8 7.616c.725-1.498 2.698-4.29 4.532-5.668C13.855.955 16 .186 16 2.632c0 .489-.28 4.105-.444 4.692-.572 2.04-2.653 2.561-4.504 2.246 3.236.551 4.06 2.375 2.281 4.2-3.376 3.464-4.852-.87-5.23-1.98-.07-.204-.103-.3-.103-.218 0-.081-.033.014-.102.218-.379 1.11-1.855 5.444-5.231 1.98-1.778-1.825-.955-3.65 2.28-4.2-1.85.315-3.932-.205-4.503-2.246C.28 6.737 0 3.12 0 2.632 0 .186 2.145.955 3.468 1.948"/></svg></a>
</div>
<p class="bsky-text">Passkeys can be stored just like password hashes!

I&#39;m proposing an interoperable $webauthn$v=1$… format, and a Go API that uses these passkey records for authentication.

I&#39;m looking for feedback before proposing this as crypto/passkey for Go 1.28!</p>
<a href="https://words.filippo.io/passkey-record/" class="bsky-link">
<div class="bsky-link-title">Opaque, Interoperable Passkey Records (and a Go API)</div>
<div class="bsky-link-desc">Passkey records are an interoperable format for WebAuthn credentials, similar to password hash strings. I propose a potential crypto/passkey Go API based on them.</div>
<div class="bsky-link-domain">words.filippo.io</div>
</a>
<div class="bsky-foot">
<a href="https://bsky.app/profile/did:plc:x2nsupeeo52oznrmplwapppl/post/3mr4gv7zs222d"><span>Jul 20, 2026 · 73 ❤️ · 12 🔁</span></a>
<a href="https://bsky.app/profile/did:plc:x2nsupeeo52oznrmplwapppl/post/3mr4gv7zs222d">Read 4 replies on Bluesky →</a>
</div>
</div>

    </aside>
    <script>
        const h2first = document.querySelector("article h2:first-of-type")
        h2first.parentElement.insertBefore(document.getElementsByClassName("subscribe")[0].cloneNode(true), h2first)
        const h2last = document.querySelector("h2#the-picture")
        if (h2last) h2last.parentElement.insertBefore(document.getElementsByClassName("bsky")[0], h2last)
        if (h2last && h2last != h2first) h2last.parentElement.insertBefore(document.getElementsByClassName("subscribe")[0].cloneNode(true), h2last)
    </script>
    
