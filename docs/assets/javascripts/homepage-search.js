document.addEventListener("DOMContentLoaded", function () {
  var trigger = document.getElementById("tron-search-trigger");
  var toggle = document.querySelector('[data-md-toggle="search"]');
  var realInput = document.querySelector(".md-search__input");

  if (!trigger || !toggle || !realInput) return;

  // The homepage box never holds its own text or its own search logic —
  // it only opens Material's real search and hands it keyboard focus.
  trigger.readOnly = true;

  function openRealSearch() {
    toggle.checked = true;
    realInput.focus();
  }

  trigger.addEventListener("mousedown", function (event) {
    event.preventDefault(); // stop the readonly field from taking focus itself
    openRealSearch();
  });

  trigger.addEventListener("focus", openRealSearch);
});
