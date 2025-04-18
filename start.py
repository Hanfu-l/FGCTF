import subprocess
import os
import signal
import sys

# 获取当前文件路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件的目录
current_dir = os.path.dirname(current_file_path)

# 定义 Django 和 Vue 项目的路径
DJANGO_PROJECT_RELATIVE_PATH = "awd_django"  # Django 项目的相对路径
VUE_PROJECT_RELATIVE_PATH = "awd_vue"  # Vue 项目的相对路径

DJANGO_PROJECT_PATH = os.path.join(current_dir, DJANGO_PROJECT_RELATIVE_PATH)
VUE_PROJECT_PATH = os.path.join(current_dir, VUE_PROJECT_RELATIVE_PATH)

def run_django():
    """使用 screen 启动 Django 服务器"""
    os.chdir(DJANGO_PROJECT_PATH)  # 切换到 Django 项目目录
    print("启动 Django 服务器...")
    # 使用 screen 启动 Django，会话名称为 fgctfdjango
    return subprocess.Popen(["screen", "-dmS", "fgctfdjango", "python3", "manage.py", "runserver"])

def run_vue():
    """使用 screen 启动 Vue 开发服务器"""
    os.chdir(VUE_PROJECT_PATH)  # 切换到 Vue 项目目录
    print("启动 Vue 开发服务器...")
    # 使用 screen 启动 Vue，会话名称为 fgctfvue
    return subprocess.Popen(["screen", "-dmS", "fgctfvue", "npm", "run", "serve"])

def main():
    # 启动 Django 和 Vue
    django_process = run_django()
    vue_process = run_vue()

    # 捕获 Ctrl+C 信号，优雅地关闭进程
    def signal_handler(sig, frame):
        print("检测到 Ctrl+C，关闭服务器...")
        # 终止 screen 会话
        subprocess.run(["screen", "-XS", "fgctfdjango", "quit"])
        subprocess.run(["screen", "-XS", "fgctfvue", "quit"])
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    # 等待进程结束
    django_process.wait()
    vue_process.wait()

if __name__ == "__main__":
    main()