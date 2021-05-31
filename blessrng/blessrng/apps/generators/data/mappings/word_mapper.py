from generators.data.dto.stat_dto import WordStatDto
from generators.models import RandWordSet


def map_word_to_stat_dto(obj: RandWordSet):
    return WordStatDto(
        type='word',
        generated_at=obj.generated_at,
        count=obj.count,
        values=obj.values,
        alltext=obj.all_text,
    )

