---
title: "how to create accessible modals and pop ups using html css and minimal javascript"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - async
  - container
  - edge
  - gpt
  - news
  - search
---

# how to create accessible modals and pop ups using html css and minimal javascript

> **Source:** how-to-create-accessible-modals-and-pop-ups-using-html-css-and-minimal-javascript-2026-07-18.md
> **Type:** comparison
> **Created:** 2026-07-18
> **Updated:** 2026-07-18
> **Confidence:** high
> **Description:** --- source_url: https://www.freecodecamp.org/news/how-to-create-accessible-modals-and-pop-ups-using-html-css-and-minimal-javascript/ ingested: 2026-07-18 sha256: 1ae1a390217528db72a90169907152d6e47927...
> **Sources:**
>   - how-to-create-accessible-modals-and-pop-ups-using-html-css-and-minimal-javascript-2026-07-18.md
> **Links:**
- [[intro to shaders javascript and p5 js course for beginners]]
- [[a beginner s guide to python hands on projects to get you coding]]
- [[5 Agent Skills I Use Every Day]]
- [[master full stack mobile development with react native]]
- [[2026 2 release]]

## Key Findings

---
source_url: https://www.freecodecamp.org/news/how-to-create-accessible-modals-and-pop-ups-using-html-css-and-minimal-javascript/
ingested: 2026-07-18
sha256: 1ae1a390217528db72a90169907152d6e47927202597167ece3ca5e9a5e92e59
blog_source: FreeCodeCamp Blog
---
How to Create Accessible Modals and Pop-ups Using HTML, CSS, and Minimal JavaScript
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
[![freeCodeCamp.org](https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg)](https://www.freecodecamp.org/news/)
- 
English
- 
Español
- 
中文（简体字）
- 
Italiano
- 
Português
- 
Українська
- 
日本語
- 
한국어
Menu
- 
- Forum
- Curriculum
- 
Night Mode
Donate
July 17, 2026
/
#anchor css
# How to Create Accessible Modals and Pop-ups Using HTML, CSS, and Minimal JavaScript
![jabo Landry](https://avatars.githubusercontent.com/u/153087724?v=4)
[
jabo Landry
](/news/author/Arnold-Jabo/)
![How to Create Accessible Modals and Pop-ups Using HTML, CSS, and Minimal JavaScript](https://cdn.hashnode.com/uploads/covers/5e1e335a7a1d3fcc59028c64/e929b316-4b85-459b-9c40-1b7928518077.png)
Creating pop-ups and modals on your site can be a complicated process. And it often requires a lot of boilerplate code to get started.
But the real challenge comes when you want to make that modal or pop-up accessible.
Today, I'll show you how you can use `<dialog>` to create an accessible modal/pop-up with minimal setup using HTML, CSS and JavaScript.
## Prerequisites
Before diving in, it helps if you’re comfortable with a few basics:
- **CSS fundamentals**: You should be familiar with common CSS terminology and concepts (selectors, properties, positioning, and so on).
- **HTML structure**: A working knowledge of how elements are organized in the DOM will make the examples easier to follow.
- **JavaScript DOM basics**: While this guide uses only minimal JavaScript, understanding how to query and manipulate DOM elements will give you more confidence as you experiment.
That’s all you need. No frameworks, no heavy boilerplate. Just a foundation in the core web technologies.
## Table of Contents
- [Prerequisites](#heading-prerequisites)
- [How to Create Pop-ups with `popover`](#heading-how-to-create-pop-ups-with-popover)
- [How to Create a Modal Using the `dialog` Tag](#heading-how-to-create-a-modal-using-the-dialog-tag)
- [Gotchas to Pay Attention to](#heading-gotchas-to-pay-attention-to)
- [The `::backdrop pseudo` class](#heading-the-backdrop-pseudo-class)
- [Final Thoughts](#heading-final-thoughts)
## How to Create Pop-ups with `popover`
Creating a pop-up from scratch using HTML, CSS and JavaScript can be quite challenging. A pop-up is a small dialog box that appears on the screen to show extra information or ask for input. Because it’s temporary by design, users expect it to disappear once they’re done interacting with it, like when they press Escape or click outside of it.
Using the HTML `popover` and `popovertarget` attributes, you can have several built-in accessibility and intera

## Summary

ction behaviors, such as Escape-to-close and light dismiss, but you still need to choose the right semantic element and test keyboard and screen reader behavior.
### Setting Up the Pop-up with HTML
To be practical, let's create a common example and use case for pop-ups on a webpage. We'll create a nav element that displays when a user clicks a hamburger menu or the menu list.
First, you'll set the `popover` attribute on the pop-up container. This tells HTML to treat the containing block as a pop-up and hide it from the screen by default.
Then you set the `popovertarget` attribute on the element that will trigger the pop-up (like a button element or something else) to unhide the hidden element with an attribute of `popover`.
#### Example:
```
<button popovertarget="navbar-menu" id='nav-btn'>open</button>
<nav id="navbar-menu" popover>
<a href="#">Home</a>
<a href="#">About</a>
<a href="#">Address</a>
</nav>
```
With the above setup, you have a pop-up with useful built-in interaction behaviors, including Escape-to-close and light dismiss. You can hide it from the screen by pressing the `ESC` key on the keyboard or when you click anywhere else on the page (as long as it's not inside the pop-up section).
Remember that the `popover` attribute alone doesn't automatically make a pop-up accessible. You still need to use the appropriate semantic elements, provide accessible labels where needed, and test keyboard and screen reader behavior.
### How to Align the Pop-up
Now you'll want to align the pop-up and place it where you want it to be. By default, the pop-up (or modal) that's created using either the `popover` attribute or the dialog tag will be centered on the page.
This is because by default elements with `popover` have a position of `fixed` and the `inset` of 0, which centers the pop-up box and a margin of `auto`.
**Note:** `inset` is the shorthand for top, bottom, left and right of an element's position on the page. If you want to have the same size on all of sides of an element, use inset.
If you don't want your pop-up in the center, you can start by setting the element with `popover` position to absolute to isolate it from the page's flow:
```
#navbar-menu {
position: absolute;
}
```
You can then disable the margin to 0 and positions (inset) to `unset`:
```
#navbar-menu {
position: absolute;
margin: 0;
inset: unset;
}
```
After this, you can then place the popover element on the side of the page you want.
### How to Use the `position-anchor` Property
**Note:** CSS Anchor Positioning is a newer feature. Check browser support before relying on it in production and provide a fallback for browsers that don't support it yet.
The next step is to position the element close to the element that triggers it. For it we can use the [`position-anchor` property of CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor).
The `position-anchor` property in CSS specifies a default anchor element that an absolutely or fixed-posi

## Related Articles

- [[intro to shaders javascript and p5 js course for beginners]]
- [[a beginner s guide to python hands on projects to get you coding]]
- [[5 Agent Skills I Use Every Day]]
- [[master full stack mobile development with react native]]
- [[2026 2 release]]
