from generators.data.dto.stat_dto import PwdStatDto
from generators.models import RandPwdSet


def map_pwd_to_stat_dto(obj: RandPwdSet):
    return PwdStatDto(
        type='pwd',
        generated_at=obj.generated_at,
        count=obj.count,
        passwords=obj.values,
        length=obj.pwd_length,
    )
