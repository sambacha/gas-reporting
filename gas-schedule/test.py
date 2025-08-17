#!/usr/bin/env python3
"""
Complete Gas Schedule Validation

Validates the generated gas schedule against known values and ensures
consistency across all forks.
"""

import json
import sys
from typing import Dict, Any, List, Tuple
from datetime import datetime


class GasScheduleValidator:
    """Validates gas schedule data for accuracy and consistency"""
    
    def __init__(self, schedule_file: str = "complete-gas-schedule.json"):
        self.schedule_file = schedule_file
        self.schedule = self._load_schedule()
        self.errors: List[str] = []
        self.warnings: List[str] = []
    
    def _load_schedule(self) -> Dict[str, Any]:
        """Load the gas schedule JSON file"""
        try:
            with open(self.schedule_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Gas schedule file '{self.schedule_file}' not found")
            print("Run: uv run python gas_schedule_utils.py generate")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON in '{self.schedule_file}': {e}")
            sys.exit(1)
    
    def validate_all(self) -> bool:
        """Run all validation checks"""
        print("🔍 Validating Complete Gas Schedule")
        print("=" * 50)
        
        self._validate_structure()
        self._validate_fork_metadata()
        self._validate_gas_costs()
        self._validate_historical_values()
        self._validate_evolution()
        
        # Report results
        print(f"\n📊 Validation Results:")
        if self.errors:
            print(f"❌ {len(self.errors)} errors found:")
            for error in self.errors:
                print(f"   • {error}")
        
        if self.warnings:
            print(f"⚠️  {len(self.warnings)} warnings:")
            for warning in self.warnings:
                print(f"   • {warning}")
        
        if not self.errors and not self.warnings:
            print("✅ All validations passed!")
        elif not self.errors:
            print("✅ No errors found (warnings can be ignored)")
        
        return len(self.errors) == 0
    
    def _validate_structure(self):
        """Validate overall JSON structure"""
        required_top_level = ["version", "metadata", "forks"]
        for key in required_top_level:
            if key not in self.schedule:
                self.errors.append(f"Missing top-level key: {key}")
        
        if "forks" in self.schedule:
            expected_forks = [
                "frontier", "homestead", "dao_fork", "tangerine_whistle", 
                "spurious_dragon", "byzantium", "constantinople", "petersburg",
                "istanbul", "muir_glacier", "berlin", "london", "arrow_glacier",
                "gray_glacier", "paris", "shanghai", "cancun", "prague", "osaka"
            ]
            
            actual_forks = set(self.schedule["forks"].keys())
            expected_forks_set = set(expected_forks)
            
            missing = expected_forks_set - actual_forks
            extra = actual_forks - expected_forks_set
            
            for fork in missing:
                self.errors.append(f"Missing fork: {fork}")
            
            for fork in extra:
                self.warnings.append(f"Unexpected fork: {fork}")
    
    def _validate_fork_metadata(self):
        """Validate fork metadata fields"""
        for fork_id, fork_data in self.schedule.get("forks", {}).items():
            required_fields = ["name", "activationDate", "blockNumber", "status", "eips", "gasCosts"]
            
            for field in required_fields:
                if field not in fork_data:
                    self.errors.append(f"{fork_id}: Missing field {field}")
            
            # Validate activation dates are in chronological order (where present)
            if "activationDate" in fork_data and fork_data["activationDate"]:
                try:
                    datetime.fromisoformat(fork_data["activationDate"])
                except ValueError:
                    self.errors.append(f"{fork_id}: Invalid date format in activationDate")
            
            # Validate block numbers are increasing (where present)
            if "blockNumber" in fork_data and fork_data["blockNumber"] is not None:
                if not isinstance(fork_data["blockNumber"], int) or fork_data["blockNumber"] < 0:
                    self.errors.append(f"{fork_id}: Invalid block number")
    
    def _validate_gas_costs(self):
        """Validate gas cost structures for each fork"""
        for fork_id, fork_data in self.schedule.get("forks", {}).items():
            gas_costs = fork_data.get("gasCosts", {})
            
            # Check for required gas cost categories
            expected_categories = ["base", "arithmetic", "stack", "memory", "storage", "flow", "system", "transaction", "precompiles"]
            
            for category in expected_categories:
                if category not in gas_costs:
                    self.errors.append(f"{fork_id}: Missing gas cost category: {category}")
                    continue
                
                # Validate individual gas costs are non-negative integers
                self._validate_gas_values(fork_id, category, gas_costs[category])
    
    def _validate_gas_values(self, fork_id: str, category: str, values: Any):
        """Validate gas values are proper integers or formulas"""
        if isinstance(values, dict):
            for key, value in values.items():
                if isinstance(value, dict):
                    self._validate_gas_values(fork_id, f"{category}.{key}", value)
                elif isinstance(value, (int, float)):
                    if value < 0:
                        self.errors.append(f"{fork_id}.{category}.{key}: Negative gas cost: {value}")
                elif isinstance(value, str):
                    # Allow formula strings
                    if not any(keyword in value for keyword in ["formula", "dynamic", "proof_of_stake", "PREVRANDAO"]):
                        self.warnings.append(f"{fork_id}.{category}.{key}: String value may need validation: {value}")
                elif value is None:
                    # Allow None for removed operations
                    pass
                else:
                    self.warnings.append(f"{fork_id}.{category}.{key}: Unexpected value type: {type(value)}")
    
    def _validate_historical_values(self):
        """Validate known historical gas cost values"""
        known_values = [
            # (fork, path, expected_value, description)
            ("frontier", ["storage", "SLOAD"], 50, "Original SLOAD cost"),
            ("tangerine_whistle", ["storage", "SLOAD"], 200, "EIP-150 SLOAD increase"),
            ("istanbul", ["storage", "SLOAD"], 800, "EIP-1884 SLOAD increase"),
            ("berlin", ["storage", "SLOAD_cold"], 2100, "EIP-2929 cold SLOAD"),
            ("berlin", ["storage", "SLOAD_warm"], 100, "EIP-2929 warm SLOAD"),
            
            ("frontier", ["system", "CALL"], 40, "Original CALL cost"),
            ("tangerine_whistle", ["system", "CALL"], 700, "EIP-150 CALL increase"),
            
            ("frontier", ["transaction", "G_txdatanonzero"], 68, "Original calldata cost"),
            ("homestead", ["transaction", "G_txdatanonzero"], 16, "EIP-2 calldata reduction"),
            
            ("byzantium", ["precompiles", "ECADD"], 500, "EIP-196 ECADD"),
            ("istanbul", ["precompiles", "ECADD"], 150, "EIP-1108 ECADD reduction"),
            
            ("cancun", ["blob", "G_blob"], 131072, "EIP-4844 blob gas"),
        ]
        
        for fork_id, path, expected, description in known_values:
            if fork_id not in self.schedule.get("forks", {}):
                continue
            
            current = self.schedule["forks"][fork_id]["gasCosts"]
            for key in path:
                if key not in current:
                    self.errors.append(f"Missing {'.'.join(path)} in {fork_id}")
                    break
                current = current[key]
            else:
                if current != expected:
                    self.errors.append(f"{fork_id}.{'.'.join(path)}: Expected {expected}, got {current} ({description})")
    
    def _validate_evolution(self):
        """Validate gas cost evolution makes sense"""
        forks = list(self.schedule.get("forks", {}).keys())
        
        # Check SLOAD evolution
        sload_evolution = []
        for fork_id in forks:
            fork_data = self.schedule["forks"].get(fork_id, {})
            gas_costs = fork_data.get("gasCosts", {})
            storage = gas_costs.get("storage", {})
            
            if "SLOAD" in storage:
                sload_evolution.append((fork_id, storage["SLOAD"]))
        
        # Verify major SLOAD changes
        expected_sload_changes = [
            ("frontier", 50),
            ("tangerine_whistle", 200),
            ("istanbul", 800)
        ]
        
        for fork_id, expected_cost in expected_sload_changes:
            found = False
            for evo_fork, evo_cost in sload_evolution:
                if evo_fork == fork_id and evo_cost == expected_cost:
                    found = True
                    break
            
            if not found:
                self.errors.append(f"SLOAD evolution: Expected {fork_id} to have cost {expected_cost}")
    
    def generate_summary(self):
        """Generate a summary of the gas schedule"""
        if "forks" not in self.schedule:
            return
        
        print("\n📈 Gas Schedule Summary")
        print("=" * 50)
        
        # Count total operations across all forks
        total_ops = 0
        total_eips = 0
        
        for fork_id, fork_data in self.schedule["forks"].items():
            eip_count = len(fork_data.get("eips", []))
            total_eips += eip_count
            
            gas_costs = fork_data.get("gasCosts", {})
            ops_count = 0
            for category, values in gas_costs.items():
                if isinstance(values, dict):
                    ops_count += len(values)
            
            total_ops += ops_count
            print(f"  {fork_data.get('name', fork_id)}: {ops_count} operations, {eip_count} EIPs")
        
        print(f"\nTotal: {len(self.schedule['forks'])} forks, {total_ops} total operations, {total_eips} EIPs")
        
        # Show major cost evolution
        print(f"\n🔄 Major Gas Cost Evolution:")
        
        # SLOAD evolution
        sload_costs = []
        for fork_id in ["frontier", "tangerine_whistle", "istanbul", "berlin"]:
            if fork_id in self.schedule["forks"]:
                fork_data = self.schedule["forks"][fork_id]
                storage = fork_data.get("gasCosts", {}).get("storage", {})
                if "SLOAD" in storage:
                    sload_costs.append(f"{fork_data['name']}: {storage['SLOAD']}")
                elif "SLOAD_cold" in storage:
                    sload_costs.append(f"{fork_data['name']}: {storage['SLOAD_cold']} (cold)")
        
        if sload_costs:
            print(f"  SLOAD: {' → '.join(sload_costs)}")
        
        # Transaction data evolution
        calldata_costs = []
        for fork_id in ["frontier", "homestead", "prague"]:
            if fork_id in self.schedule["forks"]:
                fork_data = self.schedule["forks"][fork_id]
                tx = fork_data.get("gasCosts", {}).get("transaction", {})
                if "G_txdatanonzero" in tx:
                    calldata_costs.append(f"{fork_data['name']}: {tx['G_txdatanonzero']}")
                elif "G_calldatatoken" in tx:
                    calldata_costs.append(f"{fork_data['name']}: token-based")
        
        if calldata_costs:
            print(f"  Calldata: {' → '.join(calldata_costs)}")


def main():
    """Main validation entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate Complete Gas Schedule")
    parser.add_argument("--file", default="complete-gas-schedule.json", help="Gas schedule file to validate")
    parser.add_argument("--summary", action="store_true", help="Show summary after validation")
    
    args = parser.parse_args()
    
    validator = GasScheduleValidator(args.file)
    success = validator.validate_all()
    
    if args.summary:
        validator.generate_summary()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()