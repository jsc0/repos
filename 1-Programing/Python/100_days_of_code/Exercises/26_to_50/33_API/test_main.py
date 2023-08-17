
MY_LAT = 55.953251 # Your latitude
MY_LONG = -3.188267 # Your longitude





iss_latitude = 51.54
iss_longitude = 1


if int(iss_latitude) in range(50, 60) and int(iss_longitude) in range(2, -9, -1):

    sunrise = 4
    sunset = 19

    hour = 21
    if hour >= sunset or hour <= sunrise:
        print("Ullet")

    else:
        print("No ISS")






