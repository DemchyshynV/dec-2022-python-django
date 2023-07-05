import os
from uuid import uuid1

from core.dataclasses.user_dataclass import ProfileDataClass


def upload_avatar(instance, file: str) -> str:
    ext = file.split('.')[-1]
    return os.path.join(instance.profile.surname, 'avatar', f'{uuid1()}.{ext}')
