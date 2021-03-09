import astute.login
import astute.sinthesizer


class Icon:
    def __init__(self, path):
        self.path = path


def main(icon=None):
    login_app = astute.login.LoginApp(icon)
    login_app.initialize()

    if login_app.has_logged_in is True:
        main_app = astute.sinthesizer.MainApp(icon, credentials=login_app.credentials)
        main_app.initialize()


if __name__ == "__main__":
    main(icon=Icon('astute.ico'))
