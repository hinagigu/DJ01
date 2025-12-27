# __Text

## 方法

### AsCurrency_Float
```angelscript
FText AsCurrency_Float(float32 Value, ERoundingMode RoundingMode, bool bAlwaysSign, bool bUseGrouping, int MinimumIntegralDigits, int MaximumIntegralDigits, int MinimumFractionalDigits, int MaximumFractionalDigits, FString CurrencyCode)
```
Converts a passed in float to a text formatted as a currency

### AsCurrency_Integer
```angelscript
FText AsCurrency_Integer(int Value, ERoundingMode RoundingMode, bool bAlwaysSign, bool bUseGrouping, int MinimumIntegralDigits, int MaximumIntegralDigits, int MinimumFractionalDigits, int MaximumFractionalDigits, FString CurrencyCode)
```
Converts a passed in integer to a text formatted as a currency

### AsCurrencyBase
```angelscript
FText AsCurrencyBase(int BaseValue, FString CurrencyCode)
```
Generate an FText that represents the passed number as currency in the current culture.
BaseVal is specified in the smallest fractional value of the currency and will be converted for formatting according to the selected culture.
Keep in mind the CurrencyCode is completely independent of the culture it's displayed in (and they do not imply one another).
For example: FText::AsCurrencyBase(650, TEXT("EUR")); would return an FText of "<EUR>6.50" in most English cultures (en_US/en_UK) and "6,50<EUR>" in Spanish (es_ES) (where <EUR> is U+20AC)

### AsDate_DateTime
```angelscript
FText AsDate_DateTime(FDateTime InDateTime)
```
Converts a passed in date & time to a text, formatted as a date using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

### AsDateTime_DateTime
```angelscript
FText AsDateTime_DateTime(FDateTime In)
```
Converts a passed in date & time to a text, formatted as a date & time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

### AsPercent_Float
```angelscript
FText AsPercent_Float(float32 Value, ERoundingMode RoundingMode, bool bAlwaysSign, bool bUseGrouping, int MinimumIntegralDigits, int MaximumIntegralDigits, int MinimumFractionalDigits, int MaximumFractionalDigits)
```
Converts a passed in float to a text, formatted as a percent

### AsTime_DateTime
```angelscript
FText AsTime_DateTime(FDateTime In)
```
Converts a passed in date & time to a text, formatted as a time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

### AsTimespan_Timespan
```angelscript
FText AsTimespan_Timespan(FTimespan InTimespan)
```
Converts a passed in time span to a text, formatted as a time span

### AsTimeZoneDate_DateTime
```angelscript
FText AsTimeZoneDate_DateTime(FDateTime InDateTime, FString InTimeZone)
```
Converts a passed in date & time to a text, formatted as a date using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

### AsTimeZoneDateTime_DateTime
```angelscript
FText AsTimeZoneDateTime_DateTime(FDateTime InDateTime, FString InTimeZone)
```
Converts a passed in date & time to a text, formatted as a date & time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

### AsTimeZoneTime_DateTime
```angelscript
FText AsTimeZoneTime_DateTime(FDateTime InDateTime, FString InTimeZone)
```
Converts a passed in date & time to a text, formatted as a time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

### Conv_BoolToText
```angelscript
FText Conv_BoolToText(bool InBool)
```
Converts a boolean value to formatted text, either 'true' or 'false'

### Conv_ByteToText
```angelscript
FText Conv_ByteToText(uint8 Value)
```
Converts a byte value to formatted text

### Conv_ColorToText
```angelscript
FText Conv_ColorToText(FLinearColor InColor)
```
Converts a linear color value to localized formatted text, in the form '(R=,G=,B=,A=)'

### Conv_DoubleToText
```angelscript
FText Conv_DoubleToText(float Value, ERoundingMode RoundingMode, bool bAlwaysSign, bool bUseGrouping, int MinimumIntegralDigits, int MaximumIntegralDigits, int MinimumFractionalDigits, int MaximumFractionalDigits)
```
Converts a passed in double to text based on formatting options

### Conv_Int64ToText
```angelscript
FText Conv_Int64ToText(int64 Value, bool bAlwaysSign, bool bUseGrouping, int MinimumIntegralDigits, int MaximumIntegralDigits)
```
Converts a passed in integer to text based on formatting options

### Conv_IntToText
```angelscript
FText Conv_IntToText(int Value, bool bAlwaysSign, bool bUseGrouping, int MinimumIntegralDigits, int MaximumIntegralDigits)
```
Converts a passed in integer to text based on formatting options

### Conv_NameToText
```angelscript
FText Conv_NameToText(FName InName)
```
Converts Name to culture invariant text

### Conv_ObjectToText
```angelscript
FText Conv_ObjectToText(UObject InObj)
```
Converts a UObject value to culture invariant text by calling the object's GetName method

### Conv_RotatorToText
```angelscript
FText Conv_RotatorToText(FRotator InRot)
```
Converts a rotator value to localized formatted text, in the form 'P= Y= R='

### Conv_StringToText
```angelscript
FText Conv_StringToText(FString InString)
```
Converts string to culture invariant text. Use 'Make Literal Text' to create localizable text, or 'Format' if concatenating localized text

