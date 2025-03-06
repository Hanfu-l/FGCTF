# 使用 Python 3.8.10 作为基础镜像
FROM python:3.8.10-slim

# 设置工作目录
WORKDIR /app

# 替换 apt-get 源为阿里云镜像
RUN sed -i 's|http://deb.debian.org|http://mirrors.aliyun.com|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org|http://mirrors.aliyun.com|g' /etc/apt/sources.list

# 安装必要的系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 设置 pip 镜像源为阿里云
RUN pip install --no-cache-dir --upgrade pip && \
    pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# 复制项目依赖文件
COPY requirements.txt /app/

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . /app/

# 确保 static 目录存在
RUN mkdir -p /app/static

# 收集静态文件（防止数据库连接失败）
RUN python manage.py collectstatic --noinput || true

# 暴露端口
EXPOSE 8000

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 启动 Django 应用
CMD ["gunicorn", "awd_django.wsgi:application", "--bind", "0.0.0.0:8000"]
