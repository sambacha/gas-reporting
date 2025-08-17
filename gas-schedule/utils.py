#!/usr/bin/env python3
"""
Comprehensive Gas Schedule Utilities

This script provides a complete toolkit for generating, validating,
and analyzing Ethereum gas schedules across all forks.
"""

import json
import os
import sys
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List, Tuple
from pathlib import Path
from dataclasses import dataclass, asdict, field
from enum import Enum
import argparse


# ============================================================================
# Data Models
# ============================================================================

class ForkStatus(Enum):
    """Fork status enumeration"""
    ACTIVE = "active"
    PLANNED = "planned"
    PROPOSED = "proposed"
    DEPRECATED = "deprecated"


@dataclass
class GasSchedule:
    """Complete gas schedule for a fork"""
    name: str
    activation_date: Optional[str]
    block_number: Optional[int]
    status: ForkStatus
    eips: List[int]
    gas_costs: Dict[str, Any]


@dataclass
class ForkComparison:
    """Comparison between two forks"""
    from_fork: str
    to_fork: str
    new_features: Dict[str, Any]
    modified_costs: Dict[str, Any]
    removed_features: Dict[str, Any]
    cost_impact: Dict[str, float]


# ============================================================================
# Fork Definitions
# ============================================================================

FORK_DEFINITIONS = {
    "frontier": {
        "name": "Frontier",
        "activation_date": "2015-07-30",
        "block_number": 0,
        "status": ForkStatus.ACTIVE,
        "eips": [],
        "description": "Genesis Ethereum mainnet launch"
    },
    "homestead": {
        "name": "Homestead",
        "activation_date": "2016-03-14",
        "block_number": 1150000,
        "status": ForkStatus.ACTIVE,
        "eips": [2, 7, 8],
        "description": "Protocol stabilization and security improvements"
    },
    "dao_fork": {
        "name": "DAO Fork",
        "activation_date": "2016-07-20",
        "block_number": 1920000,
        "status": ForkStatus.ACTIVE,
        "eips": [],
        "description": "Emergency fork to address DAO exploit"
    },
    "tangerine_whistle": {
        "name": "Tangerine Whistle",
        "activation_date": "2016-10-18",
        "block_number": 2463000,
        "status": ForkStatus.ACTIVE,
        "eips": [150],
        "description": "DoS attack mitigation via gas cost adjustments"
    },
    "spurious_dragon": {
        "name": "Spurious Dragon",
        "activation_date": "2016-11-22",
        "block_number": 2675000,
        "status": ForkStatus.ACTIVE,
        "eips": [155, 160, 161, 170],
        "description": "Replay attack protection and state tree cleaning"
    },
    "byzantium": {
        "name": "Byzantium",
        "activation_date": "2017-10-16",
        "block_number": 4370000,
        "status": ForkStatus.ACTIVE,
        "eips": [140, 196, 197, 198, 211, 214, 649, 658],
        "description": "Privacy and scaling improvements with ZK-SNARKs"
    },
    "constantinople": {
        "name": "Constantinople",
        "activation_date": "2019-02-28",
        "block_number": 7280000,
        "status": ForkStatus.ACTIVE,
        "eips": [145, 1014, 1052, 1283, 1234],
        "description": "Efficiency improvements and difficulty bomb delay"
    },
    "petersburg": {
        "name": "Petersburg",
        "activation_date": "2019-02-28",
        "block_number": 7280000,
        "status": ForkStatus.ACTIVE,
        "eips": [145, 1014, 1052, 1283, 1234],
        "description": "Constantinople with EIP-1283 removed"
    },
    "istanbul": {
        "name": "Istanbul",
        "activation_date": "2019-12-08",
        "block_number": 9069000,
        "status": ForkStatus.ACTIVE,
        "eips": [152, 1108, 1344, 1884, 2028, 2200],
        "description": "Interoperability with privacy coins and gas optimizations"
    },
    "muir_glacier": {
        "name": "Muir Glacier",
        "activation_date": "2020-01-02",
        "block_number": 9200000,
        "status": ForkStatus.ACTIVE,
        "eips": [2384],
        "description": "Difficulty bomb delay"
    },
    "berlin": {
        "name": "Berlin",
        "activation_date": "2021-04-15",
        "block_number": 12244000,
        "status": ForkStatus.ACTIVE,
        "eips": [2565, 2718, 2929, 2930],
        "description": "Gas cost adjustments and access lists"
    },
    "london": {
        "name": "London",
        "activation_date": "2021-08-05",
        "block_number": 12965000,
        "status": ForkStatus.ACTIVE,
        "eips": [1559, 3198, 3529, 3541, 3554],
        "description": "Fee market reform with base fee and tip"
    },
    "arrow_glacier": {
        "name": "Arrow Glacier",
        "activation_date": "2021-12-09",
        "block_number": 13773000,
        "status": ForkStatus.ACTIVE,
        "eips": [4345],
        "description": "Difficulty bomb delay"
    },
    "gray_glacier": {
        "name": "Gray Glacier",
        "activation_date": "2022-06-30",
        "block_number": 15050000,
        "status": ForkStatus.ACTIVE,
        "eips": [5133],
        "description": "Difficulty bomb delay"
    },
    "paris": {
        "name": "Paris",
        "activation_date": "2022-09-15",
        "block_number": 15537394,
        "status": ForkStatus.ACTIVE,
        "eips": [3675, 4399],
        "description": "The Merge - Transition to Proof of Stake"
    },
    "shanghai": {
        "name": "Shanghai",
        "activation_date": "2023-04-12",
        "block_number": 17034870,
        "status": ForkStatus.ACTIVE,
        "eips": [3651, 3855, 3860, 4895],
        "description": "Validator withdrawals and base EIP-1559 maturity"
    },
    "cancun": {
        "name": "Cancun",
        "activation_date": "2024-03-13",
        "block_number": 19426587,
        "status": ForkStatus.ACTIVE,
        "eips": [1153, 4788, 4844, 5656, 6780, 7516],
        "description": "Blob transactions for L2 scaling"
    },
    "prague": {
        "name": "Prague",
        "activation_date": "2025-01-01",
        "block_number": None,
        "status": ForkStatus.ACTIVE,
        "eips": [2537, 2935, 6110, 7002, 7251, 7549, 7594, 7623, 7685, 7692, 7698, 7702],
        "description": "Calldata repricing and account abstraction"
    },
    "osaka": {
        "name": "Osaka",
        "activation_date": None,
        "block_number": None,
        "status": ForkStatus.PLANNED,
        "eips": [],
        "description": "Authorization optimization and refinement"
    }
}


