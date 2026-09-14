document.addEventListener("DOMContentLoaded", function () {
  var trigger = document.getElementById("tron-search-trigger");
  if (!trigger) return;

  trigger.addEventListener("click", function () {
    var toggle = document.querySelector('[data-md-toggle="search"]');
    if (toggle) {
      toggle.checked = true;
      toggle.dispatchEvent(new Event("change"));
    }
    var input = document.querySelector(".md-search__input");
    if (input) {
      window.setTimeout(function () {
        input.focus();
      }, 50);
    }
  });
});