### Conv_TextToString
```angelscript
FString Conv_TextToString(FText InText)
```
Converts localizable text to the string

### Conv_TransformToText
```angelscript
FText Conv_TransformToText(FTransform InTrans)
```
Converts a transform value to localized formatted text, in the form 'Translation: X= Y= Z= Rotation: P= Y= R= Scale: X= Y= Z='

### Conv_Vector2dToText
```angelscript
FText Conv_Vector2dToText(FVector2D InVec)
```
Converts a vector2d value to localized formatted text, in the form 'X= Y='

### Conv_VectorToText
```angelscript
FText Conv_VectorToText(FVector InVec)
```
Converts a vector value to localized formatted text, in the form 'X= Y= Z='

### EqualEqual_IgnoreCase_TextText
```angelscript
bool EqualEqual_IgnoreCase_TextText(FText A, FText B)
```
Returns true if A and B are linguistically equal (A == B), ignoring case.

### EqualEqual_TextText
```angelscript
bool EqualEqual_TextText(FText A, FText B)
```
Returns true if A and B are linguistically equal (A == B).

### FindTextInLocalizationTable
```angelscript
bool FindTextInLocalizationTable(FString Namespace, FString Key, FText& OutText, FString SourceString)
```
Attempts to find existing Text using the representation found in the loc tables for the specified namespace and key.
@param Namespace The namespace of the text to find (if any).
@param Key The key of the text to find.
@param SourceString If set (not empty) then the found text must also have been created from this source string.

### GetEmptyText
```angelscript
FText GetEmptyText()
```
Returns an empty piece of text.

### GetTextId
```angelscript
bool GetTextId(FText Text, FString& OutNamespace, FString& OutKey)
```
Attempts to get the ID (namespace and key) used by the given text.
@return True if the namespace (which may be empty) and key were found, false otherwise.

### GetTextSourceString
```angelscript
FString GetTextSourceString(FText Text)
```
Get the (non-localized) source string of the given text.
@note For a generated text (eg, the result of a Format), this will deep build the source string as if the generation had run for the native language.

### IsPolyglotDataValid
```angelscript
void IsPolyglotDataValid(FPolyglotTextData PolyglotData, bool& IsValid, FText& ErrorMessage)
```
Check whether the given polyglot data is valid.
@return True if the polyglot data is valid, false otherwise. ErrorMessage will be filled in if the the data is invalid.

### MakeInvariantText
```angelscript
FText MakeInvariantText(FString InString)
```
Converts string to culture invariant text. Use 'Make Literal Text' to create localizable text, or 'Format' if concatenating localized text

### NotEqual_IgnoreCase_TextText
```angelscript
bool NotEqual_IgnoreCase_TextText(FText A, FText B)
```
Returns true if A and B are linguistically not equal (A != B), ignoring case.

### NotEqual_TextText
```angelscript
bool NotEqual_TextText(FText A, FText B)
```
Returns true if A and B are linguistically not equal (A != B).

### PolyglotDataToText
```angelscript
FText PolyglotDataToText(FPolyglotTextData PolyglotData)
```
Get the text instance created from this polyglot data.
@return The text instance, or an empty text if the data is invalid.

### StringTableIdAndKeyFromText
```angelscript
bool StringTableIdAndKeyFromText(FText Text, FName& OutTableId, FString& OutKey)
```
Attempts to get the String Table ID and key used by the given text.
@return True if the String Table ID and key were found, false otherwise.

### TextFromStringTable
```angelscript
FText TextFromStringTable(FName TableId, FString Key)
```
Attempts to create a text instance from a string table ID and key.
@note This exists to allow programmatic look-up of a string table entry from dynamic content - you should favor setting your string table reference on a text property or pin wherever possible as it is significantly more robust (see "Make Literal Text").
@return The found text, or a dummy text if the entry could not be found.

### TextIsCultureInvariant
```angelscript
bool TextIsCultureInvariant(FText InText)
```
Returns true if text is culture invariant.

### TextIsEmpty
```angelscript
bool TextIsEmpty(FText InText)
```
Returns true if text is empty.

### TextIsFromStringTable
```angelscript
bool TextIsFromStringTable(FText Text)
```
Returns true if the given text is referencing a string table.

### TextIsTransient
```angelscript
bool TextIsTransient(FText InText)
```
Returns true if text is transient.

### TextToLower
```angelscript
FText TextToLower(FText InText)
```
Transforms the text to lowercase in a culture correct way.
@note The returned instance is linked to the original and will be rebuilt if the active culture is changed.

### TextToUpper
```angelscript
FText TextToUpper(FText InText)
```
Transforms the text to uppercase in a culture correct way.
@note The returned instance is linked to the original and will be rebuilt if the active culture is changed.

### TextTrimPreceding
```angelscript
FText TextTrimPreceding(FText InText)
```
Removes whitespace characters from the front of the text.

### TextTrimPrecedingAndTrailing
```angelscript
FText TextTrimPrecedingAndTrailing(FText InText)
```
Removes whitespace characters from the front and end of the text.

### TextTrimTrailing
```angelscript
FText TextTrimTrailing(FText InText)
```
Removes trailing whitespace characters.

