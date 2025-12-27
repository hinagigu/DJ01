# __String

## 方法

### BuildString_Bool
```angelscript
FString BuildString_Bool(FString AppendTo, FString Prefix, bool InBool, FString Suffix)
```
Converts a boolean->string, creating a new string in the form AppendTo+Prefix+InBool+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InBool - The bool value to convert. Will add "true" or "false" to the conversion string
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### BuildString_Color
```angelscript
FString BuildString_Color(FString AppendTo, FString Prefix, FLinearColor InColor, FString Suffix)
```
Converts a color->string, creating a new string in the form AppendTo+Prefix+InColor+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InColor - The linear color value to convert. Uses the standard ToString conversion
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### BuildString_Double
```angelscript
FString BuildString_Double(FString AppendTo, FString Prefix, float InDouble, FString Suffix)
```
Converts a double->string, create a new string in the form AppendTo+Prefix+InDouble+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InDouble - The double value to convert
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### BuildString_Int
```angelscript
FString BuildString_Int(FString AppendTo, FString Prefix, int InInt, FString Suffix)
```
Converts a int->string, creating a new string in the form AppendTo+Prefix+InInt+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InInt - The int value to convert
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### BuildString_IntVector
```angelscript
FString BuildString_IntVector(FString AppendTo, FString Prefix, FIntVector InIntVector, FString Suffix)
```
Converts an IntVector->string, creating a new string in the form AppendTo+Prefix+InIntVector+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InIntVector - The intVector value to convert. Uses the standard FVector::ToString conversion
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### BuildString_Name
```angelscript
FString BuildString_Name(FString AppendTo, FString Prefix, FName InName, FString Suffix)
```
Converts a color->string, creating a new string in the form AppendTo+Prefix+InName+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InName - The name value to convert
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### BuildString_Object
```angelscript
FString BuildString_Object(FString AppendTo, FString Prefix, UObject InObj, FString Suffix)
```
Converts a object->string, creating a new string in the form AppendTo+Prefix+object name+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InObj - The object to convert. Will insert the name of the object into the conversion string
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### BuildString_Rotator
```angelscript
FString BuildString_Rotator(FString AppendTo, FString Prefix, FRotator InRot, FString Suffix)
```
Converts a rotator->string, creating a new string in the form AppendTo+Prefix+InRot+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InRot - The rotator value to convert. Uses the standard ToString conversion
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### BuildString_Vector
```angelscript
FString BuildString_Vector(FString AppendTo, FString Prefix, FVector InVector, FString Suffix)
```
Converts a vector->string, creating a new string in the form AppendTo+Prefix+InVector+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InVector - The vector value to convert. Uses the standard FVector::ToString conversion
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### BuildString_Vector2d
```angelscript
FString BuildString_Vector2d(FString AppendTo, FString Prefix, FVector2D InVector2d, FString Suffix)
```
Converts a vector2d->string, creating a new string in the form AppendTo+Prefix+InVector2d+Suffix
@param AppendTo - An existing string to use as the start of the conversion string
@param Prefix - A string to use as a prefix, after the AppendTo string
@param InVector2d - The vector2d value to convert. Uses the standard FVector2D::ToString conversion
@param Suffix - A suffix to append to the end of the conversion string
@return A new string built from the passed parameters

### Concat_StrStr
```angelscript
FString Concat_StrStr(FString A, FString B)
```
Concatenates two strings together to make a new string
@param A - The original string
@param B - The string to append to A
@returns A new string which is the concatenation of A+B

### Contains
```angelscript
bool Contains(FString SearchIn, FString Substring, bool bUseCase, bool bSearchFromEnd)
```
Returns whether this string contains the specified substring.

@param SubStr                 Find to search for
@param SearchCase             Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )
@param SearchDir                      Indicates whether the search starts at the begining or at the end ( defaults to ESearchDir::FromStart )
@return                                       Returns whether the string contains the substring

### Conv_BoolToString
```angelscript
FString Conv_BoolToString(bool InBool)
```
Converts a boolean value to a string, either 'true' or 'false'

### Conv_BoxCenterAndExtentsToString
```angelscript
FString Conv_BoxCenterAndExtentsToString(FBox Box)
```
Converts a FBox value to a string of its Center and Extents values.

