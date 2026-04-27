// Source of truth for Async Digital brand constants loaded by every page
// across async-digital.com and demo.async-digital.com. Mailto links marked
// with data-brand-mailto use BRAND.email (general / sales / support);
// links marked with data-brand-privacy-mailto use BRAND.privacyEmail
// (data-protection / legal / technical). Legal footer text and Organization
// JSON-LD stay static in each page for robustness.
// TEMPORARY: BRAND.email points to r.nash1 instead of h.nash1 while
// Helen's inbox is unreachable. Revert when access is restored.
// Tracked in async-digital-ltd/audient-site#25.
window.BRAND = Object.freeze({
  email: "r.nash1@async-digital.com",
  privacyEmail: "r.nash1@async-digital.com",
  companyName: "Async Digital Ltd",
  companyNumber: "16950485",
  registeredOffice: "167–169 Great Portland Street, London, W1W 5PF"
});

function applyBrandMailtos() {
  var general = document.querySelectorAll("a[data-brand-mailto]");
  for (var i = 0; i < general.length; i++) {
    general[i].href = "mailto:" + window.BRAND.email;
  }
  var privacy = document.querySelectorAll("a[data-brand-privacy-mailto]");
  for (var j = 0; j < privacy.length; j++) {
    privacy[j].href = "mailto:" + window.BRAND.privacyEmail;
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", applyBrandMailtos);
} else {
  applyBrandMailtos();
}
