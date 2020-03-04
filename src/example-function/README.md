# my-example-function

Is an example of a Lambda function built in Python, compliant with the Connect pipeline.
This example sets out recommended conventions for working with Python Connect components.

The main function implementation is contained in `example_lambda.py`. When called, the function will return `HelloMessage`
to get the IP address of the execution location, and return a simple response including the message.

In addition, the files `/test/integration/pre_traffic_test_data.py` and `/test/integration/post_traffic_test_data.py` provide simple examples of how to implement a pre-traffic shifting hook
and post-traffic shifting hook, respectively. Both of the hook functions use the `boto3` lambda client to invoke the `example_lambda.py` function
and test that the response was succesful . However, it's possible to run any arbitrary code within these checks,
depending on what's useful for the real function being tested. Consideration of how to test a function needs to be made during the
design of a new function, and it may not always be necessary or useful to include traffic shifting hooks.

Unit tests are includes under the `test/unit` subdirectory of the function.


## Pre-requisites

Your development environment needs to have the following pre-requisites configured:

#### [Python 3.7](https://www.python.org/downloads/release/python-370/)
    
If on OSX, install using [these](https://docs.python-guide.org/starting/install3/osx/) instructions.

#### [pipenv](https://pypi.org/project/pipenv/)

pipenv is a package manager which combines the functionalities of pip and virtualenv.

Install using instructions [here](https://pypi.org/project/pipenv/). e.g. for OSX `brew install pipenv`

#### Development environment

Once above tools are installed...
Clone the repo, open a terminal window at the repo root, then change directory to the source code for the function
you plan to work on (`cd my-example-function`). Then:

```bash
pipenv sync --dev
```

This command creates a Python virtual environment, then installs Python 3.7 and libraries to the virtual environment.
Effectively it synchronises your environment with the contents of Pipfile.lock.

If you want to check where the virtual environment is on the filesystem, use the command `pipenv --venv`.

Subsequent commands to run tests, etc, will need to be executed via pipenv to ensure that they run within the
correct virtual env.

## Running tests
Tests can be run within the pipenv environment using [pytest](https://docs.pytest.org/en/latest/). Do this from within the function's directory (i.e.
where the Pipfile is located). Use this command...

```bash
AWS_XRAY_CONTEXT_MISSING=LOG_ERROR pipenv run pytest . -W "ignore::DeprecationWarning" --cov=. --cov-fail-under 80
```

If everything is working, you should see output similar to:

```
================================================================================ test session starts =================================================================================
platform darwin -- Python 3.7.2, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /Users/tomasz/Workspace/internal/cx-project-skeleton-repo/src/cx-example-function, inifile: pytest.ini
plugins: cov-2.7.1, html-1.21.1, mock-1.10.4, metadata-1.8.0
collected 1 item                                                                                                                                                                     

test/unit/test_example_lambda.py .                                                                                                                                             [100%]

---------- coverage: platform darwin, python 3.7.2-final-0 -----------
Name                Stmts   Miss  Cover
---------------------------------------
example_lambda.py      13      0   100%

Required test coverage of 80% reached. Total coverage: 100.00%

============================================================================== 1 passed in 4.74 seconds ==============================================================================
```

The `pipenv run` command here is running pytest within the virtual env created earlier. The `-W` flag tells it to
ignore warnings of type DeprecationWarning containing the specified text. These warnings come from a library requirement.
The `--cov` flag tells pytest to report test coverage, and `--cov-fail-under 80` will cause pytest to fail if unit test
coverage is below 80%.


## Lint checks

Besides unit tests, the pipeline runs several static lint checking tools. It's also possible to run these tools locally if desired, as follows.

### flake8

Another useful tool to run is [flake8](http://flake8.pycqa.org/en/latest/):
```bash
pipenv run flake8 . --max-complexity 10
``` 
flake8 carries out static analysis of the source code to check for consistency with [pep8](https://www.python.org/dev/peps/pep-0008/) coding style.
The `--max-complexity` flag instructs flake8 to also measure the "McCabe complexity" of the code and to fail if this exceeds a score of 10.

### safety

The [safety](https://pypi.org/project/safety/) tool checks library requirements against a vulnerability database. This tool is integrated with
pipenv. To run use:

```bash
pipenv check
```

### bandit

[Bandit](https://pypi.org/project/bandit/) is a security linting tool, which can be run using the command:

```bash
pipenv run bandit -r . -x test
``` 

