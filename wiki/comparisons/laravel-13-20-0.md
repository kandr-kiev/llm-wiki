---
title: "laravel 13 20 0"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - api
  - application
  - async
  - data
  - image-generation
  - news
  - nlp
  - offline
  - use-case
---

# laravel 13 20 0

> **Source:** first-party-image-processing-in-laravel-1320-2026-07-17.md
> **Type:** comparison
> **Created:** 2026-07-17
> **Updated:** 2026-07-17
> **Confidence:** high
> **Description:** --- source_url: https://laravel-news.com/laravel-13-20-0?utm_medium=feed&utm_source=feedpress.me&utm_campaign=Feed%3A+laravelnews ingested: 2026-07-17 sha256: 12e2030141a64e597780cda4e6c9bf52efd2b1d85...
> **Sources:**
>   - first-party-image-processing-in-laravel-1320-2026-07-17.md
> **Links:**
- [[build-a-laravel-scout-search-endpoint-with-the-http-query-method]]
- [[enforce-per-action-waiting-periods-in-laravel-with-cooldown]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
- [[release-v0251]]
- [[workers-cache]]

## Key Findings

---
source_url: https://laravel-news.com/laravel-13-20-0?utm_medium=feed&utm_source=feedpress.me&utm_campaign=Feed%3A+laravelnews
ingested: 2026-07-17
sha256: 12e2030141a64e597780cda4e6c9bf52efd2b1d858b6d749d5b16ca10430c93b
blog_source: Laravel News
---
First-Party Image Processing in Laravel 13.20 - Laravel News
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
- - - 
{
this.mobileMenuIsOpen = false;
this.searchModalIsOpen = false;
});
},
}"
>
 
