# __USharedImageConstRefBlueprintFns

## 方法

### GetHeight
```angelscript
int GetHeight(FSharedImageConstRefBlueprint Image)
```
Returns -1 if Image is invalid

### GetPixelLinearColor
```angelscript
FLinearColor GetPixelLinearColor(FSharedImageConstRefBlueprint Image, int X, int Y, bool& bValid, FLinearColor FailureColor)
```
Returns the color value for the given pixel. If the input position is invalid, the format is invalid,
or the reference isn't set, bValid will be false and the function will return FailureColor. The color
is converted using the image's gamma space in to linear space.

Do not use this for full image processing as it will be extremely slow, contact support if you need such
functionality.

### GetPixelValue
```angelscript
FVector4f GetPixelValue(FSharedImageConstRefBlueprint Image, int X, int Y, bool& bValid)
```
Returns the value in the texture for the given pixel as a float vector. If the input position is invalid, the format is invalid,
or the reference isn't set, bValid will be false and the function will return FVector4(0,0,0,0).

Pixel values are directly returned with no gamma transformation to allow for lookup tables. Also note that
8 bit formats that you might normally expect to be normalized to 0..1 will return their values directly as 0..256.

This supports all image formats.

G8 is replicated to X/Y/Z/1.
R16/R32 is returned as R/0/0/1.

Do not use this for full image processing as it will be extremely slow, contact support if you need such
functionality.

### GetSize
```angelscript
FVector2f GetSize(FSharedImageConstRefBlueprint Image)
```
Returns (-1, -1) if Image is invalid

### GetWidth
```angelscript
int GetWidth(FSharedImageConstRefBlueprint Image)
```
Returns -1 if Image is invalid

### IsValid
```angelscript
bool IsValid(FSharedImageConstRefBlueprint Image)
```

### StaticClass
```angelscript
UClass StaticClass()
```

