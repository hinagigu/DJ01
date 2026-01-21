# FDJ01DamageScaling

单个伤害加成配置

示例配置:
- "+80% Total AD": Layer=Total, AttributeSetClass=UDJ01StatSet, AttributeName="AttackPower", Ratio=0.8
- "+10% Target MaxHP": Layer=Total, AttributeName="MaxHealth", bFromTarget=true, Ratio=0.1

## 属性

### AttributeSetClass
- **类型**: `TSubclassOf<UAttributeSet>`

### AttributeName
- **类型**: `FName`

### Layer
- **类型**: `EDJ01AttributeLayer`

### Ratio
- **类型**: `float32`

### bFromTarget
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FDJ01DamageScaling& opAssign(FDJ01DamageScaling Other)
```

