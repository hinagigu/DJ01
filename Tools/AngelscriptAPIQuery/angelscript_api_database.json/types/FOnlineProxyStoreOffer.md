# FOnlineProxyStoreOffer

Offer entry for display from online store

## 属性

### OfferId
- **类型**: `FString`
- **描述**: Unique offer identifier

### Title
- **类型**: `FText`
- **描述**: Title for display

### Description
- **类型**: `FText`
- **描述**: Short description for display

### LongDescription
- **类型**: `FText`
- **描述**: Full description for display

### RegularPriceText
- **类型**: `FText`
- **描述**: Regular non-sale price as text for display

### RegularPrice
- **类型**: `int`
- **描述**: Regular non-sale price in numeric form for comparison/sorting

### PriceText
- **类型**: `FText`
- **描述**: Final-Pricing (Post-Sales/Discounts) as text for display

### NumericPrice
- **类型**: `int`
- **描述**: Final-Price (Post-Sales/Discounts) in numeric form for comparison/sorting

### CurrencyCode
- **类型**: `FString`
- **描述**: Price currency code

### ReleaseDate
- **类型**: `FDateTime`
- **描述**: Date the offer was released

### ExpirationDate
- **类型**: `FDateTime`
- **描述**: Date this information is no longer valid (maybe due to sale ending, etc)

### DiscountType
- **类型**: `EOnlineProxyStoreOfferDiscountType`
- **描述**: Type of discount currently running on this offer (if any)

### DynamicFields
- **类型**: `TMap<FString,FString>`

## 方法

### opAssign
```angelscript
FOnlineProxyStoreOffer& opAssign(FOnlineProxyStoreOffer Other)
```

