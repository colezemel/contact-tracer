import requests
import gpxpy
import gpxpy.gpx


# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("https://www.strava.com/oauth/authorize")

# Print the status code of the response.
print(response.status_code)




# # Parsing an existing file:
# # -------------------------

# gpx_file = open('test_files/cerknicko-jezero.gpx', 'r')

# gpx = gpxpy.parse(gpx_file)

# for track in gpx.tracks:
#     for segment in track.segments:
#         for point in segment.points:
#             print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

# for waypoint in gpx.waypoints:
#     print('waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude))

# for route in gpx.routes:
#     print('Route:')
#     for point in route.points:
#         print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

# # There are many more utility methods and functions:
# # You can manipulate/add/remove tracks, segments, points, waypoints and routes and
# # get the GPX XML file from the resulting object:

# print('GPX:', gpx.to_xml())