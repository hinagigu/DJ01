# __EditorDialog

## 方法

### ShowMessage
```angelscript
EAppReturnType ShowMessage(FText Title, FText Message, EAppMsgType MessageType, EAppReturnType DefaultValue, EAppMsgCategory MessageCategory)
```
Open a modal message box dialog with the given message. If running in "-unattended" mode it will immediately
return the value specified by DefaultValue. If not running in "-unattended" mode then it will block execution
until the user makes a decision, at which point their decision will be returned.
@param Title                 The title of the created dialog window
@param Message               Text of the message to show
@param MessageType   Specifies which buttons the dialog should have
@param DefaultValue  If the application is Unattended, the function will log and return DefaultValue
@param MessageCategory The category of the message (affects the icon used)
@return The result of the users decision, or DefaultValue if running in unattended mode.

### ShowObjectDetailsView
```angelscript
bool ShowObjectDetailsView(FText Title, UObject InOutObject, FEditorDialogLibraryObjectDetailsViewOptions Options)
```
Open a modal message box dialog containing a details view for inspecting / modifying a UObject.
@param Title                 The title of the created dialog window
@param InOutObject   Object instance of ClassOfObject which is supposed to be viewed
@param Options               Optional settings to customize the look of the details view
@return The result of the users decision, true=Ok, false=Cancel, or false if running in unattended mode.

### ShowObjectsDetailsView
```angelscript
bool ShowObjectsDetailsView(FText Title, TArray<UObject> InOutObjects, FEditorDialogLibraryObjectDetailsViewOptions Options)
```
Open a modal message box dialog containing a details view for inspecting / modifying multiples UObjects.
@param Title                 The title of the created dialog window
@param InOutObjects  Array of object instances which are supposed to be viewed
@param Options               Optional settings to customize the look of the details view
@return The result of the users decision, true=Ok, false=Cancel, or false if running in unattended mode.

### ShowSuppressableWarningDialog
```angelscript
bool ShowSuppressableWarningDialog(FText Title, FText Message, FString InIniSettingName, FString InIniSettingFileNameOverride, bool bDefaultValue)
```
Open a modal suppressable warning window, if suppressed will return the default value
@param Title                                                  The title of the created dialog window
@param Message                                                Text of the message to show
@param InIniSettingName                               The name of the entry in the INI where the state of the "Disable this warning" check box is stored
@param InIniSettingFileNameOverride   The name of the INI where the state of the InIniSettingName flag is stored (defaults to GEditorPerProjectIni)
@param bDefaultValue                                  If the warning is suppressed, the function will log and return DefaultValue
@return The result of the users decision, or DefaultValue if suppressed.

