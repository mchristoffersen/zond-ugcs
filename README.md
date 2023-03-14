# readZond
Python reader for Zond Aero 500 GPR SEG-Y files

This program reads in a Zond Aero 500 SEG-Y file and its associated CSV position file, then returns a dictionary containing information from the SEG-Y and position file. The dictionary's contents are specified below:

    dataDict = {
        "bscan": bscan,           # The BScan or radargram, data acquired by the GPR (size: mxn)
        "lon": lon,               # Longitude of the UAS (WGS84) (size: n)
        "lat": lat,               # Latitude of the UAS (WGS84) (size: n)
        "hgt": hgt,               # Height of the UAS about the WGS84 ellipsoid (size: n)
        "agl": agl,               # Height of the UAS above ground (size: n)
        "speed": speed,           # Speed of the UAS (m/s) (size: n)
        "rtkMask": rtkMask,       # Mask for lon, lat, and hgt fields denoting which entries come from RTK (True == RTK) (size: n)
        "altMask": aglMask,       # Mask for agl field denoting which entries come from laser altimeter (True == altimeter) (size: n)
        "speedMask": speedMask,   # Mask for speed field denoting which entries are not nan (True == not nan) (size: n)
        "time": time,             # Time of the acquisition of each trace (size: n)
        "dt": dt,                 # Fast time sampling interval of the GPR (size: 1)
    }
    
To install:

    pip install git+https://github.com/mchristoffersen/zond_ugcs

Then to run:

    import zond_ugcs
    data = zond_ugcs.read("your_data_file.sgy")
