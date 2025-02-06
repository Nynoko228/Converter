class AllUnits:
    pressure_units = {
        "Pa": 1,
        "kiloPa": 1000,
        "MegaPa": 1000000,
        "bar": 100000,
        "atm": 101325,
        "cmHg": 1333.22,  # centimeters of mercury
        "dyne/cm2": 0.1, # dyne per square centimeter
        "inches of mercury": 3386.39,   # inches of mercury
        "kg/cm2": 98066.5,  # kilogram per square centimeter
        "kg/m2": 9.80665,   # kilogram per square meter
        "microbar": 0.1, # microbar (same as dyne/cm2)
        "millibar": 100,
        "millimeters of mercury": 133.322,  # millimeters of mercury
        "pound/foot2": 47.8803,  # pound per square foot
        "pound/inch2": 6894.76,   # pound per square inch (PSI)
        "PSI": 6894.76,      # PSI
        "ton/ft2": 95760.52, # ton (short ton) per square foot
        "ton/in2": 13789514.56, # ton (short ton) per square inch
        "torr": 133.322,     # Torr
    }

    speed_units = {
        "m/s": 1,
        "km/h": 1000 / 3600,  # 1 km = 1000 m, 1 h = 3600 s
        # "mph": 0.44704,
        "knot": 0.514444,
        "c": 299792458,  # Speed of light in m/s
        "cm/h": 0.01 / 3600,  # 1 cm = 0.01 m, 1 h = 3600 s
        "cm/min": 0.01 / 60,  # 1 cm = 0.01 m, 1 min = 60 s
        "cm/s": 0.01,  # 1 cm = 0.01 m
        "ft/h": 0.3048 / 3600,  # 1 ft = 0.3048 m, 1 h = 3600 s
        "ft/min": 0.3048 / 60,  # 1 ft = 0.3048 m, 1 min = 60 s
        "ft/s": 0.3048,  # 1 ft = 0.3048 m
        "km/min": 1000 / 60,  # 1 km = 1000 m, 1 min = 60 s
        "km/s": 1000,  # 1 km = 1000 m
        "m/h": 1 / 3600,  # 1 h = 3600 s
        "m/min": 1 / 60,  # 1 min = 60 s
        "mile/h": 1609.34 / 3600,  # 1 mile = 1609.34 m, 1 h = 3600 s
        "mile/min": 1609.34 / 60,  # 1 mile = 1609.34 m, 1 min = 60 s
        "mile/s": 1609.34,  # 1 mile = 1609.34 m
        "mach": 343,  # Speed of sound in dry air at 20°C, approximately
    }