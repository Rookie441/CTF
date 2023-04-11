## Navigating The Unknown

[README.md](https://github.com/Rookie441/CTF/blob/main/Categories/Blockchain/Easy/navigating-the-unknown/README.md)  
[Setup.sol](https://github.com/Rookie441/CTF/blob/main/Categories/Blockchain/Easy/navigating-the-unknown/Setup.sol)  
[Unknown.sol](https://github.com/Rookie441/CTF/blob/main/Categories/Blockchain/Easy/navigating-the-unknown/Unknown.sol)  

> By analyzing Setup.sol and Unknown.sol, we can deduce that in order for `isSolved()` to return True, we need to pass in the argument `10` of type uint256 to the function `updateSensors()`

```c
pragma solidity ^0.8.18;

import {Unknown} from "./Unknown.sol";

contract Setup {
    Unknown public immutable TARGET;

    constructor() {
        TARGET = new Unknown();
    }

    function isSolved() public view returns (bool) {
        return TARGET.updated();
    }
}
```

```c
pragma solidity ^0.8.18;


contract Unknown {

    bool public updated;

    function updateSensors(uint256 version) external {
        if (version == 10) {
            updated = true;
        }
    }

}
```

> We can visualize this in the [Remix IDE](https://remix.ethereum.org/). First, compile the two .sol files and then deploy the `Setup.sol`. Then, call the `TARGET` and copy the address to be used for the address-specific deployment of `Unknown.sol`

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Blockchain/Easy/navigating-the-unknown/deploy.png)  

> We can then proceed to call the `updateSensors()` function with `10` as the argument and check if updated is `True`, then we can also see that `isSolved()` is now `True`.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Blockchain/Easy/navigating-the-unknown/issolved.png)  

> In this challenge however, we need to connect to the netcat service to give us the flag. We are given the `RFC URL`, and also other connection information details like `Target contract address` and `Setup contract address`.

> The following is the python code created to solve this challenge. We first need to define the ABI for the contracts from the .sol codes. One way to get the ABI is to paste it in Remix IDE, compile it, and then click the `ABI` button to copy the ABI into your clipboard.

> Alternatively, we can also use [chatGPT](https://chat.openai.com/chat) to do it for us. The following is the final python code:

```python
from web3 import Web3

# Connect to the RFC URL
w3 = Web3(Web3.HTTPProvider('http://165.232.98.11:32633/'))

# Define the ABI for the contracts
setup_abi = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [],
    "name": "TARGET",
    "outputs": [
      {
        "internalType": "contract Unknown",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "isSolved",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
] # ABI for the Setup contract


unknown_abi = [
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "version",
        "type": "uint256"
      }
    ],
    "name": "updateSensors",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "updated",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
] # ABI for the Unknown contract

# Define the addresses for the contracts
setup_address = '0x5b48152d48D1ACb5a7e03a2FcC4A8C49320b4700' # Address of the Setup contract
unknown_address = '0xe90f7BFd428C52870E86Cf787691D4f0E06033E6' # Address of the Unknown contract

# Create contract instances
setup_contract = w3.eth.contract(address=setup_address, abi=setup_abi)
unknown_contract = w3.eth.contract(address=unknown_address, abi=unknown_abi)

# Call the isSolved function on the Setup contract
is_solved = setup_contract.functions.isSolved().call()

# Check if the puzzle is already solved
if is_solved:
    print('The puzzle is already solved!')
else:
    # Call the updateSensors function on the Unknown contract
    tx_hash = unknown_contract.functions.updateSensors(10).transact()

    # Wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # Check if the transaction was successful
    if receipt.status == 1:
        print('The puzzle has been solved!')
    else:
        print('Failed to solve the puzzle :(')
```

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Blockchain/Easy/navigating-the-unknown/Solved.png)  

> An alternative approach is to use foundry as shown [here](https://sirius-a.github.io/ctf-writeups/writeups/2023/HTB-cyber-apocalypse/blockchain_navigating_the_unknown/)

`HTB{9P5_50FtW4R3_UPd4t3D}`
