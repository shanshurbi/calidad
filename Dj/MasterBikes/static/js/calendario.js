const root = document.currentScript.closest(".example");

const input = root.querySelector("sl-input");
const popup = root.querySelector("sl-popup");
const toggle = root.querySelector("sl-button");
const calendar = root.querySelector("calendar-range");

function open() {
  popup.active = true;
  requestAnimationFrame(() => calendar.focus());
}

function close() {
  popup.active = false;
  toggle.focus();
}

toggle.addEventListener("click", () => {
  popup.active? close() : open();
});

calendar.addEventListener("keydown", (e) => {
  // handle keydown event
});