# UEditorLoadingAndSavingUtils

**继承自**: `UObject`

This class is a wrapper for editor loading and saving functionality
It is meant to contain only functions that can be executed in script (but are also allowed in C++).
It is separated from FEditorFileUtils to ensure new easier to use methods can be created without breaking FEditorFileUtils backwards compatibility
However this should be used in place of FEditorFileUtils wherever possible as the goal is to deprecate FEditorFileUtils eventually