[
![Laravel News](https://picperf.io/https://laravel-news.com/images/logo.svg)
Laravel News
](/)
[
Blog
](/blog)
[
Tutorials
](/category/tutorials)
[
Packages
](/category/packages)
[
Newsletter
](/newsletter)
[
Podcasts
](/podcasts)
[
Partners
](/partners)
[
Links
](/links)
[
Your Account
](/login)
![Search](https://picperf.io/https://laravel-news.com/images/icons/search.svg)
Search
![Menu](https://picperf.io/https://laravel-news.com/images/icons/menu.svg)
Menu
[
![Laravel News](https://picperf.io/https://laravel-news.com/images/logo.svg)
## Laravel News
](/)
Close menu
![Close menu](https://picperf.io/https://laravel-news.com/images/icons/close.svg)
[
Blog
](/blog)
[
Tutorials
](/category/tutorials)
[
Packages
](/category/packages)
[
Podcasts
](/podcasts)
[
Newsletter
](/newsletter)
[
Community Links
](/links)
[
Partners
](/partners)
---
[
Your Account
](/login)
[
Advertising
](/partnerships)
{
if (! this.initialized) {
search.start();
this.initialized = true;
}
if (value) {
setTimeout(() => {
this.$el.querySelector('input').focus();
}, 100);
}
});
},
}"
x-dialog
x-model="searchModalIsOpen"
x-cloak
@keydown.slash.meta.window="searchModalIsOpen = !searchModalIsOpen"
@keydown.k.meta.window="searchModalIsOpen = !searchModalIsOpen"
@keydown.escape.window="searchModalIsOpen = false"
>
## Search Articles
Close search
![Close menu](https://picperf.io/https://laravel-news.com/images/icons/close.svg)
Or try
[
paginated search →
](/search)
- 
# First-Party Image Processing in Laravel 13.20
Last updated on
July 14th, 2026
by
[
Paul Redmond
](/@paulredmond)
![First-Party Image Processing in Laravel 13.20 image](https://picperf.io/https://laravelnews.s3.amazonaws.com/featured-images/laravel-13-featured.png)
Laravel 13.20.0 adds first-party image processing to the framework, with an immutable, driver-based API for transforming images that come from uploads, storage, URLs, or raw bytes. The release also brings a `WithoutMiddleware` controller attribute, a dedicated session prefix for Redis, and a batch of Eloquent and queue additions.
- First-party image processing via the new `Image` facade
- A new `#[WithoutMiddleware]` controller attribute
- Configure a separate Redis prefix for sessions
- Quietly increment and decrement on Eloquent models
- Enums accepted as `WithoutOverlapping` queue keys
- And more
## #What's New
### #First-Party Image Processing
Laravel 13.20 introduces an `Illuminate\Image` component that handles resizing, cropping, format conversion, and storage without reaching for a third-party wrapper.
Images are immuta

## Summary

ble: every transformation returns a new instance, and the queued transformations are applied when you ask for the result.
The most common path starts with an upload. `Request::image()` returns an `Image` instance for a given file key, or `null` if the key does not hold an uploaded file:
```
$request->image('avatar') ->cover(200, 200) ->toWebp() ->store('avatars');
```
You can also build an image from a path, a URL, raw bytes, base64, or a storage disk:
```
Image::fromPath('/path/to/photo.jpg');Image::fromUrl('https://example.com/photo.jpg');Image::fromBytes($bytes);Image::fromStorage('photos/avatar.jpg', 's3'); Storage::disk('s3')->image('photos/avatar.jpg');
```
Transformations, output options, and inspection methods are all available on the instance:
```
// Transformations...$image->cover(200, 200);$image->contain(800, 600);$image->crop(200, 200);$image->resize(1024, 768);$image->scale(1200, 800);$image->rotate(90);$image->blur(10);$image->sharpen(10);$image->grayscale();$image->flip();$image->flop();$image->orient(); // Applies EXIF rotation... // Output format and quality...$image->toWebp();$image->toJpg()->quality(80);$image->optimize(); // WebP at quality 70...$image->optimize('jpg', 85); // Reading and inspecting...$image->toBytes();$image->toBase64();$image->toDataUri();$image->width();$image->height();$image->dimensions();$image->mimeType();$image->extension();
```
Because instances are immutable, you can branch from one source image to produce several variants:
```
$image = $request->image('photo'); $image->cover(200, 200)->toWebp()->store('thumbnails');$image->grayscale()->toWebp()->store('grayscale');
```
Two drivers ship with the component, both backed by Intervention Image v4: GD and Imagick. You can pick a driver per image, and the `Image` facade lets you override how a driver handles a given transformation:
```
use Illuminate\Image\Transformations\Sharpen; // Pick a driver per image...$image->using('imagick');$image->usingGd();$image->usingImagick(); // Override how a driver handles a transformation...Image::transformUsing('gd', Sharpen::class, function ($image, Sharpen $sharpen) { // Custom sharpen handling for the GD driver...  return $image;});
```
Intervention Image is a suggested dependency rather than a required one, so you install it yourself:
```
composer require intervention/image
```
See [#59276](https://github.com/laravel/framework/pull/59276).
### #A `#[WithoutMiddleware]` Controller Attribute
The routing attributes gain a counterpart to `#[Middleware]`. Where the latter attaches middleware to a controller class or method, `#[WithoutMiddleware]` excludes it, giving you the "excluding middleware" behavior of route groups at the attribute level:
```
use App\Http\Middleware\EnsureTokenIsValid;use Illuminate\Routing\Controllers\Attributes\Middleware;use Illuminate\Routing\Controllers\Attributes\WithoutMiddleware; #[Middleware(EnsureTokenIsValid::class)]class UserController{ public function index() { // Middleware applies h

## Related Articles

- [[build-a-laravel-scout-search-endpoint-with-the-http-query-method]]
- [[enforce-per-action-waiting-periods-in-laravel-with-cooldown]]
- [[the-illustrated-stable-diffusion-2026-07-07]]
- [[release-v0251]]
- [[workers-cache]]
