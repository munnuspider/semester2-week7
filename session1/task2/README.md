# Task 2

## `undefined.c`

1. Compile  `undefined.c` without any special compiler options:

       gcc undefined.c

2. Run the compiled program to see what it does:

       ./a.out

   **Then remove `a.out`**.

3. Recompile `undefined.c`, this time using the `-Wall` option:

       gcc -Wall undefined.c

   What do you see in the terminal?

4. Run the program to verify that behaviour is unchanged,
   **then remove `a.out` once again**.

5. Recompile `undefined.c` using the `-Wall` and `-Werror` options. Does the
   compiler output change in any way? Is an executable generated? An executable isn't generated, instead it shows the uninitialised i and j: we know that there are no exisiting values of i and j being set.
   We'd have to do something along the lines of:
   int i = 0, j = 0; 

## `double_free.c`

1. Compile `double_free.c` using the `-Wall`, `-Wextra` and `-Werror`
   compiler options. Do you see any messages from the compiler?
   Does compilation succeed? Compilation doesn't succeed.
   Error messages include stuff like "pointer 'a' used after 'free'"

2. Run the compiled program. What happens? Do you get any clues about what
   has gone wrong? It says Aborted (core dumped) - could imply that the second "free(a) is undefined"

3. Repeat Step 1 for `crash.c` from Task 1. What can you conclude from these
   experiments about the compiler options that you have used?
   Initially, just recompiling the double_free.c file and running it different times, you get a random value from memory each time which is a key example of undefined behaviour i.e., we cannot predict the value returned by the value.
