import pytest
from mimesis.enums import DurationUnit
from mimesis.schema import Field, Schema

from polyfactory_speed import MyUser, CITIES


def _schema():
    subscription_start = mf('datetime.datetime')
    subscription_end = subscription_start + mf(
        'datetime.duration',
        duration_unit=DurationUnit.WEEKS,
    )
    return {
        'email': mf('person.email'),
        'full_name': mf('full_name'),
        'age': mf('numeric.integer_number', start=0, end=130),
        'country': mf('address.country'),
        'city': mf('choice.choice', items=CITIES),
        'address': mf('address.address'),
        'subscription_starts': subscription_start,
        'subscription_ends': subscription_end,
    }

mf = Field()
schema = Schema(
    iterations=1,
    schema=_schema,
)


@pytest.mark.parametrize('i', range(100))
def test_my_user(i: int) -> None:
    user = MyUser.model_validate({**schema.create()[0], 'id': i})
    assert isinstance(user, MyUser)