### Conv_BoxToString
```angelscript
FString Conv_BoxToString(FBox Box)
```
Converts a FBox value to a string

### Conv_ByteToString
```angelscript
FString Conv_ByteToString(uint8 InByte)
```
Converts a byte value to a string

### Conv_ColorToString
```angelscript
FString Conv_ColorToString(FLinearColor InColor)
```
Converts a linear color value to a string, in the form '(R=,G=,B=,A=)'

### Conv_DoubleToString
```angelscript
FString Conv_DoubleToString(float InDouble)
```
Converts a double value to a string

### Conv_InputDeviceIdToString
```angelscript
FString Conv_InputDeviceIdToString(FInputDeviceId InDeviceId)
```
Converts a InputDeviceId value to a string

### Conv_Int64ToString
```angelscript
FString Conv_Int64ToString(int64 InInt)
```
Converts an 64-bit integer value to a string

### Conv_IntPointToString
```angelscript
FString Conv_IntPointToString(FIntPoint InIntPoint)
```
Converts an IntPoint value to a string, in the form 'X= Y='

### Conv_IntToString
```angelscript
FString Conv_IntToString(int InInt)
```
Converts an integer value to a string

### Conv_IntVectorToString
```angelscript
FString Conv_IntVectorToString(FIntVector InIntVec)
```
Converts an IntVector value to a string, in the form 'X= Y= Z='

### Conv_MatrixToString
```angelscript
FString Conv_MatrixToString(FMatrix InMatrix)
```
Converts a name value to a string

### Conv_NameToString
```angelscript
FString Conv_NameToString(FName InName)
```
Converts a name value to a string

### Conv_ObjectToString
```angelscript
FString Conv_ObjectToString(UObject InObj)
```
Converts a UObject value to a string by calling the object's GetName method

### Conv_PlatformUserIdToString
```angelscript
FString Conv_PlatformUserIdToString(FPlatformUserId InPlatformUserId)
```
Converts a PlatformUserId value to a string

### Conv_RotatorToString
```angelscript
FString Conv_RotatorToString(FRotator InRot)
```
Converts a rotator value to a string, in the form 'P= Y= R='

### Conv_StringToColor
```angelscript
void Conv_StringToColor(FString InString, FLinearColor& OutConvertedColor, bool& OutIsValid)
```
Convert String Back To Color. IsValid indicates whether or not the string could be successfully converted.

### Conv_StringToDouble
```angelscript
float Conv_StringToDouble(FString InString)
```
Converts a string to a double value

### Conv_StringToInt
```angelscript
int Conv_StringToInt(FString InString)
```
Converts a string to a int value

### Conv_StringToInt64
```angelscript
int64 Conv_StringToInt64(FString InString)
```
Converts a string to a int value

### Conv_StringToName
```angelscript
FName Conv_StringToName(FString InString)
```
Converts a string to a name value

### Conv_StringToRotator
```angelscript
void Conv_StringToRotator(FString InString, FRotator& OutConvertedRotator, bool& OutIsValid)
```
Convert String Back To Rotator. IsValid indicates whether or not the string could be successfully converted.

### Conv_StringToVector
```angelscript
void Conv_StringToVector(FString InString, FVector& OutConvertedVector, bool& OutIsValid)
```
Convert String Back To Vector. IsValid indicates whether or not the string could be successfully converted.

### Conv_StringToVector2D
```angelscript
void Conv_StringToVector2D(FString InString, FVector2D& OutConvertedVector2D, bool& OutIsValid)
```
Convert String Back To Vector2D. IsValid indicates whether or not the string could be successfully converted.

### Conv_StringToVector3f
```angelscript
void Conv_StringToVector3f(FString InString, FVector3f& OutConvertedVector, bool& OutIsValid)
```
Convert String Back To Float Vector. IsValid indicates whether or not the string could be successfully converted.

### Conv_TransformToString
```angelscript
FString Conv_TransformToString(FTransform InTrans)
```
Converts a transform value to a string, in the form 'Translation: X= Y= Z= Rotation: P= Y= R= Scale: X= Y= Z='

### Conv_Vector2dToString
```angelscript
FString Conv_Vector2dToString(FVector2D InVec)
```
Converts a vector2d value to a string, in the form 'X= Y='

