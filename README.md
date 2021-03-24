# ready-python-logs
## Setup

```shell
pip install git+https://github.com/alejandroperezcosio/ready-python-logs.git
```

## Usage
```python
from ready-python-logs import log

something = 2+2
log.info('Log this line with a variable {}'.format(something))
```