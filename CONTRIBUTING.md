# Contributing
to improve productivity, follow these rules please.

## important notes
- ensure any install or build dependencies are removed before the end of the layer when doing a build.
- write tests for any function you are working on (more details in tests section)

## tests
- all tests must be placed inside `app/test` directory
- the test file name must be in the format **[name_in_snake_case]_test.py**

for more details see [this](app/test/model_puzzle_test.py).

**NOTE**: to check your code is working fine, import your blahblah_test.py inside [run_tests.py](app/test/run_tests.py). then run `python run_tests.py` and check the results.

## preferred development way
TDD. turn requirements into very specific test cases, then write a code which pass the test.
