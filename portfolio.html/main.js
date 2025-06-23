$('.count').each(function() {
  var $this = $(this);
  var target = +$this.data('target');

  $this.prop('Counter', 0).animate(
    { Counter: target },
    {
      duration: 2000,
      easing: 'swing',
      step: function(now) {
        $this.text(Math.ceil(now));
      },
      done: function() {
        $this.text(target); // ensure exact final value
      }
    }
  );
});
