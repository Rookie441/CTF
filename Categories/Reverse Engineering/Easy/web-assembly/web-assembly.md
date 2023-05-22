## Web Assembly

 [chall.js](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Easy/web-assembly/chall.js)

```js
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Gimme something: ', (flag) => {
    const wasmBinBuf = new Uint8Array([0, 97, 115, 109, 1, 0, 0, 0, 1, 5, 1, 96, 0, 1, 127, 2, 11, 1, 2, 106, 115, 3, 109, 101, 109, 2, 0, 1, 3, 2, 1, 0, 7, 9, 1, 5, 99, 104, 101, 99, 107, 0, 0, 10, 122, 1, 120, 1, 3, 127, 65, 0, 33, 0, 65, 1, 33, 2, 3, 64, 2, 64, 2, 64, 2, 64, 2, 64, 2, 64, 32, 0, 65, 4, 112, 14, 3, 3, 2, 1, 0, 11, 65, 137, 2, 33, 1, 12, 3, 11, 65, 59, 33, 1, 12, 2, 11, 65, 41, 33, 1, 12, 1, 11, 65, 31, 33, 1, 12, 0, 11, 32, 1, 65, 255, 1, 32, 0, 40, 2, 0, 113, 108, 65, 255, 1, 113, 32, 0, 65, 192, 0, 106, 40, 2, 0, 65, 255, 1, 113, 115, 65, 0, 70, 32, 2, 108, 33, 2, 32, 0, 65, 1, 106, 33, 0, 32, 0, 65, 46, 72, 13, 0, 11, 32, 2, 11])
    const wasmMem = new WebAssembly.Memory({ initial: 10, maximum: 100 });
    var strBuf = new TextEncoder().encode(flag.slice(0, 64));
    const memBuf = new Uint8Array(wasmMem.buffer);

    for (let i = 0; i < strBuf.length; i++) {
        memBuf[i] = strBuf[i];
    }

    data = [121, 66, 71, 65, 229, 176, 150, 150, 43, 107, 209, 212, 12, 217, 16, 222, 129, 189, 55, 185, 82, 127, 229, 47, 45, 178, 252, 11, 107, 43, 31, 114, 20, 97, 229, 185, 237, 55, 252, 87, 12, 168, 75, 222, 121, 5]

    for (let i = 0; i < data.length; i++) {
        memBuf[i + 64] = data[i]
    }

    WebAssembly.instantiate(wasmBinBuf, {js: {mem: wasmMem}}).then(wasmModule => {
        result = wasmModule.instance.exports.check();
        if (result) {
            console.log("Correct flag!");
        } else {
            console.log("?")
        }
    });
    rl.close();
});
```

> This program will ask for the flag and if it is correct, it prints "Correct flag!", else it prints "?".

> The flag checking function can be found in `wasmModule.instance.exports.check();`. However, we do not have access to this. We do however, have access to the `wasmBinBuf` which is instantiated as a `Uint8Array`

> To visualize what those values represent, I ran a simple python script to convert the integers in the array using python `chr()` method.

```python
memory = [0, 97, 115, 109, 1, 0, 0, 0, 1, 5, 1, 96, 0, 1, 127, 2, 11, 1, 2, 106, 115, 3, 109, 101, 109, 2, 0, 1, 3, 2, 1, 0, 7, 9, 1, 5, 99, 104, 101, 99, 107, 0, 0, 10, 122, 1, 120, 1, 3, 127, 65, 0, 33, 0, 65, 1, 33, 2, 3, 64, 2, 64, 2, 64, 2, 64, 2, 64, 2, 64, 32, 0, 65, 4, 112, 14, 3, 3, 2, 1, 0, 11, 65, 137, 2, 33, 1, 12, 3, 11, 65, 59, 33, 1, 12, 2, 11, 65, 41, 33, 1, 12, 1, 11, 65, 31, 33, 1, 12, 0, 11, 32, 1, 65, 255, 1, 32, 0, 40, 2, 0, 113, 108, 65, 255, 1, 113, 32, 0, 65, 192, 0, 106, 40, 2, 0, 65, 255, 1, 113, 115, 65, 0, 70, 32, 2, 108, 33, 2, 32, 0, 65, 1, 106, 33, 0, 32, 0, 65, 46, 72, 13, 0, 11, 32, 2, 11]
chr_values = [chr(element) for element in memory]
print(''.join(chr_values))
```

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Easy/web-assembly/wasm.png)

> In the output, we can see `asm` which is a header for `.wasm` files. We can also see `check`, which is the name of the function

> We can then output this into a `.wasm` file using the following python code:

