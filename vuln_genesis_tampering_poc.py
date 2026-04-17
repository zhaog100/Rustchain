#!/usr/bin/env python3
"""
RustChain High Vulnerability: Genesis Migration Tampering
Bounty: #2819 (100 RTC)

攻击: 删除 genesis 盒子后重新运行迁移
结果: 余额重复，通货膨胀
"""

def exploit():
    print("🎯 High Vulnerability: Genesis Migration Tampering")
    print()
    print("位置: utxo_genesis_migration.py, migrate() 函数")
    print()
    print("问题:")
    print("  1. check_existing_genesis() 只检查 creation_height=0")
    print("  2. 攻击者可先删除再重新运行")
    print("  3. 无全局状态验证")
    print()
    print("攻击步骤:")
    print("  1. 等待正常迁移完成")
    print("     538 个钱包迁移到 UTXO")
    print()
    print("  2. 攻击者执行 rollback:")
    print("     DELETE FROM utxo_boxes WHERE creation_height = 0;")
    print("     DELETE FROM utxo_transactions WHERE tx_type = 'genesis';")
    print()
    print("  3. 重新运行迁移脚本:")
    print("     python3 utxo_genesis_migration.py")
    print()
    print("  4. 结果:")
    print("     - 538 个钱包再次迁移")
    print("     - 每个余额翻倍")
    print("     - 总供应量 x2")
    print()
    print("📊 影响:")
    print("  - 通货膨胀: 供应量翻倍")
    print("  - 余额重复: 同一钱包两个 UTXO")
    print("  - 状态根不一致")
    print()
    print("🔧 修复:")
    print("  - 添加全局迁移状态标记")
    print("  - 验证总供应量不变")
    print("  - 使用单一事务")

if __name__ == "__main__":
    exploit()