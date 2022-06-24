# 欢迎使用Hdu Course Killer！
本项目旨在帮助杭电学生查询课程信息、快速自助选课  
本软件能够实时监视课程余量，并在第一时间发出选课请求。
# 声明
2022年6月4日更新：已知使用本软件有**封号**的风险，若您仍需使用本脚本，后果自负。
使用本软件不能排除被封禁的风险，禁止恶意修改请求频次，以免对学校服务器造成过大压力。  
作者([@littleherozzzx](https://github.com/LitttleHeroZZZX))对由于使用本软件导致的一切后果不承担任何责任，使用本软件的任何潜在风险均由使用者承担。  
若在使用过程中发现问题，欢迎提issue或者邮件联系作者[zzzx@hdu.edu.cn](mailto:zzzx@hdu.edu.cn)。
# 使用说明

## 方法1：直接使用发行版本
1. 点击下载[最新发行版本](https://github.com/LitttleHeroZZZX/HduCourseKiller/releases/download/v1.0.0/HduCourseKiller-1.0.0-win64.zip)，并将整个文件夹解压。
2. 运行文件夹内的main.exe程序。

## 方法2：使用Python脚本
**使用该方法前请确认您的电脑已配置Python环境，本说明使用的Python版本为3.9.7。**  
1. 在命令行clone项目仓库：
   ```bash
   git clone git@github.com:LitttleHeroZZZX/HduCourseKiller.git
   cd HduCourseKiller
   ```
2. 安装依赖库：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行脚本：
   ```bash
   python main.py
   ```
# 程序运行效果
![](docs/demo.gif)


# 更新日志
## v1.0.1
- 修复了长时间抢课过程中异常停止的bug

# TODO
- [ ] 设置中心
- [ ] 已选课表查询
- [ ] 退课
- [ ] 条件选课
