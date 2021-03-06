import json
import os
import logging
from PyUtils.Obj2Json import Obj2Json


class AppSettings:
    """
    Store all settings from the application.
    """
    SKYRIM_PATH = ".\\Sandbox\\"
    DOGEN_DIR = ".\\OUTPUT\\"
    ACTORS_FILE = ".\\Actors.csv"
    COMMENTS_FILE = ".\\Comments.csv"
    SCENE_ORDER_FILE = ".\\SceneOrder.csv"
    TOPIC_SORT_BY_NAME = "true"
    CMD_COMMENT = "Use \"Process\" string for multiprocessing import, otherwise will be executed as a batch command. Use {file} variable to pass the csv file full path. Any other command line application can be set as editor."
    DEFAULT_THEME = "DarkBlue12"

    def __init__(self, json_file):
        self.settings_file = json_file
        with open(json_file) as f:
            self.data = json.load(f)
        self.skyrim_path = self.data["skyrim-path"]
        self.docgen_dir = os.path.abspath(self.data["dogen-dir"])
        self.log_level = self.data["log-level"]
        self.actors_file = self.data["actors-file"]
        self.comments_file = self.data["comments-file"]
        self.scene_order_file = self.data["scene-order-file"]
        self.topic_sort_by_name = self.data["topic-sort-by-name"]
        self.app_theme = self.data["app_theme"]
        self.csv_editor_cmd_comments = self.data["csv_editor_cmd_comments"]
        self.csv_editor_cmd = self.data["csv_editor_cmd"]
        # derivated settings
        self.docgen_dir_md = self.docgen_dir + "\\Md\\"
        self.docgen_dir_json = self.docgen_dir + "\\Json\\"
        self.docgen_dir_html = self.docgen_dir + "\\Html\\"
        self.docgen_dir_docx = self.docgen_dir + "\\Docx\\"
        self.docgen_reports = self.docgen_dir + "\\Reports\\"

    def save(self):
        self.data["skyrim-path"] = self.skyrim_path
        self.data["dogen-dir"] = self.docgen_dir
        self.data["log-level"] = self.log_level
        self.data["actors-file"] = self.actors_file
        self.data["comments-file"] = self.comments_file
        self.data["scene-order-file"] = self.scene_order_file
        self.data["topic-sort-by-name"] = self.topic_sort_by_name
        self.data["app_theme"] = self.app_theme
        self.data["csv_editor_cmd"] = self.csv_editor_cmd
        with open(self.settings_file, "w") as a_file:
            json.dump(self.data, a_file, indent=4)

    def log_level(self):
        return {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARN": logging.WARN,
            "ERROR": logging.ERROR,
        }.get(self.log_level, logging.DEBUG)

    def topic_sort_by_name_ret(self):
        if self.topic_sort_by_name.upper() == "TRUE":
            return True
        else:
            return False

    def reset(self):
        self.skyrim_path = AppSettings.SKYRIM_PATH
        self.docgen_dir = AppSettings.DOGEN_DIR
        self.actors_file = AppSettings.ACTORS_FILE
        self.comments_file = AppSettings.COMMENTS_FILE
        self.scene_order_file = AppSettings.SCENE_ORDER_FILE
        self.topic_sort_by_name = AppSettings.TOPIC_SORT_BY_NAME
        self.app_theme = AppSettings.DEFAULT_THEME

    def reset_and_save(self):
        self.reset()
        self.save()


class AppInfo:
    APP_NAME_SHORT = "CKQuestDialogManager"
    APP_NAME_LARGE = "Quest Dialog Manager for CreationKit"
    APP_VERSION = "v0.1.0.0"
    APP_VERSION_NAME = "Snowberry Crostata"

    def __init__(self, app_dir=".\\App\\"):
        self.app_dir = os.path.abspath(app_dir) + "\\"
        self.audio_encoder_dir = self.app_dir + "Bin\\"
        self.img_dir = self.app_dir + "Img\\"
        self.pages_dir = self.app_dir + "Pages\\"
        self.log_dir = self.app_dir + "Logs\\"
        self.csv_actors = self.app_dir + "Db\\Actors.csv"
        self.csv_comments = self.app_dir + "Db\\Comments.csv"
        self.csv_scene_order = self.app_dir + "Db\\SceneOrder.csv"
        self.app_icon_ico = self.img_dir + "sbc.ico"
        self.app_icon_png = self.img_dir + "Snowberry_crostata.png"
        self.log_file = self.log_dir + "ck-dialog-docgen.log"
        self.tutorial_html = self.pages_dir + "tutorial.html"
        self.url_github = "https://github.com/AndersonPaschoalon/CreationKit-DialogDocGen.git"
        self.url_nexus = "https://www.nexusmods.com/skyrim"
        self.tutorial_html = self.pages_dir + "tutorial.html"
        self.settings_file = self.app_dir + "settings.json"
        self.label_main_window = "Quest Dialog Manager for CK"
        self.label_audio_window = "Quest Audio Manager for CK"
        self.app_version = AppInfo.APP_VERSION + " -- " + AppInfo.APP_VERSION_NAME
        self.app_name_short = AppInfo.APP_NAME_SHORT
        self.app_name_LARGE = AppInfo.APP_NAME_LARGE
        self.license = self.app_dir + "Misc\\LICENSE.md"
        self.settings_obj = AppSettings(self.settings_file)
        self.creation_kit_exe = self.settings_obj.skyrim_path + "\\CreationKit.exe"

    def tutorial_url(self):
        url_tutorial = "file:///" + os.path.realpath(self.tutorial_html)
        return url_tutorial

    def to_string(self):
        obj = Obj2Json()
        obj.add("app_dir", self.app_dir)
        obj.add("img_dir", self.img_dir)
        obj.add("pages_dir", self.pages_dir)
        obj.add("log_dir", self.log_dir)
        obj.add("csv_actors", self.csv_actors)
        obj.add("csv_comments", self.csv_comments)
        obj.add("csv_scene_order", self.csv_scene_order)
        obj.add("app_icon_ico", self.app_icon_ico)
        obj.add("app_icon_png", self.app_icon_png)
        obj.add("log_file", self.log_file)
        obj.add("tutorial_html", self.tutorial_html)
        obj.add("settings_file", self.settings_file)
        obj.add("label_main_window", self.label_main_window)
        obj.add("label_audio_window", self.label_audio_window)
        obj.add("app_version", self.app_version)
        settings = str(self.settings_obj.data)
        obj.add("settings_obj", settings)
        return obj.json()


if __name__ == '__main__':
    aa = AppInfo()
    print(aa.to_string())
    aa.settings_obj.docgen_dir = "../OUTPUT/"
    aa.settings_obj.save()
