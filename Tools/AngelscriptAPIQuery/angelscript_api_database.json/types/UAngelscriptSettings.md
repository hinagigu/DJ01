# UAngelscriptSettings

**继承自**: `UObject`

## 属性

### PreprocessorFlags
- **类型**: `TArray<FString>`
- **描述**: Additional preprocessor flags which will be defined when preprocessing angelscript files.
Add them e.g. to BaseEngine.ini:
  [/Script/AngelscriptCode.AngelscriptSettings]
  +PreprocessorFlags="FOO"
  +PreprocessorFlags="BAR"

### bAllowImplicitPropertyAccessors
- **类型**: `bool`
- **描述**: Whether to allow any C++ function that starts with Get...() to be accessed as a property. (Requires editor restart)

### bAutomaticImports
- **类型**: `bool`
- **描述**: Whether to use the new automatic import system (explicit import statements no longer used)

### bWarnOnManualImportStatements
- **类型**: `bool`
- **描述**: Emit warnings when import statements are used while automatic imports are turned on.

### MathNamespace
- **类型**: `EAngelscriptMathNamespace`
- **描述**: Namespace to use for math library functions in angelscript

### bDefaultFunctionBlueprintCallable
- **类型**: `bool`
- **描述**: Whether UFUNCTION()s should be BlueprintCallable by default without explicit BlueprintCallable specifier.

### DefaultPropertyEditSpecifier
- **类型**: `EAngelscriptPropertyEditSpecifier`
- **描述**: Default Edit access specifier for script UPROPERTY()s without explicit Edit specifier on classes.

### DefaultPropertyEditSpecifierForStructs
- **类型**: `EAngelscriptPropertyEditSpecifier`
- **描述**: Default Edit access specifier for script UPROPERTY()s without explicit Edit specifier on structs.

### DefaultPropertyBlueprintSpecifier
- **类型**: `EAngelscriptPropertyBlueprintSpecifier`
- **描述**: Default Blueprint access specifier for script UPROPERTY()s without explicit Blueprint specifier.

### bMarkNonUpropertyPropertiesAsTransient
- **类型**: `bool`
- **描述**: Some properties are implicitly treated as UPROPERTY:s to be seen correctly by the GC, if true this ensures such properties are marked as transient to avoid unintentional serialization

### StaticClassDeprecation
- **类型**: `EAngelscriptStaticClassMode`
- **描述**: Whether to deprecate or disallow the usage of AAnyClass::StaticClass().
The newer alternative does not require the StaticClass call, the class name can be used directly.

### bUseScriptNameForBlueprintLibraryNamespaces
- **类型**: `bool`
- **描述**: Whether we should use the ScriptName meta tag for namespaced binds if available.

### bAllowRawConstructorsForComponentsAndActors
- **类型**: `bool`
- **描述**: Whether to allow actor and component classes to be instantiated using their raw constructor, instead of forcing SpawnActor or UComponent::Create() calls.

### bForceConstWithinDevelopmentOnlyFunctions
- **类型**: `bool`
- **描述**: Whether any code that is placed within check() asserts, Print() statements and other development-only functions should only be allowed to call const methods.
This is intended to help catch issues with side-effects being placed inside expressions that get compiled out in shipping builds.

### BlueprintLibraryNamespacePrefixesToStrip
- **类型**: `TArray<FString>`
- **描述**: Strip these prefixes from namespaced binds. For example, when stripping "Kismet": `UKismetSystemLibrary::IsStandalone()` becomes `SystemLibrary::IsStandalone()`

### BlueprintLibraryNamespaceSuffixesToStrip
- **类型**: `TArray<FString>`
- **描述**: Strip these suffixes from namespaced binds. For example, when stripping "Library": `SystemLibrary::IsStandalone()` becomes `System::IsStandalone()`

### EditorMaximumScriptExecutionTime
- **类型**: `float32`
- **描述**: Only in editor:
If a script function takes longer than this time to execute, kill it with an exception.
This allows the editor to recover from accidental infinite loops, but does not work in cooked games!

### bScriptFloatIsFloat64
- **类型**: `bool`
- **描述**: In order to avoid confusion with blueprints, make the 'float' type in script resolve to 'float64'.

### bDeprecateDoubleType
- **类型**: `bool`
- **描述**: Deprecate usage of the 'double' type in script, in favor of 'float64' or just 'float' when bScriptFloatIsFloat64.

### bWarnOnFloatConstantsForDoubleValues
- **类型**: `bool`
- **描述**: Emit a warning when using a float constant (eg `0.f`) to initialize a double value.

### bWarnIntegerDivision
- **类型**: `bool`
- **描述**: Emit a warning for precision loss when integer division is used.

### bErrorWhenUsingInvalidWorldContext
- **类型**: `bool`
- **描述**: Throw an exception when calling a function that requires a World Context to be set, but the current object is not in a world.
Note: this error is only checked in editor for performance reasons.

### bWarnOnUnusedReturnValueForConstMethods
- **类型**: `bool`
- **描述**: Show a warning when the result of a const method is not used.

### bWarnOnImplicitSignedUnsignedConversion
- **类型**: `bool`
- **描述**: Show a warning when an implicit conversion between signed/unsigned integers can cause incorrect results.

### bErrorOnIncorrectEditorOnlyCode
- **类型**: `bool`
- **描述**: Show an error when a function or property that is editor-only is used outside of an EDITOR block or editor-only script module.

Note: Can cause false positives if a function or property is declared separately in editor-only and not-editor-only blocks.
In that case, put the preprocessor directives inside the function body, instead of around the whole function.

### bWarnOnDivergentComparisonOperatorOverloads
- **类型**: `bool`
- **描述**: Show a warning when a comparison operator overload is implemented targeting a different type than the containing type.

### bWarnOnIncrementDecrementInComplexExpression
- **类型**: `bool`
- **描述**: Show a warning when an increment or decrement (++ / --) expression is used within a complex expression.
Side effects are not usually expected for longer expressions and can be hard to read.

