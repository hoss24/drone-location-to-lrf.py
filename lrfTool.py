# from lat_lon_parser import lat_long


class lrfTool:
    # return the laser range finder latitude and longitude from the image metadata
    # file_tag_data must include "-GPSStatus", "-LRFStatus", "-LRFTargetLon", "-LRFTargetLat"
    @staticmethod
    def get_lat_lon(file_tag_data):
        # lrf property is valid only if LRFStatus is "Normal" and (drone) GpsStatus is "GPS" or "RTK".
        if "Normal" in file_tag_data and any(item in file_tag_data for item in ["GPS", "RTK"]):
            # string manipulation to pull out lat and lon values
            # removing beginning of string (everything before ": ") and end (\n') of string
            # partition taking second part, split, then strip off end
            lrf_lat = file_tag_data.partition("LRF Target Lat                  : ")[2].split(r"LRF", 1)[0].rstrip(
                r"\\n'")
            lrf_lon = file_tag_data.partition("LRF Target Lon                  : ")[2].split(r"LRF", 1)[0].rstrip(
                r"\\n'")
            return lrf_lat, lrf_lon

    # @staticmethod
    # # input Decimal Degrees (ex: 31.3420215) return formatted Degrees Minutes Seconds (ex: 28 deg 44\' 56.31" N)
    # # exiftool does not require conversion to write metadata
    # def to_deg_min_sec_cardinal(decimal_coordinates):
    #     # used to round seconds
    #     def round_traditional(val, digits):
    #         return round(val + 10 ** (-len(str(val)) - 1), digits)
    #
    #     def convert_format(dec_coordinates, card_direction):
    #         deg_min_sec = lat_long.to_deg_min_sec(dec_coordinates)
    #         format_deg = int(deg_min_sec[0])
    #         format_min = int(deg_min_sec[1])
    #         format_sec = round_traditional(deg_min_sec[2], 2)
    #         deg_min_sec_cardinal = f'{format_deg} deg {format_min}\' {format_sec}" {card_direction}'
    #         return deg_min_sec_cardinal
    #
    #     # positive latitudes are north of the equator, negative latitudes are south of the equator
    #     if float(decimal_coordinates[0]) >= 0.0:
    #         cardinal = "N"
    #     else:
    #         cardinal = "S"
    #     formatted_lat = convert_format(float(decimal_coordinates[0]), cardinal)
    #
    #     # positive longitudes are east of the Prime Meridian, negative longitudes are west of the Prime Meridian
    #     if float(decimal_coordinates[1]) >= 0.0:
    #         cardinal = "E"
    #     else:
    #         cardinal = "W"
    #     formatted_lon = convert_format(float(decimal_coordinates[1]), cardinal)
    #
    #     return formatted_lat, formatted_lon
