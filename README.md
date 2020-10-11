# Algo Studies

This is a catch-all repo for my study of algorithms and their implementations in Python 3.
There is no real structure to it, so one can find solutions to problems from the [Daily Coding Problem](https://www.amazon.com/Daily-Coding-Problem-exceptionally-interviews/dp/1793296634) book, leetcode solutions or programming assignments from the [Algorithms](https://www.coursera.org/specializations/algorithms) specialization on coursera...

## How to run the tests

All tests are under the root folder `test`

At first I wrote them using the built-in `unittest` module. To run those in the `dynamic` package, run the below : 
```shell script
python -m unittest discover test/dynamic -v
```
I found `unittest` worked but was slightly verbose and did not auto-discover test modules. So I switched to [`pytest`](https://docs.pytest.org/en/stable/index.html) for the coursera programming assignments.
```shell script
PYTHONPATH=. pytest test/coursera/ -v
```
