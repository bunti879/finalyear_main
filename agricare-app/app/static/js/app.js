if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("/static/service-worker.js")
    .then(() => console.log("Service Worker registered"))
    .catch(err => console.error("SW failed:", err));
}
