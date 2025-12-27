# UPythonCallableForDelegate

**继承自**: `UObject`

UObject proxy base used to wrap a callable Python object so that it can be used with an Unreal delegate
@note This can't go inside the WITH_PYTHON block due to UHT parsing limitations (it doesn't understand that macro)

