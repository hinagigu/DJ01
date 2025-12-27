# UInterchangePythonPipelineAsset

**继承自**: `UObject`

* This class is a helper class for Python pipelines. It allows the class picker to filter the Content Browser instance we want to support
* in the pipeline stack.
*
* Use this class factory to be able to create an instance of a Python pipeline in the Content Browser.
* A Python pipeline does not have any locked properties, and all default values must be set in the Python script.
* This restriction exists because Python classes are transient, so any assets created from a Python class cannot be saved.

## 属性

### PythonClass
- **类型**: `TSoftClassPtr<UInterchangePythonPipelineBase>`
- **描述**: The Python class we want to use as a pipeline.

