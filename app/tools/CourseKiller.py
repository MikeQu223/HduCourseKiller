import base64
from cgi import print_arguments
from email import header
import json
import os.path
import sys
import threading
import time
import pandas as pd
import requests
import rsa

import bs4
import requests
from Config import Config
from pandas import DataFrame, concat
from PySide6.QtWidgets import QTextBrowser
from time import sleep

class Coursekiller:
    def __init__(self, config_file):
        self.config = Config(config_file)
        self.session = requests.Session()
        self.session.trust_env = self.config.config["session"]["trust_env"]
        self.session.verify = self.config.config["session"]["verify"]
        self.session.timeout = self.config.config["session"]["timeout"]
        self.session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
        # self.session.headers = self.config.config["session"]["headers"]  # 不能用这种方式设置，会报错
        self.headers = self.config.config["session"]["headers"]  # 只有在登录时要用到这个头
        self.userinfo = self.config.config["userinfo"]
        self.params = self.config.config["params"]
        self.courses = self.config.config["courses"]

    def save(self):
        self.config.config["courses"] = self.courses
        self.config.saveConfig("app/config/config.yaml")

    def set_pubKey(self):
        try:
            params = {"time": int(time.time() * 1000)}
            response = self.session.get(self.config.config["session"]["url"]["set_pubKey"], params=params)
            data = response.json()
            self.modulus = base64.b64decode(data["modulus"])
            self.exponent = base64.b64decode(data["exponent"])
            self.pub_key = rsa.PublicKey(int.from_bytes(
                self.modulus, 'big'), int.from_bytes(self.exponent, 'big'))
        except:
            raise ConnectionError("set pubKey failed")
    
    def encoded(self, s):
        encoded_pwd = rsa.encrypt(s, self.pub_key)
        return base64.b64encode(encoded_pwd)
    
    def set_csrftoken(self):
        try:
            params = {
                "languege": "zh_CN",
                "_t": int(time.time() * 1000),
            }
            response = self.session.get(self.config.config["session"]["url"]["set_csrtoken"], params=params)
            self.headers["Cookie"] = "JSESSIONID={}; route={}".format(
                self.session.cookies["JSESSIONID"], self.session.cookies["route"])
            page = bs4.BeautifulSoup(response.text, features="html.parser")
            self.csrftoken = page.find("input", attrs={"id": "csrftoken"})["value"]
        except:
            raise ConnectionError("set csrftoken failed")
    
    def login(self, username="", password="", remember=False):
        try:
            if username != "" and password != "":
                self.userinfo["username"] = username
                self.userinfo["password"] = password
            self.set_pubKey()
            self.set_csrftoken()
            encoded_password = self.encoded(bytes(self.userinfo["password"], encoding="utf-8")).decode("utf-8")
            data = {
                "csrftoken": self.csrftoken,
                "language": "zh_CN",
                "yhm": self.userinfo["username"],
                "mm": [encoded_password, encoded_password]
                }
            params = {"time": int(time.time() * 1000)}
            response = self.session.post(self.config.config["session"]["url"]["set_csrtoken"], data=data, params=params, allow_redirects=False)
            if response.status_code == 302:
                self.index = self.session.get(url=response.headers["Location"])
                if remember:
                    self.config.config["userinfo"]["username"] = username
                    self.config.config["userinfo"]["password"] = password
                    self.config.config["userinfo"]["remember"] = True
                    self.config.saveConfig("app/config/config.yaml")
                else:
                    self.config.config["userinfo"]["username"] = username
                    self.config.config["userinfo"]["password"] = password
                    self.config.config["userinfo"]["remember"] = False
                    self.config.saveConfig("app/config/config.yaml")
                self.get_params()
                return (True, "登录成功")
            else:
                return (False, "登录失败")
        except Exception as e:
            raise e

    def delete_item(self, index):
        self.courses["show_info"].drop(self.courses["show_info"].index[index], inplace=True)
        self.courses["query_data"].pop(index)
        self.save()

    def get_params(self):
        """
        加载网页参数
        """
        # http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=20051336
        hparams = {
            "gnmkdm": "N253512",
            "layout": "default",
            "su": self.userinfo["username"],
        }
        page =bs4.BeautifulSoup(self.session.get(self.config.config["session"]["url"]["init_params1"], params=hparams).text, features="html.parser")
        params = {x.get("name", "null"):x.get("value", "") for x in page.find_all("input")}
        XKKZ = {x.text: x["onclick"].split(",")[1:3] for x in page.find_all(attrs={"data-toggle": "tab"})}
        XKKZ = {x: [yy.replace("'","") for yy in y] for x, y in XKKZ.items()}
        XKKZ = {y[0]: {"xkkz_id": y[1], "kklxdm": y[0]} for x, y in XKKZ.items()}
        self.session.headers["Content-Type"] = "application/x-www-form-urlencoded"
        for k in XKKZ.keys():
            page = bs4.BeautifulSoup(self.session.post(self.config.config["session"]["url"]["init_params2"], data={
                "xkkz_id": XKKZ[k]["xkkz_id"],
                "xszxzt": "1",
                "kspage": "0",
                "jspage": "0"
            }, params=hparams).text, features="html.parser")
            XKKZ[k].update({x.get("name", "null"):x.get("value", "") for x in page.find_all("input")})
            XKKZ[k]["kklxdm"] = k
        self.params = XKKZ
        for k in self.params.keys():
            temp = params.copy()
            temp.update(self.params[k])
            self.params[k] = temp


    def search(self, info):
        """
        搜索指定课程，最多返回100条
        """
        self.course_list = []
        data = self.params[info["kklxdm"]]
        data["filter_list"] = info["filter_list"]
        data["kspage"] = "1"
        data["jspage"] = "100"
        data["jg_id"] = "05"
        params = {"gnmkdm": "N253512", "su": "20051336"}
        try:
            res1 = self.session.post(url=self.config.config["session"]["url"]["query_course1"],
                data=data,params=params).json()["tmpList"]
        except:
            self.re_login()
            res1 = self.session.post(url=self.config.config["session"]["url"]["query_course1"],
                data=data,params=params).json()["tmpList"]
        for course in res1:
            data["kch_id"] = course["kch_id"]
            data["filter_list"] = [course["jxbmc"]]
            try:
                res2 = self.session.post(url=self.config.config["session"]["url"]["query_course2"],
                    data=data,params=params).json()
            except:
                self.re_login()
                res2 = self.session.post(url=self.config.config["session"]["url"]["query_course2"],
                    data=data,params=params).json()
            for course_detail in res2:
                course_info = {
                    "show_info":{
                        "课程号":course["kch_id"],
                        "课程名":course["kcmc"],
                        "授课教师":course_detail["jsxx"],
                        "上课时间":course_detail["sksj"],
                        "上课地点":course_detail["jxdd"],
                        "剩余容量":str(int(course_detail["jxbrl"]) - int(course["yxzrs"])),
                        "总容量":course_detail["jxbrl"],
                    },
                    "query_data":{
                        "jxb_ids":course_detail["do_jxb_id"],
                        "kch_id":course["kch_id"],
                        "kcmc":course["kcmc"],
                        "rwlx": data["rwlx"],
                        "rlkz": data["rlkz"],
                        "rlzlkz": data["rlzlkz"],
                        "sxbj": "1",
                        "xxkbj": course["xxkbj"],
                        "qz": "0",
                        "cxbj": course["cxbj"],
                        "xkkz_id": data["xkkz_id"],
                        "njdm_id": data["njdm_id"],
                        "zyh_id": data["zyh_id"],
                        "kklxdm": data["kklxdm"],
                        "xklc": data["xklc"],
                        "xkxnm": data["xkxnm"],
                        "xkxqm": data["xkxqm"]
                    }
                }
                course_info["query_data"].update(data)
                self.course_list.append(course_info)
                if len(self.course_list) >= 100:
                    return DataFrame([x["show_info"] for x in self.course_list], columns=self.courses["show_info"].columns)
        return DataFrame([x["show_info"] for x in self.course_list], columns=self.courses["show_info"].columns)

    def add_course(self, index):
        self.courses["show_info"] = concat([self.courses["show_info"], DataFrame(self.course_list[index]["show_info"], index=[len(self.courses["show_info"])])])
        self.courses["query_data"].append(self.course_list[index]["query_data"])
        self.save()
        return self.courses["show_info"]

    def get_run_info(self):
        info = {
            "interval": self.config.settings["interval"],
            "trials": self.config.settings["trials"],
            "todo": len(self.courses["show_info"])
        }
        return info

    def get_course_info(self):
        return self.courses["show_info"]

    def logout(self):
        params={
            "t": str(int(time.time()*1000)),
            "login_type": "",
        }
        self.session.get(url=self.config.config["session"]["url"]["logout"], params=params)

    def re_login(self):
            self.set_pubKey()
            self.set_csrftoken()
            encoded_password = self.encoded(bytes(self.userinfo["password"], encoding="utf-8")).decode("utf-8")
            data = {
                "csrftoken": self.csrftoken,
                "language": "zh_CN",
                "yhm": self.userinfo["username"],
                "mm": [encoded_password, encoded_password]
                }
            params = {"time": int(time.time() * 1000)}
            response = self.session.post(self.config.config["session"]["url"]["set_csrtoken"], data=data, params=params, allow_redirects=False)


    def run(self, out1: QTextBrowser, out2: QTextBrowser, finish):
        first = True
        info = self.get_run_info()
        indexes = list(range(info["todo"]))
        for _ in range(info["trials"]):
            out1.append(f"第{_+1}次尝试：")
            for index in indexes.copy():
                
                course = self.courses["query_data"][index]
                try:
                    res = self.session.post(url=self.config.config["session"]["url"]["run"], data=course).json()
                except Exception as e:
                    out1.append(f"重新登录")
                    self.logout()
                    out1.append(f"退出登录")
                    self.re_login()
                    out1.append("登录成功")
                    res = self.session.post(url=self.config.config["session"]["url"]["run"], data=course).json()
                if res["flag"] == "-1":
                    out1.append(f"{self.courses['show_info'].iloc[index]['课程名']}-{self.courses['show_info'].iloc[index]['授课教师']}-{self.courses['show_info'].iloc[index]['上课时间']}：人数已满")
                    out1.verticalScrollBar().setValue(out1.verticalScrollBar().maximum()+10)
                elif res["flag"] == "1":
                    if first:
                        first = False
                        out2.append("Hdu Course Killer帮你抢到课啦！有任何问题欢迎提issue或发邮件（github链接在界面左下角）！如果你能给我点一个star就更好啦~")
                    out1.append(f"{self.courses['show_info'].iloc[index]['课程名']}-{self.courses['show_info'].iloc[index]['授课教师']}-{self.courses['show_info'].iloc[index]['上课时间']}：选课成功")
                    out2.append(f"{self.courses['show_info'].iloc[index]['课程名']}-{self.courses['show_info'].iloc[index]['授课教师']}-{self.courses['show_info'].iloc[index]['上课时间']}")
                    indexes.remove(index)
                    out1.verticalScrollBar().setValue(out1.verticalScrollBar().maximum()+10)
                else:
                    out1.append(f"{self.courses['show_info'].iloc[index]['课程名']}-{self.courses['show_info'].iloc[index]['授课教师']}-{self.courses['show_info'].iloc[index]['上课时间']}：{res['msg']}")
                    out1.verticalScrollBar().setValue(out1.verticalScrollBar().maximum()+10)
            sleep(info["interval"])
            if finish():
                return 
            if indexes == []:
                out1.append("所有课程均已选上！")
                return

                    





            

    

if __name__ == "__main__":
    coursekiller = Coursekiller("app/config/config.yaml")
    print(coursekiller.login(coursekiller.config.config["userinfo"]["username"], coursekiller.config.config["userinfo"]["password"]))
    coursekiller.search(info={"filter_list": ["吴永胜"], "kklxdm": "01"})
    

        

        


        

