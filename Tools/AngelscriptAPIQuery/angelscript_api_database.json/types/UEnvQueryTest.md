# UEnvQueryTest

**继承自**: `UEnvQueryNode`

## 属性

### TestPurpose
- **类型**: `EEnvTestPurpose`
- **描述**: The purpose of this test.  Should it be used for filtering possible results, scoring them, or both?

### TestComment
- **类型**: `FString`
- **描述**: Optional comment or explanation about what this test is for.  Useful when the purpose of tests may not be clear,
especially when there are multiple tests of the same type.

### MultipleContextFilterOp
- **类型**: `EEnvTestFilterOperator`
- **描述**: Determines filtering operator when context returns multiple items

### MultipleContextScoreOp
- **类型**: `EEnvTestScoreOperator`
- **描述**: Determines scoring operator when context returns multiple items

### FilterType
- **类型**: `EEnvTestFilterType`
- **描述**: Does this test filter out results that are below a lower limit, above an upper limit, or both?  Or does it just look for a matching value?

### BoolValue
- **类型**: `FAIDataProviderBoolValue`
- **描述**: Desired boolean value of the test for scoring to occur or filtering test to pass.

### FloatValueMin
- **类型**: `FAIDataProviderFloatValue`
- **描述**: Minimum limit (inclusive) of valid values for the raw test value. Lower values will be discarded as invalid.

### FloatValueMax
- **类型**: `FAIDataProviderFloatValue`
- **描述**: Maximum limit (inclusive) of valid values for the raw test value. Higher values will be discarded as invalid.

### ScoringEquation
- **类型**: `EEnvTestScoreEquation`
- **描述**: The shape of the curve equation to apply to the normalized score before multiplying by factor.

### ClampMinType
- **类型**: `EEnvQueryTestClamping`
- **描述**: How should the lower bound for normalization of the raw test value before applying the scoring formula be determined?
          Should it use the lowest value found (tested), the lower threshold for filtering, or a separate specified normalization minimum?

### ClampMaxType
- **类型**: `EEnvQueryTestClamping`
- **描述**: How should the upper bound for normalization of the raw test value before applying the scoring formula be determined?
          Should it use the highest value found (tested), the upper threshold for filtering, or a separate specified normalization maximum?

### NormalizationType
- **类型**: `EEQSNormalizationType`
- **描述**: Specifies how to determine value span used to normalize scores

### ScoreClampMin
- **类型**: `FAIDataProviderFloatValue`
- **描述**: Minimum value to use to normalize the raw test value before applying scoring formula.

### ScoreClampMax
- **类型**: `FAIDataProviderFloatValue`
- **描述**: Maximum value to use to normalize the raw test value before applying scoring formula.

### ScoringFactor
- **类型**: `FAIDataProviderFloatValue`
- **描述**: The weight (factor) by which to multiply the normalized score after the scoring equation is applied.

### ReferenceValue
- **类型**: `FAIDataProviderFloatValue`
- **描述**: When specified gets used to normalize test's results in such a way that the closer a value is to ReferenceValue
    the higher normalized result it will produce. Value farthest from ReferenceValue will be normalized
    to 0, and all the other values in between will get normalized linearly with the distance to ReferenceValue.

### bDefineReferenceValue
- **类型**: `bool`
- **描述**: When set to true enables usage of ReferenceValue. It's false by default

