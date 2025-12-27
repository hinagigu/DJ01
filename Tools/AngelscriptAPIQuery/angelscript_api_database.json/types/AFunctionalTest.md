# AFunctionalTest

**继承自**: `AActor`

## 属性

### TestLabel
- **类型**: `FString`

### Author
- **类型**: `FString`

### Description
- **类型**: `FString`

### LogErrorHandling
- **类型**: `EFunctionalTestLogHandling`

### LogWarningHandling
- **类型**: `EFunctionalTestLogHandling`

### ObservationPoint
- **类型**: `AActor`

### RandomNumbersStream
- **类型**: `FRandomStream`

### Result
- **类型**: `EFunctionalTestResult`

### PreparationTimeLimit
- **类型**: `float32`

### TimesUpMessage
- **类型**: `FText`

### TimesUpResult
- **类型**: `EFunctionalTestResult`
- **描述**: If test is limited by time this is the result that will be returned when time runs out

### OnTestPrepare
- **类型**: `FFunctionalTestEventSignature`

### OnTestStart
- **类型**: `FFunctionalTestEventSignature`

### OnTestFinished
- **类型**: `FFunctionalTestEventSignature`

### TotalTime
- **类型**: `float32`

### bIsEnabled
- **类型**: `bool`

### bShouldDelayGarbageCollection
- **类型**: `bool`

### TimeLimit
- **类型**: `float32`

## 方法

### AddError
```angelscript
void AddError(FString Message)
```

### AddInfo
```angelscript
void AddInfo(FString Message)
```

### AddRerun
```angelscript
void AddRerun(FName Reason)
```
Causes the test to be rerun for a specific named reason.

### AddWarning
```angelscript
void AddWarning(FString Message)
```

### AssertEqual_Bool
```angelscript
bool AssertEqual_Bool(bool Actual, bool Expected, FString What, const UObject ContextObject)
```
Assert that two bools are equal
@param What   A name to use in the message if the assert fails (What: expected {Actual} to be Equal To {Expected} for context '')

