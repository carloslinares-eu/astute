import as2t.login.local

credentials_file_path = "./as2t/login/gcloud_credentials.json"

credentials, scoped_credentials = as2t.login.local.login_with_json(credentials_file_path)


