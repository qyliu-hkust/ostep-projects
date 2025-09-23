
# Install Notes

We use xv6-riscv for our experiments, which is the major version of xv6 maintained 
by MIT. 

## The xv6 Source Code

To obtain the xv6 source code, just clone it from github:

```sh
prompt> git clone https://github.com/mit-pdos/xv6-riscv.git
```

There! Now you have completed the easiest part.

## Prepare Dependencies for xv6

### Linux (Ubuntu/WSL or other distributions)
```sh
prompt> sudo apt-get install git build-essential gdb-multiarch qemu-system-misc gcc-riscv64-linux-gnu binutils-riscv64-linux-gnu
```

### MacOS (Suppose you have homebrew)
```sh
prompt> brew tap riscv/riscv
prompt> brew install riscv-tools
prompt> brew install qemu
```

## Compile and Play
```sh
prompt> make qemu
```

## Some Notes

- How to quit xv6? `Ctrl+A` then `X`
- Reference: https://pdos.csail.mit.edu/6.828/2012/xv6/book-rev7.pdf
- User space utilities and libraries are under `/user` folder
- Kernel space implementations are under `/kernel` folder
