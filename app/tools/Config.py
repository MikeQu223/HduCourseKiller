import yaml
import os
from pandas import DataFrame
import copy


class Config:
    def __init__(self, config_file):
        if not config_file.endswith('.yaml'):
            raise Exception('Config file must be a yaml file')
        if not os.path.exists(config_file):
            self._initConfig()
            self.saveConfig(config_file)
        else:
            try:
                self.loadConfig(config_file)
            except Exception as e:
                self._initConfig()
                self.saveConfig(config_file)


    def _initConfig(self):
        self.session = {} # session相关配置
        self.userinfo = {} # 用户信息
        self.settings = {# 设置相关配置
            "interval": 5,
            "trials": 1000,

        } 
        
        self.session["headers"] = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Length": "477",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "",
            "Host": "newjw.hdu.edu.cn",
            "Origin": "http://newjw.hdu.edu.cn",
            "Referer": "http://newjw.hdu.edu.cn/jwglxt/xtgl/login_slogin.html",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
        }
        self.session["url"] = {
            "set_pubKey": "http://newjw.hdu.edu.cn/jwglxt/xtgl/login_getPublicKey.html",
            "set_csrtoken": "http://newjw.hdu.edu.cn/jwglxt/xtgl/login_slogin.html",
            "login": "http://newjw.hdu.edu.cn/jwglxt/xtgl/login_slogin.html",
            "init_params1": "http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html",
            "init_params2": "http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbDisplay.html",
            "query_course1": "http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html",
            "query_course2": "http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzbjk_cxJxbWithKchZzxkYzb.html",
            "run": "http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html",
            "logout": "http://newjw.hdu.edu.cn/jwglxt/logout.html",
        }
        self.session["trust_env"] = False
        self.session["verify"] = False
        self.session["timeout"] = 10
        

        self.userinfo["username"] = ""
        self.userinfo["password"] = ""
        self.userinfo["remember"] = True
        self.params = None
        self.courses = {"show_info":DataFrame(columns=['课程号', '课程名', '授课教师', '上课时间', '上课地点', '剩余容量', '总容量']), "query_data":[]}
        self.config = {
            "session": self.session,
            "userinfo": self.userinfo,
            "settings": self.settings,
            "params": self.params,
            "courses": self.courses,


        }

    def init_params(self, params):
        self.params = {x["id"]: x["valus"] for x in params}




    def loadConfig(self, config_file):
        with open(config_file, 'r', encoding="utf-8") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        self.session = config["session"]
        self.userinfo = config["userinfo"]
        self.settings = config["settings"]
        self.params = config["params"]
        self.courses = config["courses"]
        self.courses["show_info"] = DataFrame(self.courses["show_info"], columns=['课程号', '课程名', '授课教师', '上课时间', '上课地点', '剩余容量', '总容量'])
        self.config = {
            "session": self.session,
            "userinfo": self.userinfo,
            "settings": self.settings,
            "params": self.params,
            "courses": self.courses,
        }

    def updateConfig(self, config):
        self.config.update(config)




    def saveConfig(self, config_file):
        with open(config_file, 'w+', encoding="utf-8") as f:
            config = copy.deepcopy(self.config)
            config["courses"]["show_info"] = config["courses"]["show_info"].to_dict(orient="records")
            if not config["userinfo"]["remember"]:
                config["userinfo"]["password"] = ""
            yaml.dump(config, f, encoding="utf-8", allow_unicode=True)

    



if __name__ == '__main__':
    config = Config('app/config/config.yaml')
    config.saveConfig('app/config/config.yaml')