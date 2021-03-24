# ready-python-logs
Simple logger ready to use.

## Setup

```shell
pip install git+https://github.com/alejandroperezcosio/ready-python-logs.git
```

## Usage
```python
from rpylogs import log

something = 2+2
log.info('Log this line with a variable {}'.format(something))
```

## Log levels
```python
log.debug('message')
2021-03-24 15:11:20,719Z DEBUG: message

log.info('message')
2021-03-24 15:11:26,413Z INFO: message

log.warning('message')
2021-03-24 15:11:31,501Z WARNING: message

log.error('message')
2021-03-24 15:11:35,591Z ERROR: message
```