// =============================================================================
// DJ01HealthBarBase - 自动生成的 Widget 基类
// 
// 描述: 
// 生成时间: 2026-01-21 13:10:07
// 
// ⚠️ 此文件由 UI Generator 自动生成，请勿手动修改
// =============================================================================

#include "DJ01HealthBarBase.h"

#include "Components/ProgressBar.h"
#include "Components/TextBlock.h"
#include "Components/Image.h"
#include "Components/CanvasPanelSlot.h"
#include "Components/CanvasPanel.h"

UDJ01HealthBarBase::UDJ01HealthBarBase(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

void UDJ01HealthBarBase::NativeConstruct()
{
	Super::NativeConstruct();
	
	// 初始化绑定
	UpdateBindings();
}

void UDJ01HealthBarBase::NativeDestruct()
{
	UnbindFromASC();
	Super::NativeDestruct();
}

void UDJ01HealthBarBase::BindToASC(UAbilitySystemComponent* InASC)
{
	if (!InASC || BoundASC.Get() == InASC)
	{
		return;
	}
	
	// 先解除旧绑定
	UnbindFromASC();
	
	BoundASC = InASC;
	InitBindingSet_ReSources(InASC);
	
	// 初始化 UI
	UpdateBindings();
}

void UDJ01HealthBarBase::UnbindFromASC()
{
	if (BoundASC.IsValid())
	{
		CleanupBindingSet_ReSources(BoundASC.Get());
		BoundASC.Reset();
	}
}

void UDJ01HealthBarBase::UpdateBindings()
{
	if (HealthBar)
	{
		HealthBar->SetPercent(PercentHealth);
	}
	if (HealthText)
	{
		HealthText->SetText(FText::AsNumber(CurrentHealth));
	}
}
