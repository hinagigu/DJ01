// =============================================================================
// DJ01PlayerHUDBase - 自动生成的 Widget 基类
// 
// 描述: 玩家主HUD - 血条、蓝条、伤害飘字容器
// 生成时间: 2026-01-21 13:10:07
// 
// ⚠️ 此文件由 UI Generator 自动生成，请勿手动修改
// =============================================================================

#pragma once

#include "CommonUserWidget.h"
#include "Components/CanvasPanel.h"
#include "Components/Image.h"
#include "Components/Overlay.h"
#include "Components/ProgressBar.h"
#include "Components/SizeBox.h"
#include "Components/TextBlock.h"
#include "Components/VerticalBox.h"
#include "DJ01/AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h"

#include "DJ01PlayerHUDBase.generated.h"

class UCanvasPanel;
class UImage;
class UOverlay;
class UProgressBar;
class USizeBox;
class UTextBlock;
class UVerticalBox;

/**
 * DJ01PlayerHUD 基类
 * 
 * 玩家主HUD - 血条、蓝条、伤害飘字容器
 * 
 * 使用方式：
 * 1. 创建继承此类的 Widget Blueprint
 * 2. 在 Designer 中添加对应名称的控件
 * 3. 调整布局和样式
 */
UCLASS(Abstract, Blueprintable)
class DJ01_API UDJ01PlayerHUDBase : public UCommonUserWidget
{
	GENERATED_BODY()

public:
	UDJ01PlayerHUDBase(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

protected:
	//~ Begin UUserWidget Interface
	virtual void NativeConstruct() override;
	virtual void NativeDestruct() override;
	//~ End UUserWidget Interface

public:
	// ===== BindingSet: ReSources =====
	// 以下变量和函数由 DJ01_DECLARE_BINDING_SET(ReSources) 自动生成
	DJ01_DECLARE_BINDING_SET(ReSources)

protected:
	/** ASC 弱引用 */
	TWeakObjectPtr<UAbilitySystemComponent> BoundASC;

public:
	/** 绑定到 AbilitySystemComponent */
	UFUNCTION(BlueprintCallable, Category = "Binding")
	void BindToASC(UAbilitySystemComponent* InASC);

	/** 解除绑定 */
	UFUNCTION(BlueprintCallable, Category = "Binding")
	void UnbindFromASC();


	// ===== UI 组件 (BindWidget) =====
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UCanvasPanel> RootCanvas;
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UVerticalBox> StatusContainer;  // 状态栏容器(左上角)
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<USizeBox> HealthBarContainer;
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UOverlay> HealthBarOverlay;
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UImage> HealthBarBg;  // 血条背景(深红)
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UProgressBar> HealthBar;  // 血条进度
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UTextBlock> HealthText;  // 血量数字
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<USizeBox> ManaBarContainer;
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UOverlay> ManaBarOverlay;
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UImage> ManaBarBg;  // 蓝条背景(深蓝)
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UProgressBar> ManaBar;  // 蓝条进度
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UTextBlock> ManaText;  // 蓝量数字
	UPROPERTY(BlueprintReadWrite, meta = (BindWidgetOptional))
	TObjectPtr<UCanvasPanel> DamagePopupContainer;  // 伤害飘字容器(全屏)

	// ===== 属性 =====
	/** 伤害飘字Widget类 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Popup")
	TSubclassOf<UUserWidget> DamagePopupClass;

	// ===== 派生属性 (代码计算) =====
	/** 格式化的血量文字 (当前/最大) */
	UPROPERTY(BlueprintReadOnly, Category = "Display")
	FText HealthDisplayText;
	/** 格式化的蓝量文字 (当前/最大) */
	UPROPERTY(BlueprintReadOnly, Category = "Display")
	FText ManaDisplayText;
	/** 上次血量值(用于计算伤害差值) */
	UPROPERTY(BlueprintReadOnly, Category = "Internal")
	float LastHealth = -1.0f;

public:
	// ===== 函数 =====
	/** 在屏幕指定位置显示伤害飘字 */
	UFUNCTION(BlueprintCallable, Category = "UI")
	void ShowDamagePopup(float DamageAmount, FVector2D ScreenPosition, bool bIsCritical);
	/** 显示治疗飘字 */
	UFUNCTION(BlueprintCallable, Category = "UI")
	void ShowHealPopup(float HealAmount, FVector2D ScreenPosition);
	/** 处理血量变化差值 - 计算并显示飘字 */
	UFUNCTION(BlueprintCallable, Category = "UI")
	void HandleHealthDelta(float NewHealth);

private:
	/** 更新所有 UI 绑定 */
	void UpdateBindings();

};