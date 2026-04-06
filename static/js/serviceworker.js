// Service Worker for ProjectSite PWA

// Install Event - Cache static assets
self.addEventListener('install', function(e) {
    console.log('Service Worker: Installing...');
    e.waitUntil(
        caches.open('projectsite-cache-v1').then(function(cache) {
            console.log('Service Worker: Caching Files');
            return cache.addAll([
                '/',
                '/static/css/bootstrap.min.css',
                '/static/js/main.js',
            ]);
        })
    );
});

// Fetch Event - Serve cached content when offline
self.addEventListener('fetch', function(e) {
    console.log('Service Worker: Fetching');
    e.respondWith(
        caches.match(e.request).then(function(response) {
            // Return cached version or fetch from network
            return response || fetch(e.request);
        })
    );
});