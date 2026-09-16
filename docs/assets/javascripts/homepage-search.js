document.addEventListener("DOMContentLoaded", function () {
  var trigger = document.getElementById("tron-search-trigger");
  var toggle = document.querySelector('[data-md-toggle="search"]');
  var realInput = document.querySelector(".md-search__input");

  if (!trigger || !toggle || !realInput) return;

  trigger.readOnly = true;

  function openRealSearch() {
    if (!toggle.checked) {
      toggle.checked = true;
      // Setting .checked alone doesn't fire "change" — Material's own
      // search engine (index loading, results wiring) listens for that
      // event, so without it the popup can appear empty/dead.
      toggle.dispatchEvent(new Event("change", { bubbles: true }));
    }
    window.setTimeout(function () {
      realInput.focus();
    }, 0);
  }

  trigger.addEventListener("mousedown", function (event) {
    event.preventDefault();
    openRealSearch();
  });

  trigger.addEventListener("focus", openRealSearch);
});
