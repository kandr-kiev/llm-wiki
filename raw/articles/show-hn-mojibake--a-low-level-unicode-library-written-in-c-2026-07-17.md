---
source_url: https://mojibake.zaerl.com/
ingested: 2026-07-17
sha256: ad13847f493d6e2e717c029ceb7bc0834d7704f47b1b7556a2bae8e93ab5c369
blog_source: Hacker News
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light dark">
    <meta name="theme-color" content="#0d9488">
    <meta name="description"
        content="Mojibake is a fast, self-contained Unicode 17 library for C11 and C++17.">
    <title>Mojibake â Unicode 17 for C</title>
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="stylesheet" type="text/css" href="highlight-light.css">
    <link rel="stylesheet" type="text/css" href="highlight-dark.css" media="(prefers-color-scheme: dark)">
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <a class="skip-link" href="#main">Skip to content</a>
    <header class="site-header">
        <div class="site-header-inner">
            <a class="brand" href="#top" aria-label="Mojibake home">
                <span class="brand-mark" aria-hidden="true">å­</span>
                <span>Mojibake</span>
                <span class="version-badge">v0.2.7</span>
            </a>
            <nav class="global-nav" aria-label="Global navigation">
                <a href="https://github.com/zaerl/mojibake/blob/main/API.md">API.md</a>
                <a href="https://github.com/zaerl/mojibake">GitHub</a>
            </nav>
            <button class="sidebar-toggle" id="sidebar-toggle" type="button"
                aria-controls="api-sidebar" aria-expanded="false">
                <span aria-hidden="true"></span>
                <span class="visually-hidden">Open navigation</span>
            </button>
        </div>
    </header>
    <div class="site-layout" id="top">
        <aside class="sidebar" id="api-sidebar" aria-label="Documentation navigation">
            <div class="sidebar-inner">
                <nav class="page-navigation" aria-label="On this page">
                    <p class="sidebar-heading">Documentation</p>
                    <a href="#overview">Overview</a>
                    <a href="#guide">Guide</a>
                    <a href="#playground">WASM playground</a>
                    <a href="#api-reference">API reference</a>
                </nav>
                <div class="sidebar-api-heading">
                    <p class="sidebar-heading">C API</p>
                    <span>Browse by section</span>
                </div>
                <label class="visually-hidden" for="api-filter">Filter API functions</label>
                <div class="api-filter-wrap">
                    <span class="search-icon" aria-hidden="true"></span>
                    <input id="api-filter" class="api-filter" type="search"
                        placeholder="Filter functionsâ¦" autocomplete="off">
                </div>
                <p class="filter-status" id="api-filter-status" role="status"
                    aria-live="polite"></p>
                <nav id="api-navigation" aria-label="API reference">
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Text transformation</span>
          <span class="sidebar-count" aria-label="9 functions">9</span>
        </summary>
        <ul>
          <li><a href="#mjb_normalize" data-function-link data-search="mjb_normalize normalize a string to nfc/nfkc/nfd/nfkd form."><code>mjb_normalize</code></a></li>
          <li><a href="#mjb_string_filter" data-function-link data-search="mjb_string_filter filter a string with the selected mjb_filter flags."><code>mjb_string_filter</code></a></li>
          <li><a href="#mjb_nfkc_casefold" data-function-link data-search="mjb_nfkc_casefold apply the unicode nfkc_casefold transform to a string."><code>mjb_nfkc_casefold</code></a></li>
          <li><a href="#mjb_codepoint_encode" data-function-link data-search="mjb_codepoint_encode encode a codepoint to a string."><code>mjb_codepoint_encode</code></a></li>
          <li><a href="#mjb_string_convert_encoding" data-function-link data-search="mjb_string_convert_encoding convert from one encoding to another."><code>mjb_string_convert_encoding</code></a></li>
          <li><a href="#mjb_case" data-function-link data-search="mjb_case change string case."><code>mjb_case</code></a></li>
          <li><a href="#mjb_codepoint_to_lowercase" data-function-link data-search="mjb_codepoint_to_lowercase return the codepoint lowercase codepoint."><code>mjb_codepoint_to_lowercase</code></a></li>
          <li><a href="#mjb_codepoint_to_uppercase" data-function-link data-search="mjb_codepoint_to_uppercase return the codepoint uppercase codepoint."><code>mjb_codepoint_to_uppercase</code></a></li>
          <li><a href="#mjb_codepoint_to_titlecase" data-function-link data-search="mjb_codepoint_to_titlecase return the codepoint titlecase codepoint."><code>mjb_codepoint_to_titlecase</code></a></li>
        </ul>
      </details>
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Text analysis</span>
          <span class="sidebar-count" aria-label="31 functions">31</span>
        </summary>
        <ul>
          <li><a href="#mjb_codepoint_character" data-function-link data-search="mjb_codepoint_character return the codepoint character."><code>mjb_codepoint_character</code></a></li>
          <li><a href="#mjb_string_is_normalized" data-function-link data-search="mjb_string_is_normalized check if a string is normalized to nfc/nfkc/nfd/nfkd form."><code>mjb_string_is_normalized</code></a></li>
          <li><a href="#mjb_string_encoding" data-function-link data-search="mjb_string_encoding return the string encoding (the most probable)."><code>mjb_string_encoding</code></a></li>
          <li><a href="#mjb_string_is_ascii" data-function-link data-search="mjb_string_is_ascii return true if the string is encoded in ascii."><code>mjb_string_is_ascii</code></a></li>
          <li><a href="#mjb_string_is_utf8" data-function-link data-search="mjb_string_is_utf8 return true if the string is encoded in utf-8."><code>mjb_string_is_utf8</code></a></li>
          <li><a href="#mjb_string_is_utf16" data-function-link data-search="mjb_string_is_utf16 return true if the string is encoded in utf-16be or utf-16le."><code>mjb_string_is_utf16</code></a></li>
          <li><a href="#mjb_string_length" data-function-link data-search="mjb_string_length return the length of a string."><code>mjb_string_length</code></a></li>
          <li><a href="#mjb_string_each_character" data-function-link data-search="mjb_string_each_character run a callback for each character of a string."><code>mjb_string_each_character</code></a></li>
          <li><a href="#mjb_codepoint_property_binary" data-function-link data-search="mjb_codepoint_property_binary return the value of a binary unicode property."><code>mjb_codepoint_property_binary</code></a></li>
          <li><a href="#mjb_codepoint_property_int" data-function-link data-search="mjb_codepoint_property_int return the value of an enumerated or integer unicode property."><code>mjb_codepoint_property_int</code></a></li>
          <li><a href="#mjb_codepoint_numeric_value" data-function-link data-search="mjb_codepoint_numeric_value return the numeric value of a codepoint."><code>mjb_codepoint_numeric_value</code></a></li>
          <li><a href="#mjb_codepoint_block" data-function-link data-search="mjb_codepoint_block return the character block."><code>mjb_codepoint_block</code></a></li>
          <li><a href="#mjb_codepoint_script" data-function-link data-search="mjb_codepoint_script return the script of a codepoint."><code>mjb_codepoint_script</code></a></li>
          <li><a href="#mjb_codepoint_script_extensions" data-function-link data-search="mjb_codepoint_script_extensions return the script_extensions set of a codepoint."><code>mjb_codepoint_script_extensions</code></a></li>
          <li><a href="#mjb_codepoint_is_valid" data-function-link data-search="mjb_codepoint_is_valid return true if the codepoint is valid."><code>mjb_codepoint_is_valid</code></a></li>
          <li><a href="#mjb_codepoint_is_graphic" data-function-link data-search="mjb_codepoint_is_graphic return true if the codepoint is graphic."><code>mjb_codepoint_is_graphic</code></a></li>
          <li><a href="#mjb_codepoint_is_combining" data-function-link data-search="mjb_codepoint_is_combining return true if the codepoint is combining."><code>mjb_codepoint_is_combining</code></a></li>
          <li><a href="#mjb_codepoint_is_cjk_ideograph" data-function-link data-search="mjb_codepoint_is_cjk_ideograph return if the codepoint is cjk ideograph."><code>mjb_codepoint_is_cjk_ideograph</code></a></li>
          <li><a href="#mjb_codepoint_is_cjk_ext" data-function-link data-search="mjb_codepoint_is_cjk_ext return if the codepoint is cjk extension."><code>mjb_codepoint_is_cjk_ext</code></a></li>
          <li><a href="#mjb_category_is_graphic" data-function-link data-search="mjb_category_is_graphic return true if the category is graphic."><code>mjb_category_is_graphic</code></a></li>
          <li><a href="#mjb_category_is_combining" data-function-link data-search="mjb_category_is_combining return true if the category is combining."><code>mjb_category_is_combining</code></a></li>
          <li><a href="#mjb_codepoint_is_id_start" data-function-link data-search="mjb_codepoint_is_id_start return true if the codepoint is a valid unicode identifier start (unicode 17.0.0 uax #31 id_start)."><code>mjb_codepoint_is_id_start</code></a></li>
          <li><a href="#mjb_codepoint_is_id_continue" data-function-link data-search="mjb_codepoint_is_id_continue return true if the codepoint is a valid unicode identifier continuation (unicode 17.0.0 uax #31 id_continue)."><code>mjb_codepoint_is_id_continue</code></a></li>
          <li><a href="#mjb_codepoint_is_xid_start" data-function-link data-search="mjb_codepoint_is_xid_start return true if the codepoint is a valid nfkc identifier start (unicode 17.0.0 uax #31 xid_start)."><code>mjb_codepoint_is_xid_start</code></a></li>
          <li><a href="#mjb_codepoint_is_xid_continue" data-function-link data-search="mjb_codepoint_is_xid_continue return true if the codepoint is a valid nfkc identifier continuation (unicode 17.0.0 uax #31 xid_continue)."><code>mjb_codepoint_is_xid_continue</code></a></li>
          <li><a href="#mjb_codepoint_is_pattern_syntax" data-function-link data-search="mjb_codepoint_is_pattern_syntax return true if the codepoint is reserved for use in patterns (unicode 17.0.0 uax #31 pattern_syntax)."><code>mjb_codepoint_is_pattern_syntax</code></a></li>
          <li><a href="#mjb_codepoint_is_pattern_white_space" data-function-link data-search="mjb_codepoint_is_pattern_white_space return true if the codepoint is pattern whitespace (unicode 17.0.0 uax #31 pattern_white_space)."><code>mjb_codepoint_is_pattern_white_space</code></a></li>
          <li><a href="#mjb_codepoint_is_extended_pictographic" data-function-link data-search="mjb_codepoint_is_extended_pictographic return true if the codepoint has the unicode extended_pictographic property."><code>mjb_codepoint_is_extended_pictographic</code></a></li>
          <li><a href="#mjb_codepoint_plane" data-function-link data-search="mjb_codepoint_plane return the plane of the codepoint."><code>mjb_codepoint_plane</code></a></li>
          <li><a href="#mjb_plane_is_valid" data-function-link data-search="mjb_plane_is_valid return true if the plane is valid."><code>mjb_plane_is_valid</code></a></li>
          <li><a href="#mjb_plane_name" data-function-link data-search="mjb_plane_name return the name of a plane, null if the plane specified is not valid."><code>mjb_plane_name</code></a></li>
        </ul>
      </details>
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Sorting and comparison</span>
          <span class="sidebar-count" aria-label="2 functions">2</span>
        </summary>
        <ul>
          <li><a href="#mjb_string_compare" data-function-link data-search="mjb_string_compare compare two strings using uca."><code>mjb_string_compare</code></a></li>
          <li><a href="#mjb_collation_key" data-function-link data-search="mjb_collation_key generate a uca sort key for a string."><code>mjb_collation_key</code></a></li>
        </ul>
      </details>
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Security</span>
          <span class="sidebar-count" aria-label="3 functions">3</span>
        </summary>
        <ul>
          <li><a href="#mjb_string_is_identifier" data-function-link data-search="mjb_string_is_identifier return true if the string is a valid unicode identifier (unicode 17.0.0 uax #31)."><code>mjb_string_is_identifier</code></a></li>
          <li><a href="#mjb_confusable_skeleton" data-function-link data-search="mjb_confusable_skeleton compute a unicode confusable skeleton (unicode 17.0.0 uts #39 section 4)."><code>mjb_confusable_skeleton</code></a></li>
          <li><a href="#mjb_string_is_confusable" data-function-link data-search="mjb_string_is_confusable return true if two strings are visually confusable (unicode 17.0.0 uts #39 section 4): skeleton(s1) == skeleton(s2)."><code>mjb_string_is_confusable</code></a></li>
        </ul>
      </details>
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Segmentation</span>
          <span class="sidebar-count" aria-label="7 functions">7</span>
        </summary>
        <ul>
          <li><a href="#mjb_break_line" data-function-link data-search="mjb_break_line unicode line break algorithm."><code>mjb_break_line</code></a></li>
          <li><a href="#mjb_break_word" data-function-link data-search="mjb_break_word word cluster breaking."><code>mjb_break_word</code></a></li>
          <li><a href="#mjb_break_sentence" data-function-link data-search="mjb_break_sentence sentence boundaries breaking."><code>mjb_break_sentence</code></a></li>
          <li><a href="#mjb_break_grapheme_cluster" data-function-link data-search="mjb_break_grapheme_cluster grapheme cluster breaking."><code>mjb_break_grapheme_cluster</code></a></li>
          <li><a href="#mjb_truncate" data-function-link data-search="mjb_truncate return the number of bytes that form the first `max_graphemes` grapheme cluster segments."><code>mjb_truncate</code></a></li>
          <li><a href="#mjb_truncate_word" data-function-link data-search="mjb_truncate_word return the number of bytes that form the first max_segments word-break segments."><code>mjb_truncate_word</code></a></li>
          <li><a href="#mjb_truncate_word_width" data-function-link data-search="mjb_truncate_word_width return the number of bytes whose word-break segments fit within max_columns display columns."><code>mjb_truncate_word_width</code></a></li>
        </ul>
      </details>
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Bidirectional text</span>
          <span class="sidebar-count" aria-label="4 functions">4</span>
        </summary>
        <ul>
          <li><a href="#mjb_bidi_resolve" data-function-link data-search="mjb_bidi_resolve resolve bidirectional text (tr9) for a paragraph."><code>mjb_bidi_resolve</code></a></li>
          <li><a href="#mjb_bidi_reorder_line" data-function-link data-search="mjb_bidi_reorder_line reorder a line visually (l1-l4); visual_order is caller-allocated."><code>mjb_bidi_reorder_line</code></a></li>
          <li><a href="#mjb_bidi_line_runs" data-function-link data-search="mjb_bidi_line_runs compute visual level runs; pass runs=null to count first."><code>mjb_bidi_line_runs</code></a></li>
          <li><a href="#mjb_bidi_free" data-function-link data-search="mjb_bidi_free free a bidi paragraph allocated by mjb_bidi_resolve."><code>mjb_bidi_free</code></a></li>
        </ul>
      </details>
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Emoji</span>
          <span class="sidebar-count" aria-label="9 functions">9</span>
        </summary>
        <ul>
          <li><a href="#mjb_codepoint_emoji" data-function-link data-search="mjb_codepoint_emoji return the emoji properties."><code>mjb_codepoint_emoji</code></a></li>
          <li><a href="#mjb_codepoint_is_emoji" data-function-link data-search="mjb_codepoint_is_emoji return true if the codepoint has the unicode emoji property."><code>mjb_codepoint_is_emoji</code></a></li>
          <li><a href="#mjb_codepoint_is_emoji_presentation" data-function-link data-search="mjb_codepoint_is_emoji_presentation return true if the codepoint has the unicode emoji_presentation property."><code>mjb_codepoint_is_emoji_presentation</code></a></li>
          <li><a href="#mjb_codepoint_is_emoji_modifier" data-function-link data-search="mjb_codepoint_is_emoji_modifier return true if the codepoint has the unicode emoji_modifier property."><code>mjb_codepoint_is_emoji_modifier</code></a></li>
          <li><a href="#mjb_codepoint_is_emoji_modifier_base" data-function-link data-search="mjb_codepoint_is_emoji_modifier_base return true if the codepoint has the unicode emoji_modifier_base property."><code>mjb_codepoint_is_emoji_modifier_base</code></a></li>
          <li><a href="#mjb_codepoint_is_emoji_component" data-function-link data-search="mjb_codepoint_is_emoji_component return true if the codepoint has the unicode emoji_component property."><code>mjb_codepoint_is_emoji_component</code></a></li>
          <li><a href="#mjb_string_emoji_sequence" data-function-link data-search="mjb_string_emoji_sequence return emoji sequence metadata for a complete string."><code>mjb_string_emoji_sequence</code></a></li>
          <li><a href="#mjb_string_is_emoji_sequence" data-function-link data-search="mjb_string_is_emoji_sequence return true if the complete string is an emoji sequence listed by unicode, including standardized emoji variation sequences."><code>mjb_string_is_emoji_sequence</code></a></li>
          <li><a href="#mjb_string_is_rgi_emoji" data-function-link data-search="mjb_string_is_rgi_emoji return true if the complete string is an rgi emoji sequence, excluding plain standardized variation sequences."><code>mjb_string_is_rgi_emoji</code></a></li>
        </ul>
      </details>
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Display width</span>
          <span class="sidebar-count" aria-label="3 functions">3</span>
        </summary>
        <ul>
          <li><a href="#mjb_truncate_width" data-function-link data-search="mjb_truncate_width return the number of bytes whose grapheme clusters fit within max_columns display columns."><code>mjb_truncate_width</code></a></li>
          <li><a href="#mjb_codepoint_east_asian_width" data-function-link data-search="mjb_codepoint_east_asian_width return the east asian width of a codepoint."><code>mjb_codepoint_east_asian_width</code></a></li>
          <li><a href="#mjb_display_width" data-function-link data-search="mjb_display_width return the display width of a string."><code>mjb_display_width</code></a></li>
        </ul>
      </details>
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Hangul language</span>
          <span class="sidebar-count" aria-label="8 functions">8</span>
        </summary>
        <ul>
          <li><a href="#mjb_codepoint_is_hangul_l" data-function-link data-search="mjb_codepoint_is_hangul_l return if the codepoint is a hangul l."><code>mjb_codepoint_is_hangul_l</code></a></li>
          <li><a href="#mjb_codepoint_is_hangul_v" data-function-link data-search="mjb_codepoint_is_hangul_v return if the codepoint is a hangul v."><code>mjb_codepoint_is_hangul_v</code></a></li>
          <li><a href="#mjb_codepoint_is_hangul_t" data-function-link data-search="mjb_codepoint_is_hangul_t return if the codepoint is a hangul t."><code>mjb_codepoint_is_hangul_t</code></a></li>
          <li><a href="#mjb_codepoint_is_hangul_jamo" data-function-link data-search="mjb_codepoint_is_hangul_jamo return if the codepoint is a hangul jamo."><code>mjb_codepoint_is_hangul_jamo</code></a></li>
          <li><a href="#mjb_codepoint_is_hangul_syllable" data-function-link data-search="mjb_codepoint_is_hangul_syllable return if the codepoint is a hangul syllable."><code>mjb_codepoint_is_hangul_syllable</code></a></li>
          <li><a href="#mjb_hangul_syllable_name" data-function-link data-search="mjb_hangul_syllable_name return hangul syllable name."><code>mjb_hangul_syllable_name</code></a></li>
          <li><a href="#mjb_hangul_syllable_decomposition" data-function-link data-search="mjb_hangul_syllable_decomposition hangul syllable decomposition."><code>mjb_hangul_syllable_decomposition</code></a></li>
          <li><a href="#mjb_hangul_syllable_composition" data-function-link data-search="mjb_hangul_syllable_composition hangul syllable composition."><code>mjb_hangul_syllable_composition</code></a></li>
        </ul>
      </details>
      <details class="sidebar-group" data-section-nav open>
        <summary>
          <span>Utilities</span>
          <span class="sidebar-count" aria-label="12 functions">12</span>
        </summary>
        <ul>
          <li><a href="#mjb_property_name" data-function-link data-search="mjb_property_name return the name of a property, null if the property specified is not valid."><code>mjb_property_name</code></a></li>
          <li><a href="#mjb_locale_parse" data-function-link data-search="mjb_locale_parse parse a bcp 47 language tag."><code>mjb_locale_parse</code></a></li>
          <li><a href="#mjb_locale_set" data-function-link data-search="mjb_locale_set set current locale used by locale-sensitive casing."><code>mjb_locale_set</code></a></li>
          <li><a href="#mjb_result_free" data-function-link data-search="mjb_result_free free a mjb_result."><code>mjb_result_free</code></a></li>
          <li><a href="#mjb_version" data-function-link data-search="mjb_version output the current library version (mjb_version)."><code>mjb_version</code></a></li>
          <li><a href="#mjb_version_number" data-function-link data-search="mjb_version_number output the current library version number (mjb_version_number)."><code>mjb_version_number</code></a></li>
          <li><a href="#mjb_unicode_version" data-function-link data-search="mjb_unicode_version output the current supported unicode version (mjb_unicode_version)."><code>mjb_unicode_version</code></a></li>
          <li><a href="#mjb_set_memory_functions" data-function-link data-search="mjb_set_memory_functions set the library memory functions."><code>mjb_set_memory_functions</code></a></li>
          <li><a href="#mjb_shutdown" data-function-link data-search="mjb_shutdown shutdown the library. not needed to be called."><code>mjb_shutdown</code></a></li>
          <li><a href="#mjb_alloc" data-function-link data-search="mjb_alloc allocate memory."><code>mjb_alloc</code></a></li>
          <li><a href="#mjb_realloc" data-function-link data-search="mjb_realloc reallocate memory."><code>mjb_realloc</code></a></li>
          <li><a href="#mjb_free" data-function-link data-search="mjb_free free memory."><code>mjb_free</code></a></li>
        </ul>
      </details>
    </nav>
                <p class="no-results" id="api-no-results" hidden>No matching functions.</p>
            </div>
        </aside>
        <button class="sidebar-backdrop" id="sidebar-backdrop" type="button" tabindex="-1"
            aria-label="Close navigation"></button>
        <main id="main">
            <section class="hero" id="overview">
                <p class="eyebrow">Unicode 17 - C11 - zero dependencies</p>
                <h1 title="æå­åã">
                    Unicode text processing,<br><em>without the baggage.</em>
                </h1>
                <p class="hero-lede">
                    Mojibake is a small, fast, self-contained Unicode library for C11 and C++17.
                    Ship standards-compliant text handling without a runtime or dependency tree.
                </p>
                <div class="hero-actions">
                    <a class="button button-primary" href="https://github.com/zaerl/mojibake/releases/download/v0.2.7/mojibake-amalgamation-027.zip">Download v0.2.7</a>
                    <a class="button button-secondary" href="#api-reference">Explore the API</a>
                </div>
                <dl class="hero-facts">
                    <div><dt>Standard</dt><dd>Unicode 17.0</dd></div>
                    <div><dt>Runtime</dt><dd>None</dd></div>
                    <div><dt>License</dt><dd>MIT</dd></div>
                </dl>
            </section>
            <section class="guide-section" id="guide">
                <header class="content-heading">
                    <p class="eyebrow">Start here</p>
                    <h2>A practical Unicode toolkit</h2>
                </header>
                <article class="guide-content">
            <p><strong>Mojibake</strong> is a low-level Unicode 17 text-processing library written in C11 and compatible
