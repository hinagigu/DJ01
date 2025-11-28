# DJ01 GameData 扩展计划

> 本文档记录了 DJ01GameData 类未来需要扩展的功能点，用于RPG游戏系统开发

## 📋 当前状态
- ✅ 基础伤害系统 (DamageGameplayEffect_SetByCaller)
- ✅ 基础治疗系统 (HealGameplayEffect_SetByCaller)
- ✅ 动态标签系统 (DynamicTagGameplayEffect)

---

## 🎯 待扩展功能

### 1. 资源系统 (Resources)
- [ ] 法力值恢复效果 (ManaRestoreGameplayEffect)
- [ ] 耐力恢复效果 (StaminaRestoreGameplayEffect)
- [ ] 其他资源类型（怒气、能量等）

### 2. 角色成长系统 (Progression)
- [ ] 经验值获取效果 (ExperienceGainGameplayEffect)
- [ ] 等级经验值数据表 (LevelExperienceTable)
- [ ] 升级奖励配置
- [ ] 技能点系统

### 3. 状态效果系统 (Status Effects)
**Debuff（减益）：**
- [ ] 中毒效果 - 持续伤害 (PoisonGameplayEffect)
- [ ] 燃烧效果 - 持续伤害 (BurnGameplayEffect)
- [ ] 冰冻效果 - 减速/定身 (FreezeGameplayEffect)
- [ ] 眩晕效果 - 无法行动 (StunGameplayEffect)
- [ ] 流血效果 - 持续伤害
- [ ] 虚弱效果 - 属性降低

**Buff（增益）：**
- [ ] 护盾效果 (ShieldGameplayEffect)
- [ ] 攻击力提升 (AttackBuffGameplayEffect)
- [ ] 防御力提升 (DefenseBuffGameplayEffect)
- [ ] 移动速度提升 (SpeedBuffGameplayEffect)
- [ ] 暴击率提升
- [ ] 生命恢复速度提升

### 4. 战斗系统扩展 (Combat)
- [ ] 元素伤害系统（火、冰、雷、暗、光）
- [ ] 物理伤害/魔法伤害分类
- [ ] 暴击系统
- [ ] 格挡/闪避系统
- [ ] 反击机制
- [ ] 伤害吸收/反弹

### 5. 死亡与复活系统 (Death & Respawn)
- [ ] 死亡效果 (DeathGameplayEffect)
- [ ] 复活效果 (RespawnGameplayEffect)
- [ ] 死亡惩罚配置
- [ ] 复活点配置

### 6. 技能系统数据 (Skills)
- [ ] 技能数据表 (SkillDataTable)
- [ ] 技能树配置
- [ ] 技能冷却系统
- [ ] 技能消耗配置
- [ ] 技能组合/连招系统

### 7. 装备与物品系统 (Items & Equipment)
- [ ] 装备数据表 (EquipmentDataTable)
- [ ] 物品品质配置
- [ ] 装备强化系统
- [ ] 套装效果
- [ ] 宝石镶嵌系统

### 8. 属性系统 (Attributes)
**基础属性：**
- [ ] 力量 (Strength) - 影响物理攻击
- [ ] 敏捷 (Agility) - 影响攻速、闪避
- [ ] 智力 (Intelligence) - 影响魔法攻击
- [ ] 体质 (Constitution) - 影响生命值

**衍生属性：**
- [ ] 暴击率/暴击伤害
- [ ] 命中率/闪避率
- [ ] 护甲穿透
- [ ] 魔法抗性
- [ ] 生命偷取/法力偷取

### 9. 队伍与社交系统 (Party & Social)
- [ ] 队伍Buff效果
- [ ] 友方治疗/Buff配置
- [ ] 经验值分配规则

### 10. 环境效果 (Environmental)
- [ ] 地形效果（岩浆、冰面等）
- [ ] 天气效果
- [ ] 陷阱伤害

---

## 📝 开发建议

### 数据组织原则
1. **分类清晰**：按功能模块分类（Category）
2. **命名规范**：统一使用 `功能名称GameplayEffect` 格式
3. **注释完整**：每个属性都有清晰的说明
4. **软引用**：使用 `TSoftClassPtr` 避免硬引用导致的加载问题

### 扩展时机
- 开发角色属性系统时 → 扩展属性相关配置
- 开发技能系统时 → 添加技能数据表和技能效果
- 开发装备系统时 → 添加装备数据表和装备效果
- 开发战斗系统时 → 完善伤害类型和战斗效果

### 文件位置
- **头文件**：`D:\UnrealProjects\DJ01\Source\DJ01\System\Public\DJ01GameData.h`
- **实现文件**：`D:\UnrealProjects\DJ01\Source\DJ01\System\Private\DJ01GameData.cpp`

---

## 🔗 相关文件
- `DJ01AssetManager.h/cpp` - 资产管理器
- `DJ01AbilitySystemComponent.h/cpp` - 能力系统组件
- `DJ01GameplayAbility.h/cpp` - 技能基类

---

**创建日期**：2025-11-27  
**最后更新**：2025-11-27  
**维护者**：开发团队

---

💡 **提示**：每次扩展 GameData 时，记得同步更新此文档，删除已完成的项目，添加新的需求。