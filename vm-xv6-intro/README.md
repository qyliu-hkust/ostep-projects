
# Intro To xv6 Virtual Memory

In this project, you'll be changing xv6 to support a feature virtually
every modern OS does: causing an exception to occur when your program
dereferences a null pointer, and adding the ability to change the protection
levels of some pages in a process's address space.

## Null-pointer Dereference

In xv6, the VM system uses a simple multi-level page table as discussed in
class. As it currently is structured, user code is loaded into the very first
part of the address space. Thus, if you dereference a null pointer, you will
not see an exception (as you might expect); rather, you will see whatever code
is the first bit of code in the program that is running. Try it and see!

Thus, the first thing you might do is create a program that dereferences a
null pointer. It is simple! See if you can do it. Then run it on Linux as well
as xv6, to see the difference.

Your job here will be to figure out how xv6 sets up a page table. Thus, once
again, this project is mostly about understanding the code, and not writing
very much. Look at how **exec()** works to better understand how address
spaces get filled with code and in general initialized.

You should also look at `fork()`, in particular the part where the
address space of the child is created by copying the address space of the
parent. What needs to change in there?

The rest of your task will be completed by looking through the code to figure
out where there are checks or assumptions made about the address space. Think
about what happens when you pass a parameter into the kernel, for example; if
passing a pointer, the kernel needs to be very careful with it, to ensure you
haven't passed it a bad pointer. How does it do this now? Does this code need
to change in order to work in your new version of xv6?

One last hint: you'll have to look at the xv6 makefile as well. In there
user programs are compiled so as to set their entry point (where the first
instruction is) to 0. If you change xv6 to make the first page invalid,
clearly the entry point will have to be somewhere else (e.g., the next page,
or 0x1000). Thus, something in the makefile will need to change to reflect
this as well.

## Report Requirement
In the report, you need to answer the following questions:
- How do you test null pointer access? And what are the results on both xv6 and a regular Linux (e.g., Ubuntu)?
- Explain the reasons if the results are different.
- Introduce how xv6 translates a virtual address.
- Introduce how you implement the zero-pointer dereference checking feature.
- Show the results of null pointer access after implementing the zero-pointer dereference checking.
- Summarize what you have learned via this experiment. 




