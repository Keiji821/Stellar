from stellar_translate import translate
from rich.console import Console
from rich.table import Table
import exiftool
import os

console = Console()

def metadata(archive_name, route):
    try:
        os.chdir(os.path.expanduser(f"~/{route}")) 
        with exiftool.ExifToolHelper() as et:
            metadata_list = et.get_metadata([archive_name])
        data = metadata_list[0] 
        
        time = str(data.get('EXIF:DateTimeOriginal', 'N/A'))
        date_time_digitized = str(data.get('EXIF:DateTimeDigitized', 'N/A'))
        date_time_modified = str(data.get('File:FileModifyDate', 'N/A'))
        timezone = str(data.get('EXIF:OffsetTimeOriginal', 'N/A'))
        timezone_digitized = str(data.get('EXIF:OffsetTimeDigitized', 'N/A'))
        timezone_modified = str(data.get('EXIF:OffsetTime', 'N/A'))
        create_date = str(data.get('XMP:CreateDate', 'N/A'))
        modify_date = str(data.get('XMP:ModifyDate', 'N/A'))
        metadata_date = str(data.get('XMP:MetadataDate', 'N/A'))
        filesize = str(data.get('File:FileSize', 'N/A'))
        file_name = str(data.get('File:FileName', 'N/A'))
        file_extension = str(data.get('File:FileExtension', 'N/A'))
        file_type = str(data.get('File:FileType', 'N/A'))
        mime_type = str(data.get('File:MIMEType', 'N/A'))
        file_permissions = str(data.get('File:FilePermissions', 'N/A'))
        model = str(data.get('EXIF:Model', 'N/A'))
        make = str(data.get('EXIF:Make', 'N/A'))
        lens_model = str(data.get('EXIF:LensModel', 'N/A'))
        lens_make = str(data.get('EXIF:LensMake', 'N/A'))
        iso = str(data.get('EXIF:ISO', 'N/A'))
        exposure = str(data.get('EXIF:ExposureTime', 'N/A'))
        aperture = str(data.get('EXIF:FNumber', 'N/A'))
        focal = str(data.get('EXIF:FocalLength', 'N/A'))
        focal_35mm = str(data.get('EXIF:FocalLengthIn35mmFilm', 'N/A'))
        flash = str(data.get('EXIF:Flash', 'N/A'))
        white_balance = str(data.get('EXIF:WhiteBalance', 'N/A'))
        metering_mode = str(data.get('EXIF:MeteringMode', 'N/A'))
        exposure_program = str(data.get('EXIF:ExposureProgram', 'N/A'))
        exposure_compensation = str(data.get('EXIF:ExposureCompensation', 'N/A'))
        digital_zoom = str(data.get('EXIF:DigitalZoomRatio', 'N/A'))
        width = str(data.get('EXIF:ImageWidth', 'N/A'))
        height = str(data.get('EXIF:ImageHeight', 'N/A'))
        bits_per_sample = str(data.get('EXIF:BitsPerSample', 'N/A'))
        compression = str(data.get('EXIF:Compression', 'N/A'))
        color_space = str(data.get('EXIF:ColorSpace', 'N/A'))
        orientation = str(data.get('EXIF:Orientation', 'N/A'))
        software = str(data.get('EXIF:Software', 'N/A'))
        artist = str(data.get('EXIF:Artist', 'N/A'))
        description = str(data.get('XMP:Description', 'N/A'))
        author = str(data.get('XMP:Creator', 'N/A'))
        copyright = str(data.get('XMP:Rights', 'N/A'))
        title = str(data.get('XMP:Title', 'N/A'))
        latitude = str(data.get('EXIF:GPSLatitude', 'N/A'))
        longitude = str(data.get('EXIF:GPSLongitude', 'N/A'))
        latitude_ref = str(data.get('EXIF:GPSLatitudeRef', 'N/A'))
        longitude_ref = str(data.get('EXIF:GPSLongitudeRef', 'N/A'))
        altitude = str(data.get('EXIF:GPSAltitude', 'N/A'))
        altitude_ref = str(data.get('EXIF:GPSAltitudeRef', 'N/A'))
        gps_speed = str(data.get('EXIF:GPSSpeed', 'N/A'))
        gps_track = str(data.get('EXIF:GPSTrack', 'N/A'))
        gps_img_direction = str(data.get('EXIF:GPSImgDirection', 'N/A'))
        gps_dest_latitude = str(data.get('EXIF:GPSDestLatitude', 'N/A'))
        gps_dest_longitude = str(data.get('EXIF:GPSDestLongitude', 'N/A'))
        gps_date_stamp = str(data.get('EXIF:GPSDateStamp', 'N/A'))
        gps_time_stamp = str(data.get('EXIF:GPSTimeStamp', 'N/A'))
        gps_h_positioning_error = str(data.get('EXIF:GPSHPositioningError', 'N/A'))
        duration = str(data.get('QuickTime:Duration', 'N/A'))
        frame_rate = str(data.get('QuickTime:FrameRate', 'N/A'))
        video_codec = str(data.get('QuickTime:VideoCodec', 'N/A'))
        audio_codec = str(data.get('QuickTime:AudioCodec', 'N/A'))
        bitrate = str(data.get('QuickTime:Bitrate', 'N/A'))
        
        console = Console()
        console.print(" ")
        table = Table(title=translate(category="metadatainfo", type="metadatainfo_message"), title_justify="center", title_style="bold green")
        table.add_column(translate(category="ipinfo", type="information_message"), style="code", no_wrap=False)
        table.add_column(translate(category="ipinfo", type="value_message"), style="code")
        
        table.add_row(f"[bold underline][code][bold green]{translate(category='metadatainfo', type='main_message')}[/bold underline][/bold green][/code]", "")
        
        table.add_row(translate(category="metadatainfo", type="archive_name_message"), archive_name)
        table.add_row(translate(category="metadatainfo", type="date_time_original"), time)
        table.add_row(translate(category="metadatainfo", type="date_time_digitized"), date_time_digitized)
        table.add_row(translate(category="metadatainfo", type="date_time_modified"), date_time_modified)
        table.add_row(translate(category="metadatainfo", type="timezone"), timezone)
        table.add_row(translate(category="metadatainfo", type="timezone_digitized"), timezone_digitized)
        table.add_row(translate(category="metadatainfo", type="timezone_modified"), timezone_modified)
        table.add_row(translate(category="metadatainfo", type="create_date"), create_date)
        table.add_row(translate(category="metadatainfo", type="modify_date"), modify_date)
        table.add_row(translate(category="metadatainfo", type="metadata_date"), metadata_date)
        table.add_row(translate(category="metadatainfo", type="file_size"), filesize)
        table.add_row(translate(category="metadatainfo", type="file_name"), file_name)
        table.add_row(translate(category="metadatainfo", type="file_extension"), file_extension)
        table.add_row(translate(category="metadatainfo", type="file_type"), file_type)
        table.add_row(translate(category="metadatainfo", type="mime_type"), mime_type)
        table.add_row(translate(category="metadatainfo", type="file_permissions"), file_permissions)
        table.add_row(translate(category="metadatainfo", type="camera_model"), model)
        table.add_row(translate(category="metadatainfo", type="camera_make"), make)
        table.add_row(translate(category="metadatainfo", type="lens_model"), lens_model)
        table.add_row(translate(category="metadatainfo", type="lens_make"), lens_make)
        table.add_row(translate(category="metadatainfo", type="iso"), iso)
        table.add_row(translate(category="metadatainfo", type="exposure_time"), exposure)
        table.add_row(translate(category="metadatainfo", type="aperture"), aperture)
        table.add_row(translate(category="metadatainfo", type="focal_length"), focal)
        table.add_row(translate(category="metadatainfo", type="focal_length_35mm"), focal_35mm)
        table.add_row(translate(category="metadatainfo", type="flash"), flash)
        table.add_row(translate(category="metadatainfo", type="white_balance"), white_balance)
        table.add_row(translate(category="metadatainfo", type="metering_mode"), metering_mode)
        table.add_row(translate(category="metadatainfo", type="exposure_program"), exposure_program)
        table.add_row(translate(category="metadatainfo", type="exposure_compensation"), exposure_compensation)
        table.add_row(translate(category="metadatainfo", type="digital_zoom"), digital_zoom)
        table.add_row(translate(category="metadatainfo", type="dimensions"), f"{width}x{height}")
        table.add_row(translate(category="metadatainfo", type="bits_per_sample"), bits_per_sample)
        table.add_row(translate(category="metadatainfo", type="compression"), compression)
        table.add_row(translate(category="metadatainfo", type="color_space"), color_space)
        table.add_row(translate(category="metadatainfo", type="orientation"), orientation)
        table.add_row(translate(category="metadatainfo", type="software"), software)
        table.add_row(translate(category="metadatainfo", type="artist"), artist)
        table.add_row(translate(category="metadatainfo", type="description"), description)
        table.add_row(translate(category="metadatainfo", type="author"), author)
        table.add_row(translate(category="metadatainfo", type="copyright"), copyright)
        table.add_row(translate(category="metadatainfo", type="title"), title)
        table.add_row(translate(category="metadatainfo", type="gps_latitude"), latitude)
        table.add_row(translate(category="metadatainfo", type="gps_longitude"), longitude)
        table.add_row(translate(category="metadatainfo", type="gps_latitude_ref"), latitude_ref)
        table.add_row(translate(category="metadatainfo", type="gps_longitude_ref"), longitude_ref)
        table.add_row(translate(category="metadatainfo", type="gps_altitude"), altitude)
        table.add_row(translate(category="metadatainfo", type="gps_altitude_ref"), altitude_ref)
        table.add_row(translate(category="metadatainfo", type="gps_speed"), gps_speed)
        table.add_row(translate(category="metadatainfo", type="gps_track"), gps_track)
        table.add_row(translate(category="metadatainfo", type="gps_img_direction"), gps_img_direction)
        table.add_row(translate(category="metadatainfo", type="gps_dest_latitude"), gps_dest_latitude)
        table.add_row(translate(category="metadatainfo", type="gps_dest_longitude"), gps_dest_longitude)
        table.add_row(translate(category="metadatainfo", type="gps_date_stamp"), gps_date_stamp)
        table.add_row(translate(category="metadatainfo", type="gps_time_stamp"), gps_time_stamp)
        table.add_row(translate(category="metadatainfo", type="gps_h_positioning_error"), gps_h_positioning_error)
        table.add_row(translate(category="metadatainfo", type="duration"), duration)
        table.add_row(translate(category="metadatainfo", type="frame_rate"), frame_rate)
        table.add_row(translate(category="metadatainfo", type="video_codec"), video_codec)
        table.add_row(translate(category="metadatainfo", type="audio_codec"), audio_codec)
        table.add_row(translate(category="metadatainfo", type="bitrate"), bitrate)        
        
        console.print(table)
        console.print(" ")
        exit()
        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='error_message')} > {e}")
        return
        

def main():
    try:
        while True:
            route = console.input(f"[bold green]{translate(category="metadatainfo", type="route_message")}[/bold green]: ")
            if not route:
                console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                continue
            else:
                is_route = os.path.expanduser(f"~/{route}")
                if os.path.exists(is_route):
                    list_archives = os.listdir(is_route)
                    print("\n")
                    for archive in list_archives:
                        console.print(f"• {archive}")
                    print("\n")    
                    archive_name = console.input(f"[bold green]{translate(category="metadatainfo", type="archive_name_message")}[/bold green]: ")
                    if not archive_name:
                        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                        continue
                    elif archive_name:
                        metadata(archive_name, route)
                else:
                    console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                    continue
                        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='error_message')} > {e}")
        return

main()