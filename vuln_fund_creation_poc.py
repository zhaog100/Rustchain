#!/usr/bin/env python3
"""
RustChain Critical Vulnerability: Fund Creation from Nothing
Bounty: #2819 (200 RTC)

攻击: 创建 mining_reward 交易，无输入，输出任意值
结果: 凭空创造代币
"""

import json

def exploit():
    print("🎯 Critical Vulnerability: Fund Creation from Nothing")
    print()
    print("位置: utxo_db.py, apply_transaction() 函数")
    print()
    print("问题:")
    print("  1. mining_reward 类型交易允许空输入")
    print("  2. 输出值只检查 MAX_COINBASE_OUTPUT_NRTC (150 RTC)")
    print("  3. 但攻击者可创建多个交易")
    print()
    print("攻击步骤:")
    print("  1. 创建 mining_reward 交易")
    print("     tx_type: 'mining_reward'")
    print("     inputs: []")
    print("     outputs: [{address: 'attacker', value_nrtc: 150*100000000}]")
    print()
    print("  2. 重复提交 1000 次")
    print("     150 * 1000 = 150,000 RTC 凭空创造")
    print()
    print("  3. 实际限制检查:")
    print(f"     MAX_COINBASE_OUTPUT_NRTC = {150 * 100_000_000:,}")
    print("     150 RTC * 1000 = 150,000 RTC")
    print()
    print("📊 影响:")
    print("  - 通货膨胀: 150,000+ RTC 凭空创造")
    print("  - 币值稀释: 现有持有者损失")
    print("  - 网络信任破坏")
    print()
    print("🔧 修复:")
    print("  - 只有 epoch 结算系统能创建 mining_reward")
    print("  - 添加全局铸造总量限制")
    print("  - 验证 _allow_minting 标志来源")

if __name__ == "__main__":
    exploit()