# DJ01 Animation System - Agent Quick Reference

## Architecture Overview
```
ABP_DJ01Character_Base (主ABP, 继承 UDJ01AnimInstance)
    ├── StateMachine: Locomotion/Jump/Fall
    ├── Implements: IALI_DJ01AnimLayers (接口)
    └── LinkAnimClassLayers() → 运行时切换
              │
              ├── ABP_AnimLayer_Unarmed (空手动画层)
              ├── ABP_AnimLayer_Katana  (刀动画层)
              └── ABP_AnimLayer_SwordShield (剑盾层)
```

## File Conventions
| Type | Path | Naming |
|------|------|--------|
| Main ABP | `Content/Characters/ABP/` | `ABP_DJ01Character_Base` |
| Layer ABP | `Content/Characters/ABP/` | `ABP_AnimLayer_<Weapon>` |
| BlendSpace | `Content/Characters/BlendSpaces/` | `BS_<Weapon>_Locomotion` |
| Montage | `Content/Characters/Montages/` | `AM_<Weapon>_<Action>` |
| Interface | `Source/DJ01/Animation/` | `ALI_DJ01AnimLayers.h` |

## InPlace vs RootMotion Decision
| Animation | Type | Reason |
|-----------|------|--------|
| Idle/Walk/Run | **InPlace** | CharacterMovement controls speed |
| Jump/Fall | **InPlace** | Physics handles trajectory |
| Attack/Combo | **RootMotion** | Precise displacement sync |
| Dodge/Roll | **RootMotion** | Consistent distance |
| Heavy Hit | **RootMotion** | Knockback matches anim |

## Animation Assets Structure
```
Content/Characters/AnimationAssets/DynamicKatanaAnims/
├── InPlace/           ← Use for Locomotion BlendSpace
│   └── Walk/          BS_Katana_Locomotion uses these
└── RootMotion/        ← Use for Combat Montages
    └── Attack/        AM_Katana_Combo uses these
```

## RootMotion Setup
1. Animation Sequence: `Enable Root Motion` = ✅
2. Montage: `Root Motion Root Lock` = `Anim First Frame`
3. AnimInstance: `RootMotionMode` = `RootMotionFromMontagesOnly`

## BindingSet → AnimBP Integration
Tags auto-sync via generated code:
| GameplayTag | AnimBP Variable | Type |
|-------------|-----------------|------|
| `Status.Movement.Jumping` | `bIsJumping` | bool |
| `Status.Movement.Crouching` | `bIsCrouching` | bool |
| `Status.Action.Attacking` | `bIsAttacking` | bool |

Config: `Source/DJ01/AbilitySystem/Attributes/BindingSets/BindingSet_AnimState.h`

## Key AnimInstance Properties (UDJ01AnimInstance)
```cpp
// Movement data (auto-updated from CharacterMovement)
float GroundSpeed;           // Current horizontal speed
float Direction;             // -180 to 180, for BlendSpace
bool bIsMoving;              // GroundSpeed > threshold
bool bIsFalling;             // !IsMovingOnGround()

// From BindingSet
bool bIsJumping;             // Status.Movement.Jumping
bool bIsAttacking;           // Status.Action.Attacking
```

## State Machine Transitions
```
┌─────────┐  GroundSpeed > 10  ┌─────────┐
│  Idle   │ ─────────────────→ │  Move   │
└─────────┘ ←───────────────── └─────────┘
                GroundSpeed < 10
     │                              │
     │ bIsJumping                   │ bIsJumping
     ▼                              ▼
┌─────────────────────────────────────────┐
│              JumpStart                   │
└─────────────────────────────────────────┘
                    │ 
                    │ Automatic (sequence end)
                    ▼
┌─────────────────────────────────────────┐
│              FallLoop                    │
└─────────────────────────────────────────┘
                    │
                    │ bIsFalling == false
                    ▼
┌─────────────────────────────────────────┐
│               Land                       │
└─────────────────────────────────────────┘
                    │
                    │ Automatic → back to Idle/Move
```

## Animation Layer Interface (ALI)
Defined in `ALI_DJ01AnimLayers.h`:
```cpp
UFUNCTION(BlueprintCallable, BlueprintImplementableEvent)
FPoseLink FullBody_IdleState();

UFUNCTION(BlueprintCallable, BlueprintImplementableEvent)
FPoseLink FullBody_MovingState();

UFUNCTION(BlueprintCallable, BlueprintImplementableEvent)
FPoseLink FullBody_JumpStartState();
```

## Runtime Layer Switching
```cpp
// Switch to Katana animations
USkeletalMeshComponent* Mesh = Character->GetMesh();
Mesh->LinkAnimClassLayers(ABP_AnimLayer_Katana::StaticClass());

// Switch to Unarmed
Mesh->LinkAnimClassLayers(ABP_AnimLayer_Unarmed::StaticClass());
```

## Common Pitfalls
| Issue | Solution |
|-------|----------|
| Sliding feet in locomotion | Use InPlace anims + adjust playrate by speed |
| RootMotion not working | Check Montage RootMotionRootLock setting |
| Wrong anim after weapon switch | Call LinkAnimClassLayers() |
| Tag not syncing to ABP | Verify BindingSet mapping exists |
| BlendSpace snapping | Check Direction calc: use -180~180 range |

## Debug Tips
- `ShowDebug Animation` in console
- AnimBP → Enable "Show Debug" on states
- Check `GroundSpeed`/`Direction` values in AnimBP preview