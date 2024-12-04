import datetime as dt

import pytest
from polyfactory import Use
from polyfactory.decorators import post_generated
from polyfactory.factories.pydantic_factory import ModelFactory

from polyfactory_speed import MyUser, CITIES


class MyUserFactory(ModelFactory[MyUser]):
    city = Use(ModelFactory.__random__.choice, CITIES)

    @post_generated
    @classmethod
    def subsription_ends(cls, subscription_starts: dt.datetime):
        return subscription_starts + cls.__faker__.time_delta()



@pytest.mark.parametrize('i', range(100))
def test_my_user(i: int) -> None:
    user = MyUserFactory.build(id=i)
    assert isinstance(user, MyUser)
