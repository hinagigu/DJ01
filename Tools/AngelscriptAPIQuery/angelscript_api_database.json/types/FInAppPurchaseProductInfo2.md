# FInAppPurchaseProductInfo2

Micro-transaction purchase information

## 属性

### Identifier
- **类型**: `FString`
- **描述**: The unique product identifier

### TransactionIdentifier
- **类型**: `FString`
- **描述**: the unique transaction identifier

### DisplayName
- **类型**: `FString`
- **描述**: The localized display name

### DisplayDescription
- **类型**: `FString`
- **描述**: The localized display description name

### DisplayPrice
- **类型**: `FString`
- **描述**: The localized display price name

### RawPrice
- **类型**: `float32`
- **描述**: Raw price without currency code and symbol

### CurrencyCode
- **类型**: `FString`
- **描述**: The localized currency code of the price

### CurrencySymbol
- **类型**: `FString`
- **描述**: The localized currency symbol of the price

### DecimalSeparator
- **类型**: `FString`
- **描述**: The localized decimal separator used in the price

### GroupingSeparator
- **类型**: `FString`
- **描述**: The localized grouping separator of the price

### ReceiptData
- **类型**: `FString`
- **描述**: Opaque receipt data for the transaction

### DynamicFields
- **类型**: `TMap<FString,FString>`
- **描述**: Dynamic fields from raw Json data.

## 方法

### opAssign
```angelscript
FInAppPurchaseProductInfo2& opAssign(FInAppPurchaseProductInfo2 Other)
```