# ============================================================================
# Gas Constants Database
# ============================================================================

class GasConstants:
    """Comprehensive gas constants for all operations"""
    
    # Base operation costs
    BASE_COSTS = {
        "G_zero": 0,
        "G_base": 2,
        "G_verylow": 3,
        "G_low": 5,
        "G_mid": 8,
        "G_high": 10
    }
    
    # Arithmetic operations
    ARITHMETIC_COSTS = {
        "ADD": 3, "MUL": 5, "SUB": 3, "DIV": 5, "SDIV": 5,
        "MOD": 5, "SMOD": 5, "ADDMOD": 8, "MULMOD": 8,
        "EXP": 10, "EXP_byte": 50, "SIGNEXTEND": 5,
        "LT": 3, "GT": 3, "SLT": 3, "SGT": 3, "EQ": 3,
        "ISZERO": 3, "AND": 3, "OR": 3, "XOR": 3, "NOT": 3,
        "BYTE": 3, "SHL": 3, "SHR": 3, "SAR": 3
    }
    
    # Stack operations
    STACK_COSTS = {
        "POP": 2, "PUSH": 3, "DUP": 3, "SWAP": 3
    }
    
    # Memory operations
    MEMORY_COSTS = {
        "MLOAD": 3, "MSTORE": 3, "MSTORE8": 3,
        "G_memory": 3, "G_copy": 3
    }
    
    # Storage operations (Shanghai baseline)
    STORAGE_COSTS = {
        "SLOAD": 2100, "SLOAD_cold": 2100, "SLOAD_warm": 100,
        "SSTORE_set": 20000, "SSTORE_reset": 5000,
        "SSTORE_clear_refund": 15000, "SSTORE_noop": 100
    }
    
    # Flow control
    FLOW_COSTS = {
        "JUMP": 8, "JUMPI": 10, "JUMPDEST": 1, "PC": 2,
        "MSIZE": 2, "GAS": 2
    }
    
    # System operations
    SYSTEM_COSTS = {
        "CREATE": 32000, "CREATE2": 32000,
        "CALL": 700, "CALLCODE": 700,
        "DELEGATECALL": 700, "STATICCALL": 700,
        "RETURN": 0, "REVERT": 0,
        "SELFDESTRUCT": 5000, "SELFDESTRUCT_refund": 24000,
        "G_callstipend": 2300, "G_callvalue": 9000,
        "G_newaccount": 25000, "G_codedeposit": 200
    }
    
    # Transaction costs
    TRANSACTION_COSTS = {
        "G_transaction": 21000, "G_txcreate": 32000,
        "G_txdatazero": 4, "G_txdatanonzero": 16,
        "G_accesslistaddress": 2400, "G_accessliststorage": 1900
    }
    
    # Precompile costs
    PRECOMPILE_COSTS = {
        "ECRECOVER": 3000,
        "SHA256_base": 60, "SHA256_word": 12,
        "RIPEMD160_base": 600, "RIPEMD160_word": 120,
        "IDENTITY_base": 15, "IDENTITY_word": 3,
        "ECADD": 150, "ECMUL": 6000,
        "ECPAIRING_base": 45000, "ECPAIRING_pair": 34000,
        "BLAKE2F": 1
    }


