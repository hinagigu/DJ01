// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "DJ01WidgetBlueprintLibrary.generated.h"

class UWidgetBlueprint;
class UWidgetTree;
class UWidget;
class UPanelWidget;

/**
 * Widget Blueprint 操作库
 * 提供 Python 可调用的函数来操作 Widget Blueprint
 * 
 * 使用示例 (Python):
 * ```python
 * import unreal
 * 
 * # 加载 Widget Blueprint
 * widget_bp = unreal.EditorAssetLibrary.load_asset("/Game/UI/MyWidget")
 * 
 * # 获取 WidgetTree
 * tree = unreal.DJ01WidgetBlueprintLibrary.get_widget_tree(widget_bp)
 * 
 * # 添加控件
 * canvas = unreal.DJ01WidgetBlueprintLibrary.add_widget_to_tree(
 *     widget_bp, unreal.CanvasPanel, "RootCanvas")
 * 
 * # 设置根控件
 * unreal.DJ01WidgetBlueprintLibrary.set_root_widget(widget_bp, canvas)
 * ```
 */
UCLASS()
class DJ01EDITOR_API UDJ01WidgetBlueprintLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
public:
	// ===== 基础操作 =====
	
	/**
	 * 获取 Widget Blueprint 的 WidgetTree
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @return WidgetTree 对象，如果失败返回 nullptr
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static UWidgetTree* GetWidgetTree(UWidgetBlueprint* WidgetBlueprint);
	
	/**
	 * 获取 Widget Blueprint 的根控件
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @return 根控件，如果没有返回 nullptr
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static UWidget* GetRootWidget(UWidgetBlueprint* WidgetBlueprint);
	
	/**
	 * 设置 Widget Blueprint 的根控件
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @param RootWidget - 要设置为根的控件
	 * @return 是否设置成功
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static bool SetRootWidget(UWidgetBlueprint* WidgetBlueprint, UWidget* RootWidget);
	
	// ===== 控件创建 =====
	
	/**
	 * 在 WidgetTree 中创建一个新控件
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @param WidgetClass - 要创建的控件类型
	 * @param WidgetName - 控件名称（用于 BindWidget）
	 * @return 创建的控件，如果失败返回 nullptr
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static UWidget* CreateWidget(UWidgetBlueprint* WidgetBlueprint, TSubclassOf<UWidget> WidgetClass, FName WidgetName);
	
	/**
	 * 创建 CanvasPanel 控件
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @param WidgetName - 控件名称
	 * @return 创建的 CanvasPanel
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static UWidget* CreateCanvasPanel(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
	
	/**
	 * 创建 ProgressBar 控件
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @param WidgetName - 控件名称
	 * @return 创建的 ProgressBar
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static UWidget* CreateProgressBar(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
	
	/**
	 * 创建 TextBlock 控件
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @param WidgetName - 控件名称
	 * @return 创建的 TextBlock
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static UWidget* CreateTextBlock(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
	
	/**
	 * 创建 Image 控件
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @param WidgetName - 控件名称
	 * @return 创建的 Image
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static UWidget* CreateImage(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
	
	// ===== 层级操作 =====
	
	/**
	 * 将子控件添加到父控件
	 * @param Parent - 父控件（必须是 PanelWidget）
	 * @param Child - 要添加的子控件
	 * @return 是否添加成功
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static bool AddChildToPanel(UWidget* Parent, UWidget* Child);
	
	/**
	 * 将控件添加到 CanvasPanel
	 * @param CanvasPanel - CanvasPanel 控件
	 * @param Child - 要添加的子控件
	 * @param Position - 位置
	 * @param Size - 大小
	 * @return 是否添加成功
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static bool AddChildToCanvas(UWidget* CanvasPanel, UWidget* Child, FVector2D Position = FVector2D::ZeroVector, FVector2D Size = FVector2D(100, 100));
	
	// ===== 查找操作 =====
	
	/**
	 * 按名称查找控件
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @param WidgetName - 控件名称
	 * @return 找到的控件，如果没找到返回 nullptr
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static UWidget* FindWidgetByName(UWidgetBlueprint* WidgetBlueprint, FName WidgetName);
	
	/**
	 * 获取所有控件
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @return 所有控件的数组
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static TArray<UWidget*> GetAllWidgets(UWidgetBlueprint* WidgetBlueprint);
	
	// ===== 保存操作 =====
	
	/**
	 * 标记 Widget Blueprint 为已修改
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static void MarkDirty(UWidgetBlueprint* WidgetBlueprint);
	
	/**
	 * 保存 Widget Blueprint
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @return 是否保存成功
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static bool SaveWidgetBlueprint(UWidgetBlueprint* WidgetBlueprint);
	
	// ===== 批量操作 =====
	
	/**
	 * 根据 Schema JSON 创建控件树
	 * @param WidgetBlueprint - Widget Blueprint 资产
	 * @param SchemaJson - Schema JSON 字符串
	 * @return 是否创建成功
	 */
	UFUNCTION(BlueprintCallable, Category = "DJ01|Widget Blueprint")
	static bool CreateWidgetsFromJson(UWidgetBlueprint* WidgetBlueprint, const FString& SchemaJson);
};