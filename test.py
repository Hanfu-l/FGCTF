from datetime import datetime

import docker
import hashlib

def Rundocker():
    # 获取docker客户端
    client = docker.from_env()

    md5=hashlib.md5()

    user='123'

    seed=user+str(datetime.timestamp(datetime.now()))

    md5.update(seed.encode('utf-8'))

    namevalue=md5.hexdigest()


    try:
        # 运行容器
        container = client.containers.run(
            "ctftraining/qwb_2019_supersqli",  # 镜像名称
            name=namevalue,                    # 容器名称
            detach=True,                        # 后台运行容器
            ports={"80/tcp": 15000}             # 映射端口（如果需要）
        )
        
        # 打印容器信息
        print(f"容器 {container.name} 已启动！")

    except docker.errors.ImageNotFound:
        print("镜像未找到，正在拉取镜像...")
    except docker.errors.APIError as e:
        print(f"启动容器失败：{e}")

if __name__ == "__main__":
    Rundocker()
