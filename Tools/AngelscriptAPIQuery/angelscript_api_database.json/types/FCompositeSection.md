# FCompositeSection

Section data for each track. Reference of data will be stored in the child class for the way they want
AnimComposite vs AnimMontage have different requirement for the actual data reference
This only contains composite section information. (vertical sequences)

## 属性

### SectionName
- **类型**: `FName`
- **描述**: Section Name

### MetaData
- **类型**: `TArray<TObjectPtr<UAnimMetaData>>`
- **描述**: Meta data that can be saved with the asset

You can query by GetMetaData function

### SlotIndex
- **类型**: `int`
- **描述**: The slot index we are currently using within LinkedMontage

### LinkMethod
- **类型**: `EAnimLinkMethod`
- **描述**: The method we are using to calculate our times

## 方法

### opAssign
```angelscript
FCompositeSection& opAssign(FCompositeSection Other)
```

