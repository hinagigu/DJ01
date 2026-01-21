# UComboGraphSystemComponent

**继承自**: `UComboGraphGameplayTasksComponent`

Gameplay Task Actor Component designed to be added in Blueprints to Actors that wants to run Start Graph Gameplay Task outside of the regular GAS route and Gameplay Abilities.

It is meant to be used for Actors not implementing IAbilitySystemInterface. On BeginPlay, this component will check owners for a valid Ability System Component
(either via the interface, or through component search) and if none is found, will spawn and register an ASC at runtime.

Once done, this component will grant a generic internal ability UComboGraphNativeAbility (which is also not Blueprintable) that the gameplay task can use to run a specific combo graph.
UComboGraphNativeAbility provides a basic implementation of a typical gameplay ability to run a combo graph via the ability task, pulling the combo graph asset from Gameplay Event Data.

