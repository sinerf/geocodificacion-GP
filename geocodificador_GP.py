def geocodificarOSM(direccion):
    from geopy.geocoders import Nominatim
    import arcpy
    arcpy.env.overwriteOutput = True
    geolocalizador = Nominatim(user_agent="Google Chrome")
    # direccion= str(input("Escribe una direccion "))
    direccionesGeo = geolocalizador.geocode(direccion, timeout=15)

    coordenadas=(str(direccionesGeo.latitude)+","+str(direccionesGeo.longitude),)
    print(coordenadas)


    # # Create an in_memory feature class to initially contain the coordinate pairs
    feature_class = arcpy.CreateFeatureclass_management(
        "in_memory", "tempfc", "POINT",spatial_reference="4326")[0]
    print(feature_class)
    feature_set = arcpy.FeatureSet()
    feature_set.load(feature_class)
    #
    # # # Open an insert cursor
    cursor= arcpy.da.InsertCursor(feature_class, ["SHAPE@XY"])
    cursor.insertRow(coordenadas)
    # # # Create a FeatureSet object and load in_memory feature class
    feature_set = arcpy.FeatureSet()
    feature_set.load(feature_class)


if __name__ == "__main__":
    geocodificarOSM(arcpy.GetParameterAsText(0))