import random
from datetime import datetime

from com.taxicoop.model.Location import Location
from com.taxicoop.service.DBHelper import DB_Helper


class LocationPublisher:

    @staticmethod
    def publish_location():
        print("Location publish called {}".format(datetime.now()))

        if DB_Helper.get_locations_count() > 0:
            return

        taxis = DB_Helper.get_all_taxis()

        for taxi in taxis:
            loc = taxi['location']
            coordinates = loc['coordinates']
            longitude = float(coordinates[0])
            latitude = float(coordinates[1])

            longitude = round(random.uniform(longitude, longitude + random.uniform(-0.9999999, 0.9999999)), 10)
            latitude = round(random.uniform(latitude, latitude + random.uniform(-0.9999999, 0.9999999)), 10)

            final_location = Location(entity_id=taxi['taxi_id'], status=taxi['status'], entity_type='Taxi',
                                      latitude=latitude, longitude=longitude, vehicle_type=taxi['type'])
            DB_Helper.publish_taxi_location(final_location)
