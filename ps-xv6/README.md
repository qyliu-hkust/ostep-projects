# xv6 Lab: Implementing proclist() and the ps Command

## Objectives
By completing this lab, you will:

- Understand how xv6 manages processes through the struct proc process table.
- Learn to safely access kernel data structures using spinlocks (p->lock).
- Implement a new system call (proclist) in xv6.
- Build a simple user-level command (ps) that lists all running processes.

## Background
In xv6, all processes are stored in the global array `proc[NPROC]`, and each process is represented by a `struct proc`:
```c
struct proc {
  struct spinlock lock;
  enum procstate state;
  int pid;
  struct proc *parent;
  char name[16];
  ...
};
```

Each process can be in one of several states:
| State      | Meaning                          |
| ---------- | -------------------------------- |
| `UNUSED`   | Unused slot                      |
| `SLEEPING` | Waiting for an event or resource |
| `RUNNABLE` | Ready to run (waiting for CPU)   |
| `RUNNING`  | Currently executing              |
| `ZOMBIE`   | Exited but not yet cleaned up    |


## Your Task
You will implement a kernel function proclist() that prints information about all processes in the system, then expose it as a system call and write a user-level command `ps`.

**Hint**:
- Always acquire `p->lock` before accessing process fields. (try to think about why)
- You may safely read `p->parent->pid` under `p->lock`.


**Expected Output**
```sh
PID     PPID    STATE           NAME
1       0       SLEEPING        init
2       1       SLEEPING        sh
3       2       RUNNING         ps
```

## Report Requirement
You should submit a report including:

1. **Objective**: Briefly describe what you learned from the lab.
2. **Design and Implementation**: How xv6 system calls work (user → kernel → function).
3. **Description of struct proc**
4. **Implementation Steps**: Show what files you modified, and how (proc.c, syscall.c, etc.).
5. **Results**: Show screenshots or terminal output from ps.
6. **Analysis**: Explain why init and sh are sleeping. Discuss lock usage and process states. Reflect on difficulties and takeaways. 