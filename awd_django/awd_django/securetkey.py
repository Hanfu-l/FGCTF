import secrets
import string
import uuid

def generate_secure_token(length=32):
    # 使用 secrets 模块生成更安全的随机 Token
    return ''.join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(length))


def create_uuid():
    random_uuid=uuid.uuid4()
    uuid_string=str(random_uuid)
    return uuid_string