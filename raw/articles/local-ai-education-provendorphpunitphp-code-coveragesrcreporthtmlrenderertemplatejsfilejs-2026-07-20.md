---
source_url: file:///workspace/Projects/AI-Education-Pro/vendor/phpunit/php-code-coverage/src/Report/Html/Renderer/Template/js/file.js
ingested: 2026-07-20
sha256: 0a34f83ead7b6377e9fac2fdb057869f80af7564b11189627289d457e6b9a922
blog_source: local:unknown
---
  $(function() {
   var $window     = $(window)
     , $top_link   = $('#toplink')
     , $body       = $('body, html')
     , offset      = $('#code').offset().top
     , hidePopover = function ($target) {
        $target.data('popover-hover', false);

        setTimeout(function () {
         if (!$target.data('popover-hover')) {
          $target.popover('hide');
         }
        }, 300);
     };

   $top_link.hide().click(function(event) {
    event.preventDefault();
    $body.animate({scrollTop:0}, 800);
   });

   $window.scroll(function() {
    if($window.scrollTop() > offset) {
     $top_link.fadeIn();
    } else {
     $top_link.fadeOut();
    }
   }).scroll();

   $('.popin')
    .popover({trigger: 'manual'})
    .on({
     'mouseenter.popover': function () {
      var $target = $(this);
      var $container = $target.children().first();

      $target.data('popover-hover', true);

      // popover already displayed
      if ($target.next('.popover').length) {
       return;
      }

      // show the popover
      $container.popover('show');

      // register mouse events on the popover
      $target.next('.popover:not(.popover-initialized)')
       .on({
        'mouseenter': function () {
         $target.data('popover-hover', true);
        },
        'mouseleave': function () {
         hidePopover($container);
        }
       })
       .addClass('popover-initialized');
     },
     'mouseleave.popover': function () {
      hidePopover($(this).children().first());
     }
    });
  });
