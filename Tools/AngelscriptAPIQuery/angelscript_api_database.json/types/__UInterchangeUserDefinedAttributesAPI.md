# __UInterchangeUserDefinedAttributesAPI

## 方法

### CreateUserDefinedAttribute_Boolean
```angelscript
bool CreateUserDefinedAttribute_Boolean(UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, bool Value, FString PayloadKey, bool RequiresDelegate)
```

### CreateUserDefinedAttribute_Double
```angelscript
bool CreateUserDefinedAttribute_Double(UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, float Value, FString PayloadKey, bool RequiresDelegate)
```

### CreateUserDefinedAttribute_Float
```angelscript
bool CreateUserDefinedAttribute_Float(UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, float32 Value, FString PayloadKey, bool RequiresDelegate)
```

### CreateUserDefinedAttribute_FString
```angelscript
bool CreateUserDefinedAttribute_FString(UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, FString Value, FString PayloadKey, bool RequiresDelegate)
```

### CreateUserDefinedAttribute_Int32
```angelscript
bool CreateUserDefinedAttribute_Int32(UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, int Value, FString PayloadKey, bool RequiresDelegate)
```

### DuplicateAllUserDefinedAttribute
```angelscript
void DuplicateAllUserDefinedAttribute(const UInterchangeBaseNode InterchangeSourceNode, UInterchangeBaseNode InterchangeDestinationNode, bool bAddSourceNodeName)
```

### GetUserDefinedAttribute_Boolean
```angelscript
bool GetUserDefinedAttribute_Boolean(const UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, bool& OutValue, FString& OutPayloadKey)
```

### GetUserDefinedAttribute_Double
```angelscript
bool GetUserDefinedAttribute_Double(const UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, float& OutValue, FString& OutPayloadKey)
```

### GetUserDefinedAttribute_Float
```angelscript
bool GetUserDefinedAttribute_Float(const UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, float32& OutValue, FString& OutPayloadKey)
```

### GetUserDefinedAttribute_FString
```angelscript
bool GetUserDefinedAttribute_FString(const UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, FString& OutValue, FString& OutPayloadKey)
```

### GetUserDefinedAttribute_Int32
```angelscript
bool GetUserDefinedAttribute_Int32(const UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName, int& OutValue, FString& OutPayloadKey)
```

### GetUserDefinedAttributeInfos
```angelscript
void GetUserDefinedAttributeInfos(const UInterchangeBaseNode InterchangeNode, TArray<FInterchangeUserDefinedAttributeInfo>& UserDefinedAttributeInfos)
```

### RemoveUserDefinedAttribute
```angelscript
bool RemoveUserDefinedAttribute(UInterchangeBaseNode InterchangeNode, FString UserDefinedAttributeName)
```
Remove the specified user-defined attribute.
@param UserDefinedAttributeName - The name of the user-defined attribute to remove.
@return - True if the attribute exists and was removed, or if the attribute doesn't exist. Returns false if the attribute exists but could not be removed.
Note - User-defined attributes are the user custom attributes from the DCC translated node (for example, extra attributes in Maya).
       The payload key points to an FRichCurve payload.

### StaticClass
```angelscript
UClass StaticClass()
```

