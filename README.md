# NWS-SPATIAL: A Simple Python Wrapper Around the NWS API
The National Weather Service (NWS) provides weather warnings for all forecast zones in the US throught their [website](https://www.weather.gov/). Unfortunately, the map that provides these warnings are not interactive, and it is difficult to glean important information from them. `nws_spatial` is a simple Python library that wraps the NWS API and serves a simple Leaflet map of current alerts. The final product can be seen at [https://mt-climate-office.github.io/nws-spatial/](https://mt-climate-office.github.io/nws-spatial/). 

This package supports three types of NWS zones:
- **Forecast Zones**: Standard weather forecast zones
- **County Zones**: County-based warning zones  
- **Fire Zones**: Fire weather zones for wildfire-related alerts

# Usage

There are three main utility functions provided by this package:

1. `get_zones`: Create a GeoPandas object of the NWS forecast zones, county zones, or fire zones.
2. `get_active_alerts_from_zones`: Query the NWS API for active weather alerts in your zones.
3. `render_templates`: Create a well-formatted and easy to read .html file for each of the active alerts. These are used as popups in the Leaflet map. 