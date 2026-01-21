// ============================================================
// DJ01DamageTypes.cpp
// ============================================================

#include "DJ01/AbilitySystem/Abilities/Public/DJ01DamageTypes.h"
#include "AbilitySystemComponent.h"
#include "DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01DamageTypes)

// ============================================================
// FDJ01DamageScaling
// ============================================================

FString FDJ01DamageScaling::GetDescription() const
{
    FString LayerStr;
    switch (Layer)
    {
    case EDJ01AttributeLayer::Base: LayerStr = TEXT("Base"); break;
    case EDJ01AttributeLayer::Bonus: LayerStr = TEXT("Bonus"); break;
    default: LayerStr = TEXT(""); break;
    }
    
    FString SourceStr = bFromTarget ? TEXT(" (Target)") : TEXT("");
    
    if (LayerStr.IsEmpty())
    {
        return FString::Printf(TEXT("%+.0f%% %s%s"), Ratio * 100.f, *AttributeName.ToString(), *SourceStr);
    }
    return FString::Printf(TEXT("%+.0f%% %s %s%s"), Ratio * 100.f, *LayerStr, *AttributeName.ToString(), *SourceStr);
}

float FDJ01DamageScaling::GetAttributeValue(UAbilitySystemComponent* ASC) const
{
    if (!ASC || AttributeName.IsNone())
    {
        return 0.f;
    }

    float ResultValue = 0.f;
    
    // 根据配置的 AttributeSetClass 获取对应的 AttributeSet
    // 如果没有指定，则尝试常见的 AttributeSet
    
    const FString AttrNameStr = AttributeName.ToString();
    
    // 定义一个 lambda 来处理分层属性的计算
    auto CalculateFromSet = [&](const UAttributeSet* Set) -> bool
    {
        if (!Set)
        {
            return false;
        }
        
        UClass* SetClass = Set->GetClass();
        
        // 根据 Layer 构造实际要读取的属性名
        FString ActualAttrName;
        switch (Layer)
        {
        case EDJ01AttributeLayer::Base:
            ActualAttrName = FString::Printf(TEXT("Base%s"), *AttrNameStr);
            break;
        case EDJ01AttributeLayer::Total:
        case EDJ01AttributeLayer::Bonus:
        default:
            // 先尝试查找 GetTotalXxx 函数
            // 如果没有，则尝试直接读取属性
            {
                FString TotalFuncName = FString::Printf(TEXT("GetTotal%s"), *AttrNameStr);
                UFunction* TotalFunc = SetClass->FindFunctionByName(*TotalFuncName);
                if (TotalFunc)
                {
                    float TotalValue = 0.f;
                    // 调用 GetTotalXxx()
                    struct { float ReturnValue; } Params;
                    const_cast<UAttributeSet*>(Set)->ProcessEvent(TotalFunc, &Params);
                    TotalValue = Params.ReturnValue;
                    
                    if (Layer == EDJ01AttributeLayer::Total)
                    {
                        ResultValue = TotalValue;
                        return true;
                    }
                    else // Bonus
                    {
                        // Bonus = Total - Base
                        FString BaseAttrName = FString::Printf(TEXT("Base%s"), *AttrNameStr);
                        FProperty* BaseProp = SetClass->FindPropertyByName(*BaseAttrName);
                        if (BaseProp)
                        {
                            const FGameplayAttributeData* BaseData = BaseProp->ContainerPtrToValuePtr<FGameplayAttributeData>(Set);
                            if (BaseData)
                            {
                                ResultValue = TotalValue - BaseData->GetCurrentValue();
                                return true;
                            }
                        }
                        // 如果找不到 Base，就用 Total
                        ResultValue = TotalValue;
                        return true;
                    }
                }
                
                // 没有 GetTotal 函数，尝试直接读取属性
                ActualAttrName = AttrNameStr;
            }
            break;
        }
        
        // 查找属性
        FProperty* Prop = SetClass->FindPropertyByName(*ActualAttrName);
        if (Prop)
        {
            const FGameplayAttributeData* AttrData = Prop->ContainerPtrToValuePtr<FGameplayAttributeData>(Set);
            if (AttrData)
            {
                ResultValue = AttrData->GetCurrentValue();
                return true;
            }
        }
        
        return false;
    };
    
    // 如果指定了 AttributeSetClass
    if (AttributeSetClass)
    {
        const UAttributeSet* Set = ASC->GetAttributeSet(AttributeSetClass);
        if (CalculateFromSet(Set))
        {
            return ResultValue;
        }
    }
    
    // 否则遍历所有 AttributeSet 查找
    for (const UAttributeSet* Set : ASC->GetSpawnedAttributes())
    {
        if (CalculateFromSet(Set))
        {
            return ResultValue;
        }
    }
    
    return 0.f;
}

// ============================================================
// FDJ01DamageConfig
// ============================================================

float FDJ01DamageConfig::CalculateRawDamage(UAbilitySystemComponent* SourceASC, UAbilitySystemComponent* TargetASC) const
{
    float TotalDamage = BaseDamage;

    for (const FDJ01DamageScaling& Scaling : Scalings)
    {
        if (FMath::IsNearlyZero(Scaling.Ratio))
        {
            continue;
        }

        UAbilitySystemComponent* ASC = Scaling.bFromTarget ? TargetASC : SourceASC;
        if (!ASC)
        {
            continue;
        }

        const float AttrValue = Scaling.GetAttributeValue(ASC);
        TotalDamage += AttrValue * Scaling.Ratio;
    }

    return FMath::Max(TotalDamage, 0.f);
}

FString FDJ01DamageConfig::GetDamageDescription() const
{
    FString Desc = FString::Printf(TEXT("%.0f"), BaseDamage);
    
    for (const FDJ01DamageScaling& Scaling : Scalings)
    {
        if (!FMath::IsNearlyZero(Scaling.Ratio))
        {
            Desc += TEXT(" ") + Scaling.GetDescription();
        }
    }
    
    switch (DamageType)
    {
    case EDJ01DamageType::Physical: Desc += TEXT(" (物理)"); break;
    case EDJ01DamageType::Magical: Desc += TEXT(" (魔法)"); break;
    case EDJ01DamageType::Pure: Desc += TEXT(" (真实)"); break;
    }
    
    return Desc;
}