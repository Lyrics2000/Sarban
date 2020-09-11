
import googlemaps
API_KEY = 'AIzaSyBl42X__wu7wo1SGMKFRTu_8coRmMMnfXw'

gmap_key = googlemaps.Client(key = API_KEY)
#owner location
newport_ri = (37.0816944, -1.1650679)


def distancePriceCalculator(distance):
    if distance >=300:
        return 800
    else:
        return 200