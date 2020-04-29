This folder is for test files.
======
Additional Unit Tests can be found in [src > polls > tests.py]
======
### System Test Breakdown:
* Correct Data Input - Tests the intended functionality of the system.
* Multiple Row Submit Test - Checks that multiple rows works correctly.
* Multiple Submission Test - Checks that data can be entered more than once for correctness.
* Negative Data Input - Checks that data cannot be entered as negatives.
* Duplicate Jar Number Test - Checks that jar numbers cannot be used more than once.
======
### Unit Test Breakdown:
* testBasicPost() - Tests that the sites responds to basic post requests
* testJSONRequest() - Tests that the API call works as intended