# Lambda Calculus in Python (2025)

([up](https://hackmd.io/@alexhkurz/HkfERdbbkl))

The following exercises are based on the Python implementation of the lambda calculus in
- [lambdaC-2024](https://codeberg.org/alexhkurz/lambdaC-2024), 

following the mathematical specification of lambda calculus from 
- [Lambda Calculus, Syntax and Semantics](https://hackmd.io/@alexhkurz/rJR2H3YCR) and 
- [Church Encodings](https://hackmd.io/@alexhkurz/Syk6Rbzyye) and 
- [Fixed Point Combinator](https://hackmd.io/@alexhkurz/H1iUDwHyyg).

## Learning Outcomes

- Direct, domain specific, technical:

	- testing and `assert` ([Python Language Reference](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-assert_stmt)) ([Stackoverflow](https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python))
	- understanding the implementation of capture-avoiding substitution
	- using the [python debugger in vscode](https://code.visualstudio.com/docs/python/debugging) 
	    - breakpoints and debug console instead of print statements
	    - creating recursive traces with the debugger
	    - comparing handcrafted traces with the ones obtained from the debugger
	- ability to modify the interpreter
	- appreciating different evaluation strategies ([Wikipedia](https://en.wikipedia.org/wiki/Reduction_strategy))

- Indirect, meta-cognitive, transferable, generic:

	- debugging of recursive algorithms
	- understanding the relationship between mathematical specifications and implementations
	- developing intuition about algorithmic behaviour through tracing executions with software tools
	- learning to read and modify existing codebases
	- making a MWE ([Stackoverflow](https://stackoverflow.com/help/minimal-reproducible-example))
	- verifying that an implementation conforms to its specification


## Exercises

Recall that a $\lambda$-expression is in ***normal form*** in case it cannot be further reduced.

0. Make a local copy of [lambdaC-2024](https://codeberg.org/alexhkurz/lambdaC-2024).

### Testing the Interpreter

1. Run `python interpreter_test.py`. Does our Python implementation of lambda calculus conforms to its specification given by its mathematical theory?

2. Add some of the lambda-expressions from the lectures on [Lambda Calculus](https://hackmd.io/@alexhkurz/rJR2H3YCR) and on [Church Encodings](https://hackmd.io/@alexhkurz/Syk6Rbzyye) to `test.lc` and run the interpreter with `python interpreter.py test.lc`. [^listOfPrograms]
    - Always formulate an expected result before executing a test. 
    - For example, explain why `a b c d` reduces to `(((a b) c) d)` and why `(a)` reduces to `a`.
    - Etc ... make your own tests ...
    - From HW5 we remember that `(\f.\x.f(f(x))) (\f.\x.(f(f(f x))))` should evaluate to the Church numeral for 9 (according to the mathematical definition of the lambda calculus operational semantics).
`

3. How does capture avoiding substitution work? Investigate both by making relevant test cases and by looking at the source code. How is it implemented?

4. Do you always get the expected result? Do all computations reduce to normal form? 

5. What is the smallest $\lambda$-expression you can find (minimal working example, MWE) that does not reduce to normal form? [^5]

[^5]: Use pen-and-paper computations (and/or the debugger, see item 6).

### Using the Debugger to Trace Executions

6. Use the python debugger to step through the interpreter.[^debugger] (You will need this for the next two items, but there is no need to write about this item in the report.)
    - In Vscode, look for "Run and Debug". Click the green play button. You should see a normal execution.
    - To "look under the hood" of the interpreter set a breakpoint. Run again. Inspect the variables. Do they match your expectation?
	- Experiment with the buttons "Continue", "Step Over", "Step Into". 
	- Follow the yellow arrow.
	- Watch the call stack.
	- Use the debug console, for example to print the value of variables as in `print(linearize(tree))`.

    Tip: If you have problems setting up your debugger, copy the file `.vscode/launch.json` from [lambdaC-2024](https://codeberg.org/alexhkurz/lambdaC-2024) in your local `.vscode` folder (create if it doesnt exist). Moreover, in Vscode use `Open Folder` to open the folder containing `interpreter.py` (to set up the correct workspace).

7. How does the interpreter evaluate `((\m.\n. m n) (\f.\x. f (f x))) (\f.\x. f (f (f x)))`? Do a calculation similarly to when you evaluated `((\m.\n. m n) (\f.\x. f (f x))) (\f.\x. f (f (f x)))` for the homework, but now follow *precisely* the steps taken by `interpreter.py`. Make a new line for each substitution.

    Tip 1: Set breakpoints in the debugger around calls to the `substitute()` function.
    
    Tip 2: To extract information from the debugger, in the debug console, use commands such as `print(linearize(x))` where `x` is a variable in scope at the current breakpoint (yellow arrow).[^variables] 
    
    Tip 3: Here is the beginning of the (linear) trace of substitutions:
    ```
    ((\m.\n. m n) (\f.\x. f (f x))) (\f.\x. f (f (f x)))
    ((\Var1. (\f.\x. f (f x)) Var1) ) (\f.\x. f (f (f x)))
    ...
    ```
    
8. Now we want to get a better understanding of the evaluation strategy by tracing recursive calls to `evaluate()`. Use `((\m.\n. m n) (\f.\x. f (f x))) (\f.\x. f x)` as your input. Write out the trace of the interpreter in the format we used to picture the [recursive trace of `hanoi`](https://hackmd.io/@alexhkurz/ByLgLqNn0#Recursive-Trace-of-hanoi). Only write lines that contain calls to `evaluate()` or calls to`substitute()`[^substitute]. Add the line numbers. 

    Tip 1: Set breakpoints in the debugger at calls to the `evaluate()` function (and possibly also where[^pass]  `evaluate()` returns).
    
    Tip 2: Here is the beginning of the recursive trace:
    ```
    12: eval (((\m.(\n.(m n))) (\f.(\x.(f (f x))))) (\f.(\x.(f x))))
        39: eval ... 
    ```

    Tip 3: Watch the call stack in the debugger and note how it helps with getting the indentations rights.
    
### Modifying the Interpreter

9. Modify the code of `interpreter.py` so that it runs as expected on the MWE and other test cases.

    Tip: Use your work on Item 8.



[^debugger]: The debugger is a very powerful tool. To make the best use of it, takes time. It feels almost like a dialogue or negotiation. Think of it as an expert on your side that answers questions and helps you navigating the landscape of your code. Sometimes, you may want to modify the code to make it more amenable to debugging.

[^listOfPrograms]: Currently `test.lc` only contains
	```
	(\x.x) a
	(\x.\y.x) a b
	(\x.\y.y) a b
    ((\m.\n. m n) (\f.\x. f (f x))) (\f.\x. f (f (f x)))
	```
    
[^pass]: If you want to insert a line of code that does nothing Python has `pass`.

[^substitute]: Write out only the calls to `substitute()` in `evaluate()`: Ignore the recursive calls of `substitute()` to itself. 

[^variables]: For the task at hand, the relevant variables are `body,name,argument,rhs`.