### Conv_Vector3fToString
```angelscript
FString Conv_Vector3fToString(FVector3f InVec)
```
Converts a float vector value to a string, in the form 'X= Y= Z='

### Conv_VectorToString
```angelscript
FString Conv_VectorToString(FVector InVec)
```
Converts a vector value to a string, in the form 'X= Y= Z='

### CullArray
```angelscript
int CullArray(FString SourceString, TArray<FString>& InArray)
```
Takes an array of strings and removes any zero length entries.

@param       InArray The array to cull

@return      The number of elements left in InArray

### EndsWith
```angelscript
bool EndsWith(FString SourceString, FString InSuffix, ESearchCase SearchCase)
```
Test whether this string ends with given string.

@param SearchCase            Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )
@return true if this string ends with specified text, false otherwise

### EqualEqual_StriStri
```angelscript
bool EqualEqual_StriStri(FString A, FString B)
```
Test if the input strings are equal (A == B), ignoring case
@param A - The string to compare against
@param B - The string to compare
@returns True if the strings are equal, false otherwise

### EqualEqual_StrStr
```angelscript
bool EqualEqual_StrStr(FString A, FString B)
```
Test if the input strings are equal (A == B)
@param A - The string to compare against
@param B - The string to compare
@returns True if the strings are equal, false otherwise

### FindSubstring
```angelscript
int FindSubstring(FString SearchIn, FString Substring, bool bUseCase, bool bSearchFromEnd, int StartPosition)
```
Finds the starting index of a substring in the a specified string
@param SearchIn The string to search within
@param Substring The string to look for in the SearchIn string
@param bUseCase Whether or not to be case-sensitive
@param bSearchFromEnd Whether or not to start the search from the end of the string instead of the beginning
@param StartPosition The position to start the search from
@return The index (starting from 0 if bSearchFromEnd is false) of the first occurence of the substring

### GetCharacterArrayFromString
```angelscript
TArray<FString> GetCharacterArrayFromString(FString SourceString)
```
Returns an array that contains one entry for each character in SourceString
@param        SourceString    The string to break apart into characters
@return       An array containing one entry for each character in SourceString

### GetCharacterAsNumber
```angelscript
int GetCharacterAsNumber(FString SourceString, int Index)
```
Gets a single character from the string (as an integer)
@param SourceString - The string to convert
@param Index - Location of the character whose value is required
@return The integer value of the character or 0 if index is out of range

### GetSubstring
```angelscript
FString GetSubstring(FString SourceString, int StartIndex, int Length)
```
Returns a substring from the string starting at the specified position
@param SourceString - The string to get the substring from
@param StartIndex - The location in SourceString to use as the start of the substring
@param Length The length of the requested substring

@return The requested substring

### IsEmpty
```angelscript
bool IsEmpty(FString InString)
```
Returns true if the string is empty
@param InString - The string to check
@return Whether or not the string is empty

### IsNumeric
```angelscript
bool IsNumeric(FString SourceString)
```
* Checks if a string contains only numeric characters
* @param       SourceString    The string to check
* @return true if the string only contains numeric characters

### JoinStringArray
```angelscript
FString JoinStringArray(TArray<FString> SourceArray, FString Separator)
```
Concatenates an array of strings into a single string.
@param SourceArray - The array of strings to concatenate.
@param Separator - The string used to separate each element.
@return The final, joined, separated string.

### Left
```angelscript
FString Left(FString SourceString, int Count)
```
Returns the left most given number of characters

### LeftChop
```angelscript
FString LeftChop(FString SourceString, int Count)
```
Returns the left most characters from the string chopping the given number of characters from the end

### LeftPad
```angelscript
FString LeftPad(FString SourceString, int ChCount)
```
* Pad the left of this string for a specified number of characters
* @param       SourceString    The string to pad
* @param       ChCount                 Amount of padding required
* @return      The padded string

### Len
```angelscript
int Len(FString S)
```
Returns the number of characters in the string
@param SourceString - The string to measure
@return The number of chars in the string

### MatchesWildcard
```angelscript
bool MatchesWildcard(FString SourceString, FString Wildcard, ESearchCase SearchCase)
```
Searches this string for a given wild card

