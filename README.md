# GeoIPTracer

An application that creates json for [geojson.io](geojson.io).

# How to use:

Run the following django commands:
```
python manage migrate
python manage runserver
```

Then launch `bot1.py` with `python bot1.py`. Provide a seed website and let it run.
Every now and then you can check out `127.0.0.1:8000/geojson/` and copy the json
and put it into [geojson.io](geojson.io).

## Example Run:


```
bot1.py

Seed: http://www.google.com
1 216.58.193.100 -> 216.58.193.110
2 216.58.193.110 -> 216.58.193.110
3 216.58.193.110 -> 23.235.46.73
4 216.58.193.110 -> 170.149.159.130
5 216.58.193.110 -> 70.96.0.8
6 216.58.193.110 -> 70.96.0.8
7 216.58.193.110 -> 68.71.212.186
...
18 216.58.193.110 -> 52.27.112.186
19 216.58.193.110 -> 148.62.5.86
20 216.58.193.110 -> 67.192.6.224
21 216.58.193.110 -> 70.96.0.16
22 216.58.193.110 -> 52.4.131.106
23 216.58.193.110 -> 208.111.178.243
24 216.58.193.110 -> 64.94.90.198
25 216.58.193.110 -> 70.96.0.8
26 216.58.193.110 -> 70.96.0.18
27 216.58.193.110 -> 192.0.79.32
28 148.62.5.86 -> 148.62.5.86

```


```
http://127.0.0.1:8000/geojson

{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-82.3529, 28.1203], [-82.3529, 28.1203]]}, "properties": {"from_ip": "100.3.138.228", "to_ip": "100.3.138.229"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-122.0574, 37.4192], [-122.0574, 37.4192]]}, "properties": {"from_ip": "216.58.216.132", "to_ip": "216.58.193.110"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-122.0574, 37.4192], [-122.0574, 37.4192]]}, "properties": {"from_ip": "216.58.193.110", "to_ip": "216.58.193.78"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-122.0574, 37.4192], [-122.3933, 37.7697]]}, "properties": {"from_ip": "216.58.193.110", "to_ip": "23.23...

...tring", "coordinates": [[116.391248, 39.9059631], [116.391248, 39.9059631]]}, "properties": {"from_ip": "203.205.150.26", "to_ip": "180.149.134.141"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[116.391248, 39.9059631], [116.391248, 39.9059631]]}, "properties": {"from_ip": "203.205.150.26", "to_ip": "54.223.113.236"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-2.2385271, 53.4768564], [-111.6585336, 40.2338438]]}, "properties": {"from_ip": "69.58.188.40", "to_ip": "50.87.248.95"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-2.2385271, 53.4768564], [-71.0956777766393, 42.3583961]]}, "properties": {"from_ip": "69.58.188.40", "to_ip": "104.126.153.243"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-2.2385271, 53.4768564], [-87.6244211, 41.8755546]]}, "properties": {"from_ip": "69.58.188.40", "to_ip": "23.235.40.84"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[116.391248, 39.9059631], [114.600869096993, 38.10071215]]}, "properties": {"from_ip": "203.205.150.26", "to_ip": "60.6.197.39"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-2.2385271, 53.4768564], [-87.6244211, 41.8755546]]}, "properties": {"from_ip": "69.58.188.40", "to_ip": "23.235.37.217"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[116.391248, 39.9059631], [113.533050689617, 23.22589025]]}, "properties": {"from_ip": "203.205.150.26", "to_ip": "112.90.77.139"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-83.221873, 42.4733689], [-87.6244211, 41.8755546]]}, "properties": {"from_ip": "104.207.232.191", "to_ip": "104.156.81.84"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-77.1776326, 38.9342888], [-77.1776326, 38.9342888]]}, "properties": {"from_ip": "148.62.5.86", "to_ip": "148.62.5.86"}}]}

```
