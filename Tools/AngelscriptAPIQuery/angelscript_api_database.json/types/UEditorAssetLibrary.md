# UEditorAssetLibrary

**继承自**: `UBlueprintFunctionLibrary`

Utility class to do most of the common functionalities with the ContentBrowser.
The AssetRegistryHelpers class has more complex utilities. Use FindAssetData to get a FAssetData from an Asset Path.
The Asset Path can be represented by
            ie. (Reference/Text Path)       StaticMesh'/Game/MyFolder/MyAsset.MyAsset'
            ie. (Full Name)                         StaticMesh /Game/MyFolder/MyAsset.MyAsset
            ie. (Path Name)                         /Game/MyFolder/MyAsset.MyAsset
            ie. (Package Name)                      /Game/MyFolder/MyAsset
The Directory Path can be represented by
            ie. /Game/MyNewFolder/
            ie. /Game/MyNewFolder
All operations can be slow. The editor should not be in play in editor mode. It will not work on assets of the type level.