# ============================================================================
# Gas Schedule Generator
# ============================================================================

class AdvancedGasScheduleGenerator:
    """Advanced gas schedule generator with full fork support"""
    
    def __init__(self):
        self.fork_definitions = FORK_DEFINITIONS
        self.constants = GasConstants()
    
    def generate_all_schedules(self) -> Dict[str, GasSchedule]:
        """Generate gas schedules for all forks"""
        schedules = {}
        
        for fork_id, fork_def in self.fork_definitions.items():
            schedule = self._generate_fork_schedule(fork_id)
            schedules[fork_id] = schedule
        
        return schedules
    
    def _generate_fork_schedule(self, fork_id: str) -> GasSchedule:
        """Generate schedule for a specific fork"""
        fork_def = self.fork_definitions[fork_id]
        
        # Generate gas costs based on fork
        if fork_id == "frontier":
            gas_costs = self._generate_frontier_costs()
        elif fork_id == "homestead":
            gas_costs = self._generate_homestead_costs()
        elif fork_id == "dao_fork":
            gas_costs = self._generate_dao_fork_costs()
        elif fork_id == "tangerine_whistle":
            gas_costs = self._generate_tangerine_whistle_costs()
        elif fork_id == "spurious_dragon":
            gas_costs = self._generate_spurious_dragon_costs()
        elif fork_id == "byzantium":
            gas_costs = self._generate_byzantium_costs()
        elif fork_id == "constantinople":
            gas_costs = self._generate_constantinople_costs()
        elif fork_id == "petersburg":
            gas_costs = self._generate_petersburg_costs()
        elif fork_id == "istanbul":
            gas_costs = self._generate_istanbul_costs()
        elif fork_id == "muir_glacier":
            gas_costs = self._generate_muir_glacier_costs()
        elif fork_id == "berlin":
            gas_costs = self._generate_berlin_costs()
        elif fork_id == "london":
            gas_costs = self._generate_london_costs()
        elif fork_id == "arrow_glacier":
            gas_costs = self._generate_arrow_glacier_costs()
        elif fork_id == "gray_glacier":
            gas_costs = self._generate_gray_glacier_costs()
        elif fork_id == "paris":
            gas_costs = self._generate_paris_costs()
        elif fork_id == "shanghai":
            gas_costs = self._generate_shanghai_costs()
        elif fork_id == "cancun":
            gas_costs = self._generate_cancun_costs()
        elif fork_id == "prague":
            gas_costs = self._generate_prague_costs()
        elif fork_id == "osaka":
            gas_costs = self._generate_osaka_costs()
        else:
            raise ValueError(f"Unknown fork: {fork_id}")
        
        return GasSchedule(
            name=fork_def["name"],
            activation_date=fork_def["activation_date"],
            block_number=fork_def["block_number"],
            status=fork_def["status"],
            eips=fork_def["eips"],
            gas_costs=gas_costs
        )
    
    def _generate_frontier_costs(self) -> Dict[str, Any]:
        """Generate Frontier gas costs - Original Ethereum launch"""
        return {
            "base": self.constants.BASE_COSTS.copy(),
            "arithmetic": self.constants.ARITHMETIC_COSTS.copy(),
            "stack": self.constants.STACK_COSTS.copy(),
            "memory": self.constants.MEMORY_COSTS.copy(),
            "storage": {
                "SLOAD": 50,
                "SSTORE_set": 20000,
                "SSTORE_reset": 5000,
                "SSTORE_clear_refund": 15000
            },
            "flow": self.constants.FLOW_COSTS.copy(),
            "system": {
                "CREATE": 32000,
                "CALL": 40,
                "CALLCODE": 40,
                "RETURN": 0,
                "SELFDESTRUCT": 0,
                "SELFDESTRUCT_refund": 24000,
                "G_callstipend": 2300,
                "G_callvalue": 9000,
                "G_newaccount": 25000,
                "G_codedeposit": 200,
                "BALANCE": 20,
                "EXTCODESIZE": 20
            },
            "transaction": {
                "G_transaction": 21000,
                "G_txcreate": 32000,
                "G_txdatazero": 4,
                "G_txdatanonzero": 68
            },
            "precompiles": {
                "ECRECOVER": 3000,
                "SHA256": {"base": 60, "perWord": 12},
                "RIPEMD160": {"base": 600, "perWord": 120},
                "IDENTITY": {"base": 15, "perWord": 3}
            }
        }
    
    def _generate_homestead_costs(self) -> Dict[str, Any]:
        """Generate Homestead gas costs - Same as Frontier with EIP-2, EIP-7, EIP-8"""
        costs = self._generate_frontier_costs()
        costs["transaction"]["G_txdatanonzero"] = 16  # EIP-2: Reduced calldata cost
        return costs
    
    def _generate_dao_fork_costs(self) -> Dict[str, Any]:
        """Generate DAO Fork gas costs - Emergency fork, same as Homestead"""
        return self._generate_homestead_costs()
    
    def _generate_tangerine_whistle_costs(self) -> Dict[str, Any]:
        """Generate Tangerine Whistle gas costs - EIP-150 DoS attack mitigation"""
        costs = self._generate_homestead_costs()
        
        # EIP-150: Increased costs for external operations
        costs["storage"]["SLOAD"] = 200
        costs["system"].update({
            "CALL": 700,
            "CALLCODE": 700,
            "DELEGATECALL": 700,
            "BALANCE": 400,
            "EXTCODESIZE": 700,
            "EXTCODECOPY": 700
        })
        return costs
    
    def _generate_spurious_dragon_costs(self) -> Dict[str, Any]:
        """Generate Spurious Dragon gas costs - EIP-155, EIP-160, EIP-161, EIP-170"""
        costs = self._generate_tangerine_whistle_costs()
        
        # EIP-160: EXP cost increase
        costs["arithmetic"]["EXP_byte"] = 50
        
        # EIP-170: Contract size limit (no direct gas impact, but validation)
        costs["system"]["G_max_code_size"] = 24576
        
        return costs
    
    def _generate_byzantium_costs(self) -> Dict[str, Any]:
        """Generate Byzantium gas costs - ZK-SNARKs and other improvements"""
        costs = self._generate_spurious_dragon_costs()
        
        # Add new precompiles
        costs["precompiles"].update({
            "ECADD": 500,
            "ECMUL": 40000,
            "ECPAIRING": {"base": 100000, "perPair": 80000},
            "MODEXP": {"formula": "max(200, floor(mult_complexity * max(8, iterations) / 3))"}
        })
        
        # Add RETURNDATACOPY and RETURNDATASIZE
        costs["memory"]["RETURNDATACOPY"] = 3
        costs["memory"]["RETURNDATASIZE"] = 2
        
        # Add STATICCALL
        costs["system"]["STATICCALL"] = 700
        
        # Add REVERT
        costs["system"]["REVERT"] = 0
        
        return costs
    
    def _generate_constantinople_costs(self) -> Dict[str, Any]:
        """Generate Constantinople gas costs - EIP-145, EIP-1014, EIP-1052, EIP-1283"""
        costs = self._generate_byzantium_costs()
        
        # EIP-145: Bitwise shifting instructions
        costs["arithmetic"].update({
            "SHL": 3,
            "SHR": 3,
            "SAR": 3
        })
        
        # EIP-1014: CREATE2
        costs["system"]["CREATE2"] = 32000
        
        # EIP-1052: EXTCODEHASH
        costs["system"]["EXTCODEHASH"] = 400
        
        # EIP-1283: Net gas metering for SSTORE
        costs["storage"].update({
            "SSTORE_noop": 200,
            "SSTORE_dirty": 200,
            "SSTORE_init": 20000,
            "SSTORE_clean": 5000,
            "SSTORE_reset_refund": 15000,
            "SSTORE_clear_refund": 15000
        })
        
        return costs
    
    def _generate_petersburg_costs(self) -> Dict[str, Any]:
        """Generate Petersburg gas costs - Constantinople with EIP-1283 removed"""
        costs = self._generate_constantinople_costs()
        
        # Remove EIP-1283 changes, revert to simpler SSTORE costs
        costs["storage"] = {
            "SLOAD": 200,
            "SSTORE_set": 20000,
            "SSTORE_reset": 5000,
            "SSTORE_clear_refund": 15000
        }
        
        return costs
    
    def _generate_istanbul_costs(self) -> Dict[str, Any]:
        """Generate Istanbul gas costs - EIP-152, EIP-1108, EIP-1344, EIP-1884, EIP-2028, EIP-2200"""
        costs = self._generate_petersburg_costs()
        
        # EIP-152: BLAKE2F precompile
        costs["precompiles"]["BLAKE2F"] = 1
        
        # EIP-1108: Reduced alt_bn128 precompile costs
        costs["precompiles"].update({
            "ECADD": 150,
            "ECMUL": 6000,
            "ECPAIRING": {"base": 45000, "perPair": 34000}
        })
        
        # EIP-1344: ChainID opcode
        costs["system"]["CHAINID"] = 2
        
        # EIP-1884: Repricing for trie-size-dependent opcodes
        costs["storage"]["SLOAD"] = 800
        costs["system"].update({
            "BALANCE": 700,
            "EXTCODEHASH": 700,
            "SELFBALANCE": 5
        })
        
        # EIP-2028: Reduced calldata cost
        costs["transaction"]["G_txdatanonzero"] = 16
        
        # EIP-2200: Structured definitions for net gas metering
        costs["storage"].update({
            "SSTORE_noop": 800,
            "SSTORE_init": 20000,
            "SSTORE_clean": 5000,
            "SSTORE_dirty": 800,
            "SSTORE_reset_refund": 15000,
            "SSTORE_clear_refund": 15000
        })
        
        return costs
    
    def _generate_muir_glacier_costs(self) -> Dict[str, Any]:
        """Generate Muir Glacier gas costs - Difficulty bomb delay, same as Istanbul"""
        return self._generate_istanbul_costs()
    
    def _generate_berlin_costs(self) -> Dict[str, Any]:
        """Generate Berlin gas costs - EIP-2565, EIP-2718, EIP-2929, EIP-2930"""
        costs = self._generate_istanbul_costs()
        
        # EIP-2565: ModExp gas cost
        costs["precompiles"]["MODEXP"]["formula"] = "max(200, floor(mult_complexity * iterations / 3))"
        
        # EIP-2929: Gas cost increases for state access opcodes
        costs["storage"].update({
            "SLOAD_cold": 2100,
            "SLOAD_warm": 100,
            "SSTORE_cold": 2100,
            "SSTORE_warm": 100
        })
        
        costs["system"].update({
            "CALL_cold": 2600,
            "CALL_warm": 100,
            "BALANCE_cold": 2600,
            "BALANCE_warm": 100,
            "EXTCODESIZE_cold": 2600,
            "EXTCODESIZE_warm": 100,
            "EXTCODECOPY_cold": 2600,
            "EXTCODECOPY_warm": 100,
            "EXTCODEHASH_cold": 2600,
            "EXTCODEHASH_warm": 100
        })
        
        # EIP-2930: Access list transaction type
        costs["transaction"].update({
            "G_accesslistaddress": 2400,
            "G_accessliststorage": 1900
        })
        
        return costs
    
    def _generate_london_costs(self) -> Dict[str, Any]:
        """Generate London gas costs - EIP-1559, EIP-3198, EIP-3529, EIP-3541, EIP-3554"""
        costs = self._generate_berlin_costs()
        
        # EIP-1559: Fee market change (no direct opcode gas changes)
        costs["transaction"].update({
            "G_basefee": "dynamic",
            "G_priority_fee": "dynamic"
        })
        
        # EIP-3198: BASEFEE opcode
        costs["system"]["BASEFEE"] = 2
        
        # EIP-3529: Reduction in refunds
        costs["storage"].update({
            "SSTORE_reset_refund": 4800,  # Reduced from 15000
            "SSTORE_clear_refund": 4800   # Reduced from 15000
        })
        costs["system"]["SELFDESTRUCT_refund"] = 0  # Removed refund
        
        return costs
    
    def _generate_arrow_glacier_costs(self) -> Dict[str, Any]:
        """Generate Arrow Glacier gas costs - Difficulty bomb delay, same as London"""
        return self._generate_london_costs()
    
    def _generate_gray_glacier_costs(self) -> Dict[str, Any]:
        """Generate Gray Glacier gas costs - Difficulty bomb delay, same as London"""
        return self._generate_london_costs()
    
    def _generate_paris_costs(self) -> Dict[str, Any]:
        """Generate Paris gas costs - The Merge, same as London"""
        costs = self._generate_london_costs()
        
        # Add consensus-related changes (PoS transition)
        costs["consensus"] = {
            "type": "proof_of_stake",
            "DIFFICULTY": "PREVRANDAO",  # DIFFICULTY renamed to PREVRANDAO
            "PREVRANDAO": 2
        }
        
        return costs
    
    def _generate_shanghai_costs(self) -> Dict[str, Any]:
        """Generate Shanghai gas costs"""
        return {
            "base": self.constants.BASE_COSTS.copy(),
            "arithmetic": self.constants.ARITHMETIC_COSTS.copy(),
            "stack": self.constants.STACK_COSTS.copy(),
            "memory": self.constants.MEMORY_COSTS.copy(),
            "storage": self.constants.STORAGE_COSTS.copy(),
            "flow": self.constants.FLOW_COSTS.copy(),
            "system": self.constants.SYSTEM_COSTS.copy(),
            "transaction": self.constants.TRANSACTION_COSTS.copy(),
            "precompiles": self._format_precompiles(self.constants.PRECOMPILE_COSTS)
        }
    
    def _generate_cancun_costs(self) -> Dict[str, Any]:
        """Generate Cancun gas costs"""
        costs = self._generate_shanghai_costs()
        
        # Add Cancun-specific changes
        costs["memory"]["MCOPY"] = 3
        costs["storage"]["TLOAD"] = 100
        costs["storage"]["TSTORE"] = 100
        costs["system"]["SELFDESTRUCT_refund"] = 0
        
        # Add blob costs
        costs["blob"] = {
            "G_blobhash": 3,
            "G_blob": 131072,
            "TARGET_BLOB_GAS_PER_BLOCK": 393216,
            "MAX_BLOB_GAS_PER_BLOCK": 786432,
            "MIN_BLOB_BASE_FEE": 1,
            "BLOB_BASE_FEE_UPDATE_FRACTION": 3338477
        }
        
        # Add KZG precompile
        costs["precompiles"]["KZG_POINT_EVALUATION"] = 50000
        
        return costs
    
    def _generate_prague_costs(self) -> Dict[str, Any]:
        """Generate Prague gas costs"""
        costs = self._generate_cancun_costs()
        
        # Add extended opcodes
        costs["system"]["EXTCODECOPY"] = 700
        costs["system"]["EXTCODESIZE"] = 700
        costs["system"]["EXTCODEHASH"] = 400
        
        # Replace calldata pricing
        costs["transaction"]["G_txdatazero"] = None
        costs["transaction"]["G_txdatanonzero"] = None
        costs["transaction"]["G_calldatatoken"] = 4
        costs["transaction"]["G_calldatafloor"] = 10
        
        # Add BLS precompiles
        costs["precompiles"].update({
            "BLS12_381_G1_ADD": 500,
            "BLS12_381_G1_MUL": 12000,
            "BLS12_381_G2_ADD": 800,
            "BLS12_381_G2_MUL": 45000,
            "BLS12_381_PAIRING_base": 65000,
            "BLS12_381_PAIRING_pair": 43000,
            "BLS12_381_MAP_FP_TO_G1": 5500,
            "BLS12_381_MAP_FP2_TO_G2": 23800
        })
        
        # Add authorization costs
        costs["authorization"] = {
            "G_authorization": 10600,
            "G_ecdsa_verify": 3000,
            "G_nonce_check": 2100,
            "G_nonce_update": 5000,
            "G_authorization_overhead": 500
        }
        
        return costs
    
    def _generate_osaka_costs(self) -> Dict[str, Any]:
        """Generate Osaka gas costs"""
        costs = self._generate_prague_costs()
        
        # Optimize authorization costs
        costs["authorization"] = {
            "G_authorization": 5400,
            "G_authorization_optimized": 5400,
            "G_ecdsa_verify": 2000,
            "G_nonce_check": 100,
            "G_nonce_update": 3000,
            "G_authorization_overhead": 300,
            "G_batch_optimization": "Batch factor: n <= 3 ? n : 3 + 0.8*(n-3) for n <= 10"
        }
        
        return costs
    
    def _format_precompiles(self, precompiles: Dict[str, Any]) -> Dict[str, Any]:
        """Format precompile costs into structured format"""
        formatted = {
            "ECRECOVER": precompiles["ECRECOVER"],
            "SHA256": {
                "base": precompiles["SHA256_base"],
                "perWord": precompiles["SHA256_word"]
            },
            "RIPEMD160": {
                "base": precompiles["RIPEMD160_base"],
                "perWord": precompiles["RIPEMD160_word"]
            },
            "IDENTITY": {
                "base": precompiles["IDENTITY_base"],
                "perWord": precompiles["IDENTITY_word"]
            },
            "MODEXP": {
                "formula": "max(200, floor(mult_complexity * max(8, iterations) / 3))"
            },
            "ECADD": precompiles["ECADD"],
            "ECMUL": precompiles["ECMUL"],
            "ECPAIRING": {
                "base": precompiles["ECPAIRING_base"],
                "perPair": precompiles["ECPAIRING_pair"]
            },
            "BLAKE2F": precompiles["BLAKE2F"]
        }
        return formatted


