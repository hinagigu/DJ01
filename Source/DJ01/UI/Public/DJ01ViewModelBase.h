// Copyright DJ01. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "MVVMViewModelBase.h"
#include "DJ01ViewModelBase.generated.h"

class APlayerController;
class UAbilitySystemComponent;

/**
* DJ01 ViewModel 基类
* 
* 所有游戏 ViewModel 的基类，提供：
* - 与 GAS 属性系统的集成（通过 BindingSet）
* - 玩家上下文获取
* - 通用的初始化/清理逻辑
* 
* 使用方式：
* 1. 继承此类创建具体的 ViewModel
* 2. 使用 DJ01_DECLARE_BINDING_SET(Name) 声明需要的绑定
* 3. 在 InitializeViewModel_Implementation 中调用 DJ01_INIT_BINDING_SET
* 4. 在 UninitializeViewModel_Implementation 中调用 DJ01_CLEANUP_BINDING_SET
* 
* @see DJ01HealthViewModel 完整使用示例
*/
UCLASS(Abstract, Blueprintable, BlueprintType)
class DJ01_API UDJ01ViewModelBase : public UMVVMViewModelBase
{
	GENERATED_BODY()

public:
	UDJ01ViewModelBase();

	/**
	 * 初始化 ViewModel
	 * 子类应重写此函数以调用 DJ01_INIT_BINDING_SET
	 */
	UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "ViewModel")
	void InitializeViewModel(UAbilitySystemComponent* ASC);

	/**
	 * 清理 ViewModel
	 * 子类应重写此函数以调用 DJ01_CLEANUP_BINDING_SET
	 */
	UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "ViewModel")
	void UninitializeViewModel();

	/** 检查 ViewModel 是否已初始化 */
	UFUNCTION(BlueprintCallable, Category = "ViewModel")
	bool IsInitialized() const { return BoundASC.IsValid(); }

	/** 获取绑定的 ASC */
	UFUNCTION(BlueprintCallable, Category = "ViewModel|GAS")
	UAbilitySystemComponent* GetAbilitySystemComponent() const { return BoundASC.Get(); }

protected:
	/** 已绑定的 ASC */
	UPROPERTY(Transient)
	TWeakObjectPtr<UAbilitySystemComponent> BoundASC;

	/**
	 * 辅助函数：安全地设置属性并触发通知
	 * 仅当值发生变化时才触发通知
	 */
	template<typename T>
	bool SetPropertyValue(T& Property, const T& NewValue, UE::FieldNotification::FFieldId FieldId)
	{
		if (Property != NewValue)
		{
			Property = NewValue;
			BroadcastFieldValueChanged(FieldId);
			return true;
		}
		return false;
	}
};