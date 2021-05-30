from generators.data.dto.dto import IntStatDto
from generators.models import RandIntSet


def map_int_to_stat_dto(obj: RandIntSet):
    return IntStatDto(
        type='int',
        generated_at=obj.generated_at,
        count=obj.count,
        floor=obj.floor,
        ceiling=obj.ceiling,
        values=obj.values
    )