@param Wildcard              *?-type wildcard
@param SearchCase    Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )
@return true if this string matches the *?-type wildcard given.
@warning This is a simple, SLOW routine. Use with caution

### Mid
```angelscript
FString Mid(FString SourceString, int Start, int Count)
```
Returns the substring from Start position for Count characters.

### NotEqual_StriStri
```angelscript
bool NotEqual_StriStri(FString A, FString B)
```
Test if the input string are not equal (A != B), ignoring case differences
@param A - The string to compare against
@param B - The string to compare
@return Returns true if the input strings are not equal, false if they are equal

### NotEqual_StrStr
```angelscript
bool NotEqual_StrStr(FString A, FString B)
```
Test if the input string are not equal (A != B)
@param A - The string to compare against
@param B - The string to compare
@return Returns true if the input strings are not equal, false if they are equal

### ParseIntoArray
```angelscript
TArray<FString> ParseIntoArray(FString SourceString, FString Delimiter, bool CullEmptyStrings)
```
Gets an array of strings from a source string divided up by a separator and empty strings can optionally be culled.
@param SourceString - The string to chop up
@param Delimiter - The string to delimit on
@param CullEmptyStrings = true - Cull (true) empty strings or add them to the array (false)
@return The array of string that have been separated

### Replace
```angelscript
FString Replace(FString SourceString, FString From, FString To, ESearchCase SearchCase)
```
Replace all occurrences of a substring in this string

@param From substring to replace
@param To substring to replace From with
@param SearchCase    Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )
@return a copy of this string with the replacement made

### ReplaceInline
```angelscript
int ReplaceInline(FString& SourceString, FString SearchText, FString ReplacementText, ESearchCase SearchCase)
```
Replace all occurrences of SearchText with ReplacementText in this string.

@param       SearchText      the text that should be removed from this string
@param       ReplacementText         the text to insert in its place
@param SearchCase    Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )

@return      the number of occurrences of SearchText that were replaced.

### Reverse
```angelscript
FString Reverse(FString SourceString)
```
Returns a copy of this string, with the characters in reverse order

### Right
```angelscript
FString Right(FString SourceString, int Count)
```
Returns the string to the right of the specified location, counting back from the right (end of the word).

### RightChop
```angelscript
FString RightChop(FString SourceString, int Count)
```
Returns the string to the right of the specified location, counting forward from the left (from the beginning of the word).

### RightPad
```angelscript
FString RightPad(FString SourceString, int ChCount)
```
* Pad the right of this string for a specified number of characters
* @param       SourceString    The string to pad
* @param       ChCount                 Amount of padding required
* @return      The padded string

### Split
```angelscript
bool Split(FString SourceString, FString InStr, FString& LeftS, FString& RightS, ESearchCase SearchCase, ESearchDir SearchDir)
```
Splits this string at given string position case sensitive.

@param InStr The string to search and split at
@param LeftS out the string to the left of InStr, not updated if return is false
@param RightS out the string to the right of InStr, not updated if return is false
@param SearchCase             Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )
@param SearchDir                      Indicates whether the search starts at the begining or at the end ( defaults to ESearchDir::FromStart )
@return true if string is split, otherwise false

### StartsWith
```angelscript
bool StartsWith(FString SourceString, FString InPrefix, ESearchCase SearchCase)
```
Test whether this string starts with given string.

@param SearchCase            Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )
@return true if this string begins with specified text, false otherwise

### TimeSecondsToString
```angelscript
FString TimeSecondsToString(float32 InSeconds)
```
Convert a number of seconds into minutes:seconds.milliseconds format string (including leading zeroes)

@return A new string built from the seconds parameter

### ToLower
```angelscript
FString ToLower(FString SourceString)
```
Returns a string converted to Lower case
@param        SourceString    The string to convert
@return       The string in lower case

### ToUpper
```angelscript
FString ToUpper(FString SourceString)
```
Returns a string converted to Upper case
@param       SourceString    The string to convert
@return      The string in upper case

### Trim
```angelscript
FString Trim(FString SourceString)
```
Removes whitespace characters from the front of this string.

### TrimTrailing
```angelscript
FString TrimTrailing(FString SourceString)
```
Removes trailing whitespace characters