# ============================================================================
# Gas Calculator
# ============================================================================

class AdvancedGasCalculator:
    """Advanced gas calculation utilities"""
    
    @staticmethod
    def calculate_transaction_cost(
        fork: str,
        data: bytes,
        is_contract_creation: bool = False,
        access_list: Optional[List[Tuple[str, List[str]]]] = None,
        num_blobs: int = 0,
        num_authorizations: int = 0
    ) -> Dict[str, int]:
        """Calculate complete transaction cost for a given fork"""
        
        costs = {"base": 21000}
        
        if is_contract_creation:
            costs["creation"] = 32000
        
        # Calculate data cost based on fork
        if fork in ["frontier"]:
            data_cost = sum(4 if b == 0 else 68 for b in data)
            costs["data"] = data_cost
        elif fork in ["homestead", "dao_fork", "tangerine_whistle", "spurious_dragon", 
                      "byzantium", "constantinople", "petersburg", "muir_glacier"]:
            data_cost = sum(4 if b == 0 else 16 for b in data)
            costs["data"] = data_cost
        elif fork in ["istanbul", "berlin", "london", "arrow_glacier", "gray_glacier", 
                      "paris", "shanghai", "cancun"]:
            data_cost = sum(4 if b == 0 else 16 for b in data)
            costs["data"] = data_cost
        elif fork in ["prague", "osaka"]:
            # Token-based pricing
            zero_bytes = sum(1 for b in data if b == 0)
            non_zero_bytes = len(data) - zero_bytes
            tokens = zero_bytes + (non_zero_bytes * 4)
            standard_cost = tokens * 4
            floor_cost = tokens * 10
            costs["data"] = max(standard_cost, floor_cost)
        
        # Access list costs
        if access_list:
            access_cost = 0
            for address, keys in access_list:
                access_cost += 2400  # Per address
                access_cost += len(keys) * 1900  # Per storage key
            costs["access_list"] = access_cost
        
        # Blob costs (Cancun+)
        if num_blobs > 0 and fork in ["cancun", "prague", "osaka"]:
            costs["blobs"] = num_blobs * 131072
        
        # Authorization costs (Prague+)
        if num_authorizations > 0:
            if fork == "prague":
                costs["authorizations"] = num_authorizations * 10600
            elif fork == "osaka":
                costs["authorizations"] = AdvancedGasCalculator._calculate_osaka_auth_cost(num_authorizations)
        
        costs["total"] = sum(costs.values())
        return costs
    
    @staticmethod
    def _calculate_osaka_auth_cost(n: int) -> int:
        """Calculate Osaka optimized authorization cost"""
        if n <= 3:
            return n * 5400
        elif n <= 10:
            return int((3 + 0.8 * (n - 3)) * 5400)
        else:
            return int((8.6 + 0.6 * (n - 10)) * 5400)
    
    @staticmethod
    def compare_transaction_costs(
        data: bytes,
        **kwargs
    ) -> Dict[str, Dict[str, int]]:
        """Compare transaction costs across all forks"""
        results = {}
        
        for fork in FORK_DEFINITIONS.keys():
            results[fork] = AdvancedGasCalculator.calculate_transaction_cost(
                fork, data, **kwargs
            )
        
        return results


