# UGeneralProjectSettings

**继承自**: `UObject`

## 属性

### CompanyName
- **类型**: `FString`
- **描述**: The name of the company (author, provider) that created the project.

### CompanyDistinguishedName
- **类型**: `FString`
- **描述**: The Distinguished Name of the company (author, provider) that created the project, which is used by publishing tools on some platforms.

### CopyrightNotice
- **类型**: `FString`
- **描述**: The project's copyright and/or trademark notices.

### Description
- **类型**: `FString`
- **描述**: The project's description text.

### Homepage
- **类型**: `FString`
- **描述**: The project's homepage URL.

### LicensingTerms
- **类型**: `FString`
- **描述**: The project's licensing terms.

### PrivacyPolicy
- **类型**: `FString`
- **描述**: The project's privacy policy.

### ProjectID
- **类型**: `FGuid`
- **描述**: The project's unique identifier.

### ProjectName
- **类型**: `FString`
- **描述**: The project's non-localized name.

### ProjectVersion
- **类型**: `FString`
- **描述**: The project's version number.

### SupportContact
- **类型**: `FString`
- **描述**: The project's support contact information.

### ProjectDisplayedTitle
- **类型**: `FText`
- **描述**: The project's title as displayed on the window title bar (can include the tokens {GameName}, {PlatformArchitecture}, {BuildConfiguration} or {RHIName}, which will be replaced with the specified text)

### ProjectDebugTitleInfo
- **类型**: `FText`
- **描述**: Additional data to be displayed on the window title bar in non-shipping configurations (can include the tokens {GameName}, {PlatformArchitecture}, {BuildConfiguration} or {RHIName}, which will be replaced with the specified text)

### bShouldWindowPreserveAspectRatio
- **类型**: `bool`
- **描述**: Should the game's window preserve its aspect ratio when resized by user.

### bUseBorderlessWindow
- **类型**: `bool`
- **描述**: Should the game use a borderless Slate window instead of a window with system title bar and border

### bStartInVR
- **类型**: `bool`
- **描述**: Should the game attempt to start in VR, regardless of whether -vr was set on the commandline

### bAllowWindowResize
- **类型**: `bool`
- **描述**: Should the user be allowed to resize the window used by the game, when not using full screen

### bAllowClose
- **类型**: `bool`
- **描述**: Should a close button be shown for the game's window, when not using full screen

### bAllowMaximize
- **类型**: `bool`
- **描述**: Should a maximize button be shown for the game's window, when not using full screen

### bAllowMinimize
- **类型**: `bool`
- **描述**: Should a minimize button be shown for the game's window, when not using full screen

### EyeOffsetForFakeStereoRenderingDevice
- **类型**: `float32`
- **描述**: Determines the Eye offset of the virtual stereo device created when " -emulatestereo" command line arg is detected

### FOVForFakeStereoRenderingDevice
- **类型**: `float32`
- **描述**: Determines the Field Of View of the virtual stereo device created when " -emulatestereo" command line arg is detected

