from django.forms import ModelForm

from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField
# Next two lines are only used for generating the upload preset sample name
from cloudinary.compat import to_bytes
import cloudinary, hashlib

from portalapp.models import ACEUserProfile

class PhotoForm(ModelForm):
    class Meta:
        model = ACEUserProfile
        fields = '__all__'

class PhotoDirectForm(PhotoForm):
    picture = CloudinaryJsFileField()

class PhotoUnsignedDirectForm(PhotoForm):
    upload_preset_name = "sample_" + hashlib.sha1(to_bytes(cloudinary.config().api_key + cloudinary.config().api_secret)).hexdigest()[0:10]
    picture = CloudinaryUnsignedJsFileField(upload_preset_name)