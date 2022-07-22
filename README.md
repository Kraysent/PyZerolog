# PyZerolog
This is yet another python logger inspired by logging module for Go programming language [zerolog](https://github.com/rs/zerolog).

## Why another logger?
Python has very powerful `logging` module which covers most of the needs. Though when in comes to JSON logging, it becomes hard to deal with: you need at to write the whole another formatter at the very least. 

This logging module has JSON logging enabled by default. It also takes advantage of types of fields provided in the logger and anables user to write their own type formatter. 

You can install it with
```bash
pip install pyzerolog
```

## Getting started

It is as easy as:
```python
from zlog import logger

logger.info().msg("Some logging message")
```
Which should print the following line into stdout:
```
{"level": "info", "message": "Some logging message", "timestamp": "2022-07-22T21:58:55.203468"}
```

### Adding custom fields
If you want to print your own fields, you may very well do so:
```python
logger.info().string("string_key", "value").msg("Message with string")

logger.info().int("integer_key", 123).msg("Message with int")

logger.info().string("some_key", "example").int("another_key", 5).msg("Message with int and string")

logger.info().bool("is_valid", True).string("login", "super_user").int("attempt", 8).msg("Some logging data about the user")
```
Which will print (line by line):
```
{"fields": {"string_key": "value"}, "level": "info", "message": "Message with string", "timestamp": "2022-07-22T21:58:56.929238"}
```
```
{"fields": {"integer_key": 123}, "level": "info", "message": "Message with int", "timestamp": "2022-07-22T21:58:56.930486"}
```
```
{"fields": {"another_key": 5, "some_key": "example"}, "level": "info", "message": "Message with int and string", "timestamp": "2022-07-22T21:58:56.930695"}
```
```
{"fields": {"attempt": 8, "is_valid": true, "login": "super_user"}, "level": "info", "message": "Some logging data about the user", "timestamp": "2022-07-22T21:58:56.930921"}
```

As you see, all of your fields would be stored under the `fields` key.

### Making output more readable

Despite being very convinient when reading logs with machinery, raw JSON may not be as pretty when read by human. You can customize your logs with several different approaches:

#### Customize JSON itself
Under the hood initial logger uses special JSON formatter. It can be customized. For example:
```python
logger.prettify = False
logger.info().msg("This message would be in one line.")
logger.prettify = True
logger.info().msg("And this would have some nice formatting.")
```
Which will print
```
{"level": "info", "message": "This message would be in one line.", "timestamp": "2022-07-22T21:59:00.839581"}
```
```
{
  "level": "info",
  "message": "And this would have some nice formatting.",
  "timestamp": "2022-07-22T21:59:00.840572"
}
```

#### Use special console formatter
If you don't plan to use your logs outside the terminal, you may use `ConsoleFormatter` which prints the log entry in human-readable format:
```python
from zlog import logger, ConsoleFormatter

logger.formatter = ConsoleFormatter()
logger.info().string("android", "iphone").bool("error", False).msg("Convinient one-liner message")
```

Which results in pretty-looking
```
23:06 INF Convinient one-liner message android=iphone error=False
```
