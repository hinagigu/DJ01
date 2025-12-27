# FPaintContext

The state passed into OnPaint that we can expose as a single painting structure to blueprints to
allow script code to override OnPaint behavior.

## 方法

### GetAllottedGeometry
```angelscript
FGeometry GetAllottedGeometry()
```

### GetStyleColor
```angelscript
FLinearColor GetStyleColor(FName Color)
```

### GetStyleBrush
```angelscript
FSlateBrush GetStyleBrush(FName Brush)
```

### GetStyleFont
```angelscript
FSlateFontInfo GetStyleFont(int Size)
```

### DrawBox
```angelscript
void DrawBox(FVector2D Position, FVector2D Size, FLinearColor Color)
```

### DrawBox
```angelscript
void DrawBox(FVector2D Position, FVector2D Size, FName BrushName, FLinearColor TintColor)
```

### DrawBox
```angelscript
void DrawBox(FVector2D Position, FVector2D Size, FSlateBrush Brush, FLinearColor TintColor)
```

### DrawBox
```angelscript
void DrawBox(FVector2D Position, FVector2D Size, USlateBrushAsset Brush, FLinearColor TintColor)
```

### DrawLine
```angelscript
void DrawLine(FVector2D PositionA, FVector2D PositionB, FLinearColor Color, float32 Thickness, bool bAntiAlias)
```

### DrawLines
```angelscript
void DrawLines(TArray<FVector2D> Points, FLinearColor Color, float32 Thickness, bool bAntiAlias)
```

### DrawText
```angelscript
void DrawText(FString Text, FVector2D Position, FLinearColor Color)
```

### DrawText
```angelscript
void DrawText(FSlateFontInfo Font, FString Text, FVector2D Position, FLinearColor Color)
```

### opAssign
```angelscript
FPaintContext& opAssign(FPaintContext Other)
```

