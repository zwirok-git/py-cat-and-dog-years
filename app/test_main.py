from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (-1, -1, [0, 0]),
    (0, 0, [0, 0]),
    (23, 23, [1, 1]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
],
    ids=[
        "negative_input",
        "zero_input",
        "boundary_23",
        "boundary_28",
        "large_input_100",
]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "age_before_boundary, age_on_boundary, "
    "expected_before_boundary, expected_on_boundary",
    [
    (14, 15, [0, 0], [1, 1]),
    (23, 24, [1, 1], [2, 2]),
    (27, 28, [2, 2], [3, 2]),
    (28, 29, [3, 2], [3, 3]),
],
    ids=[
        "first_year",
        "second_year",
        "cat_step",
        "dog_step",
    ]
)
def test_get_human_age_boundaries(
    age_before_boundary: int,
    age_on_boundary: int,
    expected_before_boundary: list,
    expected_on_boundary: list,
) -> None:
    assert (
        get_human_age(age_before_boundary, age_before_boundary)
        == expected_before_boundary
    )
    assert (
        get_human_age(age_on_boundary, age_on_boundary)
        == expected_on_boundary
    )


def test_type_error_when_input_is_string() -> None:
    with pytest.raises(TypeError):
        get_human_age("0", "0")
