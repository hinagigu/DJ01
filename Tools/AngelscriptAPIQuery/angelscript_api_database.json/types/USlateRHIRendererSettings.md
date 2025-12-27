# USlateRHIRendererSettings

**继承自**: `UDeveloperSettings`

Settings used to control slate rendering

## 属性

### SlatePostSettings
- **类型**: `TMap<ESlatePostRT,FSlatePostSettings>`
- **描述**: Map of all slate post RT's and their settings
Note that each post RT used in a frame will result in 1 full framebuffer copy for slate to sample from.
If a post RT is not used, no copy will occur & that post RT will be resized to 1x1 after 2 frames of non-use.

By default only SlatePostRT_0 is enabled. The rest must manually be enabled in settings below.
        // Map is nice since needs no editor customization. After initial run there should be no more than 5 lookups each frame.

## 方法

### GetMutableSlatePostSetting
```angelscript
FSlatePostSettings& GetMutableSlatePostSetting(ESlatePostRT InPostBufferBit)
```
Get settings struct for a particular post buffer index

### GetSlatePostSetting
```angelscript
FSlatePostSettings GetSlatePostSetting(ESlatePostRT InPostBufferBit)
```
Get settings struct for a particular post buffer index