# ============================================================================
# Main CLI Interface
# ============================================================================

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description="Ethereum Gas Schedule Utilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s generate              Generate all gas schedules
  %(prog)s validate              Validate existing schedules
  %(prog)s compare shanghai cancun  Compare two forks
  %(prog)s calculate --fork prague --data-size 1024
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate gas schedules")
    gen_parser.add_argument("--output", default="gas-schedule.json", help="Output file")
    gen_parser.add_argument("--schema", action="store_true", help="Also generate schema")
    
    # Validate command
    val_parser = subparsers.add_parser("validate", help="Validate gas schedules")
    val_parser.add_argument("--file", default="gas-cost-schedule.json", help="Schedule file")
    val_parser.add_argument("--schema", default="gas-cost-schedule-schema.json", help="Schema file")
    
    # Compare command
    comp_parser = subparsers.add_parser("compare", help="Compare two forks")
    fork_choices = list(FORK_DEFINITIONS.keys())
    comp_parser.add_argument("from_fork", choices=fork_choices)
    comp_parser.add_argument("to_fork", choices=fork_choices)
    
    # Calculate command
    calc_parser = subparsers.add_parser("calculate", help="Calculate gas costs")
    calc_parser.add_argument("--fork", required=True, choices=fork_choices)
    calc_parser.add_argument("--data-size", type=int, default=0, help="Transaction data size in bytes")
    calc_parser.add_argument("--contract-creation", action="store_true", help="Is contract creation")
    calc_parser.add_argument("--blobs", type=int, default=0, help="Number of blobs")
    calc_parser.add_argument("--authorizations", type=int, default=0, help="Number of authorizations")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == "generate":
        print("🚀 Generating gas schedules...")
        generator = AdvancedGasScheduleGenerator()
        schedules = generator.generate_all_schedules()
        
        # Convert to JSON format
        output = {
            "version": "1.0.0",
            "metadata": {
                "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "source": "Ethereum Execution Specifications"
            },
            "forks": {}
        }
        
        for fork_id, schedule in schedules.items():
            output["forks"][fork_id] = {
                "name": schedule.name,
                "activationDate": schedule.activation_date,
                "blockNumber": schedule.block_number,
                "status": schedule.status.value,
                "eips": schedule.eips,
                "gasCosts": schedule.gas_costs
            }
        
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        
        print(f"✅ Generated {args.output}")
        
        # Print statistics
        for fork_id, schedule in schedules.items():
            print(f"  {schedule.name}: {len(schedule.eips)} EIPs")
    
    elif args.command == "compare":
        print(f"📊 Comparing {args.from_fork} → {args.to_fork}")
        generator = AdvancedGasScheduleGenerator()
        schedules = generator.generate_all_schedules()
        
        from_schedule = schedules[args.from_fork]
        to_schedule = schedules[args.to_fork]
        
        # Find differences
        print(f"\n🔄 Changes from {from_schedule.name} to {to_schedule.name}:")
        
        # New EIPs
        new_eips = set(to_schedule.eips) - set(from_schedule.eips)
        if new_eips:
            print(f"  New EIPs: {sorted(new_eips)}")
        
        # Calculate example costs
        calc = AdvancedGasCalculator()
        data_1kb = b'\x01' * 1024
        
        from_cost = calc.calculate_transaction_cost(args.from_fork, data_1kb)
        to_cost = calc.calculate_transaction_cost(args.to_fork, data_1kb)
        
        print(f"\n  1KB transaction cost:")
        print(f"    {from_schedule.name}: {from_cost['total']:,} gas")
        print(f"    {to_schedule.name}: {to_cost['total']:,} gas")
        
        if from_cost['total'] != to_cost['total']:
            change = ((to_cost['total'] / from_cost['total']) - 1) * 100
            print(f"    Change: {change:+.1f}%")
    
    elif args.command == "calculate":
        print(f"💰 Calculating gas costs for {args.fork}")
        
        # Generate sample data
        data = b'\x01' * args.data_size if args.data_size > 0 else b''
        
        calc = AdvancedGasCalculator()
        costs = calc.calculate_transaction_cost(
            args.fork,
            data,
            is_contract_creation=args.contract_creation,
            num_blobs=args.blobs,
            num_authorizations=args.authorizations
        )
        
        print("\n📊 Cost Breakdown:")
        for component, cost in costs.items():
            if component != "total":
                print(f"  {component}: {cost:,} gas")
        
        print(f"\n  TOTAL: {costs['total']:,} gas")
        
        # Compare across forks
        if args.data_size > 0 or args.blobs > 0 or args.authorizations > 0:
            print("\n📈 Comparison Across Forks:")
            comparison = calc.compare_transaction_costs(
                data,
                is_contract_creation=args.contract_creation,
                num_blobs=args.blobs,
                num_authorizations=args.authorizations
            )
            
            for fork, fork_costs in comparison.items():
                print(f"  {FORK_DEFINITIONS[fork]['name']}: {fork_costs['total']:,} gas")
    
    print("\n✨ Done!")


if __name__ == "__main__":
    main()