```python
import array
memory = [0, 97, 115, 109, 1, 0, 0, 0, 1, 5, 1, 96, 0, 1, 127, 2, 11, 1, 2, 106, 115, 3, 109, 101, 109, 2, 0, 1, 3, 2, 1, 0, 7, 9, 1, 5, 99, 104, 101, 99, 107, 0, 0, 10, 122, 1, 120, 1, 3, 127, 65, 0, 33, 0, 65, 1, 33, 2, 3, 64, 2, 64, 2, 64, 2, 64, 2, 64, 2, 64, 32, 0, 65, 4, 112, 14, 3, 3, 2, 1, 0, 11, 65, 137, 2, 33, 1, 12, 3, 11, 65, 59, 33, 1, 12, 2, 11, 65, 41, 33, 1, 12, 1, 11, 65, 31, 33, 1, 12, 0, 11, 32, 1, 65, 255, 1, 32, 0, 40, 2, 0, 113, 108, 65, 255, 1, 113, 32, 0, 65, 192, 0, 106, 40, 2, 0, 65, 255, 1, 113, 115, 65, 0, 70, 32, 2, 108, 33, 2, 32, 0, 65, 1, 106, 33, 0, 32, 0, 65, 46, 72, 13, 0, 11, 32, 2, 11]
# Convert memory to bytes
memory_bytes = array.array('B', memory).tobytes()
# Write bytes to a .wasm file
with open('output.wasm', 'wb') as file:
    file.write(memory_bytes)
```

> Now, with the `.wasm` file, we can proceed to use tools to give us a human-readable format of the `check()` function

> I used [WebAssembly Binary Toolkit](https://github.com/WebAssembly/wabt), setup was done in Linux so I used Cmake and Ninja.

> I can then supply the `output.wasm` file and direct the output to a new file named `output.dump`

```
bin/wasm-decompile ../../../output.wasm -o ../../../output.dump
```

> We get a more readable format:

```c
import memory js_mem;

export function check():int {
  var b:int;
  var a:int_ptr = 0;
  var c:int = 1;
  loop L_a {
    br_table[B_c, B_d, B_e, ..B_f](a % 4)
    label B_f:
    b = 265;
    goto B_b;
    label B_e:
    b = 59;
    goto B_b;
    label B_d:
    b = 41;
    goto B_b;
    label B_c:
    b = 31;
    goto B_b;
    label B_b:
    c = (((b * (255 & a[0]) & 255) ^ ((a + 64)[0]:int & 255)) == 0) * c;
    a = a + 1;
    if (a < 46) continue L_a;
  }
  return c;
}
```

> We can sort of see what the function does to check if the flag is the correct one. But to make it easier for us to write a script, I will ask ChatGPT to convert the above to Python.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Easy/web-assembly/chatgpt.png)

> Now, we can create a python script to solve the challenge. I did not reverse from the elements of the data array, but instead used bruteforce since it is not intensive

```python
##mem = [0, 97, 115, 109, 1, 0, 0, 0, 1, 5, 1, 96, 0, 1, 127, 2, 11, 1, 2, 106, 115, 3, 109, 101, 109, 2, 0, 1, 3, 2, 1, 0, 7, 9, 1, 5, 99, 104, 101, 99, 107, 0, 0, 10, 122, 1, 120, 1, 3, 127, 65, 0, 33, 0, 65, 1, 33, 2, 3, 64, 2, 64, 2, 64, 2, 64, 2, 64, 2, 64, 32, 0, 65, 4, 112, 14, 3, 3, 2, 1, 0, 11, 65, 137, 2, 33, 1, 12, 3, 11, 65, 59, 33, 1, 12, 2, 11, 65, 41, 33, 1, 12, 1, 11, 65, 31, 33, 1, 12, 0, 11, 32, 1, 65, 255, 1, 32, 0, 40, 2, 0, 113, 108, 65, 255, 1, 113, 32, 0, 65, 192, 0, 106, 40, 2, 0, 65, 255, 1, 113, 115, 65, 0, 70, 32, 2, 108, 33, 2, 32, 0, 65, 1, 106, 33, 0, 32, 0, 65, 46, 72, 13, 0, 11, 32, 2, 11]
data = [121, 66, 71, 65, 229, 176, 150, 150, 43, 107, 209, 212, 12, 217, 16, 222, 129, 189, 55, 185, 82, 127, 229, 47, 45, 178, 252, 11, 107, 43, 31, 114, 20, 97, 229, 185, 237, 55, 252, 87, 12, 168, 75, 222, 121, 5]
##mem[64:64+len(data)] = data

def check(x,a):
    b = 0
    c = 1
    if a % 4 == 0:
        b = 31
    elif a % 4 == 1:
        b = 41
    elif a % 4 == 2:
        b = 59
    else:
        b = 265

    c = ((b * (255 & x) & 255) ^ (data[a] & 255) == 0) * c
    #a += 1

##    if a >= 46:
##        break
    return c

for y in range(46):
    for i in range(128): # Use 256 for full range
        if check(i,y) == 1:
            print(chr(i),end="")
            break
```

```
grey{0bfusc4t10n_u51ng_w3b4s53mbly_1s_4_th1ng}
```

`grey{0bfusc4t10n_u51ng_w3b4s53mbly_1s_4_th1ng}`
