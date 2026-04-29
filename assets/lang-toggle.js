// Sitewide EN/CY language preference handling for async-digital.com.
//
// Cooperates with the existing static `<p class="lang-switch">` markup
// (privacy/, audient/, four-blocker/). When a visitor clicks a language
// link, their choice is stored in localStorage. On subsequent visits to
// any page that has hreflang alternates, the script redirects to the
// preferred language if the current page's <html lang> differs.
//
// Detect-and-bail by design:
//   - No `.lang-switch` block on the page → no click handlers attached.
//   - No `<link rel="alternate" hreflang>` tags → no redirect.
//   - localStorage unavailable (private mode, disabled) → silent no-op.
//
// Loaded only by async-digital-site pages. Not bundled into brand.js
// because brand.js is cross-loaded by audient-site and speed-to-lead-site.
(function () {
  "use strict";

  var STORAGE_KEY = "async-digital-lang";

  function readPref() {
    try {
      return window.localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function writePref(value) {
    try {
      window.localStorage.setItem(STORAGE_KEY, value);
    } catch (e) {
      // private mode or storage disabled — fall through silently
    }
  }

  function maybeRedirect() {
    var pref = readPref();
    if (!pref) return;
    var current = document.documentElement.lang || "en-GB";
    if (pref === current) return;

    var alts = document.querySelectorAll('link[rel="alternate"][hreflang]');
    for (var i = 0; i < alts.length; i++) {
      var hl = alts[i].getAttribute("hreflang");
      if (hl === pref && hl !== current) {
        window.location.replace(alts[i].href);
        return;
      }
    }
  }

  function attachClickPersist() {
    var links = document.querySelectorAll(".lang-switch a[lang]");
    for (var i = 0; i < links.length; i++) {
      links[i].addEventListener("click", function (e) {
        var chosen = e.currentTarget.getAttribute("lang");
        if (chosen) writePref(chosen);
      });
    }
  }

  function init() {
    maybeRedirect();
    attachClickPersist();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
