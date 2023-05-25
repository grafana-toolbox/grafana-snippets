# Grafana Text Panel snippets


## About

Ready-to-run implementations for [Grafana Text Panel]'s HTML display mode.


## Details

### Embedding remote images, with interval-based refresh and cache busting

A HTML/JavaScript component, which applies refreshing to an image in the HTML body.
It will also handle cache busting properly, by appending a `?nocache=` query parameter
with a random value to the image source URL.

The refresh rate can be determined with the `data-refresh` attribute. The unit is "seconds".
```html
<img id="image" src="https://www.euse.de/honig/beescale/latest.jpg" data-refresh="30" />
```

Reference: https://community.hiveeyes.org/t/panel-fur-webcam-bild-das-regelmassig-aktualisiert-wird/4921


[Grafana Text Panel]: https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/text/
