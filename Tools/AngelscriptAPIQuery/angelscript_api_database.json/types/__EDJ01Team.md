# __EDJ01Team

EDJ01Team - 基于位标志的团队系统

设计理念：
1. 每个Team是一个独立的bit
2. 通过位掩码定义"攻击目标"关系
3. 一行代码判断敌对：(MyAttackMask & TargetTeam) != 0

优势：
- 极简：只需要位运算，不需要复杂的子系统
- 高效：位运算性能极高
- 灵活：支持"一对多"关系（一个单位可以同时属于多个阵营）
- 可扩展：最多支持32个阵营（uint32）

## 属性

### None
- **类型**: `EDJ01Team`

### Player
- **类型**: `EDJ01Team`

### Monster
- **类型**: `EDJ01Team`

### NPC
- **类型**: `EDJ01Team`

### Boss
- **类型**: `EDJ01Team`

### Neutral
- **类型**: `EDJ01Team`

### TeamRed
- **类型**: `EDJ01Team`

### TeamBlue
- **类型**: `EDJ01Team`

### TeamGreen
- **类型**: `EDJ01Team`

### EDJ01Team_MAX
- **类型**: `EDJ01Team`

