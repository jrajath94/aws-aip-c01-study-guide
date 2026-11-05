/* Offline treatise behavior: section filter, scroll spy, answer reveal. */
(function () {
  "use strict";

  var toc = document.getElementById("toc");
  var filter = document.getElementById("section-filter");
  var burger = document.getElementById("nav-toggle");
  var backdrop = document.getElementById("nav-backdrop");
  var progress = document.getElementById("progress");
  var headings = Array.prototype.slice.call(document.querySelectorAll("main h2[id]"));

  function closeNav() {
    document.body.classList.remove("nav-open");
    if (burger) burger.setAttribute("aria-expanded", "false");
  }
  function openNav() {
    document.body.classList.add("nav-open");
    if (burger) burger.setAttribute("aria-expanded", "true");
    if (filter) filter.focus();
  }

  if (burger) {
    burger.addEventListener("click", function () {
      if (document.body.classList.contains("nav-open")) closeNav();
      else openNav();
    });
  }
  if (backdrop) backdrop.addEventListener("click", closeNav);

  if (toc) {
    headings.forEach(function (heading) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = "#" + heading.id;
      a.textContent = heading.textContent.replace(/\s+/g, " ").trim();
      a.addEventListener("click", function () {
        if (window.matchMedia("(max-width: 960px)").matches) closeNav();
      });
      li.appendChild(a);
      toc.appendChild(li);
    });
  }

  function applyFilter() {
    var q = (filter && filter.value || "").trim().toLowerCase();
    var visible = 0;
    var links = toc ? toc.querySelectorAll("a") : [];
    Array.prototype.forEach.call(links, function (a) {
      var show = !q || a.textContent.toLowerCase().indexOf(q) !== -1;
      a.parentElement.hidden = !show;
      if (show) visible += 1;
      var id = a.getAttribute("href").slice(1);
      var topic = document.getElementById(id);
      if (topic) {
        var article = topic.closest(".topic");
        if (article) article.hidden = q ? !show : false;
      }
    });
    var empty = document.getElementById("toc-empty");
    if (empty) empty.hidden = visible !== 0;
  }
  if (filter) filter.addEventListener("input", applyFilter);

  if ("IntersectionObserver" in window && headings.length) {
    var current = null;
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        current = entry.target.id;
      });
      if (!current || !toc) return;
      Array.prototype.forEach.call(toc.querySelectorAll("a"), function (a) {
        var on = a.getAttribute("href") === "#" + current;
        if (on) a.setAttribute("aria-current", "true");
        else a.removeAttribute("aria-current");
      });
    }, { rootMargin: "-20% 0px -65% 0px", threshold: 0.01 });
    headings.forEach(function (heading) { spy.observe(heading); });
  }

  if (!CSS.supports("(animation-timeline: scroll())") && progress) {
    var ticking = false;
    var onScroll = function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var max = document.documentElement.scrollHeight - window.innerHeight;
        var ratio = max > 0 ? window.scrollY / max : 0;
        progress.style.scale = ratio + " 1";
        ticking = false;
      });
    };
    document.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  document.querySelectorAll(".pq").forEach(function (card) {
    if (card.tagName === "DETAILS") return;
    var button = card.querySelector(".pq-reveal");
    var answer = card.querySelector(".pq-answer");
    if (!button || !answer) return;
    button.setAttribute("aria-expanded", "false");
    if (answer.id) button.setAttribute("aria-controls", answer.id);
    button.addEventListener("click", function () {
      var open = card.classList.toggle("is-open");
      button.setAttribute("aria-expanded", open ? "true" : "false");
      button.textContent = open ? "Hide answer" : "Reveal answer";
    });
  });

  document.addEventListener("keydown", function (event) {
    var tag = document.activeElement && document.activeElement.tagName;
    var typing = tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT";
    if (event.key === "/" && !typing && filter) {
      event.preventDefault();
      if (window.matchMedia("(max-width: 960px)").matches) openNav();
      filter.focus();
    }
    if (event.key === "Escape") {
      if (document.body.classList.contains("nav-open")) closeNav();
      else if (filter && document.activeElement === filter) {
        filter.value = "";
        applyFilter();
        filter.blur();
      }
    }
  });
})();
