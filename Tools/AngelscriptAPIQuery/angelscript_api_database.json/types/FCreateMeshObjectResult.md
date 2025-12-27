# FCreateMeshObjectResult

FCreateMeshObjectResult is returned by UModelingObjectsCreationAPI::CreateMeshObject()
to indicate success/failure and provide information about created mesh objects

## 属性

### NewComponent
- **类型**: `UPrimitiveComponent`
- **描述**: A pointer to a newly-created PrimitiveComponent for the mesh object, if applicable (eg StaticMeshComponent)

## 方法

### opAssign
```angelscript
FCreateMeshObjectResult& opAssign(FCreateMeshObjectResult Other)
```

