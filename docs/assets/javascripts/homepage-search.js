document.addEventListener("DOMContentLoaded", function () {
  var trigger = document.getElementById("tron-search-trigger");
  var toggle = document.querySelector('[data-md-toggle="search"]');
  var realInput = document.querySelector(".md-search__input");

  if (!trigger || !toggle || !realInput) return;

  function openRealSearch() {
    toggle.checked = true;
    window.setTimeout(function () {
      realInput.focus();
    }, 60);
  }

  trigger.addEventListener("focus", openRealSearch);
  trigger.addEventListener("click", openRealSearch);
});
