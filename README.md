python-geoio
============

Python bindings for the geo.io API. (http://geo.io)

##Installation 
You can install the package from pypi:
```
pip install python-figo
```
Or from source:
```
git clone git@github.com:geoio/python-geoio.git
cd python-geoio
python setup.py install

```

##Usage 
```python
# coding: utf-8

from geoio import GeoioClient

client = GeoioClient("YOUR_API_KEY")

client.geocoding("Deichstraße 27 Hamburg")
client.geocoding(["Deichstraße 27 Hamburg", "Willy-Brandt-Straße 1, 10557 Berlin, Deutschland"])

client.reverse_geocoding({"lat":53.54604, "lon":9.98744})
client.reverse_geocoding([{"lat":53.54604, "lon":9.98744}, {"lat":52.5201891, "lon":13.3691599542106, "max_rank": "gt_street"}])
```
