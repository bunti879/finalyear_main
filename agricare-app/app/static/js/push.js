async function subscribeToPush() {
  if (!("serviceWorker" in navigator)) return;
  const reg = await navigator.serviceWorker.ready;
  const sub = await reg.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: "<PUBLIC_VAPID_KEY>"
  });
  await fetch("/notify/subscribe", {
    method: "POST",
    body: JSON.stringify(sub),
    headers: {"Content-Type": "application/json"}
  });
  console.log("Subscribed:", sub);
}
