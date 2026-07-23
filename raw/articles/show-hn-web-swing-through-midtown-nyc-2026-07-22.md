---
source_url: https://www.swingnyc.com/
ingested: 2026-07-22
sha256: b1684e9fc57fe55f4a3eb9e067a63650acd1aa24b08f533a36cc971df70a0420
blog_source: Hacker News
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>SWING NYC</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🕸️</text></svg>" />
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { width: 100%; height: 100%; overflow: hidden; background: #0b0e14; touch-action: none; overscroll-behavior: none; }
    body { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; color: #e8ecf1; }
    #c { display: block; width: 100%; height: 100%; }
    #overlay {
      position: fixed; inset: 0; display: flex; flex-direction: column;
      align-items: center; justify-content: center; gap: 20px;
      background: radial-gradient(ellipse at center, rgba(8,11,18,0.18) 0%, rgba(8,11,18,0.62) 100%);
      cursor: pointer; user-select: none; text-align: center; z-index: 10;
    }
    #overlay h1 {
      font-size: 58px; letter-spacing: 10px; font-weight: 800;
      color: #fff; text-shadow: 0 4px 28px rgba(0,0,0,0.75), 0 1px 0 rgba(0,0,0,0.5);
    }
    #overlay h1 span {
      color: #e63946;
      text-shadow: 0 4px 28px rgba(230,57,70,0.45), 0 1px 0 rgba(0,0,0,0.5);
    }
    #overlay .sub { font-size: 13px; color: #cfd8e3; letter-spacing: 3px; text-shadow: 0 2px 8px rgba(0,0,0,0.8); }
    #overlay .controls {
      display: grid; grid-template-columns: auto auto; gap: 11px 18px;
      align-items: center; text-align: left;
      font-size: 13px; color: #dfe6ee;
      background: rgba(9, 13, 21, 0.72); padding: 22px 30px; border-radius: 14px;
      border: 1px solid rgba(255,255,255,0.09);
      box-shadow: 0 12px 40px rgba(0,0,0,0.45);
      backdrop-filter: blur(6px);
    }
    #overlay .controls .keys { justify-self: end; white-space: nowrap; }
    #overlay .controls .desc b { color: #ffd166; font-weight: 600; }
    kbd {
      display: inline-block; min-width: 17px; padding: 4px 9px 3px;
      font-family: inherit; font-size: 12px; font-weight: 700; text-align: center;
      color: #f2f5f9; letter-spacing: 0.5px;
      background: linear-gradient(180deg, #313b4e 0%, #232b3a 100%);
      border: 1px solid #4d5a70; border-bottom-width: 3px;
      border-radius: 7px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.09);
    }
    kbd.mouse { background: linear-gradient(180deg, #5c2530 0%, #401821 100%); border-color: #8a3a47; }
    #overlay .cta {
      font-size: 16px; letter-spacing: 4px; color: #fff; font-weight: 700;
      text-shadow: 0 0 18px rgba(230,57,70,0.8), 0 2px 8px rgba(0,0,0,0.8);
      animation: pulse 1.6s ease-in-out infinite;
    }
    #overlay .credit { font-size: 10px; color: #8b96a5; letter-spacing: 2px; text-shadow: 0 1px 6px rgba(0,0,0,0.8); }
    @keyframes pulse { 50% { opacity: 0.4; } }

    /* Touch controls (shown only on coarse-pointer devices while playing) */
    #touchui, #btnPause { display: none; }
    body.touch.playing #touchui { display: block; }
    body.touch.playing #btnPause { display: flex; }
    #joyBase {
      position: fixed; left: 28px; bottom: 32px; width: 118px; height: 118px;
      border-radius: 50%; z-index: 6;
      background: rgba(255,255,255,0.06); border: 2px solid rgba(255,255,255,0.2);
    }
    #joyKnob {
      position: absolute; left: 50%; top: 50%; width: 54px; height: 54px; margin: -27px;
      border-radius: 50%; background: rgba(255,255,255,0.3);
      border: 1px solid rgba(255,255,255,0.4);
    }
    .tbtn {
      position: fixed; z-index: 6; display: flex; align-items: center; justify-content: center;
      border-radius: 50%; background: rgba(18,24,36,0.55);
      border: 2px solid rgba(255,255,255,0.24); color: #fff;
      font-weight: 700; letter-spacing: 1px;
      user-select: none; -webkit-user-select: none; -webkit-tap-highlight-color: transparent;
    }
    .tbtn.held { background: rgba(230,57,70,0.5); border-color: rgba(230,57,70,0.8); }
    #btnWeb { right: 26px; bottom: 34px; width: 98px; height: 98px; font-size: 42px; border-color: rgba(230,57,70,0.6); }
    #btnJump { right: 140px; bottom: 104px; width: 66px; height: 66px; font-size: 13px; }
    #btnDive { right: 150px; bottom: 28px; width: 58px; height: 58px; font-size: 12px; }
    #btnPause {
      position: fixed; top: 16px; right: 16px; width: 42px; height: 42px; z-index: 6;
      align-items: center; justify-content: center; border-radius: 10px;
      background: rgba(18,24,36,0.55); border: 1px solid rgba(255,255,255,0.2);
      color: #fff; font-size: 13px;
      -webkit-tap-highlight-color: transparent;
    }
    /* On touch, the web button owns the bottom-right corner; stack the
       readouts on the left instead */
    body.touch #speed { right: auto; left: 24px; bottom: 44px; text-align: left; font-size: 24px; }
    body.touch #alt { bottom: 20px; left: 24px; }
    body.touch #joyBase { bottom: 90px; }
    #dot {
      position: fixed; left: 50%; top: 50%; width: 5px; height: 5px; margin: -2.5px;
      border-radius: 50%; background: rgba(255,255,255,0.85); z-index: 5;
      box-shadow: 0 0 6px rgba(0,0,0,0.8); display: none;
    }
    #dot.webbed { background: #e63946; box-shadow: 0 0 10px rgba(230,57,70,0.9); }
    #webtarget {
      position: fixed; width: 26px; height: 26px; margin: -13px;
      border: 3px solid rgba(255, 209, 102, 0.95); border-radius: 50%;
      box-shadow: 0 0 10px rgba(255, 190, 70, 0.55), 0 0 4px rgba(0,0,0,0.6);
      display: none; z-index: 5; pointer-events: none;
    }
    #webtarget::after {
      content: ''; position: absolute; left: 50%; top: 50%;
      width: 5px; height: 5px; margin: -2.5px;
      background: rgba(255, 209, 102, 0.95); border-radius: 50%;
    }
    /* Arrow pointing off-screen toward the anchor; shown only in edge mode */
    #webtarget::before {
      content: ''; position: absolute; left: 50%; top: -17px; margin-left: -7px;
      border: 7px solid transparent;
      border-bottom: 11px solid rgba(255, 209, 102, 0.95);
      display: none;
    }
    #webtarget.edge {
      transform: rotate(var(--ang, 0deg)) scale(1.6);
      animation: wtpulse 0.9s ease-in-out infinite;
    }
    #webtarget.edge::before { display: block; }
    @keyframes wtpulse { 50% { opacity: 0.55; } }
    #speed {
      position: fixed; right: 22px; bottom: 18px; z-index: 5; text-align: right;
      font-size: 30px; font-weight: 700; color: #fff;
      text-shadow: 0 2px 10px rgba(0,0,0,0.7); display: none;
    }
    #speed small { display: block; font-size: 11px; font-weight: 400; color: #aeb9c6; letter-spacing: 2px; }
    #alt {
      position: fixed; left: 22px; bottom: 18px; z-index: 5;
      font-size: 14px; color: #cdd6e0; text-shadow: 0 2px 8px rgba(0,0,0,0.7); display: none;
    }
  </style>
  <script type="module" crossorigin src="/assets/index-Bnkelmpd.js"></script>
