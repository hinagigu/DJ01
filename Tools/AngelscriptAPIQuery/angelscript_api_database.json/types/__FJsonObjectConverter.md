# __FJsonObjectConverter

## 方法

### UStructToJsonObjectString
```angelscript
bool UStructToJsonObjectString(? MaybeStruct, FString&out Result, int CheckFlags, int SkipFlags, int Indent, bool PrettyPrint)
```

### AppendUStructToJsonObjectString
```angelscript
bool AppendUStructToJsonObjectString(? MaybeStruct, FString& InOutString, int CheckFlags, int SkipFlags, int Indent, bool PrettyPrint)
```

### JsonObjectStringToUStruct
```angelscript
bool JsonObjectStringToUStruct(FString JsonString, ? MaybeStruct, int CheckFlags, int SkipFlags)
```

