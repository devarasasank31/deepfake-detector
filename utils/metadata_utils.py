import tempfile
import os
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(uploaded_file):
    try:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        # Open image and extract EXIF
        image = Image.open(tmp_path)
        exif_data = image._getexif()
        image.close()

        # Parse EXIF data
        if exif_data is not None:
            metadata = {
                TAGS.get(tag, tag): value
                for tag, value in exif_data.items()
            }
        else:
            metadata = {"warning": "No EXIF metadata found."}

        os.remove(tmp_path)  # Clean up temp file
        return metadata

    except Exception as e:
        return {"error": str(e)}
