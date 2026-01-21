// =============================================================================
// DJ01DamagePopupBase - 自动生成的 Widget 基类
// 
// 描述: 伤害飘字Widget - 显示伤害/治疗数值，带上飘+淡出动画
// 生成时间: 2026-01-21 13:10:07
// 
// ⚠️ 此文件由 UI Generator 自动生成，请勿手动修改
// =============================================================================

#include "DJ01DamagePopupBase.h"

#include "Components/ProgressBar.h"
#include "Components/TextBlock.h"
#include "Components/Image.h"
#include "Components/CanvasPanelSlot.h"
#include "Components/CanvasPanel.h"

UDJ01DamagePopupBase::UDJ01DamagePopupBase(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
}

void UDJ01DamagePopupBase::NativeConstruct()
{
	Super::NativeConstruct();
	
	// 初始化绑定
	UpdateBindings();
}

void UDJ01DamagePopupBase::NativeDestruct()
{
	Super::NativeDestruct();
}

void UDJ01DamagePopupBase::UpdateBindings()
{
	// 在此添加绑定更新逻辑
}

void UDJ01DamagePopupBase::ShowDamage(float DamageAmount, bool bIsCritical)
{
	if (!DamageText) return;

	// 设置颜色
	FSlateColor TextColor = bIsCritical ? FSlateColor(CriticalColor) : FSlateColor(DamageColor);
	DamageText->SetColorAndOpacity(TextColor);

	// 设置文字（暴击加感叹号）
	FString DamageStr = bIsCritical ? FString::Printf(TEXT("%.0f!"), DamageAmount) : FString::Printf(TEXT("%.0f"), DamageAmount);
	DamageText->SetText(FText::FromString(DamageStr));

	// 播放动画
	PlayPopupAnimation();
}

void UDJ01DamagePopupBase::ShowHeal(float HealAmount)
{
	if (!DamageText) return;

	// 设置绿色
	DamageText->SetColorAndOpacity(FSlateColor(HealColor));

	// 设置文字（+号前缀）
	FString HealStr = FString::Printf(TEXT("+%.0f"), HealAmount);
	DamageText->SetText(FText::FromString(HealStr));

	// 播放动画
	PlayPopupAnimation();
}
