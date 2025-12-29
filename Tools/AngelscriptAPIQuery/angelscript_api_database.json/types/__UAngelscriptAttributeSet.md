# __UAngelscriptAttributeSet

## 方法

### CompareGameplayAttributes
```angelscript
bool CompareGameplayAttributes(FGameplayAttribute First, FGameplayAttribute Second)
```
Comapre two gameplay attributes whether or not they are equal

### GetGameplayAttribute
```angelscript
FGameplayAttribute GetGameplayAttribute(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName)
```
Get an attribute on an attribute set that you expects will exist and want to assert if it for whatever reason does not.

### TryGetGameplayAttribute
```angelscript
bool TryGetGameplayAttribute(TSubclassOf<UAngelscriptAttributeSet> AttributeSetClass, FName AttributeName, FGameplayAttribute& OutGameplayAttribute)
```
Attempt to find a gameplay attribute. This is useful with for example dynamic attributes where you are not sure if the attribute exists.

### StaticClass
```angelscript
UClass StaticClass()
```