with C++17. It is released under the MIT License.</p>
<h2>Usage</h2>
<p>You don't need to install anything. There are two files (<code>mojibake.c</code>, <code>mojibake.h</code>) to add to your
C/C++ project. Download it here <a href="https://github.com/zaerl/mojibake/releases/download/v0.2.7/mojibake-amalgamation-027.zip">mojibake-amalgamation-027.zip</a></p>
<p>Examples of normalization, characters count and NFKC casefold.</p>
<pre><code class="language-c"><span class="hljs-meta">#<span class="hljs-keyword">include</span> <span class="hljs-string">&lt;stdio.h&gt;</span></span>
<span class="hljs-meta">#<span class="hljs-keyword">include</span> <span class="hljs-string">&lt;string.h&gt;</span></span>

<span class="hljs-meta">#<span class="hljs-keyword">include</span> <span class="hljs-string">&quot;mojibake.h&quot;</span></span>

<span class="hljs-type">void</span> <span class="hljs-title function_">print_string</span><span class="hljs-params">(<span class="hljs-type">const</span> <span class="hljs-type">char</span> *input, <span class="hljs-type">size_t</span> length)</span>;

<span class="hljs-type">int</span> <span class="hljs-title function_">main</span><span class="hljs-params">(<span class="hljs-type">int</span> argc, <span class="hljs-type">char</span> *<span class="hljs-type">const</span> argv[])</span> {
    <span class="hljs-type">const</span> <span class="hljs-type">char</span> *input = <span class="hljs-string">&quot;Cafe\xCC\x81&quot;</span>;
    <span class="hljs-type">size_t</span> length = <span class="hljs-built_in">strlen</span>(input);
    <span class="hljs-type">mjb_result</span> result;

    <span class="hljs-comment">// Normalize example: in NFC e + âÌ -&gt; Ã© (U+00E9)</span>
    <span class="hljs-keyword">if</span>(mjb_normalize(input, length, MJB_ENC_UTF_8, MJB_NORMALIZATION_NFC, MJB_ENC_UTF_8,
        &amp;result) != MJB_STATUS_OK) {
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
    }

    <span class="hljs-comment">// Cafe + âÌ (U+0301, COMBINING ACUTE ACCENT) -&gt; CafÃ©</span>
    print_string(input, length);

    <span class="hljs-comment">// Caf + Ã© (U+00E9, LATIN SMALL LETTER E WITH ACUTE) -&gt; CafÃ©</span>
    print_string(result.output, result.output_size);

    <span class="hljs-type">const</span> <span class="hljs-type">char</span> *mojibake = <span class="hljs-string">&quot;æå­åã&quot;</span>;
    length = <span class="hljs-built_in">strlen</span>(mojibake);

    <span class="hljs-comment">// String length example: mjb_string_length counts the number of characters in a</span>
    <span class="hljs-comment">// string, not the number of bytes.</span>
    <span class="hljs-built_in">printf</span>(<span class="hljs-string">&quot;\&quot;%s\&quot; encoded in UTF-8 is %zu bytes long, and %zu characters long\n&quot;</span>,
        mojibake, length, mjb_string_length(mojibake, length, MJB_ENC_UTF_8));

    mjb_result_free(&amp;result);

    <span class="hljs-type">const</span> <span class="hljs-type">char</span> *case_input = <span class="hljs-string">&quot;StraÃe&quot;</span>;

    <span class="hljs-comment">// NFKC casefold example: in NFKC casefold, Ã -&gt; ss</span>
    <span class="hljs-keyword">if</span>(mjb_nfkc_casefold(case_input, <span class="hljs-built_in">strlen</span>(case_input), MJB_ENC_UTF_8, MJB_ENC_UTF_8,
        &amp;result) != MJB_STATUS_OK) {
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
    }

    <span class="hljs-built_in">printf</span>(<span class="hljs-string">&quot;%s -&gt; %.*s\n&quot;</span>, case_input, (<span class="hljs-type">int</span>)result.output_size, result.output);
    mjb_result_free(&amp;result);

    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
}

