# UIllegalPluginDependenciesValidator

**继承自**: `UEditorValidatorBase`

Ensures that non-GameFeaturePlugins do not depend on GameFeaturePlugins.
GameFeaturePlugins will load content later than non-GameFeaturePlugins which could cause linker load issues if they do not exist.