</head>
<body>
  <canvas id="c"></canvas>
  <div id="dot"></div>
  <div id="webtarget"></div>
  <div id="speed">0<small>MPH</small></div>
  <div id="alt"></div>
  <div id="overlay">
    <h1>SWING <span>NYC</span></h1>
    <div class="sub" id="status">GENERATING VOXEL MANHATTAN…</div>
    <div class="controls" id="controls" style="display:none">
      <span class="keys"><kbd class="mouse">LEFT MOUSE</kbd></span>
      <span class="desc"><b>hold</b> to web-swing · <b>release</b> at the top of the arc</span>
      <span class="keys"><kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd></span>
      <span class="desc">steer on the ground and in the air</span>
      <span class="keys"><kbd>SPACE</kbd></span>
      <span class="desc">tap to jump · <b>hold &amp; release</b> for a SUPER JUMP</span>
      <span class="keys"><kbd>SPACE</kbd> <span style="color:#8b96a5">in air</span></span>
      <span class="desc"><b>air dash</b> toward held direction (one per swing) · hold to web</span>
      <span class="keys"><kbd>SHIFT</kbd></span>
      <span class="desc">dive — trade altitude for speed</span>
      <span class="keys"><kbd>R</kbd></span>
      <span class="desc">respawn on the rooftop</span>
    </div>
    <div class="controls" id="controlsTouch" style="display:none">
      <span class="keys"><kbd class="mouse">🕸</kbd></span>
      <span class="desc"><b>hold</b> to web-swing · <b>release</b> at the top of the arc</span>
      <span class="keys"><kbd>STICK</kbd></span>
      <span class="desc">move · drag the right side of the screen for camera</span>
      <span class="keys"><kbd>JUMP</kbd></span>
      <span class="desc">tap to jump / <b>air dash</b> · hold &amp; release for SUPER JUMP</span>
      <span class="keys"><kbd>DIVE</kbd></span>
      <span class="desc">hold to dive for speed</span>
    </div>
    <div class="cta" id="cta" style="display:none">CLICK TO SWING</div>
    <div class="credit" id="credit" style="display:none">MUSIC — “POWERUP!” BY JEREMY BLAKE</div>
  </div>
  <div id="touchui">
    <div id="joyBase"><div id="joyKnob"></div></div>
    <div class="tbtn" id="btnWeb">🕸</div>
    <div class="tbtn" id="btnJump">JUMP</div>
    <div class="tbtn" id="btnDive">DIVE</div>
  </div>
  <div id="btnPause">❚❚</div>
  <script>
    // Google Analytics — paste your GA4 measurement ID (e.g. 'G-ABC123XYZ')
    // and analytics activates; empty string = no-op.
    var GA_ID = 'G-RP3VWPVC8M';
    if (GA_ID) {
      var s = document.createElement('script');
      s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { dataLayer.push(arguments); };
      gtag('js', new Date());
      gtag('config', GA_ID);
      // Game events: play session starts (pointer lock)
      document.addEventListener('pointerlockchange', function () {
        if (document.pointerLockElement) gtag('event', 'play_start');
      });
    }
  </script>
</body>
</html>