<span class="hljs-type">void</span> <span class="hljs-title function_">print_string</span><span class="hljs-params">(<span class="hljs-type">const</span> <span class="hljs-type">char</span> *input, <span class="hljs-type">size_t</span> length)</span> {
    <span class="hljs-keyword">for</span>(<span class="hljs-type">size_t</span> i = <span class="hljs-number">0</span>; i &lt; length; ++i) {
        <span class="hljs-type">unsigned</span> <span class="hljs-type">char</span> byte = (<span class="hljs-type">unsigned</span> <span class="hljs-type">char</span>)input[i];

        <span class="hljs-keyword">if</span>(byte &gt;= <span class="hljs-number">0x21</span> &amp;&amp; byte &lt;= <span class="hljs-number">0x7E</span>) {
            <span class="hljs-built_in">printf</span>(<span class="hljs-string">&quot;%c&quot;</span>, byte);
        } <span class="hljs-keyword">else</span> {
            <span class="hljs-built_in">printf</span>(<span class="hljs-string">&quot;&lt;%02X&gt;&quot;</span>, byte);
        }
    }

    <span class="hljs-built_in">printf</span>(<span class="hljs-string">&quot;\n&quot;</span>);
}
</code></pre>
<p>This output:</p>
<pre><code>Cafe&lt;CC&gt;&lt;81&gt;
Caf&lt;C3&gt;&lt;A9&gt;
&quot;æå­åã&quot; encoded in UTF-8 is 12 bytes long, and 4 characters long
StraÃe -&gt; strasse
</code></pre>
<p>Mojibake aims to be:</p>
<ol>
<li>Small</li>
<li>Easy to use</li>
<li>Fast</li>
<li>Self-contained</li>
</ol>
<p>Mojibake do:</p>
<ol>
<li>Run in all modern OSes (Linux, macOS, FreeBSD, OpenBSD, NetBSD, Windows 10/11)</li>
<li>Pass the official Unicode test suites for supported algorithms</li>
<li>Implement all Unicode standard algorithms</li>
<li>Satisfy all <a href="https://github.com/zaerl/mojibake/blob/main/CONFORMANCE_REQUIREMENTS.md">Unicode Conformance Requirements</a></li>
</ol>
<h2>Feature highlights</h2>
<p>All the C files, together with the Unicode data tables, are concatenated into a single large file
and header: <code>mojibake.c</code> and <code>mojibake.h</code>. Zero dependencies.</p>
<p><strong>Text transformation</strong></p>
<ul>
<li><strong>Normalization</strong>: NFC/NFD/NFKC/NFKD (<code>mjb_normalize</code>), identifier-oriented NFKC case folding
(<code>mjb_nfkc_casefold</code>), plus a fast quick-check
(<code>mjb_string_is_normalized</code>) (<a href="https://www.unicode.org/reports/tr15/tr15-57.html">UAX #15, Unicode 17.0.0</a>)</li>
<li><strong>Case conversion</strong>: uppercase, lowercase, titlecase, and case folding with full special-casing
and conditional mappings (<code>mjb_case</code>)</li>
<li><strong>Filtering</strong>: strip controls, spaces, or numeric characters while normalizing
(<code>mjb_string_filter</code>)</li>
</ul>
<p><strong>Text analysis</strong></p>
<ul>
<li><strong>Character database</strong>: every Unicode Character Database property: category, script and
Script_Extensions, block, plane, numeric value, name (<code>mjb_codepoint_character</code>,
<code>mjb_codepoint_script_extensions</code>)</li>
<li><strong>Segmentation</strong>: grapheme clusters, words, sentences, and line-break opportunities
(<a href="https://www.unicode.org/reports/tr29/tr29-47.html">UAX #29, Unicode 17.0.0</a>,
<a href="https://www.unicode.org/reports/tr14/tr14-55.html">UAX #14, Unicode 17.0.0</a>)</li>
<li><strong>Bidirectional text</strong>: full Unicode Bidirectional Algorithm: paragraph resolution, line
reordering, runs (<a href="https://www.unicode.org/reports/tr9/tr9-51.html">UAX #9, Unicode 17.0.0</a>)</li>
<li><strong>Emoji</strong>: codepoint properties, sequence analysis, RGI emoji detection</li>
<li><strong>Display width</strong>: East Asian width and terminal display width, with width-aware truncation
(<code>mjb_display_width</code>, <code>mjb_truncate_width</code>)</li>
</ul>
<p><strong>Sorting and comparison</strong></p>
<ul>
<li><strong>Collation</strong>: Unicode Collation Algorithm string comparison and sort keys, in shifted and
non-ignorable modes (<code>mjb_string_compare</code>, <code>mjb_collation_key</code>,
<a href="https://www.unicode.org/reports/tr10/tr10-53.html">UTS #10, Unicode 17.0.0</a>)</li>
</ul>
<p><strong>Security</strong></p>
<ul>
<li><strong>Confusable detection</strong>: generate reusable skeletons and check if strings are visually
confusable (<code>mjb_confusable_skeleton</code>, <code>mjb_string_is_confusable</code>,
<a href="https://www.unicode.org/reports/tr39/tr39-32.html">UTS #39, Unicode 17.0.0</a>)</li>
<li><strong>Identifier validation</strong>: XID/ID checks for parser and compiler authors
(<code>mjb_string_is_identifier</code>, <a href="https://www.unicode.org/reports/tr31/tr31-43.html">UAX #31, Unicode 17.0.0</a>)</li>
</ul>
<p><strong>Integration</strong></p>
<ul>
<li><strong>Encodings</strong>: the API accepts and outputs UTF-8, UTF-16LE, UTF-16BE, UTF-32LE, UTF-32BE
strings, with encoding detection and conversion (<code>mjb_string_encoding</code>,
<code>mjb_string_convert_encoding</code>)</li>
<li><strong>Parsing and string functions</strong>: character-by-character iteration (<code>mjb_next_character</code>) and
standard C <code>string.h</code>-style helpers (<code>mjb_string_length</code>, and others)</li>
<li><strong>Locales</strong>: strict BCP 47 language tag parsing (<code>mjb_locale_parse</code>)</li>
<li><strong>Embeddable</strong>: custom allocators (<code>mjb_set_memory_functions</code>), build-time feature flags to trim
table size, a C++17 wrapper (<code>src/cpp/mojibake.hpp</code>), a CLI tool (<code>src/shell</code>), and a
WASM + TypeScript API (<code>src/api</code>)</li>
<li><strong>Tested</strong>: Mojibake uses <a href="https://github.com/zaerl/attractor/">Attractor</a> as test suite and run
<a href="https://github.com/zaerl/mojibake/blob/main/TESTS.md">1.5M+ assertions</a> including the
official Unicode conformance suites for supported algorithms</li>
<li><strong>Fuzz</strong> Mojibake is fuzzed with <a href="https://llvm.org/docs/LibFuzzer.html">libFuzzer</a> over untrusted
byte input</li>
<li><code>AddressSanitizer</code> and <code>UBSan</code> clean</li>
</ul>
<h3>Build-time features</h3>
<p>Mojibake can compile out optional feature tables to reduce binary size. Feature macros default to
enabled.</p>
<ul>
<li><code>#define MJB_FEATURE_CHARACTER_NAMES</code> controls the Unicode character-name tables used by
<code>mjb_codepoint_character(...)</code> to fill <code>mjb_character.name</code>. When disabled, the tables are not
compiled and <code>mjb_character.name</code> is reported as <code>Codepoint U+XXXX</code>. This will redude the output
of <strong>~30%</strong>.</li>
</ul>
<p>With CMake:</p>
<pre><code class="language-bash">cmake -S . -B build-no-name -DMJB_FEATURE_CHARACTER_NAMES=OFF
cmake --build build-no-name
</code></pre>
<p>With the provided Makefile:</p>
<pre><code class="language-bash">make build BUILD_DIR=build-no-name FEATURE_CHARACTER_NAMES=OFF
make test-no-names
</code></pre>
<h3>API documentation</h3>
<p>See <a href="https://github.com/zaerl/mojibake/blob/main/API.md">API.md</a> or the site for the detailed
documentation.</p>
<h3>CLI</h3>
<p>The <code>src/shell</code> directory builds the <code>mojibake</code> CLI used to test the library. Example usage:</p>
<pre><code class="language-bash"># This outputs &quot;NFC: CafÃ©&quot;, e + âÌ -&gt; Ã©
mojibake nfc $'Cafe\u0301'

# The output an emoji sequence [1] Basic, [2] Fully-qualified of two characters U+263A U+FE0F
mojibake emoji &quot;âºï¸&quot;
</code></pre>
<h2>Building from source and contributing</h2>
<p>See <a href="https://github.com/zaerl/mojibake/blob/main/CONTRIBUTING.md">CONTRIBUTING.md</a> for instructions.</p>
<h2>Licenses</h2>
<p>Mojibake is released under the MIT License (see <a href="https://github.com/zaerl/mojibake/blob/main/LICENSE">LICENSE</a>).</p>
<h2>Legalese</h2>
<p>Here you can find the very detailed and boring informations needed to have this library conformant
to the Unicode standard, or at least what I got, at
<a href="https://github.com/zaerl/mojibake/blob/main/CONFORMANCE_REQUIREMENTS.md">CONFORMANCE_REQUIREMENTS.md</a></p>
<h2>Thanks</h2>
<p>Mojibake is built using the work of extraordinary individuals and teams.</p>
<ol>
<li>Unicode Character Database - Copyright Â© 1991-2026 Unicode, Inc.
(see <a href="https://www.unicode.org/license.txt">license.txt</a>)</li>
<li>Unicode CLDR Project - Copyright Â© 2004-2026 Unicode, Inc.
(see <a href="https://raw.githubusercontent.com/unicode-org/cldr/refs/heads/main/LICENSE">LICENSE</a>)</li>
</ol>

                </article>
            </section>
            <section class="playground-callout" id="playground">
                <div>
                    <p class="eyebrow">No installation required</p>
                    <h2>Try every function in your browser</h2>
                </div>
                <div>
                    <p>
                        Each API reference below includes a live form backed by the WASM build.
                        Expand a function, enter its arguments, and inspect the result immediately.
                    </p>
                    <a href="https://github.com/zaerl/mojibake/releases/download/v0.2.7/mojibake-wasm-027.zip">
                        Download mojibake-wasm-027.zip <span aria-hidden="true">â</span>
                    </a>
                </div>
            </section>
            <section class="api-reference" id="api-reference">
                <header class="api-reference-heading">
                    <p class="eyebrow">Reference</p>
                    <h2>C API</h2>
                    <p>
                        Functions are organized by their metadata section. Select the plus button
                        to see detailed behavior, examples, specifications, and the live WASM form.
                    </p>
                </header>
                <div id="functions">
    <section class="api-section" id="api-text-transformation" data-api-section>
      <header class="api-section-header">
        <div>
          <p class="eyebrow">API section</p>
          <h2>Text transformation</h2>
          <p>Normalize, case-convert, filter, and convert Unicode text.</p>
        </div>
        <span class="api-section-count">9 functions</span>
      </header>
<article class="function-reference" id="mjb_normalize" data-function-reference data-search="mjb_normalize normalize a string to nfc/nfkc/nfd/nfkd form.">
      <h3 class="function-name"><a href="#mjb_normalize" aria-label="Link to mjb_normalize">mjb_normalize</a></h3>
      <p class="function-call-comment">Normalize a string to NFC/NFKC/NFD/NFKD form.</p>
      <div class="function-call" id="mjb_normalize-function">
        <pre><code class="hljs language-c"><span class="hljs-type">mjb_status</span> <span class="hljs-title function_">mjb_normalize</span><span class="hljs-params">(
    <span class="hljs-type">const</span> <span class="hljs-type">char</span> *buffer,
    <span class="hljs-type">size_t</span> byte_length,
    <span class="hljs-type">mjb_encoding</span> encoding,
    <span class="hljs-type">mjb_normalization</span> form,
    <span class="hljs-type">mjb_encoding</span> output_encoding,
    <span class="hljs-type">mjb_result</span> *result
)</span>;</code></pre>
        <button type="button" class="function-toggle" id="mjb_normalize-toggle"
          aria-expanded="false" aria-controls="mjb_normalize-card"
          aria-label="Show details and WASM form for mjb_normalize"
          onclick="toggleFunctionCall('mjb_normalize')"></button>
      </div>
      <div class="function-card" id="mjb_normalize-card">
        <div class="function-docs">
          <p>Normalize a string to the requested Unicode normalization form. If the input is already normalized and no encoding conversion is needed, the input buffer is returned as-is in <code>result-&gt;output</code> with <code>result-&gt;transformed</code> set to false, without allocating.</p>
          <h3>Returns</h3>
          <ul>
            <li><code>MJB_STATUS_OK</code> â The string was normalized (or already normal)</li>
            <li><code>MJB_STATUS_INVALID_ARGUMENT</code> â <code>result</code> is NULL, or <code>buffer</code> is NULL with a non-zero size</li>
            <li><code>MJB_STATUS_INVALID_FORM</code> â <code>form</code> is not NFC, NFD, NFKC, or NFKD</li>
            <li><code>MJB_STATUS_OVERFLOW</code> â The output size would overflow</li>
            <li><code>MJB_STATUS_NO_MEMORY</code> â Allocation failed</li>
          </ul>
          <h3>Example</h3>
          <pre><code class="hljs language-c"><span class="hljs-type">const</span> <span class="hljs-type">char</span> *input = <span class="hljs-string">&quot;Cafe\xCC\x81&quot;</span>; <span class="hljs-comment">// &quot;Cafe&quot; + U+0301 COMBINING ACUTE ACCENT</span>
<span class="hljs-type">mjb_result</span> result;

<span class="hljs-keyword">if</span>(mjb_normalize(input, <span class="hljs-built_in">strlen</span>(input), MJB_ENC_UTF_8, MJB_NORMALIZATION_NFC, MJB_ENC_UTF_8,
    &amp;result) != MJB_STATUS_OK) {
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
}

<span class="hljs-comment">// NFC: CafÃ©</span>
<span class="hljs-built_in">printf</span>(<span class="hljs-string">&quot;NFC: %.*s&quot;</span>, (<span class="hljs-type">int</span>)result.output_size, result.output);

<span class="hljs-keyword">if</span>(result.transformed) {
    mjb_free(result.output);
}</code></pre>
          <h3>Related</h3>
          <ul>
            <li><a href="#mjb_string_is_normalized"><code>mjb_string_is_normalized</code></a></li>
            <li><a href="#mjb_string_filter"><code>mjb_string_filter</code></a></li>
          </ul>
          <h3>Specifications</h3>
          <ul>
            <li><a href="https://www.unicode.org/reports/tr15/tr15-57.html" target="_blank" rel="noopener">UAX #15: Unicode Normalization Forms, Unicode 17.0.0</a></li>
          </ul>
        </div>
        <div>
          <form id="mjb_normalize-wasm-form" class="function-form" onsubmit="return false;">
            <div><label for="mjb_normalize-buffer">buffer</label><input id="mjb_normalize-buffer" type="text" name="mjb_normalize-buffer" placeholder="The string to normalize" ></div>
            <div><label for="mjb_normalize-byte_length" class="text-secondary">byte length</label><input id="mjb_normalize-byte_length" type="text" name="mjb_normalize-byte_length" placeholder="The length of the string, in bytes (automatically generated)" disabled></div>
            <div><label for="mjb_normalize-encoding">encoding</label><select id="mjb_normalize-encoding" name="mjb_normalize-encoding" title="The encoding of the string" ><option value="2">MJB_ENC_UTF_8</option><option value="8">MJB_ENC_UTF_16BE</option><option value="16">MJB_ENC_UTF_16LE</option><option value="64">MJB_ENC_UTF_32BE</option><option value="128">MJB_ENC_UTF_32LE</option></select></div>
            <div><label for="mjb_normalize-form">form</label><select id="mjb_normalize-form" name="mjb_normalize-form" title="The normalization form to use" ><option value="0">MJB_NORMALIZATION_NFC</option><option value="1">MJB_NORMALIZATION_NFD</option><option value="2">MJB_NORMALIZATION_NFKC</option><option value="3">MJB_NORMALIZATION_NFKD</option></select></div>
            <div><label for="mjb_normalize-output_encoding">output encoding</label><select id="mjb_normalize-output_encoding" name="mjb_normalize-output_encoding" title="The output encoding of the string" ><option value="2">MJB_ENC_UTF_8</option><option value="8">MJB_ENC_UTF_16BE</option><option value="16">MJB_ENC_UTF_16LE</option><option value="64">MJB_ENC_UTF_32BE</option><option value="128">MJB_ENC_UTF_32LE</option></select></div>
            <div><label for="mjb_normalize-result" class="text-secondary">result</label><input id="mjb_normalize-result" type="text" name="mjb_normalize-result" placeholder="The pointer to store the result (automatically generated)" disabled></div>
            <div class="function-form-button">
              <button type="submit" id="mjb_normalize-submit">Call function</button>
            </div>
          </form>
</div>
        <div id="mjb_normalize-results" class="function-results code"></div>
      </div>
    </article>
<article class="function-reference" id="mjb_string_filter" data-function-reference data-search="mjb_string_filter filter a string with the selected mjb_filter flags.">
      <h3 class="function-name"><a href="#mjb_string_filter" aria-label="Link to mjb_string_filter">mjb_string_filter</a></h3>
      <p class="function-call-comment">Filter a string with the selected mjb_filter flags.</p>
      <div class="function-call" id="mjb_string_filter-function">
        <pre><code class="hljs language-c"><span class="hljs-type">mjb_status</span> <span class="hljs-title function_">mjb_string_filter</span><span class="hljs-params">(
    <span class="hljs-type">const</span> <span class="hljs-type">char</span> *buffer,
    <span class="hljs-type">size_t</span> byte_length,
    <span class="hljs-type">mjb_encoding</span> encoding,
    <span class="hljs-type">mjb_filter</span> filters,
    <span class="hljs-type">mjb_encoding</span> output_encoding,
    <span class="hljs-type">mjb_result</span> *result
)</span>;</code></pre>
        <button type="button" class="function-toggle" id="mjb_string_filter-toggle"
          aria-expanded="false" aria-controls="mjb_string_filter-card"
          aria-label="Show details and WASM form for mjb_string_filter"
          onclick="toggleFunctionCall('mjb_string_filter')"></button>
      </div>
      <div class="function-card" id="mjb_string_filter-card">
        <div class="function-docs">
          <p><code>MJB_FILTER_LIMIT_COMBINING</code> removes combining marks after the first <code>MJB_FILTER_MAX_COMBINING_MARKS</code> consecutive marks in an emitted run. This is useful for reducing Zalgo-style text while keeping ordinary accents and stacked marks.</p>
          <h3>Example</h3>
          <pre><code class="hljs language-c"><span class="hljs-type">const</span> <span class="hljs-type">char</span> *mixed_whitespace = <span class="hljs-string">&quot;Hello\t\t\n\nworld&quot;</span>;
<span class="hljs-type">mjb_result</span> result;

<span class="hljs-keyword">if</span>(mjb_string_filter(mixed_whitespace, <span class="hljs-built_in">strlen</span>(mixed_whitespace), MJB_ENC_UTF_8,
    MJB_FILTER_COLLAPSE_SPACES, MJB_ENC_UTF_8, &amp;result) != MJB_STATUS_OK) {
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
}

<span class="hljs-comment">// Filtered: Hello world</span>
<span class="hljs-built_in">printf</span>(<span class="hljs-string">&quot;Filtered: %.*s&quot;</span>, (<span class="hljs-type">int</span>)result.output_size, result.output);

<span class="hljs-keyword">if</span>(result.transformed) {
    mjb_free(result.output);
}

<span class="hljs-type">const</span> <span class="hljs-type">char</span> *controls = <span class="hljs-string">&quot;\x1\x2\t\n\v\f\r\x1f&quot;</span>;

<span class="hljs-keyword">if</span>(mjb_string_filter(controls, <span class="hljs-built_in">strlen</span>(controls), MJB_ENC_UTF_8, MJB_FILTER_CONTROLS,
    MJB_ENC_UTF_8, &amp;result) != MJB_STATUS_OK) {
    <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
}

<span class="hljs-comment">// Filtered: \t\n\v\f\r</span>
<span class="hljs-built_in">printf</span>(<span class="hljs-string">&quot;Filtered: %.*s&quot;</span>, (<span class="hljs-type">int</span>)result.output_size, result.output);

<span class="hljs-keyword">if</span>(result.transformed) {
    mjb_free(result.output);
}</code></pre>
          <h3>Related</h3>
          <ul>
            <li><a href="#mjb_normalize"><code>mjb_normalize</code></a></li>
          </ul>
        </div>
        <div>
          <form id="mjb_string_filter-wasm-form" class="function-form" onsubmit="return false;">
            <div><label for="mjb_string_filter-buffer">buffer</label><input id="mjb_string_filter-buffer" type="text" name="mjb_string_filter-buffer" placeholder="The string to filter" ></div>
            <div><label for="mjb_string_filter-byte_length" class="text-secondary">byte length</label><input id="mjb_string_filter-byte_length" type="text" name="mjb_string_filter-byte_length" placeholder="The length of the string, in bytes (automatically generated)" disabled></div>
            <div><label for="mjb_string_filter-encoding">encoding</label><select id="mjb_string_filter-encoding" name="mjb_string_filter-encoding" title="The encoding of the string" ><option value="2">MJB_ENC_UTF_8</option><option value="8">MJB_ENC_UTF_16BE</option><option value="16">MJB_ENC_UTF_16LE</option><option value="64">MJB_ENC_UTF_32BE</option><option value="128">MJB_ENC_UTF_32LE</option></select></di