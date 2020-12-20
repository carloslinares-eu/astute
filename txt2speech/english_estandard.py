import txt2speech.login.local

credentials_file_path = "./txt2speech/login/gcloud_credentials.json"

credentials, scoped_credentials = txt2speech.login.local.login_with_json(credentials_file_path)


