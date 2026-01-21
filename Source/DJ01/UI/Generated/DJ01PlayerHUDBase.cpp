// =============================================================================
// DJ01PlayerHUDBase - 自动生成的 Widget 基类
// 
// 描述: 玩家主HUD - 血条、蓝条、伤害飘字容器
// 生成时间: 2026-01-21 13:10:07
// 
// ⚠️ 此文件由 UI Generator 自动生成，请勿手动修改
// =============================================================================

#include "DJ01PlayerHUDBase.h"

#include "Components/ProgressBar.h"
#include "Components/TextBlock.h"
#include "Components/Image.h"
#include "Components/CanvasPanelSlot.h"
#include "Components/CanvasPanel.h"
#include "DJ01DamagePopupBase.h"

UDJ01PlayerHUDBase::UDJ01PlayerHUDBase(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

void UDJ01PlayerHUDBase::NativeConstruct()
{
	Super::NativeConstruct();
	
	// 初始化绑定
	UpdateBindings();
}

void UDJ01PlayerHUDBase::NativeDestruct()
{
	UnbindFromASC();
	Super::NativeDestruct();
}

void UDJ01PlayerHUDBase::BindToASC(UAbilitySystemComponent* InASC)
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

void UDJ01PlayerHUDBase::UnbindFromASC()
{
	if (BoundASC.IsValid())
	{
		CleanupBindingSet_ReSources(BoundASC.Get());
		BoundASC.Reset();
	}
}

void UDJ01PlayerHUDBase::UpdateBindings()
{
	if (HealthBar)
	{
		HealthBar->SetPercent(PercentHealth);
	}
	if (ManaBar)
	{
		ManaBar->SetPercent(PercentMana);
	}
}

void UDJ01PlayerHUDBase::ShowDamagePopup(float DamageAmount, FVector2D ScreenPosition, bool bIsCritical)
{
	if (!DamagePopupClass || !DamagePopupContainer) return;

	// 创建伤害飘字
	UUserWidget* PopupWidget = CreateWidget<UUserWidget>(GetOwningPlayer(), DamagePopupClass);
	if (PopupWidget)
	{
		// 添加到容器并设置位置
		UCanvasPanelSlot* PanelSlot = Cast<UCanvasPanelSlot>(DamagePopupContainer->AddChild(PopupWidget));
		if (PanelSlot)
		{
			PanelSlot->SetPosition(ScreenPosition);
			PanelSlot->SetAutoSize(true);
		}
		// 调用蓝图实现的显示函数
		if (UDJ01DamagePopupBase* DamagePopup = Cast<UDJ01DamagePopupBase>(PopupWidget))
		{
			DamagePopup->ShowDamage(DamageAmount, bIsCritical);
		}
	}
}

void UDJ01PlayerHUDBase::ShowHealPopup(float HealAmount, FVector2D ScreenPosition)
{
	if (!DamagePopupClass || !DamagePopupContainer) return;

	// 创建治疗飘字
	UUserWidget* PopupWidget = CreateWidget<UUserWidget>(GetOwningPlayer(), DamagePopupClass);
	if (PopupWidget)
	{
		UCanvasPanelSlot* PanelSlot = Cast<UCanvasPanelSlot>(DamagePopupContainer->AddChild(PopupWidget));
		if (PanelSlot)
		{
			PanelSlot->SetPosition(ScreenPosition);
			PanelSlot->SetAutoSize(true);
		}
		// 调用蓝图实现的显示函数
		if (UDJ01DamagePopupBase* DamagePopup = Cast<UDJ01DamagePopupBase>(PopupWidget))
		{
			DamagePopup->ShowHeal(HealAmount);
		}
	}
}

void UDJ01PlayerHUDBase::HandleHealthDelta(float NewHealth)
{
	// 计算伤害/治疗差值
	if (LastHealth < 0.0f)
	{
		// 首次初始化，不显示飘字
		LastHealth = NewHealth;
		return;
	}

	float Delta = NewHealth - LastHealth;
	LastHealth = NewHealth;

	if (FMath::Abs(Delta) < 0.01f) return;

	// 获取屏幕中心位置作为飘字起点
	FVector2D ScreenPos = FVector2D(400.0f, 300.0f); // TODO: 使用实际位置

	if (Delta < 0.0f)
	{
		// 受到伤害
		ShowDamagePopup(FMath::Abs(Delta), ScreenPos, false);
	}
	else
	{
		// 受到治疗
		ShowHealPopup(Delta, ScreenPos);
	}
}
