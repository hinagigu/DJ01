// =============================================================================
// DJ01DamagePopupBase - 自动生成的 Widget 基类
// 
// 描述: 伤害飘字Widget - 显示伤害/治疗数值，带上飘+淡出动画
// 生成时间: 2026-01-21 13:10:07
// 
// ⚠️ 此文件由 UI Generator 自动生成，请勿手动修改
// =============================================================================

#pragma once

#include "CommonUserWidget.h"
#include "Components/CanvasPanel.h"
#include "Components/TextBlock.h"

#include "DJ01DamagePopupBase.generated.h"

class UCanvasPanel;
class UTextBlock;

/**
 * DJ01DamagePopup 基类
 * 
 * 伤害飘字Widget - 显示伤害/治疗数值，带上飘+淡出动画
 * 
 * 使用方式：
 * 1. 创建继承此类的 Widget Blueprint
 * 2. 在 Designer 中添加对应名称的控件
 * 3. 调整布局和样式
 */
UCLASS(Abstract, Blueprintable)
class DJ01_API UDJ01DamagePopupBase : public UCommonUserWidget
{
	GENERATED_BODY()

public:
	UDJ01DamagePopupBase(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

protected:
	//~ Begin UUserWidget Interface
	virtual void NativeConstruct() override;
	virtual void NativeDestruct() override;
	//~ End UUserWidget Interface


	// ===== UI 组件 (BindWidget) =====
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UCanvasPanel> RootCanvas;
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UTextBlock> DamageText;  // 伤害数字

	// ===== 属性 =====
	/** 伤害颜色(红) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Style")
	FLinearColor DamageColor;
	/** 治疗颜色(绿) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Style")
	FLinearColor HealColor;
	/** 暴击颜色(金) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Style")
	FLinearColor CriticalColor;
	/** 动画持续时间(秒) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Animation")
	float AnimationDuration = 1.0f;
	/** 上飘距离(像素) */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Animation")
	float FloatUpDistance = 80.0f;

public:
	// ===== 函数 =====
	/** 显示伤害数值 */
	UFUNCTION(BlueprintCallable, Category = "UI")
	void ShowDamage(float DamageAmount, bool bIsCritical);
	/** 显示治疗数值 */
	UFUNCTION(BlueprintCallable, Category = "UI")
	void ShowHeal(float HealAmount);
	/** 播放飘字动画(蓝图实现上飘+淡出，动画结束后RemoveFromParent) */
	UFUNCTION(BlueprintCallable, BlueprintImplementableEvent, Category = "UI")
	void PlayPopupAnimation();

private:
	/** 更新所有 UI 绑定 */
	void UpdateBindings();

};