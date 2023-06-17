# Grafana Text Panel snippets


## About

Ready-to-run implementations for [Grafana Text Panel]'s HTML display mode.


## Details

### Embedding remote images, with interval-based refresh and cache busting

A HTML/JavaScript component, which applies refreshing to all image elements in the
HTML body, which have a `data-refresh` attribute.

It will also handle cache busting properly, by appending a `?nocache=` query parameter
with a random value to the image source URL.

The refresh rate is the value of the `data-refresh` attribute. The unit is "seconds".
Individual images can have individual refresh rates.
```html
<img width="640" src="https://www.euse.de/honig/beescale/latest_b-cam1.jpg" data-refresh="10"/>
<img width="640" src="https://www.euse.de/honig/beescale/latest_b-cam2.jpg" data-refresh="15"/>
```

Reference: https://community.hiveeyes.org/t/panel-fur-webcam-bild-das-regelmassig-aktualisiert-wird/4921


[Grafana Text Panel]: https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/text/