### AssertEqual_Box2D
```angelscript
bool AssertEqual_Box2D(FBox2D Actual, FBox2D Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that two two-component boxes are (memberwise) equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_Double
```angelscript
bool AssertEqual_Double(float Actual, float Expected, FString What, float Tolerance, const UObject ContextObject)
```
Assert that two double are equal within tolerance between two doubles.
@param What  A name to use in the message if the assert fails (What: expected {Actual} to be Equal To {Expected} within Tolerance for context '')

### AssertEqual_Float
```angelscript
bool AssertEqual_Float(float32 Actual, float32 Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that two floats are equal within tolerance between two floats.
@param What  A name to use in the message if the assert fails (What: expected {Actual} to be Equal To {Expected} within Tolerance for context '')

### AssertEqual_Int
```angelscript
bool AssertEqual_Int(int Actual, int Expected, FString What, const UObject ContextObject)
```
Assert that two ints are equal
@param What   A name to use in the message if the assert fails (What: expected {Actual} to be Equal To {Expected} for context '')

### AssertEqual_Matrix
```angelscript
bool AssertEqual_Matrix(FMatrix Actual, FMatrix Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that two 4x4 matrices are (memberwise) equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_Name
```angelscript
bool AssertEqual_Name(FName Actual, FName Expected, FString What, const UObject ContextObject)
```
Assert that two FNames are equal
@param What   A name to use in the message if the assert fails (What: expected {Actual} to be Equal To {Expected} for context '')

### AssertEqual_Object
```angelscript
bool AssertEqual_Object(UObject Actual, UObject Expected, FString What, const UObject ContextObject)
```
Assert that two Objects are equal
@param What   A name to use in the message if the assert fails (What: expected {Actual} to be Equal To {Expected} for context '')

### AssertEqual_Plane
```angelscript
bool AssertEqual_Plane(FPlane Actual, FPlane Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that two planes are (memberwise) equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_Quat
```angelscript
bool AssertEqual_Quat(FQuat Actual, FQuat Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that two quats are (memberwise) equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_Rotator
```angelscript
bool AssertEqual_Rotator(FRotator Actual, FRotator Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that the component angles of two rotators are all equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_RotatorOrientation
```angelscript
bool AssertEqual_RotatorOrientation(FRotator Actual, FRotator Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that the orientation of two rotators is the same within a small tolerance. Robust to quaternion singularities where angles can differ despite having an identical orientation.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_String
```angelscript
bool AssertEqual_String(FString Actual, FString Expected, FString What, const UObject ContextObject)
```
Assert that two Strings are equal.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_TraceQueryResults
```angelscript
bool AssertEqual_TraceQueryResults(const UTraceQueryTestResults Actual, const UTraceQueryTestResults Expected, FString What, const UObject ContextObject)
```
Assert that two TraceQueryResults are equal.
@param What   A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertEqual_Transform
```angelscript
bool AssertEqual_Transform(FTransform Actual, FTransform Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that two transforms are (components memberwise - translation, rotation, scale) equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_Vector
```angelscript
bool AssertEqual_Vector(FVector Actual, FVector Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that two vectors are (memberwise) equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_Vector2D
```angelscript
bool AssertEqual_Vector2D(FVector2D Actual, FVector2D Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that two two-component vectors are (memberwise) equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertEqual_Vector4
```angelscript
bool AssertEqual_Vector4(FVector4 Actual, FVector4 Expected, FString What, float32 Tolerance, const UObject ContextObject)
```
Assert that two four-component vectors are (memberwise) equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' to be {Expected} but it was {Actual} for context ''")

### AssertFalse
```angelscript
bool AssertFalse(bool Condition, FString Message, const UObject ContextObject)
```
Assert that a boolean value is false.
@param Message       The message to display if the assert fails ("Assertion Failed: 'Message' for context ''")

### AssertIsValid
```angelscript
bool AssertIsValid(UObject Object, FString Message, const UObject ContextObject)
```
Assert that a UObject is valid
@param Message       The message to display if the object is invalid ("Invalid object: 'Message' for context ''")

### AssertNotEqual_Box2D
```angelscript
bool AssertNotEqual_Box2D(FBox2D Actual, FBox2D NotExpected, FString What, const UObject ContextObject)
```
Assert that two two-component boxes are (memberwise) not equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertNotEqual_Matrix
```angelscript
bool AssertNotEqual_Matrix(FMatrix Actual, FMatrix NotExpected, FString What, const UObject ContextObject)
```
Assert that two 4x4 matrices are (memberwise) not equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertNotEqual_Plane
```angelscript
bool AssertNotEqual_Plane(FPlane Actual, FPlane NotExpected, FString What, const UObject ContextObject)
```
Assert that two planes are (memberwise) not equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertNotEqual_Quat
```angelscript
bool AssertNotEqual_Quat(FQuat Actual, FQuat NotExpected, FString What, const UObject ContextObject)
```
Assert that two quats are (memberwise) not equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertNotEqual_Rotator
```angelscript
bool AssertNotEqual_Rotator(FRotator Actual, FRotator NotExpected, FString What, const UObject ContextObject)
```
Assert that the component angles of two rotators are all not equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertNotEqual_String
```angelscript
bool AssertNotEqual_String(FString Actual, FString NotExpected, FString What, const UObject ContextObject)
```
Assert that two Strings are not equal.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertNotEqual_Transform
```angelscript
bool AssertNotEqual_Transform(FTransform Actual, FTransform NotExpected, FString What, const UObject ContextObject)
```
Assert that two transforms are (components memberwise - translation, rotation, scale) not equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertNotEqual_Vector
```angelscript
bool AssertNotEqual_Vector(FVector Actual, FVector NotExpected, FString What, const UObject ContextObject)
```
Assert that two vectors are (memberwise) not equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertNotEqual_Vector2D
```angelscript
bool AssertNotEqual_Vector2D(FVector2D Actual, FVector2D NotExpected, FString What, const UObject ContextObject)
```
Assert that two two-component vectors are (memberwise) not equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertNotEqual_Vector4
```angelscript
bool AssertNotEqual_Vector4(FVector4 Actual, FVector4 NotExpected, FString What, const UObject ContextObject)
```
Assert that two four-component vectors are (memberwise) not equal within a small tolerance.
@param What  A name to use in the message if the assert fails ("Expected 'What' not to be {Expected} but it was {Actual} for context ''")

### AssertTrue
```angelscript
bool AssertTrue(bool Condition, FString Message, const UObject ContextObject)
```
Assert that a boolean value is true.
@param Message       The message to display if the assert fails ("Assertion Failed: 'Message' for context ''")

### AssertValue_DateTime
```angelscript
bool AssertValue_DateTime(FDateTime Actual, EComparisonMethod ShouldBe, FDateTime Expected, FString What, const UObject ContextObject)
```
Assert on a relationship between two DateTimes.
@param What  A name to use in the message if the assert fails (What: expected {Actual} to be <ShouldBe> {Expected} for context '')

### AssertValue_Double
```angelscript
bool AssertValue_Double(float Actual, EComparisonMethod ShouldBe, float Expected, FString What, const UObject ContextObject)
```
Assert on a relationship between two doubles.
@param What  A name to use in the message if the assert fails (What: expected {Actual} to be <ShouldBe> {Expected} for context '')

### AssertValue_Float
```angelscript
bool AssertValue_Float(float32 Actual, EComparisonMethod ShouldBe, float32 Expected, FString What, const UObject ContextObject)
```
Assert on a relationship between two floats.
@param What  A name to use in the message if the assert fails (What: expected {Actual} to be <ShouldBe> {Expected} for context '')

### AssertValue_Int
```angelscript
bool AssertValue_Int(int Actual, EComparisonMethod ShouldBe, int Expected, FString What, const UObject ContextObject)
```
Assert on a relationship between two integers.
@param What  A name to use in the message if the assert fails (What: expected {Actual} to be <ShouldBe> {Expected} for context '')

### DebugGatherRelevantActors
```angelscript
TArray<AActor> DebugGatherRelevantActors()
```
Used by debug drawing to gather actors this test is using and point at them on the level to better understand test's setup

### FinishTest
```angelscript
void FinishTest(EFunctionalTestResult TestResult, FString Message)
```

### GetCurrentRerunReason
```angelscript
FName GetCurrentRerunReason()
```
Returns the current re-run reason if we're in a named re-run.

### IsEnabled
```angelscript
bool IsEnabled()
```

### IsReady
```angelscript
bool IsReady()
```
IsReady() is called once per frame after a test is run, until it returns true.  You should use this function to
delay Start being called on the test until preconditions are met.

### IsRunning
```angelscript
bool IsRunning()
```
AActor interface end

### LogMessage
```angelscript
void LogMessage(FString Message)
```

### OnAdditionalTestFinishedMessageRequest
```angelscript
FString OnAdditionalTestFinishedMessageRequest(EFunctionalTestResult TestResult)
```

### OnWantsReRunCheck
```angelscript
bool OnWantsReRunCheck()
```
retrieves information whether test wants to have another run just after finishing

### PrepareTest
```angelscript
void PrepareTest()
```
Prepare Test is fired once the test starts up, before the test IsReady() and thus before Start Test is called.
So if there's some initial conditions or setup that you might need for your IsReady() check, you might want
to do that here.

### StartTest
```angelscript
void StartTest()
```
Called once the IsReady() check for the test returns true.  After that happens the test has Officially started,
and it will begin receiving Ticks in the blueprint.

### RegisterAutoDestroyActor
```angelscript
void RegisterAutoDestroyActor(AActor ActorToAutoDestroy)
```
Actors registered this way will be automatically destroyed (by limiting their lifespan)
    on test finish

### SetConsoleVariable
```angelscript
void SetConsoleVariable(FString Name, FString InValue)
```
Sets the CVar from the given input. Variable gets reset after the test.

### SetConsoleVariableFromBoolean
```angelscript
void SetConsoleVariableFromBoolean(FString Name, bool InValue)
```
Sets the CVar from the given input. Variable gets reset after the test.

### SetConsoleVariableFromFloat
```angelscript
void SetConsoleVariableFromFloat(FString Name, float32 InValue)
```
Sets the CVar from the given input. Variable gets reset after the test.

### SetConsoleVariableFromInteger
```angelscript
void SetConsoleVariableFromInteger(FString Name, int InValue)
```
Sets the CVar from the given input. Variable gets reset after the test.

### SetTimeLimit
```angelscript
void SetTimeLimit(float32 NewTimeLimit, EFunctionalTestResult ResultWhenTimeRunsOut)
```

