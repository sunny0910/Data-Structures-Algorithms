# Simple Database Challenge

In the Simple Database problem, you'll implement an in-memory key/value
database similar to Redis. For simplicity's sake, instead of dealing with IO
you only need to implement the internal functionality as if it were a database
library.

## Guidelines

* You have 45 minutes to work on the implementation. Get as far as you can and
  be prepared to discuss your approach and how you would complete the exercise
  afterward.
* Given the time limitation focus on your implementation and mention
  performance or style concerns to the interviewer for later discussion.

### Suggested Approach

* Read through this README to understand the problem.
* Read through `simpledbtest.py` and run tests to see where they fail.
* Try to get 1 test passing at a time. From top to bottom in `simpledbtest.py`.

## Database Operations

The scope of the exercise is to implement the internal functionality covered by
the test suite, **not** parsing input and producing output.

The database supports the following operations:

* `SET name value` – Set the key `name` to the integer value `value`.
* `GET name` – Retrieve the value of the key `name`.
* `UNSET name` – Unset the key `name`, making it as if the key was never set.

```
INPUT	            OUTPUT
--------------------------
SET ex 10
GET ex              10
UNSET ex
GET ex              NULL


INPUT	            OUTPUT
--------------------------
SET a 5
GET a               5
SET b 10
SET b 30
GET b               30
GET a               5
```

## Transaction Commands

In addition to the above data operations, your program should also support
transactions by implementing these operations:

* `BEGIN` – Start a new transaction. **Transactions can be nested;** a
  `BEGIN` can be issued inside of an existing transaction.
* `ROLLBACK` – Undo operations issued in the current transaction and closes it.
  Returns an error if no transaction is in progress.
* `COMMIT` – Close **all** open transactions and permanently apply the changes
  made in them. Returns an error if no transaction is in progress.

Any operation run outside of a transaction should apply immediately.

Here are some example operations:

```
INPUT	          OUTPUT
------------------------
BEGIN
SET a 10
GET a             10
BEGIN
SET a 20
GET a             20
ROLLBACK
GET a             10
ROLLBACK
GET a             NULL


INPUT	          OUTPUT
------------------------
BEGIN
SET a 30
BEGIN
SET a 40
COMMIT
GET a             40
ROLLBACK          NO TRANSACTION


INPUT	          OUTPUT
------------------------
SET a 50
BEGIN
GET a             50
SET a 60
BEGIN
UNSET a
GET a             NULL
ROLLBACK
GET a             60
COMMIT
GET a             60
```
