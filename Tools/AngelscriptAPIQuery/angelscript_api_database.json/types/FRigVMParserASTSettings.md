# FRigVMParserASTSettings

* The settings to apply during the parse of the abstract syntax tree.
* The folding settings can affect the performance of the parse dramatically.

## 属性

### bFoldAssignments
- **类型**: `bool`
- **描述**: fold assignments / copies

### bFoldLiterals
- **类型**: `bool`
- **描述**: fold literals and share memory

## 方法

### opAssign
```angelscript
FRigVMParserASTSettings& opAssign(FRigVMParserASTSettings Other)
```

