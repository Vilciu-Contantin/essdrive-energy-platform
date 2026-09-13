// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

//ERC-3643 token interface
import "@erc3643/contracts/token/IToken.sol";

contract EssToken is IToken {
    string private_name = "ESS CEF Token";
    string private_symbol = "ESS";
    uint8 private_decimals = 18;
    uint256 private_totalSupply = 1000000 * 10 ** uint256(private_decimals);

    function name() external view override returns (string memory) {
        return private_name;
    }

    function symbol() external view override returns (string memory) {
        return private_symbol;
    }

    function decimals() external view override returns (uint8) {
        return private_decimals;
    }

    function totalSupply() external view override returns (uint256) {
        return private_totalSupply;
    }
}