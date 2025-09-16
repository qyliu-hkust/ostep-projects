
In this directory, you should write the program `mycat.c` (similar to `cat` utility) and compile it into
the binary `mycat` (e.g., `gcc -o mycat mycat.c -Wall -Werror`).

After doing so, you can run the tests from this directory by running the
`test-mycat.sh` script. If all goes well, you will see:

```sh
prompt> ./test-mycat.sh
test 1: passed
test 2: passed
test 3: passed
test 4: passed
test 5: passed
test 6: passed
test 7: passed
prompt>
```

The `test-mycat.sh` script is just a wrapper for the `run-tests.sh` script in
the `tester` directory of this repository. This program has a few options; see
the relevant
[README](https://github.com/qyliu-hkust/ostep-projects/blob/master/tester/README.md)
for details.


Some Hints: 

- Check usages of `open()`
- Check each testing point under [folder](https://github.com/qyliu-hkust/ostep-projects/tree/master/initial-utilities/wcat/tests) 

