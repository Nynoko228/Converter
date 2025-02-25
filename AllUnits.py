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

    # Новое снизу

    concentration_units = {
      "kilomole/metric (kmol/mi)": 1,  # Основа
      "micromole/centimeters (umol/cmi)": 0.001,  # umol/cm3 -> kmol/m3
      "micromole/decimeter (umol/dmi)": 0.000001, #umol/dm3 -> kmol/m3
      "micromole/liter (umol/L)": 0.000001,  # umol/L -> kmol/m3
      "millimole/centimeters (mmol/cmi)": 1, #mmol/cm3 -> kmol/m3
      "millimole/decimeter (mmol/dmi)": 0.001, #mmol/dm3 -> kmol/m3
      "millimoles/liter (mmol/L)": 0.001, #mmol/L -> kmol/m3
      "millimole/meteri (mmol/mi)": 0.000001, #mmol/m3 -> kmol/m3
      "millimole/milliliter (mmol/mL)": 1, #mmol/mL -> kmol/m3
      "mole/decimeter (mol/dmi)": 1, #mol/dm3 -> kmol/m3
      "mole/liter (mol/L)": 1, #mol/L -> kmol/m3  (исправлено: 1)
      "mole/meteri (mol/mi)": 0.001, #mol/m3 -> kmol/m3 (исправлено: 1)
      "one elementary entity/meter": 1/(6.02214076 * (10**23) * 1000)  # single entity/m3 -> kmol/m3
    }

    density_units = {
        "gram/centimeter": 1000,  # грамм на кубический сантиметр (альтернативное обозначение)
        "gram/meter": 0.001,  # грамм на кубический метр
        "kilogram/meter": 1,  # килограмм на кубический метр (альтернативное обозначение)
        "milligram/meter": 0.000001,  # миллиграмм на кубический метр
        "ounce/gallon": 7.48915,  # унция на галлон (США)
        "pound/foot": 16.0185,  # фунт на кубический фут (альтернативное обозначение)
        "pound/inch": 27679.9,  # фунт на кубический дюйм (альтернативное обозначение)
        "ton/yardi": 1328.94,  # тонна на кубический ярд
    }

    distance_units = {
        "centimeter (cm)": 0.01,
        "dekameter (dm)": 10,
        "foot (ft)": 0.3048,
        "furlong": 201.168,
        "hectometer (hm)": 100,
        "inch (in)": 0.0254,
        "kilometer (km)": 1000,
        "lightyear": 9.461e+15,
        "meter (m)": 1,
        "micrometer (um)": 1e-6,
        "mil (mil)": 0.0000254,  # 1 mil = 0.001 inch
        "mile (mi)": 1609.34,
        "millimeter (mm)": 0.001,
        "nanometer (nm)": 1e-9,
        "nautical mile (M)": 1852,
        "parsec (pc)": 3.086e+16,
        "yard (yd)": 0.9144,
    }
    energy_units = {
        "attojoule": 1e-18,  # аттоджоуль
        "BTU": 1055.06,  # британская тепловая единица
        "calorie": 4.184,  # калория (альтернативное обозначение)
        "dyne-centimeter": 1e-7,  # дин-сантиметр (эрг)
        "electron volt": 1.60218e-19,  # электрон-вольт
        "erg": 1e-7,  # эрг
        "gigajoule": 1e9,  # гигаджоуль
        "gigawatt-hour": 3.6e12,  # гигаватт-час
        "gram force-centimeter": 9.80665e-5,  # грамм-сила-сантиметр
        "horsepower-hour": 2.68452e6,  # лошадиная сила-час
        "joule": 1,  # джоуль (альтернативное обозначение)
        "kilocalorie": 4184,  # килокалория (альтернативное обозначение)
        "kiloelectron volt": 1.60218e-16,  # килоэлектрон-вольт
        "kilojoule": 1000,  # килоджоуль (альтернативное обозначение)
        "kilowatt-hour": 3600000,  # киловатт-час (альтернативное обозначение)
        "megaelectron volt": 1.60218e-13,  # мегаэлектрон-вольт
        "megajoule": 1e6,  # мегаджоуль
        "megawatt-hour": 3.6e9,  # мегаватт-час
        "microjoule": 1e-6,  # микроджоуль
        "millijoule": 0.001,  # миллиджоуль
        "nanojoule": 1e-9,  # наноджоуль
        "newton-meter": 1,  # ньютон-метр (эквивалентен джоулю)
        "ounce force-inch": 0.00706155,  # унция-сила-дюйм
        "pound force-foot": 1.35582,  # фунт-сила-фут
        "pound force-inch": 0.112985,  # фунт-сила-дюйм
        "poundal-foot": 0.0421401,  # паундаль-фут
        "therm": 1.05506e8,  # терм
        "watt-hour": 3600,  # ватт-час (альтернативное обозначение)
        "watt-second": 1,  # ватт-секунда (эквивалентен джоулю)
    }

    flow_units = {
        "centimeteri/hour": 1e-6 / 3600,  # кубический сантиметр в час
        "centimeteri/minute": 1e-6 / 60,  # кубический сантиметр в минуту
        "centimeteri/second": 1e-6,  # кубический сантиметр в секунду
        "footi/hour": 0.0283168 / 3600,  # кубический фут в час
        "footi/minute": 0.0283168 / 60,  # кубический фут в минуту
        "footi/second": 0.0283168,  # кубический фут в секунду
        "gallon (UK)/day": 0.00454609 / 86400,  # галлон (Великобритания) в день
        "gallon (UK)/hour": 0.00454609 / 3600,  # галлон (Великобритания) в час
        "gallon (UK)/minute": 0.00454609 / 60,  # галлон (Великобритания) в минуту
        "gallon (UK)/second": 0.00454609,  # галлон (Великобритания) в секунду
        "gallon/day": 0.00378541 / 86400,  # галлон (США) в день
        "gallon/hour": 0.00378541 / 3600,  # галлон (США) в час
        "gallon/minute": 0.00378541 / 60,  # галлон (США) в минуту
        "gallon/second": 0.00378541,  # галлон (США) в секунду
        "liter/day": 0.001 / 86400,  # литр в день
        "liter/hour": 0.001 / 3600,  # литр в час
        "liter/minute": 0.001 / 60,  # литр в минуту
        "liter/second": 0.001,  # литр в секунду
        "meteri/day": 1 / 86400,  # кубический метр в день
        "meteri/hour": 1 / 3600,  # кубический метр в час (альтернативное обозначение)
        "meteri/minute": 1 / 60,  # кубический метр в минуту
        "meteri/second": 1,  # кубический метр в секунду (альтернативное обозначение)
        "milliliter/hour": 1e-6 / 3600,  # миллилитр в час
        "milliliter/minute": 1e-6 / 60,  # миллилитр в минуту
        "milliliter/second": 1e-6,  # миллилитр в секунду
        "ounce (UK)/hour": 0.0000284131 / 3600,  # унция (Великобритания) в час
        "ounce (UK)/minute": 0.0000284131 / 60,  # унция (Великобритания) в минуту
        "ounce (UK)/second": 0.0000284131,  # унция (Великобритания) в секунду
        "ounce/hour": 0.0000295735 / 3600,  # унция (США) в час
        "ounce/minute": 0.0000295735 / 60,  # унция (США) в минуту
        "ounce/second": 0.0000295735,  # унция (США) в секунду
        "yardi/hour": 0.764555 / 3600,  # кубический ярд в час
        "yardi/minute": 0.764555 / 60,  # кубический ярд в минуту
        "yardi/second": 0.764555,  # кубический ярд в секунду
    }

    force_units = {
        "dyne": 1e-5,  # дин
        "gram force": 0.00980665,  # грамм-сила
        "kilogram force": 9.80665,  # килограмм-сила (альтернативное обозначение)
        "kilonewton": 1000,  # килоньютон (альтернативное обозначение)
        "millinewton": 0.001,  # миллиньютон
        "newton": 1,  # ньютон (альтернативное обозначение)
        "ounce-force (ozf)": 0.278014,  # унция-сила
        "pound-force (Lbf)": 4.44822,  # фунт-сила (альтернативное обозначение)
    }

    light_units = {
        "lux": 1,  # люкс (базовая единица)
        "flame": 43.0556,  # флейм (1 флейм = 4 фут-канделы)
        "foot-candles": 10.7639,  # фут-канделы (альтернативное обозначение)
        "meter-candles": 1,  # метр-канделы (эквивалент люкса)
    }

    mass_units = {
        # "kg": 1,  # килограмм (базовая единица)
        # "g": 0.001,  # грамм
        # "mg": 0.000001,  # миллиграмм
        # "lb": 0.453592,  # фунт (avoirdupois)
        # "oz": 0.0283495,  # унция (avoirdupois)
        # "ton": 1000,  # метрическая тонна
        "carat": 0.0002,  # карат
        "grain (gr)": 0.0000647989,  # гран
        "gram (g)": 0.001,  # грамм (альтернативное обозначение)
        "kilogram (kg)": 1,  # килограмм (альтернативное обозначение)
        "megagram (Mg)": 1000,  # мегаграмм (эквивалент тонны)
        "microgram (ug)": 1e-9,  # микрограмм
        "milligram (mg)": 0.000001,  # миллиграмм (альтернативное обозначение)
        "ounce (avdp) (oz)": 0.0283495,  # унция (avoirdupois, альтернативное обозначение)
        "ounce (troy) (oz)": 0.0311035,  # унция (тройская)
        "pennyweight": 0.00155517,  # пеннивейт
        "pound (advp) (Ib)": 0.453592,  # фунт (avoirdupois, альтернативное обозначение)
        "pound (troy)": 0.373242,  # фунт (тройский)
        "stone": 6.35029,  # стоун
        "ton (long)": 1016.05,  # длинная тонна (Британская)
        "ton (short) (tn)": 907.185,  # короткая тонна (США)
        "tonne (metric ton) (t)": 1000,  # метрическая тонна (альтернативное обозначение)
    }

    power_units = {
        # "W": 1,  # ватт (базовая единица)
        # "kW": 1000,  # киловатт
        # "MW": 1000000,  # мегаватт
        # "hp": 745.7,  # лошадиная сила (механическая)
        "BTU/hour": 0.293071,  # BTU в час
        "BTU/minute": 17.5843,  # BTU в минуту
        "BTU/second": 1055.06,  # BTU в секунду
        "calorie/second": 4.184,  # калория в секунду
        "horsepower": 745.7,  # лошадиная сила (альтернативное обозначение)
        "kilowatt": 1000,  # киловатт (альтернативное обозначение)
        "megawatt": 1000000,  # мегаватт (альтернативное обозначение)
        "pound-feet/minute": 0.022597,  # фунт-фут в минуту
        "pound-feet/second": 1.35582,  # фунт-фут в секунду
        "watt": 1,  # ватт (альтернативное обозначение)
    }