# Reproduction notes

## Current status

The script in `src/lidar2_analisis.py` is the exploratory analysis used for one case study. It is not a command-line package and needs its inputs placed next to the script. It was written for a particular 2 m raster tile and three present-day IGN stream segments; paths, identifiers, clipping extents and map coordinates are hard-coded. Outputs must not be interpreted as confirmed waterfalls, pools or burial locations.

## Inputs

The following are **not included** in this public repository:

- `mdt02_700_4736.asc`: the [MDT02 tile](https://ss3.scayle.es/lidaroutput/mdt02/nw/700_4736.asc). See the [dataset description](https://open.scayle.es/es/dataset/modelo-digital-del-terreno-mdt02), quality caveats and applicable conditions.
- `WatercourseLink.gml`: modern IGN watercourse geometry for the study area, with the expected `gml_id` values. Obtain it from the relevant IGN/CNIG source under its terms.
- `AMS_1956-1957.jpg`: a historical aerial image with the exact extent expected by the script. The historical imagery source is the [IGN WMS](https://www.ign.es/wms/pnoa-historico). A different image or extent will produce misleading alignment.

## Dependencies and execution

The script imports Python packages `numpy`, `geopandas`, `rasterio`, `scipy`, `matplotlib` and `pyproj`. Install mutually compatible versions in an isolated environment, place the appropriately sourced inputs beside the script, and run:

```sh
python src/lidar2_analisis.py
```

The output comprises a figure and JSON profiles in the script directory. The analysis assumes the projected coordinate system EPSG:25829 and a 2 m raster. Check CRS, line orientation, source dates, coverage, units and extents before interpreting results. Raster cell size is not the original LiDAR point density, and the modeled terrain is not a direct observation of 1937.

## Known limitations

The script has no automated test suite and has not been validated on arbitrary input data. It is included for transparency and review; reproducing the exact workflow requires matching the inputs and software environment. No independent confirmation of a waterfall, pool or burial follows from a generated profile.

