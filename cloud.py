import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'fruit-storage-f289d333eda2'

storage_client = storage.Client()
