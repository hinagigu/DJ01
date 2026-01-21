# UComboGraphBTTask_RunComboGraph

**继承自**: `UBTTaskNode`

Run indicated ComboGraph Asset on Pawn Controlled by BT

## 属性

### ComboGraphAsset
- **类型**: `UComboGraph`
- **描述**: Animation asset to play. Note that it needs to match the skeleton of pawn this BT is controlling

### Inputs
- **类型**: `TArray<TObjectPtr<UInputAction>>`
- **描述**: Stack of Input Actions to process and simulate inputs when the underlying gameplay task receives ComboBegin event, and schedule for execution on the next frame

