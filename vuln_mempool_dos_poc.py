#!/usr/bin/env python3
"""
RustChain Medium Vulnerability: Mempool DoS via Zero-Value Outputs
Bounty: #2819 (50 RTC)

攻击: 提交大量零值输出交易到 mempool
结果: UTXO 锁定 1 小时，DoS
"""

def exploit():
    print("🎯 Medium Vulnerability: Mempool DoS via Zero-Value Outputs")
    print()
    print("位置: utxo_db.py, mempool_add() 函数")
    print()
    print("问题:")
    print("  1. 零值输出检查只针对 mining_reward")
    print("  2. transfer 类型可包含零值输出")
    print("  3. 交易进入 mempool，锁定 UTXO 1 小时")
    print()
    print("攻击步骤:")
    print("  1. 创建正常交易")
    print("     tx_type: 'transfer'")
    print("     inputs: [valid_box_id]")
    print("     outputs: [valid_output, zero_value_output]")
    print()
    print("  2. 提交到 mempool")
    print("     - 零值输出被接受")
    print("     - UTXO 被锁定")
    print("     - 交易无法上链（无效）")
    print()
    print("  3. 重复 10000 次")
    print("     - 锁定 10000 个 UTXO")
    print("     - 消耗 mempool 空间")
    print("     - 阻止正常交易")
    print()
    print("  4. 1 小时后过期")
    print("     - UTXO 释放")
    print("     - 攻击者无成本")
    print()
    print("📊 影响:")
    print("  - DoS: 阻止正常交易")
    print("  - UTXO 锁定: 资金临时冻结")
    print("  - Mempool 耗尽: 拒绝服务")
    print()
    print("🔧 修复:")
    print("  - 检查所有输出 value_nrtc > 0")
    print("  - 拒绝零值输出")
    print("  - 添加 mempool 大小限制")

if __name__ == "__main__":
    exploit()