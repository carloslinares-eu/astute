from google.oauth2 import service_account

try:
    credentials = service_account.Credentials.from_service_account_file(
        "./txt2speech/gcloud_credentials.json")

except OSError:
    print('File not found')
    credentials = service_account.Credentials.from_service_account_file(
        "login/gcloud_credentials.json")

scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])