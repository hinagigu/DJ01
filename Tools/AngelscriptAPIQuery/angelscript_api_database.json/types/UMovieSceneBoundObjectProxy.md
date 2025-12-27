# UMovieSceneBoundObjectProxy

**继承自**: `UInterface`

## 方法

### GetBoundObjectForSequencer
```angelscript
UObject GetBoundObjectForSequencer(UObject ResolvedObject)
```
Retrieve the bound object that this interface wants to animate. Could be 'this' or a transient child object.

@return Pointer to the object that should be animated, or nullptr if it's not valid.

