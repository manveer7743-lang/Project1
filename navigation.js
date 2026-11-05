"use strict";

const page = document.querySelector(".page");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
let navigationPending = false;

document.addEventListener("click", (event) => {
  const link = event.target.closest("a");
  if (
    !page ||
    !link ||
    event.defaultPrevented ||
    event.button !== 0 ||
    event.metaKey ||
    event.ctrlKey ||
    event.shiftKey ||
    event.altKey ||
    link.target ||
    link.hasAttribute("download") ||
    reduceMotion.matches
  ) {
    return;
  }

  const destination = new URL(link.href, window.location.href);
  if (
    destination.origin !== window.location.origin ||
    destination.pathname === window.location.pathname
  ) {
    return;
  }

  event.preventDefault();
  if (navigationPending) {
    return;
  }

  navigationPending = true;
  page.classList.add("is-leaving");
  window.setTimeout(() => window.location.assign(destination.href), 180);
});
