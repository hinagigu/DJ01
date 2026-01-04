// =============================================================================
// DJ01HealthBarBase - 自动生成的 Widget 基类
// 
// 描述: 
// 生成时间: 2025-12-30 20:12:25
// 
// ⚠️ 此文件由 UI Generator 自动生成，请勿手动修改
// =============================================================================

#pragma once

#include "CommonUserWidget.h"
#include "Components/CanvasPanel.h"
#include "Components/ProgressBar.h"
#include "Components/TextBlock.h"
#include "DJ01/AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h"

#include "DJ01HealthBarBase.generated.h"

class UCanvasPanel;
class UProgressBar;
class UTextBlock;

/**
 * DJ01HealthBar 基类
 * 
 * 
 * 
 * 使用方式：
 * 1. 创建继承此类的 Widget Blueprint
 * 2. 在 Designer 中添加对应名称的控件
 * 3. 调整布局和样式
 */
UCLASS(Abstract, Blueprintable)
class DJ01_API UDJ01HealthBarBase : public UCommonUserWidget
{
	GENERATED_BODY()

public:
	UDJ01HealthBarBase(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());

protected:
	//~ Begin UUserWidget Interface
	virtual void NativeConstruct() override;
	virtual void NativeDestruct() override;
	//~ End UUserWidget Interface

	// ===== BindingSet: ReSources =====
	// 以下变量和函数由 DJ01_DECLARE_BINDING_SET(ReSources) 自动生成
	DJ01_DECLARE_BINDING_SET(ReSources)

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
	TObjectPtr<UProgressBar> HealthBar;  // 血量进度条
	UPROPERTY(BlueprintReadWrite, meta = (BindWidget))
	TObjectPtr<UTextBlock> HealthText;  // 血量文字

	// ===== 属性 =====
	/** 血量百分比 */
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Default")
	float HealthPercent = 1.0f;

private:
	/** 更新所有 UI 绑定 */
	void UpdateBindings();

};