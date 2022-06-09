import subprocess


# uses Phil Harvey exif tool
class exifTool:
    @staticmethod
    def extract_tag_data(tags, file):
        return str(subprocess.run(["exiftool"] + tags + [file], stdout=subprocess.PIPE).stdout)

    @staticmethod
    def replace_gps(file, coordinates, overwrite_original, ignore_warning):
        command = ["exiftool", f"-GPSLatitude={coordinates[0]}", f"-GPSLongitude={coordinates[1]}"]
        if overwrite_original:
            command += ["-overwrite_original"]
        if ignore_warning:
            command += ["-m"]

        return str(subprocess.run(command + [file], stdout=subprocess.PIPE).stdout)
