// Re-runs on every page view, including instant navigation (Home button),
// because Material's document$ emits on each swap. DOMContentLoaded only
// fires once per real page load, which is why search died after navigating.
function initTronSearch() {
  var trigger = document.getElementById("tron-search-trigger");
  var toggle = document.querySelector('[data-md-toggle="search"]');
  var realInput = document.querySelector(".md-search__input");

  if (!trigger || !toggle || !realInput) return;
  if (trigger.dataset.bound) return; // the trigger is a new element after each swap
  trigger.dataset.bound = "1";

  trigger.readOnly = true;

  function openRealSearch() {
    if (!toggle.checked) {
      toggle.checked = true;
      // .checked alone doesn't fire "change"; Material's search listens for it.
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
}

if (typeof document$ !== "undefined") {
  document$.subscribe(initTronSearch);
} else {
  document.addEventListener("DOMContentLoaded", initTronSearch);
}
