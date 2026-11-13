/* MZE Digital — site interactions */
(function () {
  document.documentElement.classList.remove("no-js");

  // sticky header border on scroll
  var header = document.querySelector(".site-header");
  function onScroll() { if (header) header.classList.toggle("is-scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  // mobile navigation
  var toggle = document.querySelector(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () { document.body.classList.remove("nav-open"); toggle.setAttribute("aria-expanded", "false"); });
    });
  }

  // reveal on scroll
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else { items.forEach(function (el) { el.classList.add("in"); }); }

  // filters (projects, blog)
  var filters = document.querySelectorAll("[data-filter]");
  filters.forEach(function (btn) {
    btn.addEventListener("click", function () {
      filters.forEach(function (b) { b.classList.remove("active"); });
      btn.classList.add("active");
      var f = btn.getAttribute("data-filter");
      document.querySelectorAll("[data-cat]").forEach(function (card) {
        card.classList.toggle("is-hidden", f !== "all" && card.getAttribute("data-cat").indexOf(f) === -1);
      });
    });
  });

  // forms
  // - If the form has an action URL (e.g. a Formspree endpoint), it is submitted with fetch.
  // - With no action, it shows a front-end confirmation only (useful while developing).
  document.querySelectorAll("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var hp = form.querySelector(".hp input");
      if (hp && hp.value) return; // spam honeypot
      var action = form.getAttribute("action");
      function done(ok) {
        form.classList.remove("sent", "failed");
        form.classList.add(ok ? "sent" : "failed");
        if (ok) form.querySelectorAll("input, textarea, select, button").forEach(function (el) { el.disabled = true; });
      }
      if (!action) { done(true); return; }
      fetch(action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (r) { done(r.ok); })
        .catch(function () { done(false); });
    });
  });

  // current year
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
