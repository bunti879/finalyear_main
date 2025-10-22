const CACHE_NAME = "agricare-cache-v1";
const OFFLINE_URL = "/offline.html";

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll([ "/", OFFLINE_URL ]))
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request) || caches.match(OFFLINE_URL))
  );
});

self.addEventListener("push", event => {
  const data = event.data ? event.data.json() : {};
  event.waitUntil(
    self.registration.showNotification(data.title || "AgriCare Alert", {
      body: data.body || "New update available",
      icon: "/static/icons/icon-192.png"
    })
  );
});
